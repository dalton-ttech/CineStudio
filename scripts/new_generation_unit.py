#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser(description="Create a Y-mode Generation Unit.")
    p.add_argument("project")
    p.add_argument("gu_id", help="e.g. GU001")
    args = p.parse_args()

    project = Path(args.project)
    base = project / "04_Y_MODE" / "06_GENERATION_UNITS" / args.gu_id.upper()
    base.mkdir(parents=True, exist_ok=False)
    for d in ["references", "keyframes", "audio", "outputs"]:
        (base / d).mkdir()

    template = Path(__file__).resolve().parents[1] / "templates" / "generation_unit.json"
    data = json.loads(template.read_text(encoding="utf-8"))
    data["id"] = args.gu_id.upper()
    (base / "generation_unit.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(base.resolve())


if __name__ == "__main__":
    main()
