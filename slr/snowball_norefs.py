"""Backward candidates of the included studies with no references in OpenAlex (protocol §4.2 step 8).

Input: slr/snowball/no-refs-references.csv, the reference lists extracted from the PDFs (slr/fulltext/<key>.txt)
by Claude (seed, n, title, doi, arxiv; arXiv id only when printed in the reference). Each reference is resolved in
OpenAlex by DOI, then arXiv DOI, then exact normalised title, and deduplicated as in snowball_collect.py
(against the screened records, the included studies and the existing candidates; a duplicate candidate gets the
seed added). New candidates are appended to slr/snowball/candidates.csv, continuing the numbering.
Idempotent: references already appended (same OpenAlex id) are skipped. Do not rerun snowball_collect.py after
this: it rewrites candidates.csv without these rows.
Usage: python slr/snowball_norefs.py
"""
import csv
from snowball_collect import OUT, SLR, CUTOFF, by_doi, by_title, abstract, norm_doi, norm_title

FIELDS = ["id", "openalex", "doi", "title", "year", "date", "type", "source", "seeds", "abstract"]


def main():
    cands = list(csv.DictReader(open(OUT / "candidates.csv", encoding="utf-8")))
    screened = list(csv.DictReader(open(SLR / "rayyan-after-dedup-2026-11-18.csv", encoding="utf-8")))
    seeds = list(csv.DictReader(open(OUT / "seeds.csv", encoding="utf-8")))
    screened_doi = {norm_doi(r["doi"]) for r in screened if r["doi"]}
    screened_t = {norm_title(r["title"].replace("&nbsp;", " ")) for r in screened}
    seed_ids = {i for s in seeds for i in s["openalex"].split()}
    by_id = {r["openalex"]: r for r in cands}
    by_d = {r["doi"]: r for r in cands if r["doi"]}
    by_t = {t: r for r in cands if len(t := norm_title(r["title"])) >= 20}
    n = int(cands[-1]["id"][3:])
    counts = {"references": 0, "not found": 0, "after cut-off": 0, "in screened or included": 0,
              "duplicate candidate": 0, "new": 0}
    for ref in csv.DictReader(open(OUT / "no-refs-references.csv", encoding="utf-8")):
        counts["references"] += 1
        w = (by_doi(norm_doi(ref["doi"])) if ref["doi"] else None) or \
            (by_doi(f"10.48550/arxiv.{ref['arxiv']}") if ref["arxiv"] else None) or by_title(ref["title"])
        if not w:
            counts["not found"] += 1
            continue
        doi, t = norm_doi(w.get("doi") or ""), norm_title(w.get("title") or "")
        t = t if len(t) >= 20 else ""
        if (w.get("publication_date") or "") > CUTOFF:
            counts["after cut-off"] += 1
        elif w["id"] in seed_ids or (doi and doi in screened_doi) or (t and t in screened_t):
            counts["in screened or included"] += 1
        elif dup := by_id.get(w["id"]) or (doi and by_d.get(doi)) or (t and by_t.get(t)):
            counts["duplicate candidate"] += 1
            if ref["seed"] not in dup["seeds"].split():
                dup["seeds"] = " ".join(sorted(dup["seeds"].split() + [ref["seed"]]))
                dup["source"] = "+".join(sorted(set(dup["source"].split("+")) | {"backward"}))
        else:
            n += 1
            counts["new"] += 1
            row = {"id": f"sb-{n:05d}", "openalex": w["id"], "doi": doi, "title": w.get("title") or "",
                   "year": (w.get("publication_date") or "")[:4], "date": w.get("publication_date") or "",
                   "type": w.get("type") or "", "source": "backward", "seeds": ref["seed"], "abstract": abstract(w)}
            cands.append(row)
            by_id[w["id"]] = row
            if doi:
                by_d[doi] = row
            if t:
                by_t[t] = row
    with open(OUT / "candidates.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, FIELDS)
        w.writeheader()
        w.writerows(cands)
    new = cands[len(cands) - counts["new"]:]
    print(counts, "| new from 2023:", sum(r["date"] >= "2023-01-01" for r in new), "| total candidates:", len(cands))


if __name__ == "__main__":
    main()
