# Experiment protocol

Skeleton only. To be completed after the state of the art.

## Variables

- **Approach (independent):** baseline without a spec, GitHub Spec Kit, OpenSpec, Kiro, BMAD, Tessl, AGENTS.md.
- **Agent and model (independent, TBD):** each run fixes one agent + model; never assume a specific one.
- **Reference project (controlled):** the same clean copy of `experiment/reference-project/` for every run.

## Isolation

Runs happen **outside this repository**, in a fresh temporary folder created from a clean copy of the reference project,
so that this repo's CLAUDE.md, course materials and notes never enter the agent's context. Only results come back.

## Recorded per run (`experiment/results/`)

Approach and tool version, agent and version, model, date, run id, metrics (TBD), token usage, cost, logs.
