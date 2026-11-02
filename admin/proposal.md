# Dissertation Proposal: Spec-Driven Development with agents

Oct 2, 2026 · @Mr. Bruno

**Provisional title:** Spec-Driven for Agentic Software Development: A Characterisation and Comparison of Existing Approaches

**Status:** draft for discussion with the supervisor. Section 5 presents four focus variants; section 11 lists the open decisions.

## 1. The idea in a few words

Coding agents already plan, change several files and run tests with little human intervention. Spec-Driven Development (SDD) proposes that the specification, rather than the prompt or the code, should be the central artefact of that work. In little more than a year, several approaches have emerged that put this idea into practice in different ways: GitHub Spec Kit, OpenSpec, Kiro, BMAD Method, Tessl and the AGENTS.md format.

A team that wants to adopt SDD currently has no way of choosing based on evidence. The approaches differ in the artefacts they require, the number of phases, the human review points and what happens to the specification once the code exists. The available comparisons are almost all grey literature. The academic work is conceptual, taxonomic, or evaluates a single approach or property. One study on context files even shows that more documentation can increase cost by more than 20% without, in general, improving the success rate.

This dissertation proposes to study SDD approaches in two steps. First, characterise them within a common comparative framework: which "standards" exist, what each one prescribes and how it can be used. Then, apply them to the same example project, with the agents each one supports, and compare the results against a baseline without a structured specification. The focus is the spec-first level: the specification written before the code of a new project. The comparison measures the total cost and quality of development, with metrics defined in advance.

The expected outcome is a comparative framework of the approaches, a reproducible evaluation protocol with its reference project, and a decision guide indicating which approach pays off in which situation.

**Research question:** What Spec-Driven Development approaches exist for agentic development, how do they differ, and how do they affect the total cost and quality of development when applied to the same project?

## 2. Context and problem

**The problem is the lack of comparable evidence for choosing an SDD approach.** The tools have multiplied faster than the studies that evaluate them.

### 2.1 Where the problem comes from

The supervisor's original proposal, "Agentic Software Development Lifecycle", describes the shift from assistants that suggest code to agents that carry out complete tasks. It identifies as challenges token consumption, repeated context ingestion, unpredictable cost and the need for human supervision. It points to SDD, and GitHub Spec Kit in particular, as a possible response.

SDD starts from a simple idea: if the agent receives persistent, structured context, it makes fewer mistakes and needs fewer iterations. How to do this is not standardised. Böckeler distinguishes three levels: *spec-first* (the specification precedes the code for a task), *spec-anchored* (the specification is maintained as the system evolves) and *spec-as-source* (only the specification is edited by humans) ([Böckeler, 2025](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)).

### 2.2 What is already known and what is missing

| Work | Type | What it shows | What it leaves open |
| --- | --- | --- | --- |
| [Böckeler (2025)](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | Grey literature, analysis of 3 tools | Fixed workflows fit poorly with problems of different sizes; reviewing a lot of Markdown is burdensome; agents ignore part of the instructions | No measurement |
| [Piskala (2026)](https://arxiv.org/abs/2602.00180) | Conceptual preprint with case studies | Presents the three levels of rigour and a decision framework | No experimental comparison between tools |
| [Macedo (2026)](https://arxiv.org/abs/2606.04967) | Preprint; 6-dimension taxonomy applied to 6 frameworks | No framework covers all dimensions well; there is a trade-off between process depth and portability | Points to the lack of full-process benchmarks and calls for empirical evaluation |
| [Díaz et al. (2026)](https://arxiv.org/html/2609.00252v1) | Preprint; multivocal review | SDD as the basis for human-agent teamwork | States that there is not yet peer-reviewed evidence or an established common vocabulary |
| [Gloaguen et al. (2026)](https://arxiv.org/abs/2602.11988) | Preprint; controlled experiment on context files | Context files do not, in general, improve the success rate and increase inference cost by more than 20% on average | Does not evaluate complete SDD workflows |
| [Panda (2026)](https://arxiv.org/html/2606.30689) | Preprint; controlled experiment with traceSDD, Spec Kit and OpenSpec, two models | Requirement citations in the code make it possible to detect hallucinations but reduce determinism; functional correctness is the same across all conditions | Small Python tasks; does not measure token cost or human effort |
| [Taghavi and Bhavani (2026)](https://arxiv.org/abs/2604.05278) | Preprint; evaluation of an extension to Spec Kit | Small quality gains with repository context | Evaluates a single approach |
| [Alenezi (2026)](https://arxiv.org/abs/2607.16680) | Preprint; design science on published evidence | Argues for SDD as necessary governance in an enterprise context | Does not collect new data |
| [Tanaka et al. (2026)](https://arxiv.org/html/2608.30572v1) | Preprint; report on use in teaching, 14 students | Implementation throughput increases; students tend to move ahead without fully understanding the code | No concurrent control group; compares with previous years |
| [Uvik (2026)](https://uvik.net/spec-driven-development-benchmark/) | Industry benchmark, 4 frameworks and control, 50 tasks | Between 40 and 42 tasks accepted with SDD against 36 without a specification; cost per accepted task between 2.35 and 4.23 dollars | Not peer-reviewed, private code, author with a commercial interest |

The gap lies in comparing approaches under full conditions of use. There are taxonomies, evaluations of a single approach in isolation, and one controlled study comparing three frameworks on determinism and hallucination detection. The search carried out did not find a peer-reviewed study comparing SDD approaches on the same project in terms of cost, quality and human effort.

There is also an unexplained tension: SDD advocates promise less rework, while the evidence on context files suggests that more documentation can cost more with no gain.

### 2.3 Who is affected

- **Development teams:** invest time writing and reviewing specifications without knowing whether the return is worth it.
- **Organisations:** bear the token cost and the risk of platform lock-in.
- **Tool authors and the research community:** have no common evaluation protocol.

If the problem is not solved, adoption will continue to be driven by fashion or personal preference. The cost of a poor choice is wasted specification effort and specifications that diverge from the code.

## 3. Existing SDD approaches

**There are at least six candidate approaches, which differ mainly in the weight of the process and in what happens to the specification after implementation.** This table is preliminary; the first phase of the dissertation consists of systematising it.

| Approach | Origin and licence | Prescribed workflow | Main artefacts | Distinguishing feature |
| --- | --- | --- | --- | --- |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | GitHub, MIT | Constitution (once per project); Specify, Plan, Tasks, Implement, Converge (per feature) | constitution.md, spec.md, plan.md, tasks.md | Most complete and heaviest process; project principles fixed up front |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | Fission-AI, MIT | Explore (optional), Propose, Apply, Archive | proposal.md, specs in delta format, design.md, tasks.md | Lightweight; also designed for existing code; updates the specs on archiving |
| [Kiro](https://kiro.dev/docs/specs/) | AWS, proprietary product | Requirements, Design, Tasks | requirements.md, design.md, tasks.md | Integrated into its own environment; three documents per feature |
| [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) | BMad Code, MIT | Clarify, Plan, Build and Verify, Learn and Adjust | Briefs, specifications, architecture | Specialised perspectives (product, architecture, UX, development, testing) |
| Tessl | Tessl; in private beta in October 2025 | Spec editing, code generation | Specs as source; code marked as generated | The only one of the three tools analysed by [Böckeler (2025)](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) that explores *spec-as-source* |
| [AGENTS.md](https://openai.com/index/agentic-ai-foundation/) | Open format, Agentic AI Foundation (Linux Foundation) | None | A single Markdown file of instructions and context | Not a process; it is the minimum of persistent context and serves as a lightweight condition |

At present, "standard" means de facto convention rather than formal standard. Of those listed, AGENTS.md is the only format under neutral governance. The rest are single-vendor or community projects, with versions that change within a few months.

Dimensions that the final comparative framework should cover, starting from the taxonomy of [Macedo (2026)](https://arxiv.org/abs/2606.04967): specification, context, roles, execution, validation and portability. To these are added Böckeler's level of rigour and the human effort required in each phase.

### 3.1 How to separate what counts as an SDD "standard"

What is called SDD mixes three layers. The unit of comparison in this dissertation is the first; the other two are recorded as characteristics of each approach.

| Layer | What it is | Examples | Role in the study |
| --- | --- | --- | --- |
| Method | Sequence of phases and review points, from specification to implementation | Spec Kit, OpenSpec, BMAD Method and Kiro workflows | Object of comparison |
| Artefact format | Structure and notation of the documents | spec.md, delta specs, requirements.md, AGENTS.md | Characteristic described in the comparative framework |
| Execution tool | CLI, IDE, agent and model that execute the method | Kiro, GitHub Copilot, Claude Code | Factor recorded in each run |

An approach is included in the study if it meets four criteria:

1. It prescribes persistent specification artefacts, written before the code.
2. It defines a repeatable workflow from specification to implementation.
3. It has public documentation and a version that can be pinned.
4. It can carry out the example project.

For each approach, its generality is also recorded: whether it is agent-independent or tied to an environment, and whether it was designed for a particular type of project (new or existing, small or large). A format without a method, such as AGENTS.md, is not an approach; it is included only as a minimal-context condition.

## 4. Research questions and objectives

**The main question is divided into three sub-questions, which correspond to the supervisor's two requests: study the options and compare results.**

| # | Sub-question | Type (Shaw, 2002) | How it is answered |
| --- | --- | --- | --- |
| RQ1 | What SDD approaches and "standards" exist and what dimensions distinguish them? | Characterisation: "What are the varieties of X, how are they related?" | Multivocal literature review and analysis of the tools' documentation |
| RQ2 | How is each approach used in practice: what artefacts, phases and human review points does it require? | Characterisation and development method | Application of each approach to the example project, with the process recorded |
| RQ3 | How do the approaches affect the total cost and quality of development on the same project, compared with a baseline without a structured specification? | Evaluation: "How does X compare to Y?" | Controlled experiment with quantitative metrics and qualitative analysis |

Each focus variant in section 5 adds a fourth sub-question of its own.

### Objectives

1. **O1.** Systematise existing SDD approaches into a comparative framework with explicit dimensions (answers RQ1).
2. **O2.** Design a reproducible evaluation protocol: reference project, conditions, metrics and data collection procedure.
3. **O3.** Implement the reference project with each selected approach and with the baseline, recording the process (answers RQ2).
4. **O4.** Compare the approaches in terms of cost, quality, conformance with the requirements and human effort (answers RQ3).
5. **O5.** Produce a decision guide indicating which approach suits which type of task and context.

The objectives are achievable by one student in one semester because the project is small, the number of approaches is limited to three or four and metric collection is automated.

## 5. Focus variants

**All variants share the same core (RQ1 to RQ3) and differ in the fourth question, which defines where the dissertation goes deeper.** The choice rests with the student and the supervisor. The variants can be combined, but each combination increases the number of runs.

**Chosen focus (2 October 2026):** variant A, limited to the spec-first level. The work addresses the gap pointed out by Macedo (full-process benchmarks and empirical evaluation are missing) and by Díaz et al. (evidence and measurement frameworks are missing). System evolution (variant B) is out of scope; C and D remain as possible extensions.

### Variant A. Direct comparison of frameworks

- **Focus:** three or four complete approaches applied to a new (greenfield) project, plus the baseline.
- **RQ4:** For which type of task does each approach justify the specification effort it requires?
- **Rationale:** it is the most direct response to the supervisor's request. It fills the gap pointed out by Macedo and by Díaz et al.: public empirical evaluation of the approaches is missing.
- **Contribution:** controlled, reproducible comparison between SDD approaches in terms of cost, quality and human effort.
- **Risk:** a descriptive result ("A was better than B") without explaining the cause.

### Variant B. Evolution and divergence between specification and code

- **Focus:** the example project has two phases, initial construction and a series of change requests. What happens to the specification over time is measured.
- **RQ4:** How does each approach behave when the system evolves, and how far does the specification diverge from the code?
- **Rationale:** the distinction between *spec-first* and *spec-anchored* can only be observed during maintenance. Divergence between specification and code is the first recurring risk identified by Macedo. Teams' real work is mostly the evolution of existing code.
- **Contribution:** evidence on the sustainability of SDD beyond the first delivery.
- **Risk:** the example project has to be larger, and a divergence measure needs to be defined.

### Variant C. Which artefacts explain the difference

- **Focus:** after comparing the approaches, they are broken down into their artefacts (requirements, design or architecture, task list, constitution) and one is removed at a time.
- **RQ4:** Which specification artefacts contribute to the outcome and which only add cost?
- **Rationale:** it resolves the tension with Gloaguen et al., who show additional context with no gain. It revives the axis of the earlier proposal (format and granularity of requirements, architectural documentation with ADRs and C4), now anchored in real approaches.
- **Contribution:** moves from "which is best" to "why", and supports tool-independent recommendations.
- **Risk:** more experimental conditions; requires limiting the decomposition phase to two approaches.

### Variant D. Local models and cost

- **Focus:** the same approaches run with a cloud model and with a local open-weights model via Ollama.
- **RQ4:** Does a suitable SDD approach bring the performance of local models closer to that of cloud models?
- **Rationale:** it is the *cost-aware, local-first* axis of the supervisor's original proposal. It links SDD to cost and data sovereignty.
- **Contribution:** an indication of when a local model is sufficient if the specification is good.
- **Risk:** hardware dependency; local models may fail complete tasks and leave little to compare; doubles the runs.

### Comparison of the variants

| Criterion | A. Frameworks | B. Evolution | C. Artefacts | D. Local models |
| --- | --- | --- | --- | --- |
| Alignment with the supervisor's feedback | Full | High | Medium | Medium |
| Alignment with the original proposal | Medium | Medium | Low | High |
| Novelty relative to the literature | Medium | High | High | Medium |
| Experimental effort | Low | Medium | High | High |
| Execution risk | Low | Medium | Medium | High |
| Link to the student's experience in requirements and architecture | Medium | Medium | High | Low |

### Suggested starting point

A as the mandatory core, with B or C as the deeper study. Variant A on its own ensures a complete dissertation and responds to the supervisor. B costs little if the example project is designed from the outset with change requests. C makes the most of the experience in requirements and architecture. D works better as an optional variable than as a focus, because of the hardware risk.

## 6. Research method

**The work combines two strategies from Oates' (2005) model: *design and creation* for the artefacts and *experiment* for the comparison.**

| Process element (Oates) | Choice | Rationale |
| --- | --- | --- |
| Literature review | Multivocal review: academic databases (ACM DL, IEEE Xplore, Scopus, arXiv) and grey literature | The field is recent; tool documentation and practice reports are a necessary source. Grey sources are assessed with the 5W matrix given in PREPD |
| Strategy 1 | Design and creation | Designs and builds the comparative framework, the evaluation protocol and the reference project |
| Strategy 2 | Experiment | Manipulates the SDD approach (independent variable) and measures cost, quality and effort (dependent variables) |
| Data generation | Documents and observation | Agent execution logs, specification artefacts, generated code, test results and the researcher's diary |
| Analysis | Quantitative and qualitative | Descriptive statistics and comparison between conditions; thematic analysis of the process observations |

### Phases of the work

1. **Systematisation.** Literature review and analysis of the tools. Outcome: comparative framework and selection criteria for the approaches to be tested.
2. **Design.** Definition of the reference project, the neutral requirements briefing, the acceptance test suite and the measurement protocol.
3. **Construction.** Setting up the execution environment and automatic metric collection. Pilot run with one approach.
4. **Execution.** Implementation of the project with each approach and with the baseline, with repetitions.
5. **Analysis and synthesis.** Comparison of the results, discussion of threats to validity and writing of the decision guide.

### Bias control and threats to validity

| Threat | Mitigation |
| --- | --- |
| Non-determinism of the models | Several repetitions per condition; reporting of dispersion and not just means |
| A single researcher writes the specifications and learns across conditions | Single requirements briefing, fixed before execution; alternating order of conditions; rules for human intervention defined in advance |
| Tools change version | Versions pinned and recorded; execution concentrated in a short period |
| Generalisation from one project | Tasks of different types within the project; stated limits |
| Subjective quality assessment | Acceptance tests written beforehand and hidden from the agent; automatic static analysis |
| Task already known to the model | Project in an original domain, not taken from public benchmarks |

## 7. Evaluation

**The evaluation consists of implementing the same small project with each SDD approach, keeping the starting requirements and acceptance tests fixed, and comparing the results using metrics defined in advance.**

### 7.1 Example project

A small web application with a REST API, persistence and authentication, for example a room booking system. The planned size is 8 to 10 features, described in a neutral requirements briefing, identical for all conditions.

The features cover different task types, to allow analysis by type:

- simple CRUD;
- business rule with constraints (for example, booking conflicts);
- cross-cutting requirement (authentication and authorisation);
- integration between modules;
- in variant B, three to five change requests on the system already built.

Each feature has acceptance tests written before the experiment and never shown to the agent.

**Characteristics the example project must have to be usable**

| # | Characteristic | Why |
| --- | --- | --- |
| 1 | Neutral briefing, in natural language, without the format of any approach | No approach starts with an advantage |
| 2 | Executable by all approaches and agents: common stack, no dependency on an IDE | All of them must be able to run the same project |
| 3 | Automatically verifiable by external acceptance tests (via the API), independent of the internal structure of the code | Functional quality is measured in the same way for code generated in different ways |
| 4 | New project, with no prior code | It is the spec-first scenario |
| 5 | Size that forces architectural decisions but allows repetition: 8 to 10 features, one run in a few hours | Too small does not distinguish approaches; too large cannot be repeated |
| 6 | Tasks of different types: CRUD, business rule, cross-cutting requirement, integration | Shows where each approach pays off |
| 7 | Explicit, testable architectural constraints | Measures whether the agent respects what the specification fixes |
| 8 | Some deliberately ambiguous or incomplete requirements | Shows whether each approach's clarification phase detects them |
| 9 | Original domain, not taken from benchmarks or public tutorials | Reduces the risk of the model already knowing the solution |
| 10 | Reproducible: initial repository, pinned versions, containerised environment | Someone else can repeat the study |

### 7.2 Conditions

| Condition | Description | Role |
| --- | --- | --- |
| C0. Baseline | The agent receives the briefing directly as a prompt | Control |
| C1. Minimal context | Briefing plus an AGENTS.md file | Separates the effect of "some context" from the effect of "a process" |
| C2. Spec Kit | Full GitHub Spec Kit workflow | Heavyweight approach |
| C3. OpenSpec | Full OpenSpec workflow | Lightweight approach |
| C4. Third approach | Kiro or BMAD Method, to be decided | Approach with its own environment or with specialised perspectives |

Fixed across all conditions: the briefing, the acceptance tests, the technology stack, the initial repository and the rules for human intervention. The agent and the model are not fixed: each approach runs with the agents it supports, and the agent is recorded as a factor. Kiro runs in its own environment, which is acceptable in this design. To separate the effect of the approach from the effect of the agent, at least one agent should be common to several approaches.

The number of runs is the product of conditions, agents and repetitions. With five conditions, one agent and three repetitions, that is 15 runs; with two agents it is 30.

### 7.3 Metrics

| Dimension | Metric | Collection |
| --- | --- | --- |
| Cost | Input and output tokens; cost in euros; execution time; number of agent iterations | Agent logs |
| Functional quality | Percentage of acceptance tests passing | Hidden test suite |
| Internal quality | Defects and *code smells*, complexity, duplication, test coverage | Static analysis (for example, SonarQube) |
| Architectural conformance | Violations of the architectural rules defined in the briefing | Automated architecture tests |
| Conformance with the specification | Requirements implemented, omitted and not requested; in variant B, divergence between specification and code after each change | Traceability matrix completed by inspection |
| Human effort | Time spent writing and reviewing specifications; number of interventions; volume of artefacts to review | Stopwatch, diary and line count |
| User experience | Difficulties, agent deviations from the instructions, friction points | Researcher's diary, qualitative analysis |

### 7.4 Success criterion for the dissertation

The dissertation meets its objective if the protocol makes it possible to distinguish the approaches in at least one dimension and if someone else can repeat it. A result in which no approach outperforms the baseline is valid and relevant, given what Gloaguen et al. observed with context files.

## 8. Expected results and contributions

**The dissertation delivers four artefacts, three of which are reusable by third parties.**

| Deliverable | Description | Who benefits |
| --- | --- | --- |
| Comparative framework of SDD approaches | Dimensions, artefacts, workflow and level of rigour of each approach | Teams evaluating adoption; researchers |
| Evaluation protocol and reference project | Briefing, acceptance tests, execution rules and collection scripts, published in a repository | Anyone wishing to repeat the study with other tools or models |
| Experimental results | Cost, quality and effort data by approach and by task type | Research community; tool authors |
| Decision guide | Recommendations on which approach to use in which situation, with the limits of the evidence | Development teams |

The scientific contribution is a controlled, reproducible comparison between SDD approaches on the same project, in terms of cost, quality and human effort. The search carried out did not find an equivalent peer-reviewed study. The practical contribution is to reduce wasted specification effort by indicating where SDD pays off and where it does not.

## 9. Scope, assumptions, constraints and risks

### Out of scope

- The full lifecycle (deployment, operation, long-term maintenance). The study covers specification through to tested implementation.
- Studies with teams or human participants. The researcher is the sole operator, unless decided otherwise (see section 11).
- Development of a new SDD tool.
- Evolution and maintenance of the specification (spec-anchored and spec-as-source levels). Ranking of agents or models: they are a recorded factor, not the object of study.

### Assumptions and constraints

| Type | Description |
| --- | --- |
| Assumption | The selected approaches remain available and usable during the execution period |
| Assumption | A project of 8 to 10 features is enough to observe differences between approaches |
| Constraint | Limited token budget, to be defined with the supervisor |
| Constraint | A single researcher, one semester of execution |
| Constraint | Fixed PREPD and dissertation deadlines |

### Risks

| Risk | Cause | Impact | Response |
| --- | --- | --- | --- |
| Tool changes or is discontinued | Rapidly evolving field | Results are no longer reproducible | Pin versions; favour open-source tools |
| Token cost higher than expected | Heavy workflows and repetitions | Fewer repetitions or fewer conditions | Pilot run to estimate cost; reduce conditions before reducing repetitions |
| Differences between approaches are not detectable | Project too simple or high variance | Weak conclusions | Include tasks of varying difficulty; increase repetitions on discriminating tasks |
| Researcher bias | The same operator in all conditions | Reduced internal validity | Fixed, recorded intervention protocol; alternating order |
| Publication of an equivalent study | Very active topic | Reduced novelty | Monitor the literature; differentiate through the deeper-study variant |

## 10. Schedule

**The PREPD dates are fixed; those for the second semester are indicative and depend on the schedule of the Dissertation course unit.**

| Period | Activity | Milestone | Type |
| --- | --- | --- | --- |
| By 9 Oct 2026 | Finalisation of the proposal with the supervisor; assignment and approval | Proposal approved | Fixed |
| By 14 Oct 2026 | Invitation to the supervisor and submission of the formalisation | Formalisation submitted | Fixed |
| Oct to Nov 2026 | Literature review; preliminary comparative framework; project charter | State of the art written | Indicative |
| Nov to Dec 2026 | Design of the protocol and the example project; pilot run with one approach | Protocol validated | Indicative |
| 16 Dec 2026 | Extended abstract | Submission | Fixed |
| 6 Jan 2027 | Final PREPD document | Submission | Fixed |
| 4 to 9 Jan 2027 | Oral examination | Assessment | Fixed |
| Feb to Mar 2027 | Building the environment, acceptance tests and automatic collection | Environment ready | Indicative |
| Mar to May 2027 | Execution of the conditions and of the deeper-study variant | Data collected | Indicative |
| May to Jun 2027 | Analysis, decision guide and writing | Dissertation submitted | Indicative |

The pilot run in December serves to estimate the cost per run and to adjust the number of conditions before the second semester.

## 11. Questions to frame the proposal

**These decisions define the size and focus of the work. The first six should be settled before the formalisation.**

### To decide with the supervisor

| # | Question | Options | What changes |
| --- | --- | --- | --- |
| 1 | What is the deeper-study variant? | Decided: A, with a spec-first focus; C and D as possible extensions | Defines RQ4, the size of the example project and the number of runs |
| 2 | What counts as an SDD "standard"? | Only frameworks with a process; also context formats such as AGENTS.md; also requirements notations | Defines the scope of RQ1 and whether condition C1 exists |
| 3 | How many approaches, and which, are included in the experiment? | Two (Spec Kit and OpenSpec); three; four | Each approach adds three or more complete runs |
| 4 | Is the third approach Kiro or BMAD Method? | Kiro (own environment, different agent); BMAD (specialised perspectives, same agent) | Kiro breaks control of the agent; BMAD keeps it but is heavier |
| 5 | Is the cloud versus local axis kept? | Out; secondary variable in some of the tasks; focus (variant D) | Doubles runs and requires hardware |
| 6 | Is there a token budget and who covers it? | ISEP; company; self-funded | Limits conditions and repetitions |
| 7 | Is the main contribution the comparison or the decision guide? | Experimental evidence; practical artefact | Changes the relative weight of analysis and design in the document |
| 8 | Is publication of a paper planned? | Yes; no | Requires more statistical rigour and brings execution forward |

### To decide on the example project

| # | Question | Options | What changes |
| --- | --- | --- | --- |
| 9 | Is the project greenfield only or does it include evolution? | Decided: initial construction only (spec-first) | With evolution, variant B comes at almost no additional cost |
| 10 | Is the project original or does it reuse an existing one? | Original domain; a course unit project; public benchmark | A public benchmark may be known to the model |
| 11 | What is the stack? | The one most familiar to the student; the most common in training data | Affects the baseline quality of the generated code in all conditions |
| 12 | Which agents and models are included? | The agent recommended by each approach; the same two or three agents across all approaches; a combination of both | Crossing agents and approaches separates the two effects but multiplies the runs |

### To decide on measurement

| # | Question | Options | What changes |
| --- | --- | --- | --- |
| 13 | What is the main metric? | Cost per correct feature; acceptance test pass rate; human effort | Avoids choosing the metric after seeing the results |
| 14 | How much human intervention is allowed during execution? | None; only the reviews the approach prescribes; free but recorded | Without intervention, the tool is measured; with intervention, the real process is measured |
| 15 | How many repetitions per condition? | Three; five; more | More repetitions reduce noise and increase cost |
| 16 | Is there a second assessor or participants? | Only the student; second assessor for quality; small group of developers | Participants require informed consent and possibly an ethics committee opinion |
| 17 | How is divergence between specification and code measured? | Manual inspection with a traceability matrix; model-assisted verification | Only relevant in variant B |

### To confirm on the platform

- Has the proposal "Agentic Software Development Lifecycle" already been assigned? The formalisation only opens after the supervisor accepts the invitation.
- Is there a co-supervisor or company supervisor?
- Can the title of the formalisation differ from the title of the original proposal?

## 12. References

Most sources on SDD are preprints or grey literature, which reflects the maturity of the field. The literature review should confirm the publication status of each one.

**Academic and preprints**

- Alenezi, M. (2026). *Specification-Driven Development as the Foundation of AI-Native Enterprise Software Engineering*. arXiv:2607.16680. [Link](https://arxiv.org/abs/2607.16680)
- Díaz, J., Gayoso, J., Cimminio, A., Pérez, J. (2026). *Spec-Driven Development for Agentic Software Engineering: Harnessing Human-Agent Teamwork*. arXiv:2609.00252. [Link](https://arxiv.org/html/2609.00252v1)
- Gloaguen, T., Mündler-Sasahara, N., Müller, M. N., Raychev, V., Vechev, M. (2026). *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?* arXiv:2602.11988. [Link](https://arxiv.org/abs/2602.11988)
- Macedo, S. O. de (2026). *From Prompt to Process: a Process Taxonomy and Comparative Assessment of Frameworks Supporting AI Software Development Agents*. arXiv:2606.04967. [Link](https://arxiv.org/abs/2606.04967)
- Oates, B. J. (2005). *Researching Information Systems and Computing*. Sage.
- Panda, S. (2026). *Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code*. arXiv:2606.30689. [Link](https://arxiv.org/html/2606.30689)
- Piskala, D. B. (2026). *Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants*. arXiv:2602.00180. [Link](https://arxiv.org/abs/2602.00180)
- Shaw, M. (2002). What Makes Good Research in Software Engineering? *International Journal on Software Tools for Technology Transfer*, 4(1), 1-7.
- Taghavi, P., Bhavani, S. (2026). *Spec Kit Agents: Context-Grounded Agentic Workflows*. arXiv:2604.05278. [Link](https://arxiv.org/abs/2604.05278)
- Tanaka, H., Igaki, H., Shimari, K., Honda, K., Fukuyasu, N. (2026). *Practical Implementation Report on Introducing Spec-Driven Development Using AI Agents in Software Development PBL*. arXiv:2608.30572. [Link](https://arxiv.org/html/2608.30572v1)

**Grey literature and tool documentation**

- Böckeler, B. (2025). *Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl*. martinfowler.com. [Link](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- GitHub. *Spec Kit*. [Repository](https://github.com/github/spec-kit)
- Fission-AI. *OpenSpec*. [Repository](https://github.com/Fission-AI/OpenSpec)
- AWS. *Kiro: Specs*. [Documentation](https://kiro.dev/docs/specs/)
- BMad Code. *BMAD Method*. [Repository](https://github.com/bmad-code-org/BMAD-METHOD)
- OpenAI (2025). *Agentic AI Foundation*, on the donation of AGENTS.md to the Linux Foundation. [Link](https://openai.com/index/agentic-ai-foundation/)
- Uvik Software (2026). *Spec-Driven Development Benchmark 2026*. Not peer-reviewed. [Link](https://uvik.net/spec-driven-development-benchmark/)

## Use of AI-generated content

This draft was written with the support of Claude (Anthropic), based on the supervisor's original proposal, the student's first version and the feedback received. The assistant carried out the initial source search and proposed the structure and the variants. The sources were consulted on 2 October 2026 and must be read and validated by the student before any submission.
