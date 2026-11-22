"""Build the pass-3 queue (protocol §4.2 step 4b) from the pass-2 files.

Run:  python slr/build_pass3_queue.py   -> slr/pass3-queue.csv
Order: (1) the 694 pass-2 includes/maybes, in pass-2 order; (2) pass-2 exclusions where the
author's blind first decision disagreed (in/out) with the AI suggestion: first the blind includes
changed to exclude after seeing the AI, then the blind excludes the AI would have kept.
flag = "disagree" marks every record (passed or not) whose blind first decision disagreed with the AI.
Once slr/pass3-ai-suggestions.csv exists (full re-review, all criteria incl. EC6), a disagreement the new
suggestion resolves (same in/out as the author's pass-2 final decision) is dropped: excluded records leave the
queue, passed records lose the flag. Records whose blind decision the author switched after seeing the AI
are always kept and flagged (the final decision there came from the AI, so a new AI agreement is no check).
"""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
IN = {"Include", "Maybe"}


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


q = read("pass2-queue.csv")
dec = {d["key"]: d for d in read("pass2-decisions.csv")}  # last row per key wins
ai = {a["key"]: a["s"] for a in read("pass2-ai-suggestions.csv")}
new = {a["key"]: a["s"] for a in read("pass3-ai-suggestions.csv")} if os.path.exists(os.path.join(HERE, "pass3-ai-suggestions.csv")) else {}
switched_after_ai = lambda x: (dec[x["key"]]["first"] in IN) != (x["p2"] in IN)
resolved = lambda x: x["key"] in new and (new[x["key"]] in IN) == (x["p2"] in IN) and not switched_after_ai(x)

for x in q:
    d = dec[x["key"]]
    x["p2"] = d["final"]
    x["flag"] = "disagree" if (d["first"] in IN) != (ai.get(x["key"]) in IN) else ""

passed = [x for x in q if x["p2"] in IN]
for x in passed:
    if x["flag"] and resolved(x):
        x["flag"] = ""
switched = [x for x in q if x["flag"] and x["p2"] not in IN and dec[x["key"]]["first"] in IN]
kept_out = [x for x in q if x["flag"] and x["p2"] not in IN and dec[x["key"]]["first"] not in IN and not resolved(x)]
rows = passed + switched + kept_out

with open(os.path.join(HERE, "pass3-queue.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(q[0].keys()))
    w.writeheader()
    for n, x in enumerate(rows, 1):
        w.writerow({**x, "n": n})

print(f"pass3-queue.csv: {len(rows)} = {len(passed)} passed + {len(switched)} switched to exclude + {len(kept_out)} excluded against the AI")
