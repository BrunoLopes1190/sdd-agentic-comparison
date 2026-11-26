# Contingency: fewer research questions

Prepared 2026-11-26, before email 3 (plan §6 Q13). Use it only if the supervisor asks for fewer research questions.
The week 3 TP activity asks for "1-2 questions that capture the work's essence" (`course-materials/week-03/research-methods-tp.pdf`, slide 2). No course rule sets a maximum.

## Fixed points (do not change)

- **Main research question:** from the approved formalisation (D1). It stays as it is.
- **Objectives O1–O5:** from the approved formalisation. They stay; only their mapping to questions changes.
- **SLR review questions RQ1–RQ4** (`slr/protocol.md`): review questions, not research questions of the dissertation. The protocol is frozen and screening and extraction were done with them. If the supervisor also asks to cut them, argue this first (the week 4 SLR tutorial itself uses three); any change is a logged protocol change.

## Current set (for reference)

| | Question (short) | Shaw type | Objective | Answered in |
|---|---|---|---|---|
| SRQ1 | Which SDD approaches exist and what do they prescribe? | Characterisation | O1 | PREPD |
| SRQ2 | How do they differ? | Characterisation | O1 | PREPD |
| SRQ3 | How to measure total cost and quality reproducibly? | Method for analysis | O2 | PREPD (design level) |
| SRQ4 | How do they compare with each other and a baseline on the same project? | Design, evaluation or analysis of an instance | O3, O4 | Dissertation |
| SRQ5 | Which approach to use in which situation? | Method for analysis | O5 | Dissertation |

## Variant A (recommended): main question + two sub-questions

Each sub-question keeps a single Shaw type and the PREPD/dissertation split stays clear.

| | Question | Shaw type | Objectives | Strategy | Answered in |
|---|---|---|---|---|---|
| SRQ1 (SRQ1 + SRQ2) | Which SDD approaches for development with agents exist, what does each one prescribe (artefacts, phases, human review points), and how do they differ from one another? | Generalisation or characterisation: what are the varieties of X, and how are they related? | O1 | SLR and documented analysis of tool documentation; comparative framework | PREPD |
| SRQ2 (old SRQ4) | How do the selected approaches compare with each other, and with a baseline without a structured specification, in total cost and quality on the same reference project? | Design, evaluation or analysis of a particular instance: how does X compare to Y? | O2, O3, O4 | Design and creation (protocol, reference project, metrics) + experiment | Designed in PREPD, answered in the dissertation |

What happens to the rest:
- **Old SRQ3 (how to measure)** becomes the means to answer the new SRQ2: the evaluation protocol, reference project and metrics are a design-and-creation artefact and a contribution (O2). It is still bounded in PREPD at the design level.
- **Old SRQ5 (decision guide)** becomes a contribution (O5), built from the answers to SRQ1 and SRQ2. It stays in the WBS as deliverable 1.5.2.
- Contributions to list: comparative framework (O1), reproducible evaluation protocol with reference project (O2), comparison results (O3, O4), decision guide (O5).

## Variant B (minimum): main question only

If the supervisor wants a single question: keep the main question and drop the sub-questions.
Its three parts become the structure: (i) which approaches exist, (ii) how they differ, (iii) how they affect total cost and quality on the same project.
Map O1 to parts (i)–(ii), O2–O4 to part (iii); O5 (decision guide) is a contribution.
Weakness: Shaw typing per question is lost (the main question mixes three types), so explain the typing per part in the text.

## What has to change (both variants; line numbers as of 2026-11-26)

| File | Where | Change |
|---|---|---|
| `doc/chapters/03-research-method.md` | Lines 8–11 (intro: "five sub-questions") | Two sub-questions (A) or "three parts of the main question" (B) |
| same | Table `tbl:srq`, lines 15–21 | Replace with the table of the chosen variant |
| same | Lines 23–29 (review questions → SRQ; what PREPD answers) | RQ1 answers SRQ1; RQ2 and RQ3 inform the design of the protocol, the means to answer SRQ2; RQ4 the gap. PREPD answers SRQ1 and designs the protocol; the dissertation answers SRQ2 and builds the decision guide |
| same | Line 41 (framework "answers SRQ2") | "answers SRQ1" (A) |
| same | Line 42 ("main question and SRQ1–SRQ5") | "main question and SRQ1–SRQ2" (A) |
| same | Lines 45–46 (strategies ↔ SRQ3, SRQ5, SRQ4) | Design and creation produces the protocol, reference project and metrics, and later the decision guide (contributions O2, O5); the experiment answers SRQ2 |
| `doc/chapters/07-work-plan.md` | Line 31 ("SRQ1–SRQ5") | "SRQ1–SRQ2" (A) or "the main question" (B) |
| same | WBS dictionary 1.1.2 (line 207) | No change in A ("sub-questions typed by Shaw" still true); in B: "main question split into three parts" |
| same | WBS dictionary 1.2.4 (line 217) "(SRQ1, SRQ2)" | "(SRQ1)" |
| same | WBS dictionary 1.3 (line 218) "(SRQ3)" | "(O2; means for SRQ2)" |
| same | WBS dictionary 1.4 (line 223) "(SRQ4)" | "(SRQ2)" |
| same | WBS dictionary 1.5 (line 227) "(SRQ4, SRQ5)" | "(SRQ2; decision guide, O5)" |
| Extended abstract (section 3) | Main RQ and sub-RQs | Write the sub-question list as one short paragraph or table so it can be swapped in minutes |
| `planning/prepd-work-plan.md` | §6 Q13; §5 row "Sub-RQs and review RQs"; progress log | Close Q13 with the decision; log the change |
| `admin/context.md` §0 | Status | Note the decision |
| `doc/ai-usage.md` | New line | If Claude applies the change |

No change needed:
- `doc/figures/research-process.pptx`/`.png`: the box says only "Research questions" (checked 2026-11-26).
- `doc/figures/wbs.pptx`/`.png`: no SRQ labels; "1.5.2 Decision guide" stays as a deliverable.
- `slr/protocol.md`: review questions map to objectives (O1, O2, O5), not to SRQs.
- `doc/chapters/01-introduction.md`, `06-ethics.md`: no SRQ references.
- The formalisation on the platform: main question and objectives unchanged.

Effort: about 2–3 h for variant A, about 3–4 h for B (more text to rewrite). Best done on the next feedback slot of plan §2.4, before the extended abstract is finalised.

## Talking points for the meeting

- The main question is the one approved in the formalisation; the sub-questions only split it so that each one has one Shaw type, one objective and one strategy.
- SRQ1–SRQ2 are answered in PREPD; SRQ4–SRQ5 only after the experiment. Fewer questions are fine; variant A keeps the traceability with two.
- The SLR's RQ1–RQ4 are review questions; the protocol is frozen and the review is done with them.
