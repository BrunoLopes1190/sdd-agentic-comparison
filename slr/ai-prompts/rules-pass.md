# Extraction drafts: rules pass (author's rules of 2026-11-23)

Used once on drafts whose verification rounds ended before the author's rules of 2026-11-23 were added to `draft-verify.md`. It changes only what those rules require, and writes a short doubt for each flagged field so the tool can show it to the author.

## Read first

- `slr/protocol.md` §5, §6 and the change-log rows of 2026-11-23.
- Per record: the current draft `slr/extraction/ai-drafts/<key>.json` (each field has `v`, `p`, `rev` with the rounds' reasons, and `warn`) and the full text `slr/fulltext/<key>.txt` (pages separated by form feeds).

## Rules to apply

1. `Evaluation (each configuration)`: keep every configuration and its metric values. Keep a quality or cost verdict only when the authors state a success criterion for it; otherwise replace the verdict with "no criterion stated by the authors". Remove any threshold or cut-off that the extractor chose (e.g. "≥50% resolved = works"). Do the same in `Comparison: result` if it rests on such a cut-off.
2. `Q12`: a study that proposes an approach and evaluates none is N/A.
3. `Nature of the study`: descriptive repository-mining studies (e.g. of AGENTS.md or CLAUDE.md files) are `Evaluates — repository mining …`.

Change nothing else.

## Doubts

For every field whose `warn` is not empty, after applying the rules, write `doubt`: one or two plain sentences **in Portuguese (pt-PT)**, at most 40 words, saying what is unclear and what the author must check or decide, using the `rev` reasons and the text (e.g. "O artigo não diz se as tarefas partem de um repositório vazio; confirma na secção 4 e escolhe new project ou existing code base."). If the rules settle the doubt, write `doubt` as an empty string.

## Output

Write `slr/extraction/ai-drafts-rules/<key>.json` for each record:

`{"key": "...", "fields": [{"f": "<field>", "v": "<new value, only if a rule changed it>", "why": "<what changed, only if v is given>", "doubt": "<pt-PT text or empty>"}]}`

List only the fields a rule changed or that have a `warn`. Do not create helper files in `/tmp`; if you need one in the scratchpad, put `rules-<first key>-` at the start of its name.

Reply only with one line: `done K records, C changed, D doubts`.
