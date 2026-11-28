"""Snowballing full-text AI filter: batches, output check and majority (protocol §4.2 step 8 (7), 2026-11-28).

Runs 1 and 2 on every batch bNN; run 3 only on the ids where runs 1 and 2 disagree (include vs exclude), in batches tNN:
when they agree, a third run cannot change the majority.

  python slr/snowball_ft.py batches [SIZE]   add ft-batches/bNN.txt (SIZE ids, default 8) for the candidates kept at
                                             title/abstract (Include or Maybe) with a full text and no batch yet, in queue
                                             order; re-runnable (texts fetched later get new batches)
  python slr/snowball_ft.py third            add ft-batches/tNN.txt (up to 8 ids) with the ids where runs 1 and 2 disagree
  python slr/snowball_ft.py todo             the runs still to do, one "R BATCH" per line (no output file yet)
  python slr/snowball_ft.py check R BATCH    check run R of BATCH (e.g. 1 b05, 3 t02): valid JSON, every id once, allowed
                                             codes, no id outside the batch, quote verbatim in the text (exit 1 if not clean)
  python slr/snowball_ft.py                  majority into slr/snowball/ft-votes.csv (ids with a settled majority only):
                                             excluded if 2 of 2, or 2 or 3 of 3, vote an exclusion; code = most voted
                                             exclusion code, ties to the earliest run. Prints counts only.
Prompt: slr/ai-prompts/snowball-ft-vote.md. Run outputs: slr/snowball/ft-runs/rR-BATCH.jsonl.
"""
import collections
import csv
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
SB, FT = HERE / "snowball", HERE / "fulltext"
BATCHES, RUNS = SB / "ft-batches", SB / "ft-runs"
CODES = {"Include", "IC1", "IC2", "IC3", "IC4", "EC1", "EC2", "EC3", "EC4", "EC5", "EC6"}
norm = lambda s: re.sub(r"\s+", " ", re.sub(r"-\n(?=[a-z])", "", s or "")).strip().lower()  # noqa: E731


def kept():
    last = {r["id"]: r["final"] for r in csv.DictReader(open(SB / "decisions.csv", encoding="utf-8"))}
    return [r["id"] for r in csv.DictReader(open(SB / "queue.csv", encoding="utf-8")) if last[r["id"]] in ("Include", "Maybe")]


def batch_files(prefix):
    return sorted(BATCHES.glob(f"{prefix}*.txt"))


def write_batches(prefix, ids, size):
    BATCHES.mkdir(exist_ok=True)
    n0 = len(batch_files(prefix))
    for k in range(0, len(ids), size):
        (BATCHES / f"{prefix}{n0 + k // size + 1:02d}.txt").write_text("\n".join(ids[k:k + size]) + "\n")
    return -(-len(ids) // size)


def batches(size):
    done = {i for f in batch_files("b") for i in f.read_text().split()}
    ids = [i for i in kept() if i not in done and (FT / f"{i}.txt").exists() and (FT / f"{i}.txt").stat().st_size]
    n = write_batches("b", ids, size)
    print(f"{len(ids)} new ids in {n} batches; {len(kept()) - len(done) - len(ids)} kept ids still without text")


def parse(path):
    out, bad = [], 0
    for line in path.read_text(encoding="utf-8").splitlines() if path.exists() else []:
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                bad += 1
    return out, bad


def votes():
    v = collections.defaultdict(dict)
    for f in sorted(RUNS.glob("r*-*.jsonl")):
        for r in parse(f)[0]:
            v[r["id"]][int(f.name[1])] = r["s"]
    return v


def third():
    v, done = votes(), {i for f in batch_files("t") for i in f.read_text().split()}
    ids = [i for i in kept() if i not in done and 1 in v[i] and 2 in v[i] and (v[i][1] == "Include") != (v[i][2] == "Include")]
    print(f"{len(ids)} ids need run 3, in {write_batches('t', ids, 8)} new batches")


def todo():
    for f in batch_files("b") + batch_files("t"):
        for run in ((1, 2) if f.stem[0] == "b" else (3,)):
            if not (RUNS / f"r{run}-{f.stem}.jsonl").exists():
                print(run, f.stem)


def check(run, batch):
    ids = (BATCHES / f"{batch}.txt").read_text().split()
    rows, bad = parse(RUNS / f"r{run}-{batch}.jsonl")
    seen = collections.Counter(r.get("id") for r in rows)
    errs = [f"{bad} invalid lines"] if bad else []
    errs += [f"missing {i}" for i in ids if not seen[i]] + [f"twice {i}" for i, c in seen.items() if c > 1]
    errs += [f"outside batch {i}" for i in seen if i not in ids]
    for r in rows:
        if r.get("s") not in CODES:
            errs.append(f"bad code {r.get('id')}")
        elif r.get("s") != "IC4" and norm(r.get("q")) not in norm((FT / f"{r.get('id')}.txt").read_text(encoding="utf-8", errors="replace")):
            errs.append(f"quote not verbatim {r.get('id')}")
    print("\n".join(errs) or f"r{run}-{batch}: clean ({len(ids)} ids)")
    return not errs


def majority(codes):
    """Settled majority of 2 agreeing or 3 runs, else None (runs 1 and 2 disagree and run 3 is missing)."""
    if len(codes) < 2 or (len(codes) == 2 and (codes[0] == "Include") != (codes[1] == "Include")):
        return None
    exc = [c for c in codes if c != "Include"]
    return "Include" if len(exc) < 2 else max(exc, key=lambda c: (exc.count(c), -exc.index(c)))


assert [majority(c) for c in (["Include", "IC1", "Include"], ["EC6", "Include", "IC1"], ["IC1", "EC6", "EC6"])] == ["Include", "EC6", "EC6"]
assert [majority(c) for c in (["Include", "IC1", "EC6"], ["Include", "Include"], ["EC3", "IC1"], ["Include", "EC3"])] == ["IC1", "Include", "EC3", None]


def merge():
    v, out = votes(), []
    for i in kept():
        codes = [v[i][n] for n in (1, 2, 3) if n in v[i]]
        if majority(codes):
            n_in = sum(c == "Include" for c in codes)
            out.append({"id": i, "v1": codes[0], "v2": codes[1], "v3": codes[2] if len(codes) > 2 else "",
                        "majority": majority(codes), "agree": f"{max(n_in, len(codes) - n_in)}/{len(codes)}"})
    with open(SB / "ft-votes.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, ["id", "v1", "v2", "v3", "majority", "agree"])
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} of {len(kept())} kept candidates have a settled majority; ft-votes.csv written")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["batches"]:
        batches(int(a[1]) if len(a) > 1 else 8)
    elif a[:1] == ["third"]:
        third()
    elif a[:1] == ["todo"]:
        todo()
    elif a[:1] == ["check"]:
        sys.exit(0 if check(a[1], a[2]) else 1)
    else:
        merge()
