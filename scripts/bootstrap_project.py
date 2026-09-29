#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


COMMON = [
    "00_SOURCE",
    "01_STORY_MASTER",
    "02_LOOKDEV",
    "03_STORYBOARD",
]

X_DIRS = [
    "04_X_MODE/00_PLAN",
    "04_X_MODE/01_CHARACTER_ANCHORS",
    "04_X_MODE/02_SCENE_ANCHORS",
    "04_X_MODE/03_FRAMES",
    "04_X_MODE/04_REVIEW",
    "04_X_MODE/05_FINAL",
]

Y_DIRS = [
    "04_Y_MODE/00_PRODUCTION_SCRIPT",
    "04_Y_MODE/01_CHARACTER_PACK",
    "04_Y_MODE/02_SCENE_PACK",
    "04_Y_MODE/03_PROP_PACK",
    "04_Y_MODE/04_KEYFRAMES",
    "04_Y_MODE/05_SHOTLIST",
    "04_Y_MODE/06_GENERATION_UNITS",
    "04_Y_MODE/07_AUDIO",
    "04_Y_MODE/08_SEEDANCE_PACK",
    "04_Y_MODE/09_GENERATIONS",
    "04_Y_MODE/10_QC",
    "04_Y_MODE/11_EDIT_PLAN",
    "04_Y_MODE/12_FINAL",
]


def main() -> None:
    p = argparse.ArgumentParser(description="Create a local CineStudio project.")
    p.add_argument("name")
    p.add_argument("--mode", choices=["X", "Y", "BOTH"], default="Y")
    p.add_argument("--source", help="Optional source file to copy into 00_SOURCE.")
    p.add_argument("--adaptation", choices=["STRICT", "EXPAND", "ADAPT"], default="EXPAND")
    p.add_argument("--root", default="projects")
    args = p.parse_args()

    safe = "".join(c if c.isalnum() or c in "-_" else "-" for c in args.name).strip("-")
    root = Path(args.root) / safe
    dirs = list(COMMON)
    if args.mode in {"X", "BOTH"}:
        dirs += X_DIRS
    if args.mode in {"Y", "BOTH"}:
        dirs += Y_DIRS

    for d in dirs:
        (root / d).mkdir(parents=True, exist_ok=True)

    if args.source:
        src = Path(args.source)
        if not src.exists():
            raise SystemExit(f"Source not found: {src}")
        shutil.copy2(src, root / "00_SOURCE" / src.name)

    project = {
        "name": args.name,
        "mode": args.mode,
        "adaptation_mode": args.adaptation,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "x_ratio": "9:16" if args.mode in {"X", "BOTH"} else None,
        "y_ratio": "21:9" if args.mode in {"Y", "BOTH"} else None,
        "status": "SOURCE_INGESTION"
    }
    (root / "project.json").write_text(
        json.dumps(project, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    story_template = Path(__file__).resolve().parents[1] / "templates" / "story_master.json"
    if story_template.exists():
        shutil.copy2(story_template, root / "01_STORY_MASTER" / "story_master.json")

    print(root.resolve())


if __name__ == "__main__":
    main()
