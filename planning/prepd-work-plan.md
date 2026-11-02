# PREPD work plan

Created 2026-11-02. What must be produced in PREPD, mapped to the methods taught and to the deadlines.
Course facts and sources: `course-materials/course-overview.md`. Current status: `admin/context.md`.
**[F]** = documented fact. **[I]** = interpretation. **[S]** = stated by the student or supervisor.

## 1. Principle

PREPD prepares the dissertation. It does not run it.
In PREPD, the scope, method and plan are fixed and the state of the art is done.
The experiment, the reference project and the choice of agents and models belong to the dissertation (2nd semester).
[S] The supervisor asked for the course to be done following the classes. Every product below names the class it comes from.

## 2. Deadlines and targets

| Date | What | Type |
|---|---|---|
| 2026-12-04 | Extended abstract draft sent to the supervisor, with a meeting request | Target [I]: [S] the supervisor reviews it until the 15th |
| 2026-12-07 to 12-11 | Meeting with the supervisor; revise | Target |
| 2026-12-16 | Extended abstract submitted | [F] Fixed |
| 2027-01-04 | Final document + slides ready (buffer: the exam may start this day) | Target |
| 2027-01-06 | ZIP with two PDFs (report + presentation) submitted | [F] Fixed |
| 2027-01-04 to 01-09 | Oral exam, 10-min presentation | [F] Fixed; [S] date announced end of December |

## 3. Decisions taken for PREPD

| # | Decision | Basis | Status |
|---|---|---|---|
| D1 | The submitted formalisation (2026-10-14, with citations) is the reference text for title, problem, objectives and RQ | [S] | Taken |
| D2 | State of the art = **full SLR** (Kitchenham & Charters 2007): protocol written and frozen before the search, changes logged; reproducible search; IC/EC; formal quality assessment of every included study; extraction form piloted; PRISMA 2020; synthesis by RQ; threats to validity of the review | [S] student's choice; `week-04/systematic-literature-review-v1.md` slides 8, 11–22; formalisation field f | Taken |
| D2a | Single-reviewer mitigation [I]: a second person (supervisor or a colleague) independently screens a random sample of records and assesses a sample of included studies; agreement measured (Cohen's kappa); disagreements resolved and logged | Kitchenham & Charters (2007) | Confirm with the supervisor who the second reviewer is |
| D3 | arXiv preprints are an SLR source, justified by the field's age. Tool documentation, repositories and practitioner articles are **not** SLR studies: they are analysed separately, with a documented procedure and the 5W matrix, as input to the comparative framework (RQ1) | `week-03/source-evaluation-matrix.docx`; grading question on grey literature | Proposed |
| D4 | Citation style author-date (Harvard), as in the template and the submitted formalisation; `doc/ieee.csl` to be replaced | `.dotx`; formalisation | Proposed; confirm with the supervisor |
| D5 | PREPD document follows the template structure (front matter, lists, references) | `.dotx`; grading item "Document structure" | Proposed |
| D6 | No supervisor-imposed restriction on GenAI; all use is logged in `doc/ai-usage.md` and declared in the document | [S]; `ai-generated-content-guidelines.txt` | Taken |
| D7 | Experimental runs, when they happen (dissertation), may only use the student's personal Claude Pro plan; there is no token budget | [S] | Constraint (see §7) |

## 4. Products and the method each one comes from

| # | Product | Method / class | Feeds grading item | Due |
|---|---|---|---|---|
| P1 | Competency self-diagnosis + hetero-assessment by a colleague; ≥ 3 key competencies with objectives; ≥ 2 actions each, with metrics | Week 5: `competencies.pdf`, `self-assessment.docx`, `assessment.docx` | Schedule (20) | 13 Nov |
| P2 | Research design: main RQ (formalisation) + sub-RQs typed by Shaw; Oates process figure (strategies: design and creation + experiment; data: documents, observation, logs; analysis: quantitative + qualitative); validity threats and bias controls | Week 3: `research-methods-t.md`, `research-process-figure.pptx`, TP activity I | Objectives/method (10) | 13 Nov |
| P3 | SLR protocol (frozen before the search): review RQs, concept blocks and synonyms, string per database, databases and justification, search cut-off date, IC/EC, quality assessment checklist, extraction form, synthesis plan, second-reviewer procedure (D2a), protocol change log | Week 4: SLR module + mini-SLR tutorial; Kitchenham & Charters (2007) | State of the art (20) | 13 Nov |
| P4 | Pilot search on one database (inspect 20–30 results); pilot the extraction form; refine and log changes; then freeze the protocol | Week 4: tutorial slide 20, steps 1–2 | State of the art | 13 Nov |
| P5 | Final search on all databases; exports; search log (query, date, filters, n); deduplication; title/abstract and full-text screening with reasons; second-reviewer sample and kappa; backward/forward snowballing; PRISMA 2020 diagram | Week 4; Wohlin (2014); Page et al. (2021) | State of the art | 27 Nov |
| P6 | Quality assessment of every included study; extraction matrix; critical synthesis by RQ; Evidence → Limitation → Gap → RQ → Contribution chain; threats to validity of the review | Week 4: slides 22–28 | State of the art; Background (10) | 4 Dec |
| P7 | Preliminary comparative framework of SDD approaches, from the SLR plus the documented analysis of tool documentation (D3) (RQ1 / O1) | Week 4 synthesis; Macedo (2026) dimensions | State of the art | 4 Dec |
| P8 | Stakeholder analysis (power × interest) and problem interpretation from several perspectives | Week 2 charter; grading notes | Problem interpretation (10) | 27 Nov |
| P9 | Project charter for the dissertation | Week 2: `project-charter-template-v01.docx` | Schedule (20) | 27 Nov |
| P10 | Planning approach (predictive / adaptive / hybrid) with justification | Week 8: `planning-approach-v1.md` | Schedule | 4 Dec |
| P11 | WBS by life-cycle phase aligned with the research method, plus WBS dictionary (acceptance and progress criteria) | Week 8: `wbs-concepts-v01.md`, `wbs-template-v01.pptx` | Schedule | 4 Dec |
| P12 | Schedule (Gantt) Feb–Jun 2027: durations, milestones, dependencies; cost estimate; risk register; monitoring and control | Weeks 9–12 (pending); grading notes | Schedule | 11 Dec |
| P13 | Ethics: chosen code (one, applied in full); ALLEA principles; position on P.PORTO art. 10; licences and terms of the tools; FAIR data plan; conflicts of interest; GenAI use | Week 6: `t06.md`, `tp06.pdf` | Ethics (10) | 27 Nov |
| P14 | "Use of AI-generated content" section, from `doc/ai-usage.md` | `ai-generated-content-guidelines.txt` | Accuracy; Ethics | each delivery |
| P15 | Extended abstract | Condensed P2, P6–P8, P12, P13 [I] | Supervisor review | 4 Dec draft; 16 Dec |
| P16 | Final PREPD document | All of the above | All document items | 4 Jan |
| P17 | 10-min slides, paginated, readable; rehearsed with Q&A | Grading sheet "Presentation" | Presentation (25%) | 4 Jan; rehearse before the exam |

Planning outputs P10–P12 are refined as the week 9–12 materials arrive. Add each new module's method to this table.

### Proposed structure of the PREPD document [I]

Mapped to the grading items. To confirm against the week 9–13 materials and with the supervisor.

1. Front matter: abstract, keywords, ToC, lists of figures, tables and acronyms.
2. Introduction: context, problem, stakeholders, objectives, RQs, expected contributions.
3. Research method: Oates figure, strategies, data, analysis, validity threats.
4. State of the art: review method, results (PRISMA), synthesis by RQ, comparative framework, gap.
5. Proposed solution and evaluation design: what will be built and how it will be evaluated, at the level bounded in §5.
6. Ethical considerations.
7. Work plan: charter elements, planning approach, WBS, schedule, cost, risks, monitoring and control, competency plan.
8. Use of AI-generated content.
9. References.

## 5. What is bounded now vs. left to the dissertation

| Topic | Bounded in PREPD | Left to the dissertation |
|---|---|---|
| Problem, objectives, main RQ | Fixed (submitted formalisation) | — |
| Sub-RQs and review RQs | Defined | — |
| Research method | Strategies, data generation, analysis, validity threats | Detailed experimental procedures |
| State of the art | Full SLR done, with a documented cut-off date | Update search before writing the dissertation |
| SDD approaches | Candidate list and inclusion criteria from the review | Final selection and versions to pin |
| Agents and models | Constraint stated (D7); the choice is a recorded factor | Choice |
| Reference project | Required characteristics (proposal §7.1) | Design, briefing, acceptance tests, build |
| Metrics | Dimensions (cost, functional and internal quality, conformance, human effort) | Final metrics, definition of "total cost", main metric |
| Conditions and repetitions | Design principles (baseline, same briefing, fixed tests) | Number of conditions and repetitions |
| Experiment runs | None | All, outside this repo (`experiment/protocol.md`) |
| Decision guide (O5) | How it will be built and evaluated | Production |
| Plan | Full plan for Feb–Jun 2027 | Monitoring and re-planning |

## 6. Open questions for the supervisor

Send them with the extended abstract draft, or earlier by email.

1. Full SLR (D2): who can act as second reviewer for the sample (D2a)? Will the supervisor review the protocol before it is frozen (target 13 Nov)?
2. arXiv preprints in the SLR, with tool documentation analysed separately (D3): acceptable?
3. P.PORTO Code art. 10 (autonomous systems using AI): is ethics committee review required for experiments with coding agents and no human participants?
4. Citation style and template for the PREPD document (D4, D5); page limit?
5. Expected content and length of the extended abstract.
6. Experiments limited to a personal Claude Pro plan (D7): acceptable, given that it constrains the agents that can be tested?

## 7. Risks for PREPD

| Risk | Cause | Impact | Response |
|---|---|---|---|
| Full SLR not finished by 4 Dec | Searches not started; no full paper read yet; full SLR adds quality assessment and a second reviewer | Weak extended abstract; 20% item at risk | Freeze the protocol by 13 Nov; time-box screening; cut-off date; if late, report the SLR up to full-text screening in the extended abstract and finish synthesis for the final document |
| No second reviewer available | Single student | Reduced reliability of the SLR | Ask the supervisor early (§6 Q1); otherwise state it as a threat to validity |
| Formal databases return few hits | Most SDD work is arXiv or grey literature | Thin PRISMA corpus | Include arXiv and grey literature by protocol (D3), justified |
| Planning chapter depends on modules up to week 12 | Course calendar | 20% item done in a rush | Draft P9–P11 early; refine as modules arrive |
| Christmas break between 16 Dec and 6 Jan | Calendar | Less supervisor feedback | Get feedback in the December meeting; submit by 4 Jan |
| Field changes weekly | New preprints and tool versions | State of the art goes stale | Explicit cut-off date; update in the dissertation |
| No explicit grading of the extended abstract | Undefined | Effort misdirected | Treat it as a draft of the final document |
| Single vendor for runs and for the writing assistant | D7; Claude used to assist this work | Perceived conflict of interest; agent choice constrained | Declare in the ethics section; record the agent as a factor |
| Pro plan usage limits; no per-token cost visible | D7 | "Total cost" hard to measure; fewer runs | Define a cost proxy in the dissertation; state as a limitation |
| Over-reliance on AI | Heavy assistant use | Misconduct; weak oral defence | Follow the SLR-module rules on AI use; read every source; log use |
