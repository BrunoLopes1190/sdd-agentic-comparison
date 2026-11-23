# Full-text AI suggestion: one independent run (of three)

Used from 2026-11-23 for the three independent runs per record whose majority is shown to the author after their own decision (protocol §4.2 steps 7 and 9). The AI suggests; it never decides.

## Task

For each record key given to you, read the full text and suggest the full-text screening code.

## Read first

- `slr/protocol.md`: §1 (review questions) and §4 (criteria IC1–IC4, EC1–EC6, with the EC6 text).
- `slr/screening-sheet.md`: "Decision flow", "Pass 3 flow" and "Decision log".
- Per record: `slr/fulltext/<key>.txt` (pages separated by form feeds). Title and abstract: the row of `slr/pass3-queue.csv` with that key.

This is a **full-text** suggestion. For every record, first run `"/c/Users/Bruno Lopes/AppData/Local/Programs/Python/Python313/python.exe" slr/ft_view.py <key>` (Git Bash; plain `python` fails): it prints the same view the author decides on (section headings, contributions, method, evaluation, conclusion, term counts, length). Read all of it, not only the abstract or first page. Then search or read `slr/fulltext/<key>.txt` wherever the view does not settle the decision (task type, benchmark, page count, venue, another version). The full text often changes the picture (a short or position paper → EC3; the task is issue repair or tests only → EC6; the "specification" is formal methods without agents → EC2; another version of a record → EC4). Read more when these parts do not settle it.

## Independence

Do **not** open `slr/ft-ai-suggestions.csv`, `slr/ft-decisions.csv`, `slr/pass*-ai-suggestions.csv`, `slr/pass*-decisions.csv`, other files in `slr/ft-ai-runs/`, or `slr/extraction/`. Decide from the criteria and the text only.

## Rules

- Groups: (a) SDD with coding agents; (b) context mechanisms (AGENTS.md, CLAUDE.md, rules, skills, memory or instruction files) with coding agents; (c) evaluation or comparison of coding agents on software development tasks. Judge the group from the full text.
- EC5 and EC6 apply to group (c) only. Groups (a) and (b) are not narrowed by them.
- EC4: an earlier or duplicate version of another record in `slr/pass3-queue.csv` (look for a near-identical title or the same system name). Known candidate pairs: `rayyan-800486182`/`rayyan-800486847` (Needle in the Repo), `rayyan-800486075`/`rayyan-800486798` (SysSpec). EC4 goes on the less complete version; the published version is kept over the preprint.
- No full text: IC4 (should not occur; every key given has a text).
- Codes: Include, IC1, IC2, IC3, IC4, EC1, EC2, EC3, EC4, EC5, EC6. No Maybe.

## Output

After each record, append one JSON line to the output file named in your task (create it if missing):

`{"key": "...", "s": "<code>", "g": "a|b|c|" , "q": "<verbatim quote, at most 40 words, copied exactly from the full text>", "sec": "<section name, p. N>", "r": "<code>: <one-sentence reason>"}`

`g` is required for Include, and given when clear for exclusions. The quote must be copied character for character from `slr/fulltext/<key>.txt` (quotes are checked automatically).

Write the output with your file tools. Do not create helper scripts or files in `/tmp`. If you need one (e.g. in the scratchpad), put your run and batch in its name (e.g. `r2-b07-check.py`): other agents work at the same time in the same folders and a shared name overwrites theirs.

Reply only with one line: `done N of M`.
