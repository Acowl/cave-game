#!/usr/bin/env python3
"""
Autoplay route harness for PlayerGameGUI.

Runs a deterministic route through the main progression without manual GUI input,
logging each step and asserting key state transitions. Useful for quickly
reproducing/diagnosing logic bugs without playing through by hand.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List


def _ensure_import_path() -> None:
    utilities_dir = Path(__file__).resolve().parent
    project_root = utilities_dir.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))


_ensure_import_path()

import tkinter as tk  # noqa: E402
from player_gui import PlayerGameGUI  # type: ignore  # noqa: E402


def run_route(log_lines: List[str]) -> None:
    gui = PlayerGameGUI()
    gui.root.withdraw()  # hide window to avoid disrupting desktop

    # Pick a class and start
    gui.select_class("warrior")
    log_lines.append("Selected class: warrior")
    assert gui.player_character == "warrior"
    assert gui.current_scene == "cave_entrance"

    # Scene: cave_entrance → enter skull chamber (choice consequence)
    gui.handle_consequence("entered_skull_chamber")
    log_lines.append("Entered skull chamber")
    assert gui.current_scene == "skull_chamber"

    # Skull chamber collapse path → cave_in then escape → primitive_village
    gui.handle_consequence("tunnel_collapse")
    log_lines.append("Triggered cave_in")
    assert gui.current_scene == "cave_in"

    gui.handle_consequence("escaped_cave_in")
    log_lines.append("Escaped to primitive_village")
    assert gui.current_scene == "primitive_village"

    # Try invalid: approach chief's house without key (should gate and remain in village)
    prev_scene = gui.current_scene
    gui.handle_consequence("approached_chiefs_house")
    log_lines.append("Attempted chief's house without key (expect gated)")
    assert gui.current_scene == "primitive_village", "Chief's house should be gated without key"

    # Follow creature to alley → start combat and win to obtain Armory Key
    gui.handle_consequence("followed_creature_to_alley")
    log_lines.append("Moved to alley")
    assert gui.current_scene == "alley"

    gui.handle_consequence("confronted_alley_creature")
    log_lines.append("Started alley combat")
    assert gui.game_state == "in_combat"

    # Simple combat loop: attack until enemy <= 0
    while gui.game_state == "in_combat" and gui.combat_enemy_health > 0:
        # Always choose basic attack (index 1)
        gui.handle_combat_action(1)

    log_lines.append("Combat ended")
    assert gui.game_state == "exploring"
    assert "Armory Key" in gui.inventory

    # Approach armory (now allowed) and use key to obtain Chief's House Key
    gui.handle_consequence("approached_armory")
    log_lines.append("Approached armory")
    if gui.current_scene != "armory":
        gui.advance_to_scene("armory")
    assert gui.current_scene == "armory"

    gui.handle_consequence("used_armory_key")
    log_lines.append("Used armory key and looted contents")
    assert "Chief's House Key" in gui.inventory

    # Return to village then enter chief's house (now allowed)
    gui.handle_consequence("returned_to_village")
    log_lines.append("Returned to village")
    assert gui.current_scene == "primitive_village"

    gui.handle_consequence("approached_chiefs_house")
    log_lines.append("Approached chief's house (with key)")

    gui.handle_consequence("used_chiefs_house_key")
    log_lines.append("Entered chief's house and received blessing")
    assert gui.current_scene == "chiefs_house"

    # Advance to healing pool and village_changed path
    gui.handle_consequence("advanced_to_healing_pool")
    log_lines.append("Advanced to healing pool")
    assert gui.current_scene == "healing_pool"

    gui.handle_consequence("advanced_to_village_changed")
    log_lines.append("Advanced to village_changed")
    assert gui.current_scene == "village_changed"

    # Done
    gui.root.destroy()


def main() -> int:
    log_lines: List[str] = []
    try:
        run_route(log_lines)
        out = Path(__file__).resolve().parents[1] / "gui_snapshots" / "autoplay_report.txt"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(log_lines), encoding="utf-8")
        print("\n".join(log_lines))
        print(f"\nAutoplay route completed. Report: {out}")
        return 0
    except AssertionError as ae:
        print("Autoplay assertion failed:", ae)
        return 2
    except Exception as e:
        print("Autoplay crashed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


