#!/usr/bin/env python3
"""
Continuity validator for PlayerGameGUI state transitions.

Minimal rules to enforce logical flow and prevent impossible transitions.
Extend this as level_map.json grows more complete.
"""

from __future__ import annotations

from typing import Tuple, Dict, Any, List
from pathlib import Path
import json


class ContinuityValidator:
    _rules_cache: Dict[str, Any] | None = None

    @classmethod
    def _load_rules(cls) -> Dict[str, Any]:
        if cls._rules_cache is not None:
            return cls._rules_cache
        root = Path(__file__).resolve().parents[1]
        level_map = root / "docs" / "level_map.json"
        if not level_map.exists():
            cls._rules_cache = {}
            return cls._rules_cache
        data = json.loads(level_map.read_text(encoding="utf-8"))
        cls._rules_cache = data.get("rules", {})
        return cls._rules_cache

    @classmethod
    def validate(cls, gui) -> Tuple[bool, str | None]:
        """Validate the current GUI state after a transition.

        Returns (ok, message). If not ok, message is a player-facing reason.
        """
        rules = cls._load_rules()

        # Key-based prerequisites for scenes
        prereq_scenes: Dict[str, List[str]] = rules.get("prerequisites", {}).get("scenes", {})  # type: ignore
        needed = prereq_scenes.get(gui.current_scene, [])
        for item in needed:
            if item not in gui.inventory:
                return False, f"You need {item} to enter this area."

        # Combat allowed scenes
        combat_scenes: List[str] = rules.get("combat_scenes", [])  # type: ignore
        if gui.game_state == "in_combat" and gui.current_scene not in set(combat_scenes):
            return False, "You cannot enter combat here."

        # No contradictions detected
        return True, None


