#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import sys


def _ensure_import_path() -> None:
    test_dir = Path(__file__).resolve().parents[2]
    if str(test_dir) not in sys.path:
        sys.path.insert(0, str(test_dir))


_ensure_import_path()

from cave-game.utilities.continuity_validator import ContinuityValidator  # type: ignore


class DummyGUI:
    def __init__(self):
        self.current_scene = "primitive_village"
        self.inventory = []
        self.game_state = "exploring"


def test_armory_requires_key():
    gui = DummyGUI()
    gui.current_scene = "armory"
    ok, msg = ContinuityValidator.validate(gui)
    assert not ok
    assert "Armory Key" in (msg or "")


def test_chiefs_house_requires_key():
    gui = DummyGUI()
    gui.current_scene = "chiefs_house"
    ok, msg = ContinuityValidator.validate(gui)
    assert not ok
    assert "Chief's House Key" in (msg or "")


def test_combat_only_in_allowed_scenes():
    gui = DummyGUI()
    gui.current_scene = "primitive_village"
    gui.game_state = "in_combat"
    ok, msg = ContinuityValidator.validate(gui)
    assert not ok
    assert "cannot enter combat" in (msg or "").lower()


