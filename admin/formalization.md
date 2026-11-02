# PREPD formalisation: proposed answers

11 October 2026 · Bruno Lopes

## How to use this document

Each section corresponds to a field of the formalisation form (FormalizacaoMoodlePt.pdf), with the text to paste into the platform. The texts are in English and aligned with the document DissertationProposal-1240441.docx sent to the supervisor on 6 October. The outstanding decisions and the plan up to submission are at the end.

Three conditions before submitting:

- The formalisation only becomes editable after all members of the supervision team accept the invitation on the platform.
- The supervisor must approve the content before submission.
- The submission deadline is 14 October 2026.

## a) Title

**Chosen title (6 October 2026):** Spec-Driven for Agentic Software Development: A Characterisation and Comparison of Existing Approaches

Check whether it matches the title shown on the platform: an error was found in the title recorded there (see decision 2).

## b) Supervision team

- **Supervisor:** the proposing lecturer. The platform shows the supervision as accepted, but there was no email notification; confirm that the form is already editable.
- **Co-supervisor:** optional; must be from ISEP, hold a doctorate or be a specialist.
- **Supervisor (external):** only if an external organisation is involved; must be a different person from the supervisor.

## c1) Problem

Proposed text:

> AI coding agents now carry out complete development tasks: they analyse repositories, plan changes, modify multiple files and run tests. Spec-Driven Development (SDD) proposes that the specification should be the central artefact of this work, giving the agent persistent and structured context [1], [7].
>
> In little more than a year, several approaches have emerged that implement SDD in different ways, such as GitHub Spec Kit, OpenSpec, Kiro and the BMAD Method [1], [3], [5]. They differ in the artefacts they require, the phases of the process and the points of human review [5].
>
> A team that wants to adopt SDD has no comparable evidence today on which to base its choice [2]. The available comparisons are almost all grey literature [1], and the academic works are conceptual [7], taxonomic [5] or evaluate a single approach in isolation. The only controlled comparison found measures determinism and hallucination detection on small tasks, not cost or human effort [6].
>
> The problem to be addressed is the lack of a common characterisation of the existing SDD standards and of a comparison of their results when applied to the same project [2], [5].

## c2) and c3) Characteristics of a complex problem

Answer to c2: Yes. It is suggested to tick characteristics 1, 2, 3 and 5, which have solid justification. Characteristics 4 and 6 are defensible but weaker.

| # | Characteristic | Tick | Justification (text to paste) |
| --- | --- | --- | --- |
| 1 | Involves wide-ranging or conflicting technical issues | Yes | The SDD approaches use processes, artefacts and tools that are not compatible with each other. Comparing them requires a common framework and an evaluation protocol that separates the effect of the approach from the effect of the agent, the model and the operator. |
| 2 | Having no obvious solution | Yes | Evidence on SDD is scarce and partly contradictory [2]. Proponents report less rework [7], while a controlled study on repository context files found higher inference cost without an overall gain in task success [4]. It is not known which approach pays off in which situation. |
| 3 | Addressing problems not encompassed by current standards and codes | Yes | There is no formal standard for specifications written for coding agents. The existing SDD approaches are de facto conventions defined by vendors or communities, and they change within months [1]. |
| 4 | Involving diverse groups of stakeholders | No | — |
| 5 | Includes many component parts or subproblems, involving multiple disciplines | Yes | The problem combines requirements engineering, software architecture, LLM-based coding agents, software quality and empirical research methods. It breaks down into identifying the standards, designing a reference project, instrumenting the experimental runs, analysing the results and building a decision guide. |
| 6 | Having significant consequences in a variety of contexts | No | — |

## d) Objectives

Proposed text:

> **Main objective:** to identify and characterise the existing Spec-Driven Development standards for development with agents, and to compare their effect on the total cost and the quality of development when applied to the same project.
>
> **Specific objectives:**
>
> 1. Identify the existing SDD standards and characterise them in a common comparative framework: what each one prescribes and how it can be used [5].
> 2. Design a reproducible evaluation protocol, with a reference project and cost and quality metrics defined in advance.
> 3. Apply each approach to the same example project, together with a baseline without a structured specification [4].
> 4. Compare the results of the approaches, with each other and with the baseline.
> 5. Produce a decision guide on which approach to use in which situation.
>
> **Research question:** Which Spec-Driven Development approaches exist for development with agents, how do they differ, and how do they affect the total cost and the quality of development when applied to the same project?

## e) to j) Yes answers and How

**The answer is Yes in all six fields.** The PREPD rule requires design and development, so h), i) and j) cannot be left as No.

| Field | Question | Answer | How (text to paste) | Objective covered |
| --- | --- | --- | --- | --- |
| e | Will there be interpretation of the problem to be solved? | Yes | The causes of the problem (the recent proliferation of SDD approaches without comparative evaluation), the stakeholders and their interests, and the consequences of choosing an approach without evidence are analysed. The problem is examined from several perspectives (cost, quality, human effort and platform dependence), confronting partly contradictory evidence from the literature [4], [7]. | Framing |
| f | Will there be systematisation of existing knowledge? | Yes | A structured state of the art with a documented protocol: research questions, search strings, inclusion and exclusion criteria, and a PRISMA flow of the selection. The main sources are Scopus, Web of Science, IEEE Xplore and the ACM Digital Library. Tool documentation and repositories are included as primary sources for the approaches themselves [3], assessed with explicit quality criteria. The result is the identification of the existing SDD standards and a comparative framework describing what each one prescribes and how it can be used [1], [5]. | O1 |
| g | Will there be evaluation of different approaches? | Yes | At two levels. In the state of the art, existing ways of evaluating SDD and coding agents (benchmarks, controlled experiments [4], [6] and industrial comparisons) are compared to justify the design of the evaluation. In the experiment, a set of SDD approaches selected with explicit criteria is applied to the same reference project and compared with each other and with a baseline without a structured specification. | O3, O4 |
| h | Will there be design of a solution? | Yes | A reproducible evaluation protocol is designed, including the reference project, a neutral requirements brief, acceptance tests, the experimental conditions, cost and quality metrics defined in advance, and rules for human intervention. A decision guide is designed that relates SDD approach, type of task and context. | O2, O5 |
| i | Will there be construction of a solution? | Yes | The reference project is implemented with each selected approach and with the baseline, using the coding agents each approach supports. The execution environment and scripts for automatic metric collection are built, and the artefacts are kept in a repository to allow replication. The decision guide is produced from the results. | O3 |
| j | Will there be evaluation of the solution? | Yes | The protocol is evaluated by its repeatability (variation between repeated runs of the same condition) [6] and by its ability to distinguish the approaches. The decision guide is evaluated by applying it to tasks not used to build it and checking whether its recommendation matches the observed results. Threats to validity are discussed. | O4 |

### Link to the research method

If the supervisor or the reviewer asks for the method: *Research method: design and creation and experiment strategies [8], with data generated from documents and observation, and quantitative and qualitative analysis.*

## k) Bibliographic references

Same list as in the Word document (1 to 7), in the same order; the numbers correspond to the [X] citations in the text. Confirm the publication status before submitting; most are preprints.

[1] Böckeler, B. (2025). Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl. martinfowler.com. https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html

[2] Díaz, J., Gayoso, J., Cimminio, A., Pérez, J. (2026). Spec-Driven Development for Agentic Software Engineering: Harnessing Human-Agent Teamwork. arXiv:2609.00252. [Link](https://arxiv.org/html/2609.00252v1)

[3] GitHub. Spec Kit. https://github.com/github/spec-kit

[4] Gloaguen, T., Mündler-Sasahara, N., Müller, M. N., Raychev, V., Vechev, M. (2026). Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents? arXiv:2602.11988. [Link](https://arxiv.org/abs/2602.11988)

[5] Macedo, S. O. de (2026). From Prompt to Process: a Process Taxonomy and Comparative Assessment of Frameworks Supporting AI Software Development Agents. arXiv:2606.04967. [Link](https://arxiv.org/abs/2606.04967)

[6] Panda, S. (2026). Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code. arXiv:2606.30689. [Link](https://arxiv.org/html/2606.30689)

[7] Piskala, D. B. (2026). Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants. arXiv:2602.00180. [Link](https://arxiv.org/abs/2602.00180)

[8] Oates, B. J. (2005). Researching Information Systems and Computing. Sage. (not included in the Word document)

[9] Shaw, M. (2002). What Makes Good Research in Software Engineering? International Journal on Software Tools for Technology Transfer, 4(1), 1-7. (not included in the Word document)

## Open decisions (close by 12 October)

| # | Decision | Options | Recommendation | Why it matters |
| --- | --- | --- | --- | --- |
| 1 | Language of the fields | English in all; Portuguese in all | English in all (already applied in this document) | The title, the problem, the objectives and the Word document sent to the supervisor are already in English; mixing languages in the form looks careless |
| 2 | Final title | "Spec-Driven for Agentic…"; "Spec-Driven Development for Agentic…" | Confirm with the supervisor when correcting the platform error | Without "Development", the expression is incomplete in English; the formalisation title must match the one on the platform |
| 3 | Characteristics to tick in c2/c3 | 1, 2, 3 and 5; add 4; add 6 | 1, 2, 3 and 5 | The reviewer may question each one; 4 and 6 have weaker justification |
| 4 | Approaches named in g) | The four as examples; generic only | The four, with "for example" | Consistent with the Word document and does not close the selection before the state of the art |
| 5 | Metrics in j) | Examples; closed list | Examples | The total cost and the final metrics are left for the state of the art |
| 6 | Artefact repository | Public; private shared with the panel | Decide | "Public" would be a verifiable commitment; the current text only says "a repository to allow replication" |
| 7 | Co-supervisor | Yes; no | Decide with the supervisor | Must be invited and accept before submission |
| 8 | References in k) | Current list of 9; add or remove | Current list, after you have read the abstracts | You will be questioned on them in the review and in the defence |

## Plan up to submission

| When | What to do | How | Result |
| --- | --- | --- | --- |
| 11 to 12 Oct | Check the status on the platform | Log in to projetos.dei.isep.ipp.pt; confirm that the supervisor appears as accepted, that the form is editable, and copy the title exactly as it appears there | Know whether there is a blocker before investing more time |
| 12 Oct | Compare this document with the Word document | Apply the verification criteria below, field by field | List of differences to correct |
| 12 Oct | Read the three core sources | Abstract and introduction of Macedo, Díaz et al. and Gloaguen et al.; note one sentence from each that supports the gap | Be able to defend c1, c3 and the references |
| 12 Oct | Close decisions 1 to 8 | Table above | Final text of all fields |
| 12 Oct (end of day) | Ask the supervisor for approval | Short email with the final text of the fields (or a PDF of this document) and an explicit request for approval; the formalisation requires prior approval from the supervisor | Approval or comments |
| 13 Oct | Incorporate comments and fill in the platform | Paste field by field and review the formatting after pasting | Completed form |
| 13 Oct | Submit | Do not leave it until the last day | Margin for platform failures |
| 14 to 24 Oct | Follow the review | If the formalisation comes back with change requests, correct and resubmit | Formalisation accepted |

## Verification criteria

1. Title, research question, main objective and the five specific objectives are identical, word for word, to those in the Word document.
2. Each objective has at least one answer in e) to j) that delivers it ("Objective covered" column).
3. No statement depends on a source that is not in k) or that you have not read.
4. Terminology is consistent: "approach" for each way of doing SDD, "standards" for the set of conventions to be identified.
5. Nothing promises more than one semester allows: number of approaches, repository, metrics.
6. No sentence exceeds 30 words, which is an assessment criterion of the course.

## Final check before submitting

- [x] Proposal approved and assigned on the platform
- [ ] Supervision accepted and form editable (confirmed by you on the platform)
- [ ] Title error on the platform resolved and final title confirmed
- [ ] Decisions 1 to 8 closed
- [ ] Three core sources read
- [ ] Final text approved by the supervisor
- [ ] Fields pasted and formatting reviewed on the platform
- [ ] Submission made by 13 October (deadline: 14)
