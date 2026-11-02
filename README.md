# sdd-agentic-comparison

MSc dissertation (PREPD, ISEP MEI 2026/27): *Spec-Driven for Agentic Software Development: A Characterisation and Comparison of Existing Approaches*.
SDD approaches (GitHub Spec Kit, OpenSpec, Kiro, BMAD, Tessl, AGENTS.md) are characterised and applied to the same reference project, against a no-spec baseline.

| Folder | Contents |
|---|---|
| `course-materials/` | PREPD course materials by week (original language); `.md` text extracted next to key PDFs |
| `admin/` | Proposal, formalisation and working context |
| `doc/` | Dissertation in Markdown, built to `.docx` with Pandoc |
| `slr/` | Systematic literature review |
| `planning/` | Project charter, WBS, schedule |
| `experiment/` | Protocol, reference project and results |

## Building the document

Requires [Pandoc](https://pandoc.org). `doc/references.bib` is auto-exported from Zotero (Better BibTeX).

```powershell
powershell -File doc/build.ps1   # -> build/thesis.docx
```

## Milestones

Tags: `extended-abstract` (2026-12-16), `final-delivery` (2027-01-06).
