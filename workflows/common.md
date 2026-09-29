# Common Workflow

1. Ingest source.
2. Create Story Master.
3. Set adaptation mode.
4. Propose story improvements separately from source facts.
5. Lock story.
6. Build Lookboard.
7. Lock look.
8. Build Storyboard.
9. Lock storyboard.
10. Build character / scene / prop anchors.
11. Enter X or Y.

## Prompt philosophy

Reference-first.

Do not turn a strong reference image into a large list of stylistic adjectives unless a textual constraint is truly necessary.

## Worker isolation

Use focused workers/subagents when useful.

A production worker should see:
- canonical Story Master
- approved anchors needed for the task
- current scene/frame/GU
- current user feedback

It should not automatically see rejected generations or unrelated project history.
