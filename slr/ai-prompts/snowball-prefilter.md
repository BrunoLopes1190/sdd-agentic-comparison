# Snowballing AI pre-filter: one independent run (of three)

Used from 2026-11-27 (protocol §4.2 step 8). Three independent runs per candidate; a candidate excluded by the majority (2 or 3 of 3) leaves the review with the majority code. The author screens the rest blind and a random sample of 50 AI-excluded candidates. This is the only screening step where an AI decision removes records, so when in doubt, **Include**.

## Task

For each candidate id given to you, read its title and abstract in `slr/snowball/candidates.csv` and suggest the title/abstract screening code.

## Read first

- `slr/protocol.md`: §1 (review questions) and §4 (criteria IC1–IC4, EC1–EC6, with the EC6 text).
- `slr/screening-sheet.md`: "Decision flow", "Pass 3 flow" and "Decision log".

## Independence

Do **not** open `slr/snowball/prefilter-votes.csv`, other run files in `slr/snowball/`, `slr/ft-*.csv`, `slr/pass*-*.csv` or `slr/extraction/`. Decide from the criteria, the title and the abstract only.

## Rules

- Groups: (a) SDD with coding agents; (b) context mechanisms (AGENTS.md, CLAUDE.md, rules, skills, memory or instruction files) with coding agents; (c) evaluation or comparison of coding agents on software development tasks.
- EC5 and EC6 apply to group (c) only.
- IC2: published from 2023-01-01 (use the `date` column). Many backward references are older or are not about coding agents at all (general LLM papers, classic software engineering, datasets): exclude them with IC2 or IC1.
- IC3: not in English.
- No abstract: decide on the title only if it clearly fails IC1 or IC2; otherwise Include (the author decides).
- EC3: editorial, keynote, poster, abstract only, tutorial; also books, theses, web pages and software releases without a paper (`type` column helps).
- Do not use EC4 or IC4 (checked later by the author).
- Codes: Include, IC1, IC2, IC3, EC1, EC2, EC3, EC5, EC6. No Maybe.

## Output

After each candidate, append one JSON line to the output file named in your task (create it if missing):

`{"id": "sb-NNNNN", "s": "<code>", "g": "a|b|c|", "r": "<code>: <one-sentence reason>"}`

Write the output with your file tools. Do not create helper scripts. Reply only with one line: `done N of M`.
