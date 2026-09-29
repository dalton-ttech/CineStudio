# Architecture

CineStudio uses progressive disclosure. Keep the top-level workflow small; load mode-specific rules only when needed.

## Local project shape

PROJECT/
- 00_SOURCE/
- 01_STORY_MASTER/
- 02_LOOKDEV/
- 03_STORYBOARD/
- project.json

If X:
- 04_X_MODE/
  - 00_PLAN/
  - 01_CHARACTER_ANCHORS/
  - 02_SCENE_ANCHORS/
  - 03_FRAMES/
  - 04_REVIEW/
  - 05_FINAL/

If Y:
- 04_Y_MODE/
  - 00_PRODUCTION_SCRIPT/
  - 01_CHARACTER_PACK/
  - 02_SCENE_PACK/
  - 03_PROP_PACK/
  - 04_KEYFRAMES/
  - 05_SHOTLIST/
  - 06_GENERATION_UNITS/
  - 07_AUDIO/
  - 08_SEEDANCE_PACK/
  - 09_GENERATIONS/
  - 10_QC/
  - 11_EDIT_PLAN/
  - 12_FINAL/

## Context model

Canonical shared context:
- Story Master
- approved character / scene / prop anchors
- locked visual direction
- current scene / current generation unit

Do not share:
- unrelated rejected looks
- failed generations unless intentionally used for an edit
- all historical prompts
- unrelated skills or project files
