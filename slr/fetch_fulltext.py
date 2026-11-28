"""Full-text step 1: download the PDFs of the pass-3 includes from arXiv (also the arXiv version of DOI records) and extract their text.

Run: python slr/fetch_fulltext.py [sb]   (from the repository root; re-runnable, skips files already there;
     sb: the snowballing candidates decided Include or Maybe in slr/snowball/decisions.csv)
PDFs and text go to slr/fulltext/ (git-ignored: copyrighted). The access log, slr/fulltext-access.csv,
records where each full text came from (protocol §4.2 step 7, IC4) and is committed. Records with no arXiv version are
logged "to fetch by hand": save the PDF as slr/fulltext/<key>.pdf and re-run; the row is set to ok with the publisher as source.
"""
import csv
import json
import re
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

OUT = "slr/fulltext"
LOG = "slr/fulltext-access.csv"


def includes():
    """Keys whose last pass-3 decision is Include, with their queue row (sb: snowballing Include or Maybe)."""
    if sys.argv[1:] == ["sb"]:
        last = {r["id"]: r for r in csv.DictReader(open("slr/snowball/decisions.csv", encoding="utf-8"))}
        rows = [dict(r, key=r["id"]) for r in csv.DictReader(open("slr/snowball/queue.csv", encoding="utf-8"))
                if last[r["id"]]["final"] in ("Include", "Maybe")]
        for r in rows:  # arXiv DOI -> abs URL; OpenAlex-only URL -> empty, so the arXiv title search runs
            r["url"] = re.sub(r"(?i)^https://doi\.org/10\.48550/arxiv\.", "https://arxiv.org/abs/", r["url"])
            r["url"] = "" if "openalex.org" in r["url"] else r["url"]
        return rows
    last = {r["key"]: r for r in csv.DictReader(open("slr/pass3-decisions.csv", encoding="utf-8"))}
    queue = {r["key"]: r for r in csv.DictReader(open("slr/pass3-queue.csv", encoding="utf-8"))}
    return [queue[k] for k, r in last.items() if r["final"] == "Include"]


def log_rows():
    return {r["key"]: r for r in csv.DictReader(open(LOG, encoding="utf-8"))} if os.path.exists(LOG) else {}


def arxiv_ids(rows):
    """arXiv id per key for records without an arXiv URL: Semantic Scholar by DOI, else arXiv API by exact title."""
    found, doi = {}, [r for r in rows if "doi.org/" in r["url"]]
    if doi:
        req = urllib.request.Request(
            "https://api.semanticscholar.org/graph/v1/paper/batch?fields=externalIds",
            data=json.dumps({"ids": ["DOI:" + r["url"].split("doi.org/")[1] for r in doi]}).encode(),
            headers={"Content-Type": "application/json", "User-Agent": "slr-fulltext-fetch/1.0"})
        for attempt in range(6):  # the shared unauthenticated pool often answers 429
            try:
                papers = json.load(urllib.request.urlopen(req, timeout=60))
                break
            except urllib.error.HTTPError as e:
                if e.code != 429 or attempt == 5:
                    raise
                time.sleep(15 * (attempt + 1))
        for r, p in zip(doi, papers):
            if p and (p.get("externalIds") or {}).get("ArXiv"):
                found[r["key"]] = p["externalIds"]["ArXiv"]
    for r in rows:
        if not r["url"]:
            q = urllib.parse.urlencode({"search_query": f'ti:"{r["title"]}"', "max_results": 1})
            xml = urllib.request.urlopen(f"https://export.arxiv.org/api/query?{q}", timeout=60).read().decode()
            m = re.search(r"<id>https?://arxiv.org/abs/([^<v]+)", xml)
            if m:
                found[r["key"]] = m.group(1)
            time.sleep(3)
    return found


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    log = log_rows()
    rows = includes()
    other = [r for r in rows if "arxiv.org/abs/" not in r["url"] and not os.path.exists(f"{OUT}/{r['key']}.pdf")
             and log.get(r["key"], {}).get("source") != "manual"]  # already looked up, no arXiv version
    alt = arxiv_ids(other)
    for r in other:  # no arXiv version: fetched by hand (ISEP, publisher, Google Scholar), then logged
        if r["key"] not in alt and log.get(r["key"], {}).get("status") != "ok":
            log[r["key"]] = {"key": r["key"], "source": "manual", "url": r["url"], "status": "to fetch by hand",
                             "date": time.strftime("%Y-%m-%d")}
    for r in rows:
        key, url = r["key"], r["url"]
        pdf = f"{OUT}/{key}.pdf"
        if key in alt:
            url = f"https://arxiv.org/abs/{alt[key]}"
        if "arxiv.org/abs/" not in url or os.path.exists(pdf):
            continue
        src = url.replace("arxiv.org/abs/", "export.arxiv.org/pdf/")  # export mirror for programmatic access
        try:
            req = urllib.request.Request(src, headers={"User-Agent": "slr-fulltext-fetch/1.0"})
            data = urllib.request.urlopen(req, timeout=120).read()
            assert data[:4] == b"%PDF", "not a PDF"
            open(pdf, "wb").write(data)
            status = "ok"
        except Exception as e:  # logged, retried on the next run
            status = f"failed: {e}"
        log[key] = {"key": key, "source": "arXiv" if key not in alt else "arXiv version of the DOI record", "url": src, "status": status, "date": time.strftime("%Y-%m-%d")}
        print(key, status, flush=True)
        time.sleep(3)  # arXiv: one request every 3 s
    for k, row in log.items():  # hand-fetched PDF saved as <key>.pdf: mark it ok
        if row["status"] == "to fetch by hand" and os.path.exists(f"{OUT}/{k}.pdf"):
            pub = "ACM DL" if "10.1145" in row["url"] else "IEEE Xplore (ISEP)" if "10.1109" in row["url"] else "publisher (ISEP)"
            row.update(source=f"manual: {pub}", status="ok", date=time.strftime("%Y-%m-%d"))
    for f in os.listdir(OUT):
        txt = f"{OUT}/{f[:-4]}.txt"
        if f.endswith(".pdf") and not os.path.exists(txt):
            subprocess.run(["pdftotext", "-enc", "UTF-8", f"{OUT}/{f}", txt], check=False)
    with open(LOG, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, ["key", "source", "url", "status", "date"])
        w.writeheader()
        w.writerows(sorted(log.values(), key=lambda x: x["key"]))
    keys = {r["key"] for r in rows}
    ok = sum(1 for k, x in log.items() if k in keys and x["status"] == "ok")
    print(f"{ok} of {len(includes())} includes have a full text; log in {LOG}")
