"""Collect snowballing candidates from OpenAlex (protocol §4.2 step 8).

Seeds: the 246 records included at full text (last decision per key in
ft-decisions.csv). For each seed, find its OpenAlex work(s) by DOI, then arXiv
DOI, then exact normalised title; backward = referenced_works, forward = works
that cite it, published up to the cut-off. Candidates are deduplicated (OpenAlex
id, DOI, normalised title) among themselves and against the 1858 screened records.

Writes slr/snowball/candidates.csv, slr/snowball/no-refs.csv, slr/snowball/seeds.csv
and prints the counts for the search log. Raw responses are cached in
slr/snowball/raw/ (not committed), so a rerun resumes without new calls.
Usage: python slr/snowball_collect.py
"""
import csv
import hashlib
import json
import pathlib
import re
import time
import urllib.parse
import unicodedata
import urllib.request


def norm_doi(s):  # same as dedup.py (not importable: it reads argv at import)
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", s.strip().lower())


def norm_title(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s).lower())

SLR = pathlib.Path(__file__).parent
OUT = SLR / "snowball"
RAW = OUT / "raw"
CUTOFF = "2026-11-18"
API = "https://api.openalex.org/works"
SELECT = "id,doi,title,publication_date,abstract_inverted_index,referenced_works,ids,type"


def get(url):
    f = RAW / (hashlib.sha1(url.encode()).hexdigest() + ".json")
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "slr-snowballing/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.load(r)
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                data = None
                break
            time.sleep(2 ** attempt)
    else:
        raise RuntimeError(url)
    f.write_text(json.dumps(data), encoding="utf-8")
    time.sleep(0.15)
    return data


def abstract(w):
    inv = w.get("abstract_inverted_index") or {}
    pos = sorted((p, word) for word, ps in inv.items() for p in ps)
    return " ".join(word for _, word in pos)


def by_doi(doi):
    return get(f"{API}/doi:{urllib.parse.quote(doi)}?select={SELECT}") if doi else None


def by_title(title):
    q = urllib.parse.quote(re.sub(r"[^\w\s]", " ", title))
    res = get(f"{API}?filter=title.search:{q}&per-page=5&select={SELECT}") or {}
    t = norm_title(title)
    return next((w for w in res.get("results", []) if norm_title(w.get("title") or "") == t), None)


def many(ids):
    out = []
    for i in range(0, len(ids), 50):
        chunk = "|".join(x.rsplit("/", 1)[-1] for x in ids[i:i + 50])
        out += get(f"{API}?filter=openalex:{chunk}&per-page=50&select={SELECT}")["results"]
    return out


def citing(wid):
    out, cursor = [], "*"
    while cursor:
        res = get(f"{API}?filter=cites:{wid.rsplit('/', 1)[-1]},to_publication_date:{CUTOFF}"
                  f"&per-page=200&cursor={cursor}&select={SELECT}")
        out += res["results"]
        cursor = res["meta"].get("next_cursor") if res["results"] else None
    return out


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    final = {}
    for r in csv.DictReader(open(SLR / "ft-decisions.csv", encoding="utf-8")):
        final[r["key"]] = r["final"]
    screened = list(csv.DictReader(open(SLR / "rayyan-after-dedup-2026-11-18.csv", encoding="utf-8")))
    meta = {}  # full-text keys come from the second Rayyan review: metadata from the pass-3 queue
    for r in csv.DictReader(open(SLR / "pass3-queue.csv", encoding="utf-8")):
        m = re.search(r"(10\.\d{4,}/\S+)", urllib.parse.unquote(r["url"]))
        meta[r["key"]] = {"title": r["title"], "doi": m[1] if m else ""}
    arxiv = {}
    for r in csv.DictReader(open(SLR / "fulltext-access.csv", encoding="utf-8")):
        m = re.search(r"arxiv\.org/(?:pdf|abs)/([\d.]+)", r["url"])
        if m:
            arxiv[r["key"]] = m[1]
    seeds = [k for k, v in final.items() if v == "Include"]
    assert len(seeds) == 246, len(seeds)

    cands = {}  # openalex id -> row
    seed_rows, norefs = [], []
    for n, k in enumerate(seeds, 1):
        m = meta[k]
        works = []
        for w in (by_doi(norm_doi(m["doi"])),
                  by_doi(f"10.48550/arxiv.{arxiv[k]}") if k in arxiv else None):
            if w and w["id"] not in {x["id"] for x in works}:
                works.append(w)
        if not works:
            w = by_title(m["title"].replace("&nbsp;", " "))
            works = [w] if w else []
        refs = sorted({x for w in works for x in w.get("referenced_works") or []})
        back = many(refs) if refs else []
        fwd = [c for w in works for c in citing(w["id"])]
        for src, lst in (("backward", back), ("forward", fwd)):
            for c in lst:
                row = cands.setdefault(c["id"], {
                    "openalex": c["id"], "doi": norm_doi(c.get("doi") or ""), "title": c.get("title") or "",
                    "year": (c.get("publication_date") or "")[:4], "date": c.get("publication_date") or "",
                    "type": c.get("type") or "", "abstract": abstract(c), "source": set(), "seeds": set()})
                row["source"].add(src)
                row["seeds"].add(k)
        seed_rows.append({"key": k, "openalex": " ".join(w["id"] for w in works),
                          "refs": len(refs), "citing": len(fwd)})
        if not refs:
            norefs.append({"key": k, "title": m["title"], "openalex": " ".join(w["id"] for w in works),
                           "pdf": f"slr/fulltext/{k}.pdf" if (SLR / "fulltext" / f"{k}.pdf").exists() else ""})
        print(f"{n}/246 {k} works={len(works)} refs={len(refs)} citing={len(fwd)}", flush=True)

    # dedup: candidates among themselves (DOI, title), then against screened + included
    raw_total = sum(len(r["seeds"]) for r in cands.values())
    screened_doi = {norm_doi(r["doi"]) for r in screened if r["doi"]}
    screened_t = {norm_title(r["title"].replace("&nbsp;", " ")) for r in screened}
    seed_ids = {i for s in seed_rows for i in s["openalex"].split()}
    seen_doi, seen_t, out = {}, {}, []
    counts = {"in screened or included": 0, "duplicate candidate": 0, "after cut-off": 0}
    for r in cands.values():
        t = norm_title(r["title"])
        t = t if len(t) >= 20 else ""
        if r["date"] > CUTOFF:
            counts["after cut-off"] += 1
            continue
        if r["openalex"] in seed_ids or (r["doi"] and r["doi"] in screened_doi) or (t and t in screened_t):
            counts["in screened or included"] += 1
            continue
        dup = (r["doi"] and seen_doi.get(r["doi"])) or (t and seen_t.get(t))
        if dup:
            dup["source"] |= r["source"]
            dup["seeds"] |= r["seeds"]
            counts["duplicate candidate"] += 1
            continue
        if r["doi"]:
            seen_doi[r["doi"]] = r
        if t:
            seen_t[t] = r
        out.append(r)

    for i, r in enumerate(out, 1):
        r["id"] = f"sb-{i:05d}"
        r["source"] = "+".join(sorted(r["source"]))
        r["seeds"] = " ".join(sorted(r["seeds"]))
    fields = ["id", "openalex", "doi", "title", "year", "date", "type", "source", "seeds", "abstract"]
    with open(OUT / "candidates.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    for name, rows in (("seeds.csv", seed_rows), ("no-refs.csv", norefs)):
        with open(OUT / name, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, list(rows[0]) if rows else ["key"])
            w.writeheader()
            w.writerows(rows)

    print("seeds found in OpenAlex:", sum(1 for s in seed_rows if s["openalex"]), "of 246")
    print("seeds without references (no-refs):", len(norefs))
    print("seed-candidate links (raw):", raw_total, "| distinct works:", len(cands))
    print("removed:", counts)
    print("candidates:", len(out), "| backward only:", sum(r["source"] == "backward" for r in out),
          "| forward only:", sum(r["source"] == "forward" for r in out),
          "| both:", sum("+" in r["source"] for r in out),
          "| without abstract:", sum(not r["abstract"] for r in out))


if __name__ == "__main__":
    main()
