"""Second-reviewer sets (protocol §4.1): 5 calibration records from the pilot,
30 sample records from the Rayyan set after deduplication, calibration excluded.
Calibration is stratified (3 pilot includes, 2 pilot excludes) so both decisions are calibrated.
Writes Rayyan-format CSVs for a separate blind review.
Usage: python slr/draw_sample.py 2026-11-18 20261118
"""
import csv
import html
import pathlib
import random
import re
import sys
import unicodedata

import openpyxl

DATE, SEED = sys.argv[1], int(sys.argv[2])
SLR = pathlib.Path(__file__).parent


def nt(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", html.unescape(s or "")).lower())


with open(SLR / f"rayyan-after-dedup-{DATE}.csv", encoding="utf-8-sig") as fh:
    rows = list(csv.DictReader(fh))
by_title = {nt(r["title"]): r for r in rows}

ws = openpyxl.load_workbook(SLR / "pilot" / "pilot-inspection-2026-11-05.xlsx", read_only=True)["Records"]
pilot = [dict(id=r[0], title=r[2], decision=r[8]) for r in ws.iter_rows(min_row=2, values_only=True) if r[0]]
inc = [p["id"] for p in pilot if p["decision"] == "I" and nt(p["title"]) in by_title]
exc = [p["id"] for p in pilot if p["decision"] == "E" and nt(p["title"]) in by_title]
rng = random.Random(SEED)
calib_ids = sorted(rng.sample(inc, 3) + rng.sample(exc, 2))
calib = [by_title[nt(p["title"])] for p in pilot if p["id"] in calib_ids]

pool = [r for r in rows if r["key"] not in {c["key"] for c in calib}]
sample = rng.sample(pool, 30)
assert len(pool) == len(rows) - 5 and len({r["key"] for r in sample}) == 30

for name, subset in (("calibration", calib), ("sample", sample)):
    with open(SLR / f"second-reviewer-{name}-{DATE}.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(subset)

print(f"records {len(rows)}; pilot found in set: I {len(inc)}, E {len(exc)}")
print("calibration:", calib_ids, [c["key"] for c in calib])
print("sample keys:", [r["key"] for r in sample])
