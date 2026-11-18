"""Final arXiv search: run S1 and S2 (v2) through the arXiv API and save raw Atom + RIS to slr/exports/.

Run: python slr/fetch_arxiv.py   (from the repository root)
Strings come from build_strings.py, so they are the frozen v2 strings.
"""
import datetime
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, "slr")
from build_strings import ARXIV_DATES, arxiv, strings  # noqa: E402

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom",
      "os": "http://a9.com/-/spec/opensearch/1.1/"}
PAGE = 500


def fetch(query):
    """All entries for one query, paged, 3 s between calls (arXiv API terms)."""
    entries, raw, start, total = [], [], 0, None
    while total is None or start < total:
        url = f"{API}?{urllib.parse.urlencode({'search_query': query, 'start': start, 'max_results': PAGE, 'sortBy': 'submittedDate', 'sortOrder': 'ascending'})}"
        xml = urllib.request.urlopen(url, timeout=120).read()
        root = ET.fromstring(xml)
        total = int(root.find("os:totalResults", NS).text)
        page = root.findall("a:entry", NS)
        if not page and start < total:  # arXiv sometimes returns an empty page; retry once
            time.sleep(5)
            continue
        raw.append(xml.decode("utf-8"))
        entries += page
        start += PAGE
        time.sleep(3)
    return total, entries, raw


def ris(entry):
    t = lambda path: " ".join((entry.findtext(path, "", NS) or "").split())  # noqa: E731
    arxiv_id = t("a:id").rsplit("/abs/", 1)[1]
    base_id = arxiv_id.rsplit("v", 1)[0]
    doi = t("arxiv:doi") or f"10.48550/arXiv.{base_id}"
    lines = ["TY  - UNPB", f"TI  - {t('a:title')}"]
    lines += [f"AU  - {' '.join(a.findtext('a:name', '', NS).split())}" for a in entry.findall("a:author", NS)]
    lines += [f"PY  - {t('a:published')[:4]}", f"DA  - {t('a:published')[:10]}", f"AB  - {t('a:summary')}",
              f"DO  - {doi}", f"UR  - https://arxiv.org/abs/{base_id}", f"AN  - arXiv:{arxiv_id}",
              "DB  - arXiv", "PB  - arXiv"]
    if t("arxiv:journal_ref"):
        lines.append(f"N1  - Journal ref: {t('arxiv:journal_ref')}")
    lines += [f"KW  - {c.get('term')}" for c in entry.findall("a:category", NS)]
    return "\n".join(lines) + "\nER  - \n"


if __name__ == "__main__":
    today = datetime.date.today().isoformat()
    for name, s in zip(("S1", "S2"), strings(arxiv)):
        total, entries, raw = fetch(f"({s}) AND {ARXIV_DATES}")
        ids = {e.findtext("a:id", "", NS) for e in entries}
        assert len(ids) == len(entries) == total, f"{name}: total {total}, got {len(entries)}, unique {len(ids)}"
        stem = f"slr/exports/arxiv-{name}-{today}"
        open(f"{stem}.atom.xml", "w", encoding="utf-8").write("\n".join(raw))
        open(f"{stem}.ris", "w", encoding="utf-8").write("\n".join(ris(e) for e in entries))
        print(f"{name}: {total} records -> {stem}.ris")
