# Agent Bootstrap

You are configuring a local CineStudio project from this repository.

## Read order

Read only what is needed:

1. WORKFLOW.md
2. workflows/common.md
3. If mode X: workflows/x-mode.md
4. If mode Y: workflows/y-mode.md and docs/SEEDANCE_2_5.md
5. Load other docs only when their phase is active.

Avoid loading every document into context at once.

## Setup

Run:

python scripts/bootstrap_project.py PROJECT_NAME --mode X --source PATH

or:

python scripts/bootstrap_project.py PROJECT_NAME --mode Y --source PATH

or use --mode BOTH if the project will produce both deliverables.

If execution is unavailable, manually reproduce the directory layout described in docs/ARCHITECTURE.md.

## Rules

- Never create a global AGENTS.md.
- Do not silently rewrite source facts.
- Do not publish private source assets to this repository.
- Use Story Master as the canonical continuity source.
- Use references directly; do not convert visual references into bloated prompts.
- Failed generations are not canonical references.
- X and Y are separate production branches after the common story/visual-development stages.
- Y must remain live-action / photorealistic. No comic or 3D-animation visual style.
- Y final target ratio is 21:9 horizontal.
