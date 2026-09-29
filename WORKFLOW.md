# CineStudio Workflow

## 0. Source intake

Accept a user-provided screenplay, treatment, story outline, shot list, planning document, or mixed source package.

Preserve what the source actually says. Separate source facts from proposed adaptation.

Read docs/SOURCE_INGESTION.md when ingesting.

## 1. Story Master

Create the canonical story package:
- premise and logline
- synopsis
- theme
- beat sheet
- characters and relationships
- scenes / locations
- props
- timeline
- key dialogue
- visual reveals
- continuity rules
- locked facts
- open creative decisions

Set adaptation permission:
- STRICT — preserve plot and meaning; optimize only presentation and pacing.
- EXPAND — preserve intent while expanding scenes, beats, or dialogue.
- ADAPT — substantial cinematic restructuring is allowed.

Read docs/STORY_MASTER.md.

### Gate 1 — Story Lock

Do not enter full visual production until the story direction is accepted.

## 2. Look Development

Research/select visual references. Reference images carry the visual language; avoid translating them into long image prompts.

Build a compact Lookboard representing characters, locations, lighting, texture, production design, and signature moments.

### Gate 2 — Look Lock

Approve one visual direction or a deliberately mixed system.

## 3. Storyboard

Build a story-preview storyboard to evaluate:
- narrative clarity
- major compositions
- shot rhythm
- character blocking
- visual reveals
- approximate scene progression

Storyboard is not the same as production keyframes.

For Y, storyboard frames must already read as live-action / photoreal cinematic imagery.

### Gate 3 — Storyboard Lock

After approval, branch into X or Y.

## 4X. X Mode

Read workflows/x-mode.md.

Output: 9:16 vertical visual narrative image series.

## 4Y. Y Mode

Read workflows/y-mode.md and docs/SEEDANCE_2_5.md.

Output: complete 21:9 live-action cinematic production package for Seedance 2.5, including script, shots, blocking, lens/camera plan, dialogue, narration, audio, keyframes, references, generation units, prompts, edit plan, continuity QC, and final edit plan.

## 5. Revision

Choose explicitly:
- REGENERATE — start clean from canonical anchors and latest direction; do not feed the failed generation back unless a specific detail must be retained.
- EDIT — use the accepted generated asset as the target and request only the necessary change.

## 6. Continuity QC

Read docs/CONTINUITY_QC.md before final packaging.

## 7. Delivery

Deliver mode-specific final folders plus source-to-output manifest.

Do not default to HTML as an image/video production method. HTML may be used for review dashboards only.
