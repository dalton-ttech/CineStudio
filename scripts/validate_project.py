#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("project")
    args = p.parse_args()

    root = Path(args.project)
    cfg = root / "project.json"
    if not cfg.exists():
        raise SystemExit("Missing project.json")

    data = json.loads(cfg.read_text(encoding="utf-8"))
    mode = data.get("mode")
    errors = []

    for d in ["00_SOURCE", "01_STORY_MASTER", "02_LOOKDEV", "03_STORYBOARD"]:
        if not (root / d).exists():
            errors.append(f"Missing {d}")

    if mode in {"X", "BOTH"}:
        if data.get("x_ratio") != "9:16":
            errors.append("X ratio must be 9:16")
        if not (root / "04_X_MODE").exists():
            errors.append("Missing 04_X_MODE")

    if mode in {"Y", "BOTH"}:
        if data.get("y_ratio") != "21:9":
            errors.append("Y ratio must be 21:9")
        if not (root / "04_Y_MODE").exists():
            errors.append("Missing 04_Y_MODE")

    if errors:
        raise SystemExit("\n".join(errors))

    print("CineStudio project validation passed.")


if __name__ == "__main__":
    main()
