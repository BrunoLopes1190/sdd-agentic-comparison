# Work plan

## Project charter

The charter follows the course template.
It covers the whole project, from PREPD, which is its planning phase, to the delivery of the dissertation.

### General information

- **Project name:** Spec-Driven for Agentic Software Development: A Characterisation and Comparison of Existing Approaches
- **Sponsor:** the supervisor
- **Institution:** ISEP, Department of Computer Engineering (DEI), Master's in Informatics Engineering (MEI)

### Project team

: Project team {#tbl:team}

| Role | Name | Institution | Department | E-mail |
|---|---|---|---|---|
| Student | Bruno de Abreu Lopes | ISEP | DEI | 1240441@isep.ipp.pt |
| Supervisor | Paulo Gandra de Sousa | ISEP | DEI | pag@isep.ipp.pt |

### Stakeholders

The stakeholders, their power and interest, and the engagement strategy are in the stakeholder table of the introduction.

### Scope

**Problem and objectives.**
The problem is stated in the introduction.
The main research question, the sub-questions SRQ1–SRQ5 and the objectives O1–O5 are in the research method chapter.

**Benefits.**
The benefits go to the teams and practitioners who adopt SDD, the users of the results.
The values of B1 and B2 are only known after the experiment, so they are measured in the dissertation.

: Benefits and how each one is measured {#tbl:benefits}

| # | Benefit | How it is measured |
|---|---|---|
| B1 | Cost: a team knows what each approach costs on the same project and avoids paying for structure that brings no gain | Difference in total cost between the approaches and the baseline, measured in the experiment |
| B2 | Quality: a team knows the quality each approach gives and can choose the one that is enough for its case | Difference in quality (acceptance tests, internal quality) between the approaches and the baseline |
| B3 | Time to choose: the comparative framework and the decision guide spare a team from trying each approach | Qualitative: the guide covers the selected approaches |

**Deliverables.**

- PREPD: state of the art (SLR): PRISMA diagram, extraction matrix and quality assessment, synthesis by review question and gap; extended abstract; PREPD document; presentation.
- Dissertation: comparative framework (O1); evaluation protocol with the reference project and its acceptance tests (O2); experiment data and results (O3, O4); decision guide (O5); dissertation report; presentation.

**Exclusions.**

- No new SDD approach is created.
- No study with human participants is carried out.
- Agents and models are not evaluated in themselves; they are a recorded factor.

### Time

Fixed dates are set by the course and cannot change.
Committed dates are the student's own and may move; any move is logged.

: PREPD milestones {#tbl:prepd-milestones}

| Date | Milestone | Type |
|---|---|---|
| 2026-11-04 | Email 1 to the supervisor: SLR protocol draft and open questions | Committed |
| 2026-11-16 | Email 2: work up to week 9, feedback and meeting requested | Committed |
| 2026-12-01 | Email 3: supervisor's corrections applied, SLR results | Committed |
| 2026-12-13 | Extended abstract draft sent to the supervisor | Committed |
| 2026-12-16 | Extended abstract submitted | Fixed |
| 2027-01-02 | Draft of the PREPD document and slides sent to the supervisor | Committed |
| 2027-01-06 | PREPD document and presentation submitted | Fixed |
| 2027-01-04 to 01-09 | Oral exam | Fixed |

The dissertation runs from February to June 2027.
Its phases follow the research method: protocol and reference project design, experiment runs, analysis, and writing.
Their milestones are set in the schedule.
The fixed dates of the dissertation (submission and defence) are not yet known.

### Cost

: Cost sources {#tbl:cost}

| Source | Cost |
|---|---|
| Claude Pro plan (personal, used for the experiment runs) | 22.14 € per month, counted only for the months of the experiment runs |
| Personal computer and local models | No new cost: existing equipment |
| MS Project | ISEP student licence |
| Zotero, Rayyan (free plan), Pandoc, GitHub | No cost |
| Student's work | Hours, not priced; estimated in the schedule |

### Assumptions

: Assumptions and the response if each one fails {#tbl:assumptions}

| # | Assumption | If it fails |
|---|---|---|
| A1 | The selected SDD approaches keep public documentation and a version that can be pinned until the runs end | Pin the last version used; record the change |
| A2 | The agents and models chosen stay available, on the same terms, during the run months | The agent is a recorded factor; the substitution is logged |
| A3 | The SLR finds at least two approaches that meet the inclusion criteria, besides the baseline | The comparison is narrowed and the limitation is stated |
| A4 | One run of the reference project takes a few hours, so the repetitions fit the schedule | Fewer repetitions or features; decided in the protocol |
| A5 | The supervisor gives feedback at the committed milestones | Work goes on with the stated assumptions |

### Restrictions

: Restrictions and their source {#tbl:restrictions}

| # | Restriction | Source |
|---|---|---|
| R1 | Fixed dates: extended abstract on 16 Dec 2026, PREPD on 6 Jan 2027; the dissertation dates are not yet known | Course |
| R2 | Budget limited to the personal Claude Pro plan and models that run on the author's hardware; the plan's usage limits cap the runs per day | Student |
| R3 | Individual work by one student; hours are not priced | Course |
| R4 | No Scopus, for lack of an ISEP licence | Institution |
| R5 | P.PORTO code of ethics, art. 10, on autonomous AI systems | Regulator (S5) |

### Risks

These are the risks of the whole project.
The threats to the validity of the experiment are in the research method chapter.
The detailed risk register, with monitoring, is kept with the schedule.

: Project risks {#tbl:risks}

| # | Risk | Probability | Impact | Response | Link |
|---|---|---|---|---|---|
| K1 | An approach changes a lot, or is abandoned, before the runs | High | Medium | Pin versions at selection; short run window; log the change | A1, T7 |
| K2 | The provider updates or retires a model during the runs | Medium | High | Fixed model identifiers; all runs in a short window; substitution logged | A2, T7 |
| K3 | Plan usage limits slow the runs and the schedule slips | High | Medium | Slack in the schedule for the runs; fewer repetitions as a last resort | R2, A4 |
| K4 | The reference project is too large to run, or too small to tell the approaches apart | Medium | High | Pilot run with the baseline before the experiment; adjust the features | A4 |
| K5 | The full SLR is late and delays the framework | Low | High | Protocol frozen; screening time-boxed; cut-off date | A3 |
| K6 | The supervisor has little availability | Medium | Low | Assumptions stated in each email; work goes on with them; talk in person if there is no reply | A5 |
| K7 | The student has less time than planned (individual work) | Medium | High | Committed milestones with buffer; the WBS marks what can be cut first | R3 |
| K8 | A deliverable is judged insufficient and has to be reworked | Medium | Medium | Drafts sent to the supervisor before each deadline (extended abstract, PREPD document, dissertation) | R1 |

### Approval

The charter is approved by the sponsor.
It is sent to the supervisor with email 2 (16 Nov 2026).

: Charter approval {#tbl:approval}

| Role | Name | Date | Signature |
|---|---|---|---|
| Student | Bruno de Abreu Lopes | | |
| Sponsor (supervisor) | Paulo Gandra de Sousa | | |

## Competency development plan

A dissertation is a long, mostly individual project.
Its success depends on transversal competencies as well as on technical knowledge.
This section diagnoses those competencies and plans how the weakest relevant ones will be developed.

### Diagnosis

The diagnosis used the course's self-assessment grid of 27 competencies.
Each competency was rated from 1 (very low) to 5 (very high) twice: its importance for this dissertation (I) and the author's current level (L).
The gap is I − L; a positive gap marks a competency to develop.
A hetero-assessment by a colleague is planned with the same grid; it is on hold until it is discussed with the supervisor.

: Competency self-assessment (I = importance, L = current level, gap = I − L) {#tbl:competencies}

| # | Competency | I | L | Gap | Hetero-assessment |
|---|---|---|---|---|---|
| 1 | Problem analysis and solving | 5 | 4 | 1 | Pending |
| 2 | Lifelong learning | 4 | 4 | 0 | Pending |
| 3 | Teamwork and collaboration | 2 | 5 | −3 | Pending |
| 4 | Drive for excellence | 5 | 3 | 2 | Pending |
| 5 | Adaptability and flexibility | 2 | 4 | −2 | Pending |
| 6 | Ethics and social responsibility | 5 | 3 | 2 | Pending |
| 7 | Foreign languages | 2 | 4 | −2 | Pending |
| 8 | Technical competencies in the field | 5 | 4 | 1 | Pending |
| 9 | Decision making | 4 | 3 | 1 | Pending |
| 10 | Time management | 5 | 2 | 3 | Pending |
| 11 | Risk taking | 4 | 3 | 1 | Pending |
| 12 | Oral communication | 5 | 4 | 1 | Pending |
| 13 | Written communication | 5 | 3 | 2 | Pending |
| 14 | Resilience | 4 | 3 | 1 | Pending |
| 15 | Active listening | 3 | 3 | 0 | Pending |
| 16 | Interpersonal relationships | 4 | 3 | 1 | Pending |
| 17 | Leadership | 2 | 4 | −2 | Pending |
| 18 | Creativity and innovation | 4 | 3 | 1 | Pending |
| 19 | Adaptation and flexibility | 2 | 4 | −2 | Pending |
| 20 | Critical thinking | 5 | 3 | 2 | Pending |
| 21 | Planning and organisation | 4 | 4 | 0 | Pending |
| 22 | Emotion management | 4 | 2 | 2 | Pending |
| 23 | Negotiation | 2 | 2 | 0 | Pending |
| 24 | Empathy | 4 | 2 | 2 | Pending |
| 25 | Assertiveness | 5 | 3 | 2 | Pending |
| 26 | Stress management | 5 | 4 | 1 | Pending |
| 27 | Proactivity | 4 | 4 | 0 | Pending |

Items 5 and 19 are near-duplicates in the original grid; both are kept as rated.

The most developed competency is teamwork and collaboration (level 5).
Problem solving, technical competencies, oral communication and stress management are rated 4 and are also highly important (5).
Time management has the largest gap (3).
Five competencies of importance 5 have a gap of 2: drive for excellence, ethics, written communication, critical thinking and assertiveness.

### Key competencies and objectives

Three key competencies were chosen.
The criteria were the size of the gap and the weight of the assessment item each one most affects.
They are listed by priority.

: Key competencies, objectives and the assessment item each one affects {#tbl:key-competencies}

| Priority | Competency | I / L | Objective | Assessment item affected |
|---|---|---|---|---|
| A | Critical thinking | 5 / 3 | A state of the art that compares studies rather than summarising them, with every source assessed | State-of-the-art review (20%) |
| B | Time management | 5 / 2 | Meet milestones M2 to M7 on their planned dates | Schedule of activities (20%) |
| C | Written communication | 5 / 3 | A document without writing errors, with sentences under 30 words and consistent citations | Technical/scientific accuracy and writing (15%) |

### Action plan

Each competency has two actions, each with a metric and a target.
Progress is checked in the weekly review (action B1) and recorded in the plan's progress log.

: Development actions, metrics and targets {#tbl:competency-actions}

| Competency | Action | Metric | Target |
|---|---|---|---|
| A. Critical thinking | A1. Apply the quality checklist to every included study and the 5W matrix to every grey-literature source | Share of included studies quality-assessed; share of grey sources rated with 5W | 100%; 100% |
| | A2. For each review question, write the Evidence → Limitation → Gap chain and a comparison table | Review questions with a comparison table | 4 of 4 |
| | (both) Independent screening of a sample by a second reviewer, if one is available | Cohen's kappa | ≥ 0.61 |
| B. Time management | B1. Fixed weekly review (Sunday, 20 min): update the plan status and progress log; choose the three priorities of the week | Weekly reviews done | ≥ 8 by 6 Jan 2027 |
| | B2. Estimate the hours of each product before starting it; record the actual hours when it is done | Deviation between estimated and actual hours | ≤ 25% |
| | (both) Milestones met | Milestones M2–M7 met on the planned date | 6 of 6 |
| C. Written communication | C1. Revise each chapter before marking it done, with a checklist: sentences over 30 words, consistent terms, every citation exists and was read | Sentences over 30 words per chapter; citations verified | 0; 100% |
| | C2. Ask the supervisor for comments on the writing of the extended abstract draft (M4) and apply them to the final document | Writing comments from the supervisor at M6 compared with M4 | Fewer at M6 |
