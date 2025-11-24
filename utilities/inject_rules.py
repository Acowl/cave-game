#!/usr/bin/env python3
"""
Inject prerequisite and combat/revisit rules into docs/level_map.json.

This creates/updates a "rules" section to drive continuity validation.
"""

from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    level_map_path = root / "docs" / "level_map.json"
    if not level_map_path.exists():
        print("❌ level_map.json not found. Run generate_level_map.py first.")
        return 1

    data = json.loads(level_map_path.read_text(encoding="utf-8"))

    rules = data.get("rules", {})
    prerequisites = rules.get("prerequisites", {})
    scene_prereqs = prerequisites.get("scenes", {})

    # Keys needed to enter specific scenes
    scene_prereqs["armory"] = ["Armory Key"]
    scene_prereqs["chiefs_house"] = ["Chief's House Key"]

    prerequisites["scenes"] = scene_prereqs
    rules["prerequisites"] = prerequisites

    # Scenes where combat is allowed
    rules["combat_scenes"] = ["alley"]

    # Revisit rules (default allow). Example structure kept for future use.
    rules.setdefault("revisit", {"blocked": []})

    data["rules"] = rules

    level_map_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"✅ Injected rules into: {level_map_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


