#!/usr/bin/env python3
"""
Continuity validator for PlayerGameGUI state transitions.

Minimal rules to enforce logical flow and prevent impossible transitions.
Extend this as level_map.json grows more complete.
"""

from __future__ import annotations

from typing import Tuple


class ContinuityValidator:
    @staticmethod
    def validate(gui) -> Tuple[bool, str | None]:
        """Validate the current GUI state after a transition.

        Returns (ok, message). If not ok, message is a player-facing reason.
        """
        # Key-based prerequisites for scenes
        if gui.current_scene == "armory" and "Armory Key" not in gui.inventory:
            return False, "The armory is locked. You will need an Armory Key first."

        if gui.current_scene == "chiefs_house" and "Chief's House Key" not in gui.inventory:
            return False, "The chief's house is locked. You need the Chief's House Key."

        # Basic combat-state consistency: combat currently only initiated in alley
        if gui.game_state == "in_combat" and gui.current_scene not in {"alley"}:
            return False, "You cannot enter combat here."

        # No contradictions detected
        return True, None


