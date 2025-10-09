#!/usr/bin/env python3
"""
Automated GUI snapshot generator for SHABUYA Cave Adventure.

This utility renders selected scene/character/state combinations from the
Enhanced GUI sandbox and saves canvas screenshots into gui_snapshots/.

Intended to speed up visual QA without manually playing through the game.
"""

from __future__ import annotations

import argparse
import itertools
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple


def _ensure_import_path() -> None:
    """Ensure the project root (one level up from this file) is on sys.path."""
    utilities_dir = Path(__file__).resolve().parent
    project_root = utilities_dir.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))


_ensure_import_path()

try:
    # Import after path fix
    from enhanced_gui_final import EnhancedGameGUI  # type: ignore
except Exception as import_error:  # pragma: no cover
    print(f"❌ Failed to import EnhancedGameGUI: {import_error}")
    sys.exit(1)


try:
    from PIL import ImageGrab  # type: ignore
except Exception as pil_error:  # pragma: no cover
    print(
        "❌ Pillow ImageGrab not available. Install Pillow and ensure a display is present.\n"
        "   pip install Pillow"
    )
    sys.exit(1)


@dataclass
class SnapshotConfig:
    output_dir: Path
    scenes: List[str]
    characters: List[str]
    states: List[str]
    delay_ms: int = 120  # small delay to allow rendering


def _safe_filename(*parts: str) -> str:
    return "_".join(
        p.replace(" ", "_").replace("/", "-").replace("\\", "-") for p in parts
    ).lower()


def _capture_canvas_png(gui: EnhancedGameGUI, destination: Path) -> None:
    gui.root.update_idletasks()
    gui.root.update()

    x = gui.canvas.winfo_rootx()
    y = gui.canvas.winfo_rooty()
    w = gui.canvas.winfo_width()
    h = gui.canvas.winfo_height()

    # Fallback sizes in case geometry managers haven't finalized yet
    if w <= 1 or h <= 1:
        w, h = 900, 650

    bbox = (x, y, x + w, y + h)
    image = ImageGrab.grab(bbox=bbox)
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, format="PNG")


def _iter_combinations(cfg: SnapshotConfig) -> Iterable[Tuple[str, str, str]]:
    # Limit combinations to keep things fast but useful
    for scene, character, state in itertools.product(
        cfg.scenes, cfg.characters, cfg.states
    ):
        yield scene, character, state


def generate_snapshots(cfg: SnapshotConfig) -> List[Path]:
    gui = EnhancedGameGUI()

    saved_paths: List[Path] = []
    for scene, character, state in _iter_combinations(cfg):
        # Apply selection
        gui.current_scene = scene
        gui.scene_var.set(scene)
        gui.current_character = character
        gui.char_var.set(character)
        gui.game_state = state
        gui.state_var.set(state)
        gui.update_display()

        time.sleep(cfg.delay_ms / 1000.0)

        filename = _safe_filename(scene, character, state) + ".png"
        out_path = cfg.output_dir / filename
        _capture_canvas_png(gui, out_path)
        print(f"📸 Saved: {out_path}")
        saved_paths.append(out_path)

    gui.root.destroy()
    return saved_paths


def _default_config(output: Path, sample: bool) -> SnapshotConfig:
    # Build lists based on the GUI mappings to avoid drift
    tmp_gui = EnhancedGameGUI()
    scenes_all = list(tmp_gui.SCENE_BACKGROUND_MAP.keys())
    characters_all = list(tmp_gui.CHARACTER_SPRITE_MAP.keys())
    tmp_gui.root.destroy()

    # Provide a concise but representative set by default
    if sample:
        scenes = [
            s
            for s in [
                "cave_entrance",
                "skull_chamber",
                "chiefs_house",
                "primitive_village",
                "village_changed",
            ]
            if s in scenes_all
        ]
        characters = [c for c in ["warrior", "rogue", "mage"] if c in characters_all]
    else:
        scenes = scenes_all
        characters = [c for c in ["warrior", "rogue", "mage"] if c in characters_all]

    states = ["exploring", "in_combat"]

    return SnapshotConfig(
        output_dir=output,
        scenes=scenes,
        characters=characters,
        states=states,
        delay_ms=150,
    )


def _write_report(output_dir: Path, saved: List[Path]) -> None:
    report_path = output_dir / "screenshot_report.md"
    lines = [
        "# GUI Snapshot Report",
        "",
        f"Total screenshots: {len(saved)}",
        "",
        "## Files",
    ]
    for p in saved:
        lines.append(f"- {p.name}")
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"📝 Report written: {report_path}")


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Capture Enhanced GUI snapshots")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "gui_snapshots",
        help="Directory to write PNGs and report (default: gui_snapshots/)",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Capture all scenes with core characters and states (may be many)",
    )
    parser.add_argument(
        "--delay-ms",
        type=int,
        default=150,
        help="Delay after state change before capture (ms)",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    ns = parse_args(argv or sys.argv[1:])
    cfg = _default_config(ns.output, sample=not ns.full)
    cfg.delay_ms = ns.delay_ms

    print("=== SHABUYA Cave Adventure - GUI Snapshot Generator ===")
    print(f"Output directory: {cfg.output_dir}")
    print(f"Scenes: {len(cfg.scenes)} | Characters: {len(cfg.characters)} | States: {len(cfg.states)}")

    try:
        saved = generate_snapshots(cfg)
        _write_report(cfg.output_dir, saved)
        print("\n🎉 Snapshot capture complete!")
        return 0
    except Exception as e:  # pragma: no cover
        print(f"❌ Snapshot capture failed: {e}")
        return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())


