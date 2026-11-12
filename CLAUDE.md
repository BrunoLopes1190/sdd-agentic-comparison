# CLAUDE.md

MSc dissertation repo (see README.md). Comparison of Spec-Driven Development approaches for agentic coding.

Start here: `course-materials/course-overview.md` (what PREPD requires) and `planning/prepd-work-plan.md` (what to produce, by when).

**Progress tracking (always):** whenever a plan item (milestone M*, product P*) starts, finishes or moves, update its Status in `planning/prepd-work-plan.md`, add a dated line to its Progress log, then run `python planning/build_plan_html.py`. The `.md` is the source; never edit `prepd-work-plan.html` by hand.

## Rules

- Everything in English (files, folders, prose, comments). Exception: `course-materials/` content keeps its original language.
- `course-materials/` and `admin/` are read-only reference, except `admin/context.md`, the working summary, which is updated when the status changes. Use the extracted `.md` files instead of the PDFs.
- The document lives in `doc/chapters/NN-name.md` (Pandoc Markdown, citations as `[@key]`). Do not edit `doc/references.bib` by hand; it is exported from Zotero. Build with `doc/build.ps1`.
- Log every AI contribution that is not just editing or grammar in `doc/ai-usage.md` (date, system/model, part, nature and extent).
- Experiments never run inside this repo. Copy `experiment/reference-project/` to a temporary folder outside it and run there; only results go to `experiment/results/`. Treat the agent and model as variables, see `experiment/protocol.md`.
- Git: `main` only, small commits. Never commit secrets or `build/`.
