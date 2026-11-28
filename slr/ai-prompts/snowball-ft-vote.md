# Snowballing full-text AI filter: one independent run (of three)

Used from 2026-11-28 (protocol §4.2 step 8, change log 2026-11-28). The 521 snowballing candidates the author kept at title/abstract (Include or Maybe) get independent full-text runs: runs 1 and 2 on every candidate, run 3 only where they disagree. A candidate excluded by the majority (2 of 2, or 2 or 3 of 3) leaves the review with the majority code; the author reads at full text only the candidates the majority keeps, plus a blind random sample of the AI-excluded. **Strict rule (author, 2026-11-28):** Include only when the full text clearly meets every inclusion criterion and no exclusion criterion. A doubt of judgement excludes, with the code of the criterion most likely to fail. Reject what does not make sense for the review questions.

The launcher gives each agent only: "Read `slr/ai-prompts/snowball-ft-vote.md` and do it with RUN = R, BATCH = name" (e.g. `b05`, or `t02` for a run-3 batch).

## Task

You are one independent run. Repository: `C:\dev\PREPD\sdd-agentic-comparison` (in Git Bash: `/c/dev/PREPD/sdd-agentic-comparison`; work there). For each id in `slr/snowball/ft-batches/<BATCH>.txt`, read the full text and give the full-text screening code.

## Read first

- `slr/protocol.md`: §1 (review questions) and §4 (criteria IC1–IC4, EC1–EC6, with the EC6 text).
- `slr/screening-sheet.md`: "Decision flow", "Pass 3 flow" and "Decision log".
- Per candidate: title and abstract in `slr/snowball/queue.csv` (columns n, id, title, year, sources, abstract, url); full text in `slr/fulltext/<id>.txt` (pages separated by form feeds).

For every candidate, first run `"/c/Users/Bruno Lopes/AppData/Local/Programs/Python/Python313/python.exe" slr/ft_view.py <id>` (plain `python` fails): it prints the view the author decides on (section headings, contributions, method, evaluation, conclusion, term counts, length). Read all of it, then search or read `slr/fulltext/<id>.txt` wherever the view does not settle the decision (task type, benchmark, page count, venue, another version). The full text often changes the picture: a short or position paper → EC3; the task is issue repair or tests only → EC6; "specification" means formal methods without agents → EC2; general LLM code generation with no agent → IC1.

## Independence

Do **not** open `slr/snowball/decisions.csv`, `slr/snowball/prefilter.csv`, `slr/snowball/sample-50.csv`, `slr/snowball/pilot-*`, `slr/snowball/runs/`, other files in `slr/snowball/ft-runs/`, `slr/ft-*.csv`, `slr/pass*-decisions.csv`, `slr/pass*-ai-suggestions.csv` or `slr/extraction/`. Decide from the criteria and the text only.

## Rules

- Groups: (a) SDD with coding agents; (b) context mechanisms (AGENTS.md, CLAUDE.md, rules, skills, memory or instruction files) with coding agents; (c) evaluation or comparison of coding agents on software development tasks. Judge the group from the full text.
- EC5 and EC6 apply to group (c) only. Groups (a) and (b) are not narrowed by them.
- IC2: published from 2023-01-01.
- EC4: an earlier or duplicate version of another record: search `slr/snowball/queue.csv` and `slr/pass3-queue.csv` for a near-identical title or the same system name. EC4 goes on the less complete version; the published version is kept over the preprint.
- IC4: the text file is missing, empty or not the paper named in the title (wrong PDF).
- Codes: Include, IC1, IC2, IC3, IC4, EC1, EC2, EC3, EC4, EC5, EC6. No Maybe.

## Output

After each candidate, append one JSON line to `slr/snowball/ft-runs/r<RUN>-<BATCH>.jsonl` (create it if missing), in Bash with `cat >> ... <<'EOF'` … `EOF`:

`{"id": "sb-NNNNN", "s": "<code>", "g": "a|b|c|", "q": "<verbatim quote, at most 40 words, copied exactly from the full text>", "sec": "<section name, p. N>", "r": "<code>: <one-sentence reason>"}`

`g` is required for Include and given when clear for exclusions. The quote is the passage that settles the code and must be copied character for character from `slr/fulltext/<id>.txt` (checked by script). Every id of the batch exactly once, no other ids, valid JSON on each line (escape double quotes inside strings).

Do not edit any other file and do not write temporary or helper files (other agents run at the same time in the same folders).

Reply only with one line: `done N of M`.
