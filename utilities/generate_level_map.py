#!/usr/bin/env python3
"""
Generate a level map JSON by introspecting PlayerGameGUI.

Output: docs/level_map.json with scenes, choices, inferred target scenes, and basic flags.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any
import sys


def _ensure_import_path() -> None:
    utilities_dir = Path(__file__).resolve().parent
    project_root = utilities_dir.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))


_ensure_import_path()

from player_gui import PlayerGameGUI  # type: ignore  # noqa: E402


def _simulate_transition(gui: PlayerGameGUI, source_scene: str, consequence: str) -> Dict[str, Any]:
    # Reset minimal state and move to source scene context within the same GUI
    gui.current_scene = source_scene
    if source_scene not in gui.visited_scenes:
        gui.visited_scenes.append(source_scene)
    gui.game_state = "exploring"

    try:
        gui.handle_consequence(consequence)
    except Exception:
        # If any error happens during effect, capture minimal info
        return {
            "target_scene": gui.current_scene,
            "starts_combat": gui.game_state == "in_combat",
            "error": True,
        }

    return {
        "target_scene": gui.current_scene,
        "starts_combat": gui.game_state == "in_combat",
        "error": False,
    }


def build_level_map() -> Dict[str, Any]:
    # Use a single GUI instance to avoid multiple Tk roots
    gui = PlayerGameGUI()
    try:
        gui.root.withdraw()
    except Exception:
        pass

    # Initialize class once so labels/canvas exist
    gui.select_class("warrior")

    scenes = {}
    for scene_name, desc in gui.scene_descriptions.items():
        entry: Dict[str, Any] = {
            "description": desc,
            "choices": [],
        }
        if scene_name in gui.scene_choices:
            for choice in gui.scene_choices[scene_name]:
                consequence = choice.get("consequence")
                sim = _simulate_transition(gui, scene_name, consequence)
                entry["choices"].append(
                    {
                        "text": choice.get("text"),
                        "consequence": consequence,
                        "target_scene": sim.get("target_scene"),
                        "starts_combat": sim.get("starts_combat", False),
                        "sim_error": sim.get("error", False),
                    }
                )
        scenes[scene_name] = entry

    level_map = {
        "scene_progression": list(gui.scene_progression),
        "scenes": scenes,
    }

    try:
        gui.root.destroy()
    except Exception:
        pass

    return level_map


def main() -> int:
    level_map = build_level_map()
    out_path = Path(__file__).resolve().parents[1] / "docs" / "level_map.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(level_map, indent=2), encoding="utf-8")
    print(f"✅ Wrote level map: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


