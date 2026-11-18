"""Deduplicate the final-search exports (protocol §4.2 step 2, EC4).

Reads every .ris/.bib in slr/exports/, groups records with the same DOI or the
same normalised title, keeps one per group (published over arXiv preprint, then
with abstract, then with DOI), and writes:
  slr/dedup-<date>.csv          one row per removed record, with the kept one
  slr/rayyan-import-<date>.ris  the kept records, for Rayyan
Usage: python slr/dedup.py 2026-11-18
"""
import collections
import csv
import pathlib
import re
import sys
import unicodedata

DATE = sys.argv[1]
SLR = pathlib.Path(__file__).parent
DB_ORDER = ["ieee", "acm", "wos", "arxiv"]  # tie-break only
BIB_TY = {"article": "JOUR", "inproceedings": "CONF", "inbook": "CHAP"}
MIN_TITLE = 20  # ponytail: shorter titles are too generic to match on; caught by Rayyan's check


def read_ris(path):
    out = []
    for chunk in re.split(r"(?m)^ER  -.*$", path.read_text(encoding="utf-8-sig")):
        tags = collections.defaultdict(list)
        for m in re.finditer(r"(?m)^([A-Z][A-Z0-9])  - ?(.*?)\s*$", chunk):
            tags[m[1]].append(m[2])
        if tags["TY"]:
            out.append(dict(tags))
    return out


def read_bib(path):
    out = []
    for entry in re.split(r"(?m)^\s*@(?=\w+\s*\{)", path.read_text(encoding="utf-8-sig"))[1:]:
        f = {m[1].lower(): m[2].replace("{", "").replace("}", "").strip()
             for m in re.finditer(r"(?m)^(\w+) = \{(.*)\},?$", entry)}
        tags = {"TY": [BIB_TY.get(entry.split("{")[0].strip().lower(), "GEN")]}
        for tag, key in [("TI", "title"), ("AB", "abstract"), ("PY", "year"), ("DO", "doi"),
                         ("T2", "journal"), ("T2", "booktitle"), ("PB", "publisher"), ("UR", "url")]:
            if f.get(key):
                tags.setdefault(tag, [f[key]])
        tags["AU"] = [a.strip() for a in f.get("author", "").split(" and ") if a.strip()]
        tags["KW"] = [k.strip() for k in f.get("keywords", "").split(",") if k.strip()]
        out.append(tags)
    return out


def first(r, tag):
    return (r.get(tag) or [""])[0]


def norm_doi(s):
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", s.strip().lower())


def norm_title(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s).lower())


recs = []
for path in sorted((SLR / "exports").glob("*.ris")) + sorted((SLR / "exports").glob("*.bib")):
    for r in read_ris(path) if path.suffix == ".ris" else read_bib(path):
        r["_file"] = path.name
        r["_db"] = path.name.split("-")[0]
        recs.append(r)

# Union-find: same DOI, then same normalised title.
parent = list(range(len(recs)))


def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i


for key, min_len in ((lambda r: norm_doi(first(r, "DO")), 1), (lambda r: norm_title(first(r, "TI")), MIN_TITLE)):
    seen = {}
    for i, r in enumerate(recs):
        k = key(r)
        if len(k) < min_len:
            continue
        if k in seen:
            parent[find(i)] = find(seen[k])
        else:
            seen[k] = i

groups = collections.defaultdict(list)
for i, r in enumerate(recs):
    groups[find(i)].append(r)


def rank(r):  # lower is better
    return (r["_db"] == "arxiv", not first(r, "AB"), not first(r, "DO"), DB_ORDER.index(r["_db"]))


kept, removed = [], []
for g in groups.values():
    g.sort(key=rank)
    keep = g[0]
    keep["_sources"] = sorted({r["_file"].rsplit("-2026", 1)[0] for r in g})
    kept.append(keep)
    for r in g[1:]:
        same_doi = norm_doi(first(r, "DO")) and norm_doi(first(r, "DO")) == norm_doi(first(keep, "DO"))
        removed.append({
            "removed_file": r["_file"], "removed_doi": first(r, "DO"), "removed_title": first(r, "TI"),
            "kept_file": keep["_file"], "kept_doi": first(keep, "DO"), "kept_title": first(keep, "TI"),
            "match": "DOI" if same_doi else "title",
            "ec4_preprint": "yes" if r["_db"] == "arxiv" and keep["_db"] != "arxiv" else "",
        })

assert len(kept) + len(removed) == len(recs)

with open(SLR / f"dedup-{DATE}.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(removed[0]))
    w.writeheader()
    w.writerows(removed)

with open(SLR / f"rayyan-import-{DATE}.ris", "w", encoding="utf-8") as fh:
    for r in kept:
        for tag in ["TY", "TI", "AU", "PY", "T2", "PB", "DO", "UR", "KW", "AB"]:
            for v in r.get(tag, []):
                fh.write(f"{tag}  - {v}\n")
        fh.write(f"N1  - Sources: {'; '.join(r['_sources'])}\n")
        fh.write("ER  - \n\n")

per_file = collections.Counter(r["_file"] for r in recs)
print("records per file:", dict(per_file))
print(f"total {len(recs)}, removed {len(removed)} "
      f"(DOI {sum(x['match'] == 'DOI' for x in removed)}, title {sum(x['match'] == 'title' for x in removed)}, "
      f"EC4 preprints {sum(bool(x['ec4_preprint']) for x in removed)}), kept {len(kept)}")
