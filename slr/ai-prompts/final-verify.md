# Final verification of the author's checked extractions (two independent checks)

Used from 2026-11-26, after the author finished full-text screening. Every extraction and quality record the author checked and saved is verified twice more against the full text, by two independent agents (check 1 and check 2) that do not see each other's output nor the earlier AI draft. The AI never changes the author's values: it only flags fields, and the author decides each flag in `python slr/review.py` (protocol §4.2 step 7).

## Read first

- `slr/protocol.md`: §5 (quality: Q1–Q13, DARE, scoring rules), §6 (extraction form) and the change-log rows of 2026-11-11 and 2026-11-23.
- Per record:
  - the author's record `slr/extraction/final-verify/input/<key>.json` (fields `f`, `v`, `p`; `p` is the page or pages);
  - the full text `slr/fulltext/<key>.txt` (pages separated by form feeds, so page N is the text after the (N-1)th form feed).

Do **not** open anything else under `slr/extraction/` (not `slr/extraction/<key>.json`, not `ai-drafts*`, not the other check's folder), nor `slr/ft-*.csv`. The checks must stay independent of each other and of the earlier AI draft.

## Task

The author already checked every field. Look for what still matters: a wrong or missing number, metric, configuration or approach; a wrong page; a Q or DARE score that does not follow the §5 rules; a wrong nature of the study, publication type or SDD level; a claim the text does not support. **Do not flag** wording, style, language, length, or a value that is shorter than you would write but is not missing anything material. The bar: a careful second reviewer would want the author to look again.

For every field, decide:

- `confirmed`: right and supported by the text (not written to the output).
- `corrected`: wrong or incomplete in substance. Give the full corrected value.
- `uncertain`: the text does not settle it, or it is a judgement another careful reader could make differently (e.g. Q9, Q12, Q13, nature, SDD level). Give your best value.

Rules (the author's, from the protocol):
- Missing information scores No (0) in Q1–Q13. Q3–Q8 only for empirical studies (else N/A). Q13 for conceptual studies and for studies that propose an approach (also when they evaluate or compare it). DARE only for reviews that describe their search (sources and selection criteria); otherwise DARE1–4 are N/A.
- `Publication type` starts with one of: Journal, Conference, Workshop, Preprint (Preprint only when there is no published venue; a published paper read from arXiv keeps the venue type), then ` — ` and detail. Q11 follows it.
- `Nature of the study` starts with one of: Evaluates, Compares, Proposes an approach, Proposes an evaluation method, Conceptual, Review; optionally `; secondary: <one of these>`; then ` — ` and detail. Descriptive repository-mining studies are `Evaluates — repository mining …`.
- `Evaluation (each configuration)`: every configuration, the baseline included, gets its own quality and cost verdict judged on its own. A verdict only when the authors state a success criterion; otherwise the metric values and "no criterion stated by the authors". Never a threshold chosen by the extractor.
- `Q12`: N/A when the study proposes an approach and evaluates none; Partly when the authors' own approach is compared with external ones.
- Numbers must be copied from the text.

## Output

Process one record at a time. After each record write `slr/extraction/final-verify/c<N>/<key>.json` (N is your check number, given in your task), also when nothing is flagged:

```
{"key": "...", "model": "<your model>", "check": N, "checked": <number of fields read>,
 "fields": [{"f": "<field name, exactly as in the input>",
             "verdict": "corrected|uncertain",
             "sev": "high|low",
             "v": "<full proposed value, English, same format as the field, ready to replace the author's>",
             "p": "<page(s) of the evidence>",
             "quote": "<verbatim text from slr/fulltext/<key>.txt, one contiguous span, at most 50 words, copied exactly>",
             "where": "<section number and title, and page, e.g. '§4.2 Experimental Setup, p. 6' or 'Table 3, p. 8'>",
             "why": "<one sentence in English: what is wrong or unclear>",
             "doubt": "<pt-PT, at most 60 words: what is wrong or unclear, what to read, what to decide>"}]}
```

- `sev` is `high` when it changes a number, a metric, a configuration, a Q/DARE score, the nature, the publication type or the SDD level, or the answer to an RQ; `low` otherwise.
- `quote` is what lets the author settle the doubt quickly: pick the sentence or table row that decides it. If the evidence is an absence (e.g. no threats section), quote the nearest heading or sentence that shows it and say so in `why`.
- `doubt` is shown to the author as is: plain Portuguese (pt-PT), no jargon, e.g. "O artigo dá 14 tarefas na Tabela 2, não 12. Confirma na pág. 6 e corrige o tamanho." or "Não é claro se os autores criaram o Kiro; vê as afiliações na pág. 1 e decide Q12 (Não se sim, Sim se não)."

Write nothing else. Do not create helper scripts or files in `/tmp`. If you need one (e.g. in the scratchpad), put `c<N>-<first key>-` at the start of its name: other agents work at the same time.

Reply only with one line: `done K records, C corrected, U uncertain`.
