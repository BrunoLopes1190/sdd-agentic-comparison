# Ethical considerations

## Code of ethics

The work follows one code, the ACM Code of Ethics and Professional Conduct (2018) [@associationforcomputingmachineryACMCodeEthics2018].
It was chosen because it covers computing as a whole, including AI systems and the use of computing tools, and because it applies to research as well as to practice.
The ACM/IEEE Software Engineering Code is centred on professional software engineering practice, and the NSPE code on engineering in general, so they fit this work less well.
As research, the work also follows the four principles of the European Code of Conduct for Research Integrity (ALLEA) [@allea-alleuropeanacademiesEuropeanCodeConduct2023]: reliability, honesty, respect and accountability.

The table below applies each principle of the ACM code's sections 1 and 2 to this work.
Section 3 (leadership) does not apply, since the student leads no team or organisation.
Section 4 (compliance) is met by applying the code as shown.

: ACM principles applied to this work {#tbl:acm}

| Principle | How it is applied |
|---|---|
| 1.1 Contribute to society and human well-being | The results help teams choose an SDD approach (benefits B1–B3); they are published openly |
| 1.2 Avoid harm | Agents run only in isolated copies of a synthetic project, outside the repository, without secrets or access to real systems |
| 1.3 Be honest and trustworthy | Metrics and acceptance tests are fixed before any run; all results are reported, including negative ones; the use of generative AI is declared |
| 1.4 Be fair and do not discriminate | All approaches run under the same conditions: same briefing, tests, agents, models and prompts |
| 1.5 Respect the work behind ideas and artefacts | Papers and tool documentation are cited; the licence of each approach, agent and model is respected |
| 1.6 Respect privacy | No personal data are collected; logs are checked for personal data before they are published |
| 1.7 Honour confidentiality | No confidential or company data are used; the reference project is original |
| 2.1 High quality in processes and products | A reproducible protocol, frozen before the runs; validity threats T1–T10 and their mitigations |
| 2.2 Professional competence | The competency development plan, including ethics, which has a gap of 2 |
| 2.3 Know and respect the rules | P.PORTO code (art. 6, 8 and 10), ISEP dissertation rules, and the terms of use of each tool |
| 2.4 Accept and give professional review | Drafts are sent to the supervisor at each milestone; a second reviewer is sought for the SLR |
| 2.5 Thorough evaluation, including risks | Spread and limits are reported, not only means; claims are kept to what the data support |
| 2.6 Work only within competence | Statistical analysis follows established methods for software engineering experiments [@wohlinExperimentationSoftwareEngineering2012] |
| 2.7 Foster public understanding | The decision guide is written for practitioners |
| 2.8 Use resources only when authorised | Only the student's own plan, hardware and accounts are used, within each provider's terms |
| 2.9 Secure systems | Runs are sandboxed; no credentials are kept in the repository or in the logs |

## Human participants, personal data and article 10

The work has no human participants and collects no personal data.
The agents run on a synthetic reference project, created for this work.
Article 10 of the P.PORTO Code of Good Practices and Conduct [@institutopolitecnicodoportoRegulamentoCodigoBoas2020] asks for review by an ethics committee, "as required by law", for research that involves systems capable of autonomous operation, in particular AI.
This work studies such systems, but they run in an isolated environment, on synthetic material, without contact with people, personal data or real systems.
No legal requirement for ethics committee review applies, so the work is not submitted to one.
This position was stated to the supervisor on 4 Nov 2026, with a request for confirmation.

## Licences and terms of use

The licence and terms of use of each approach, agent and model are recorded at selection, with the version and the date.
They are checked for two points: whether the tool may be used for research, and who owns the code it generates.
An approach whose terms forbid this use is excluded, and the exclusion is reported.

## Research data

The data are the reference project, its acceptance tests, the session logs, the generated code and the metrics.
They follow the FAIR principles [@wilkinsonFAIRGuidingPrinciples2016]:

- **Findable:** deposited at the end of the dissertation in a public repository with a persistent identifier.
- **Accessible:** open access, without registration.
- **Interoperable:** open formats (CSV, JSON, Markdown, source code).
- **Reusable:** an open licence, the protocol, and the versions of every tool, agent and model.

Before publication, logs are checked for credentials and personal data.
The reference project is published only after the runs, so that models cannot see it beforehand (T6).

## Conflicts of interest

There is no funding, no employer link and no tie to the authors of the approaches.
One conflict is declared: Claude is both an agent under study and the assistant used for this work (T10).
The agent is a recorded factor, and the measures are automatic and fixed in advance.

## Use of generative AI

The student is responsible for all the work; AI systems are not authors.
Each use beyond editing is logged with the date, tool, model, part of the work, and nature and extent of the contribution, and is reported in the chapter on the use of AI-generated content.
Every reference is checked to exist and is read.
No experimental result is generated by AI outside the runs that the protocol defines.
Only the student's own material and public sources are given to the assistant.
