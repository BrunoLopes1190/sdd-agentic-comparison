# Snowballing AI pre-filter: task given to each agent (one batch × one run)

Used from 2026-11-27 with `snowball-prefilter.md`. The launcher gives each agent only: "Read `slr/ai-prompts/snowball-prefilter-task.md` and do it with RUN = R, BATCH = NNN" (for a re-run of missing ids: also IDS = the list and OUT = the retry file). The first 10 agents (b001–b003 and r1-b004) got the same text inline.

You are one independent run of an AI pre-filter for a systematic literature review (snowballing candidates, title/abstract screening). Repository: C:\Users\BIMMS-BLopes\Desktop\PREPD\sdd-agentic-comparison (work there; use absolute paths or cd into it).

Your full instruction is `slr/ai-prompts/snowball-prefilter.md`: read it first and follow it exactly, including the files it tells you to read and the files it forbids.

This run:
- Batch: `slr/snowball/batches/bNNN.txt` (100 candidate ids, one per line), or only the ids listed as IDS if given.
- Output file: `slr/snowball/runs/rR-bNNN.jsonl`, or OUT if given (one JSON line per candidate, the format in the instruction).
- Read the candidates 20 at a time (output is truncated above ~30 000 characters), e.g. in Bash:
  `cd /c/Users/BIMMS-BLopes/Desktop/PREPD/sdd-agentic-comparison && grep -F -f <(sed -n 1,20p slr/snowball/batches/bNNN.txt) slr/snowball/candidates.csv`
  then lines 21,40 and so on. Columns: id, openalex, doi, title, year, date, type, source, seeds, abstract.
- Write the output by appending, in groups of at most 10 candidates, e.g. `cat >> slr/snowball/runs/rR-bNNN.jsonl <<'EOF'` ... `EOF`. Every id exactly once; no other ids; valid JSON on each line (escape double quotes inside strings).
- Do not open any other file in `slr/snowball/runs/`, the `pilot-r*.jsonl` files or `prefilter.csv`. Do not edit any other file.
- Do not write temporary files (other agents run at the same time and share the scratchpad): read the candidates straight from the grep output. (Added 2026-11-27 after r3-b007 read another agent's temporary file; its check caught the wrong ids.)

Reply only with one line: `done N of M`.
