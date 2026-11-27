"""Snowballing AI pre-filter: batches, output check and merge of the three runs (protocol §4.2 step 8).

  python slr/snowball_merge.py batches        write slr/snowball/batches/bNNN.txt (100 ids each) for every candidate
                                              from 2023 without pilot votes, in the fixed order: linked to 2 or more
                                              included studies, then forward, then the rest; by id within each group
  python slr/snowball_merge.py check R NNN    check run R (1-3) of batch NNN: valid JSON, every id once, allowed codes,
                                              no id outside the batch; prints the missing ids (exit 1 if not clean)
  python slr/snowball_merge.py                merge pilot + runs into slr/snowball/prefilter.csv (resumable: uses what
                                              exists). Excluded if 2 or 3 of 3 vote an exclusion; code = most voted
                                              exclusion code, ties to the earliest run
  python slr/snowball_merge.py queue SEED     only with the pre-filter complete: random sample of 50 majority-excluded
                                              (slr/snowball/sample-50.csv) and the screening queue slr/snowball/queue.csv:
                                              the candidates that pass, in the fixed order, with the 50 at random
                                              positions within the first 300 (same seed); no votes in the queue

Run outputs: slr/snowball/runs/rR-bNNN.jsonl, plus rR-bNNN-retryK.jsonl for ids re-run after a failed check.
"""
import collections
import csv
import json
import pathlib
import random
import sys

SB = pathlib.Path(__file__).parent / "snowball"
CODES = {"Include", "IC1", "IC2", "IC3", "EC1", "EC2", "EC3", "EC5", "EC6"}


def candidates():
    return list(csv.DictReader(open(SB / "candidates.csv", encoding="utf-8")))


def group(r):
    return 1 if len(r["seeds"].split()) >= 2 else 2 if "forward" in r["source"] else 3


def order():
    pilot = set((SB / "pilot-ids.txt").read_text().split())
    rows = [r for r in candidates() if r["date"] >= "2023-01-01" and r["id"] not in pilot]
    return sorted(rows, key=lambda r: (group(r), r["id"]))


def batches():
    d = SB / "batches"
    d.mkdir(exist_ok=True)
    ids = [r["id"] for r in order()]
    for n in range(0, len(ids), 100):
        (d / f"b{n // 100 + 1:03d}.txt").write_text("\n".join(ids[n:n + 100]) + "\n")
    g = collections.Counter(group(r) for r in order())
    print(f"{len(ids)} ids in {-(-len(ids) // 100)} batches; groups 2+ links {g[1]}, forward {g[2]}, rest {g[3]}")


def lines(files):
    """(parsed lines, number of invalid lines) from the given jsonl files."""
    out, bad = [], 0
    for f in files:
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    bad += 1
    return out, bad


def check(run, b):
    ids = (SB / "batches" / f"b{b}.txt").read_text().split()
    got, bad = lines(sorted((SB / "runs").glob(f"r{run}-b{b}*.jsonl")))
    seen = collections.Counter(x.get("id") for x in got)
    wrong = [x.get("id") for x in got if x.get("s") not in CODES]
    extra = sorted(set(seen) - set(ids))
    dup = sorted(i for i, c in seen.items() if c > 1)
    missing = [i for i in ids if i not in seen]
    print(f"r{run}-b{b}: {len(got)} lines, invalid JSON {bad}, bad codes {wrong}, outside batch {extra}, "
          f"duplicated {dup}, missing {len(missing)}")
    if missing:
        print("MISSING", " ".join(missing))
    return not (bad or wrong or extra or dup or missing)


def merge():
    votes = collections.defaultdict(dict)  # id -> run -> line
    for run in "123":
        files = [SB / f"pilot-r{run}.jsonl"] + sorted((SB / "runs").glob(f"r{run}-b*.jsonl"))
        for x in lines([f for f in files if f.exists()])[0]:
            if x.get("s") in CODES:
                votes[x["id"]].setdefault(run, x)  # first valid vote of a run wins
    rows = []
    for r in candidates():
        v = votes.get(r["id"], {})
        if len(v) < 3:
            continue
        s = [v[k]["s"] for k in "123"]
        exc = [x for x in s if x != "Include"]
        cnt = collections.Counter(exc)
        maj = "Include" if len(exc) < 2 else max(exc, key=lambda c: (cnt[c], -exc.index(c)))
        rows.append({"id": r["id"], "group": group(r), "v1": s[0], "v2": s[1], "v3": s[2], "majority": maj,
                     "unanimity": "3/3" if len(exc) in (0, 3) else "2/3",
                     "r1": v["1"]["r"], "r2": v["2"]["r"], "r3": v["3"]["r"]})
    rows.sort(key=lambda r: (r["group"], r["id"]))
    with open(SB / "prefilter.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    total = len(order()) + len(set((SB / "pilot-ids.txt").read_text().split()))
    print(f"prefilter.csv: {len(rows)} of {total} with 3 votes")


def queue(seed):
    pre = list(csv.DictReader(open(SB / "prefilter.csv", encoding="utf-8")))
    total = len(order()) + len((SB / "pilot-ids.txt").read_text().split())
    assert len(pre) == total, f"pre-filter not complete: {len(pre)} of {total}"
    cand = {r["id"]: r for r in candidates()}
    excl = sorted(r["id"] for r in pre if r["majority"] != "Include")
    rng = random.Random(seed)
    sample = rng.sample(excl, 50)
    with open(SB / "sample-50.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "majority"])
        w.writerows([i, next(r["majority"] for r in pre if r["id"] == i)] for i in sample)
    ids = [r["id"] for r in sorted((cand[r["id"]] for r in pre if r["majority"] == "Include"),
                                   key=lambda c: (group(c), c["id"]))]
    n = len(ids) + len(sample)
    pos = sorted(rng.sample(range(min(300, n)), len(sample)))
    for p, i in zip(pos, sample):  # ascending positions: each insert keeps the earlier ones in place
        ids.insert(p, i)
    with open(SB / "queue.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "id", "title", "year", "sources", "abstract", "url"])
        for k, i in enumerate(ids, 1):
            c = cand[i]
            url = f"https://doi.org/{c['doi']}" if c["doi"] else c["openalex"]
            w.writerow([k, i, c["title"], c["date"] or c["year"], f"{c['type']} · {c['source']}", c["abstract"], url])
    g = collections.Counter(group(cand[i]) for i in ids if i not in sample)
    print(f"queue: {len(ids)} (pass {len(ids) - 50}: 2+ links {g[1]}, forward {g[2]}, rest {g[3]}; "
          f"sample 50 within the first 300)")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["batches"]:
        batches()
    elif a[:1] == ["queue"]:
        queue(int(a[1]))
    elif a[:1] == ["check"]:
        sys.exit(0 if check(a[1], a[2]) else 1)
    else:
        merge()
