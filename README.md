# CineStudio

CineStudio is a source-to-production workflow for AI narrative projects.

It turns a supplied story, script, treatment, shot list, or planning document into one of two production modes:

- **X Mode** — 9:16 vertical visual narrative. Uses photography, realistic illustration, or realistic comic language to tell the story with designed framing, dialogue, narration, and visual storytelling.
- **Y Mode** — 21:9 horizontal live-action cinematic production package for Seedance 2.5. Y is strictly photorealistic/live-action in visual language: no comic rendering and no 3D-animation look.

CineStudio is deliberately **workflow-first, reference-first, and agent-agnostic**. It does not require a global AGENTS.md. Any capable local coding/agent system can read this repository and create a project from it.

## Entry points

Humans: read [START_HERE.md](START_HERE.md).

Agents: read [AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md), then [WORKFLOW.md](WORKFLOW.md).

Machine-readable entrypoint: [cine-studio.manifest.json](cine-studio.manifest.json).

## Core production idea

Source → Story Master → Look Development → Storyboard → X or Y production.

For Y, keep these separate:

**Lookboard ≠ Storyboard ≠ Production Keyframes**

The storyboard previews story and cinematic direction. Production keyframes are separate high-fidelity controls used for generation.

## Repository policy

This public repository contains only reusable workflow logic, templates, validation scripts, and documentation. User source files, private reference images, generated media, voices, licensed assets, and project outputs stay local by default.

Version: see [VERSION](VERSION).
