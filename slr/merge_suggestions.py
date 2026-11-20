"""Merge AI screening suggestions (outN.jsonl) into slr/pass2-ai-suggestions.csv.
Usage: python slr/merge_suggestions.py <dir with outN.jsonl>. Later batches override earlier ones (9-10 redo 964-1307 with abstracts).
Quotes not found verbatim in the title/abstract are flagged in column q_ok."""
import csv, glob, json, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
norm = lambda s: re.sub(r"\s+", " ", s or "").strip().lower()
queue = {x["key"]: x for x in csv.DictReader(open(os.path.join(here, "pass2-queue.csv"), encoding="utf-8"))}
files = sorted(glob.glob(os.path.join(sys.argv[1], "out*.jsonl")), key=lambda p: int(re.search(r"out(\d+)", p).group(1)))
sug = {}
for p in files:
    for line in open(p, encoding="utf-8"):
        if line.strip():
            d = json.loads(line)
            if d["key"] in queue and queue[d["key"]]["abstract"] and int(re.search(r"out(\d+)", p).group(1)) in (7, 8):
                continue  # 7-8 were judged on titles only; 9-10 replace them
            sug[d["key"]] = d
with open(os.path.join(here, "pass2-ai-suggestions.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(["key", "s", "g", "q", "r", "q_ok"])
    bad = 0
    for k, d in sug.items():
        x = queue.get(k, {}); ok = norm(d["q"]) in norm(x.get("abstract", "") + " " + x.get("title", ""))
        bad += not ok
        w.writerow([k, d["s"], d.get("g", ""), d["q"], d["r"], ok])
print(f"{len(sug)} of {len(queue)} records with a suggestion; {bad} quotes not verbatim")
