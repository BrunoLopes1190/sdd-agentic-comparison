# Extraction and quality draft: first draft (group (c))

Used from 2026-11-23 for group (c) records whose AI majority suggestion is Include. The draft is then checked in rounds with `draft-verify.md`, and the author checks every field in the tool (protocol §4.2 step 7).

## Read first

- `slr/protocol.md`: §1 (review questions), §5 (quality: Q1–Q13, DARE, scoring rules), §6 (extraction form) and the change-log rows of 2026-11-11 and 2026-11-23.
- Per record: the full text `slr/fulltext/<key>.txt` (pages separated by form feeds) and its row in `slr/pass3-queue.csv` (title, abstract). An example of a finished draft: any file in `slr/extraction/ai-drafts/` with `"rounds": 3`.

## Fields, in this order

Reference, Year, Publication type, Author affiliation, Nature of the study, Approach(es): name and version, Artefacts prescribed, Phases of the flow, Human review points, Parts exercised, SDD level, Task type, Size, Domain, Team profile, Cost metrics, Functional quality metrics, Internal quality metrics, Human effort metrics, Other outcome metrics, How metrics are collected, Evaluation (each configuration), Comparison: design, Comparison: result, Comparison: did the method work, Conclusions: limitations and gaps, Notes, Q1 … Q13, DARE1 … DARE4.

## Rules

- Copy values from the text; give the page(s) in `p`. Fields that do not apply are `N/A`. Group (c) studies are evaluations of coding agents: the approach fields usually describe the agents or workflows compared, and `SDD level` is usually `Not classifiable`.
- `Publication type` starts with Journal, Conference, Workshop or Preprint (Preprint only when there is no published venue), then ` — ` and detail. `Nature of the study` starts with Evaluates, Compares, Proposes an approach, Proposes an evaluation method, Conceptual or Review; optionally `; secondary: <one of these>`; then ` — ` and detail. Repository-mining studies are `Evaluates — repository mining …`.
- `Evaluation (each configuration)`: one entry per configuration (approach or baseline + agent + model), the baseline included, each judged on its own. A quality or cost verdict only when the authors state a success criterion; otherwise "no criterion stated by the authors". Never set a threshold yourself.
- Quality: Yes (1) / Partly (0.5) / No (0) / N/A, each with a short reason. Missing information is No. Q3–Q8 only for empirical studies. Q12: an author who created an evaluated approach counts as its vendor; a study that evaluates no approach is N/A. Q13 for conceptual studies and studies that propose an approach. DARE only for reviews that describe their search.
- Notes: reporting inconsistencies with the source of each value, data or replication package, pre-registration, programming language.

## Output

Process one record at a time. After each, write `slr/extraction/ai-drafts-r0/<key>.json`:

`{"key": "...", "model": "Claude Opus 5.5 (subagent)", "fields": [{"f": "...", "v": "...", "p": "..."}]}`

Do not create helper files in `/tmp`; if you need one in the scratchpad, put `r0-<first key>-` at the start of its name.

Reply only with one line: `done K records`.
