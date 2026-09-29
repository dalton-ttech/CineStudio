#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


REQUIRED = [
    "README.md",
    "START_HERE.md",
    "AGENT_BOOTSTRAP.md",
    "WORKFLOW.md",
    "VERSION",
    "CHANGELOG.md",
    "cine-studio.manifest.json",
    "workflows/common.md",
    "workflows/x-mode.md",
    "workflows/y-mode.md",
    "docs/SEEDANCE_2_5.md",
    "scripts/bootstrap_project.py",
    "scripts/validate_project.py",
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    missing = [p for p in REQUIRED if not (root / p).exists()]
    if missing:
        raise SystemExit("Missing required files: " + ", ".join(missing))

    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    manifest = json.loads((root / "cine-studio.manifest.json").read_text(encoding="utf-8"))
    if manifest.get("version") != version:
        raise SystemExit("VERSION and manifest version do not match.")

    if manifest["modes"]["X"]["aspect_ratio"] != "9:16":
        raise SystemExit("X ratio contract changed unexpectedly.")
    if manifest["modes"]["Y"]["aspect_ratio"] != "21:9":
        raise SystemExit("Y ratio contract changed unexpectedly.")
    if "comic" not in manifest["modes"]["Y"]["forbidden_visual_policy"]:
        raise SystemExit("Y live-action policy is missing comic prohibition.")

    print(f"CineStudio repository v{version} validation passed.")


if __name__ == "__main__":
    main()
