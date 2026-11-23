# Extraction and quality draft: verification round (one of three)

Used from 2026-11-23. Each AI extraction draft is checked three times against the full text, each round by a fresh agent that starts from the previous round's output. The author then checks the result in the tool (protocol §4.2 step 7). Fields the rounds were unsure about, or kept changing, are flagged to the author.

## Read first

- `slr/protocol.md`: §5 (quality: Q1–Q13, DARE, scoring rules) and §6 (extraction form), and the change-log rows of 2026-11-11 and 2026-11-23.
- Per record: the previous round `slr/extraction/ai-drafts-r<N-1>/<key>.json` and the full text `slr/fulltext/<key>.txt` (pages separated by form feeds; the `p` of each field is the page).

## Task

For every field of the draft, check the value against the full text and the protocol, and give a verdict:

- `confirmed`: the value is right and supported by the text.
- `corrected`: the value was wrong or incomplete in substance (wrong number, missing metric, wrong Q score, wrong nature, unsupported claim). Give the corrected value and say what was wrong in `why`. Do not change wording or style only: that is not a correction.
- `uncertain`: the text does not settle the field, or it is a judgement another careful reader could make differently (e.g. Q9, Q12, Q13, nature of the study, SDD level). Give your best value and say in `why` what is unclear, so the author knows where to look.

Rules:
- Missing information scores No (0) in Q1–Q13 (§5). Q3–Q8 only for empirical studies (else N/A). Q13 for conceptual studies and for studies that propose an approach (also when they evaluate or compare it), per §5. DARE only for reviews that describe their search.
- `Publication type` starts with one of: Journal, Conference, Workshop, Preprint (Preprint only when there is no published venue; a published paper read from arXiv keeps the venue type), then ` — ` and detail.
- `Nature of the study` starts with one of: Evaluates, Compares, Proposes an approach, Proposes an evaluation method, Conceptual, Review; optionally `; secondary: <one of these>`; then ` — ` and detail.
- `Evaluation (each configuration)`: every configuration, the baseline included, gets its own quality and cost verdict judged on its own (§6), not against the baseline or the other configurations. A verdict is given only when the authors state a success criterion; otherwise keep the metric values and write "no criterion stated by the authors" instead of a verdict. Never set a threshold yourself (author's rule of 2026-11-23).
- `Q12`: a study that proposes an approach and evaluates none is N/A (author's rule of 2026-11-23). When the authors' own approach is compared with external baselines or other approaches, Q12 is Partly (§5: "Partly when this applies to only some of the approaches").
- `Nature of the study`: descriptive repository-mining studies (e.g. of AGENTS.md or CLAUDE.md files) are `Evaluates — repository mining …` (author's rule of 2026-11-23).
- Numbers must be copied from the text; if a value was rebuilt (jumbled table), say so in Notes.
- Keep every field, in the same order, with its `p` (page or pages).

## Output

Process one record at a time. After each record, write `slr/extraction/ai-drafts-r<N>/<key>.json`:

`{"key": "...", "model": "Claude Opus 5.5 (subagent)", "round": N, "fields": [{"f": "...", "v": "...", "p": "...", "verdict": "confirmed|corrected|uncertain", "why": "...", "doubt": "..."}]}`

`why` may be empty only for `confirmed`. For every `uncertain` field also give `doubt`: one or two plain sentences **in Portuguese (pt-PT)**, at most 40 words, saying what is unclear and what the author must check or decide (e.g. "O artigo não diz se as tarefas partem de um repositório vazio; confirma na secção 4 e escolhe new project ou existing code base."). The tool shows it to the author. Write nothing else. Do not create helper scripts or files in `/tmp`. If you need one (e.g. in the scratchpad), put the round and your first record key in its name (e.g. `r2-800486644-apply.py`): other agents work at the same time in the same folders and a shared name overwrites theirs.

Reply only with one line: `done K records, C corrected, U uncertain`.
