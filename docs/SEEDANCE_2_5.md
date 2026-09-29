# Seedance 2.5 Production Profile

Capability snapshot verified against official ByteDance / Volcano Engine documentation in 2026-09.

Official documentation:
- https://seed.bytedance.com/en/seedance2_5
- https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- https://docs.volcengine.com/docs/ark/seedance-2-5-prompt-guide

## Workflow assumptions

Seedance 2.5 supports up to 30-second single generations and multimodal reference inputs. Current official guidance allows up to 30 images, 10 videos, and 10 audio clips in a reference package, subject to platform implementation.

CineStudio does not assume one whole film equals one generation.

Use **Generation Units (GU)**. A GU is a Seedance-sized production unit that may contain one or several planned shots.

## Y ratio

CineStudio Y master target is **21:9 horizontal**.

If the Seedance front-end exposes 21:9 directly, use it.

If it does not, use a 21:9 first-frame / production keyframe and adaptive ratio behavior where supported, then conform final output to the 21:9 master during finishing.

## Reference strategy

Reference files answer: **what it looks/sounds/moves like**.

Prompt answers: **what happens in this GU**.

Keep prompts concise. Use reference maps such as:
- @image1 = character anchor
- @image2 = scene anchor
- @image3 = prop anchor
- @video1 = motion/camera reference
- @audio1 = voice/performance reference

## Storyboard vs keyframes

A storyboard is for narrative planning. Production keyframes are separate, clean, high-fidelity frames.

For precise character/scene alignment, prefer separate production images over a dense multi-view collage.

## GU recommendation

For complex multi-character or multi-shot work, CineStudio generally prefers smaller units rather than always using the 30-second maximum. This is a workflow recommendation, not a model limit.

Each GU package should include:
- GU brief
- expected duration
- included shots
- reference map
- production keyframes
- dialogue / VO
- ambience
- Foley
- SFX
- music intent
- Seedance prompt
- continuity requirements
- expected opening / closing state
