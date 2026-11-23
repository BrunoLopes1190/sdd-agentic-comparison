"""Majority of the three independent full-text AI runs (slr/ft-ai-runs/r1..r3/*.jsonl) into slr/ft-ai-suggestions.csv.

Usage: python slr/merge_ft_votes.py   (re-runnable while runs are still arriving)
Only records with all three runs change. Added columns: prev (suggestion shown before the vote), votes (the three codes),
agree (3/3, 2/3 or 1/3). With a majority, s/g/q/sec/r come from a majority run (one whose quote is verbatim if any);
with no majority (1/3) the earlier suggestion stays and the tool flags it. Prompt: slr/ai-prompts/ft-vote.md.
"""
import csv, glob, json, os, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
norm = lambda s: re.sub(r"\s+", " ", re.sub(r"-\n(?=[a-z])", "", s or "")).strip().lower()  # noqa: E731

runs = {}
for n in (1, 2, 3):
    for p in glob.glob(os.path.join(HERE, "ft-ai-runs", f"r{n}", "*.jsonl")):
        for line in open(p, encoding="utf-8"):
            try:
                d = json.loads(line)
                runs.setdefault(d["key"], {})[n] = d
            except (json.JSONDecodeError, KeyError):  # a batch may be mid-write
                continue

path = os.path.join(HERE, "ft-ai-suggestions.csv")
with open(path, encoding="utf-8", newline="") as f:
    rd = csv.DictReader(f)
    cols, rows = list(rd.fieldnames), list(rd)
cols += [c for c in ("prev", "votes", "agree") if c not in cols]
queue = {r["key"]: r for r in csv.DictReader(open(os.path.join(HERE, "pass3-queue.csv"), encoding="utf-8"))}

done = Counter()
for row in rows:
    v = runs.get(row["key"], {})
    if len(v) < 3:
        continue
    codes = [v[n].get("s", "") for n in (1, 2, 3)]
    top, c = Counter(codes).most_common(1)[0]
    row["prev"] = row.get("prev") or row["s"]
    row["votes"], row["agree"] = ",".join(codes), f"{c}/3"
    done[row["agree"]] += 1
    if c < 2:
        continue
    tp = os.path.join(HERE, "fulltext", row["key"] + ".txt")
    text = norm((open(tp, encoding="utf-8", errors="replace").read() if os.path.exists(tp) else "")
                + " " + queue.get(row["key"], {}).get("abstract", "") + " " + queue.get(row["key"], {}).get("title", ""))
    maj = [v[n] for n in (1, 2, 3) if v[n].get("s") == top]
    d = next((m for m in maj if norm(m.get("q")) in text), maj[0])
    row.update(s=top, g=Counter(m.get("g", "") for m in maj).most_common(1)[0][0], q=d.get("q", ""),
               sec=d.get("sec", ""), r=d.get("r", ""), q_ok=norm(d.get("q")) in text)

with open(path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)
changed = sum(1 for r in rows if r.get("votes") and r["s"] != r["prev"])
print(f"{sum(done.values())} records with 3 runs: {dict(done)}; suggestion changed on {changed}")
