"""Merge full-text AI suggestions (outN.jsonl) into slr/ft-ai-suggestions.csv, checking each quote against the full text.

Usage: python slr/merge_ft_suggestions.py <dir with outN.jsonl>   (re-runnable while batches are still being written)
A quote not found verbatim (whitespace and hyphenation ignored) in slr/fulltext/<key>.txt is flagged q_ok=False.
"""
import csv, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
norm = lambda s: re.sub(r"\s+", " ", re.sub(r"-\n(?=[a-z])", "", s or "")).strip().lower()  # noqa: E731

sug = {}
for p in sorted(glob.glob(os.path.join(sys.argv[1], "out*.jsonl"))):
    for line in open(p, encoding="utf-8"):
        if line.strip():
            try:
                d = json.loads(line)
            except json.JSONDecodeError:  # a batch may be mid-write
                continue
            sug[d["key"]] = d

queue = {r["key"]: r for r in csv.DictReader(open(os.path.join(HERE, "pass3-queue.csv"), encoding="utf-8"))}
bad = 0
with open(os.path.join(HERE, "ft-ai-suggestions.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["key", "s", "g", "q", "sec", "r", "q_ok"])
    for k, d in sug.items():
        path = os.path.join(HERE, "fulltext", k + ".txt")
        text = open(path, encoding="utf-8", errors="replace").read() if os.path.exists(path) else ""
        text += " " + queue.get(k, {}).get("abstract", "") + " " + queue.get(k, {}).get("title", "")
        ok = norm(d.get("q")) in norm(text)
        bad += not ok
        w.writerow([k, d["s"], d.get("g", ""), d.get("q", ""), d.get("sec", ""), d.get("r", ""), ok])
print(f"{len(sug)} suggestions; {bad} quotes not verbatim")
