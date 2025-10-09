#!/usr/bin/env python3
"""
Automated PlayerGameGUI snapshot generator for SHABUYA Cave Adventure.

This utility navigates through the actual game (PlayerGameGUI) and captures
screenshots of all major scenes, states, and interfaces. The snapshots allow
AI assistants to analyze and modify the GUI without manually playing through.

Usage:
    python utilities/capture_player_gui_snapshots.py
    python utilities/capture_player_gui_snapshots.py --full  # All scenes with all classes
"""

from __future__ import annotations

import argparse
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Optional, Tuple


def _ensure_import_path() -> None:
    """Ensure the project root is on sys.path."""
    utilities_dir = Path(__file__).resolve().parent
    project_root = utilities_dir.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))


_ensure_import_path()

try:
    from player_gui import PlayerGameGUI  # type: ignore
except Exception as import_error:
    print(f"❌ Failed to import PlayerGameGUI: {import_error}")
    sys.exit(1)

try:
    from PIL import ImageGrab  # type: ignore
except Exception as pil_error:
    print(
        "❌ Pillow ImageGrab not available. Install Pillow and ensure a display is present.\n"
        "   pip install Pillow"
    )
    sys.exit(1)


@dataclass
class SnapshotPlan:
    """Represents a single snapshot to capture."""
    name: str
    description: str
    setup_fn: callable  # Function to setup the GUI state
    scene: str
    character: Optional[str] = None


@dataclass
class SnapshotConfig:
    output_dir: Path
    delay_ms: int = 200
    full_coverage: bool = False


def _safe_filename(*parts: str) -> str:
    """Convert parts into a safe filename."""
    return "_".join(
        p.replace(" ", "_").replace("/", "-").replace("\\", "-").replace("'", "")
        for p in parts if p
    ).lower()


def _capture_canvas_png(gui: PlayerGameGUI, destination: Path) -> None:
    """Capture the GUI canvas as a PNG image."""
    gui.root.update_idletasks()
    gui.root.update()
    time.sleep(0.05)  # Small delay for rendering

    x = gui.root.winfo_rootx()
    y = gui.root.winfo_rooty()
    w = gui.root.winfo_width()
    h = gui.root.winfo_height()

    if w <= 1 or h <= 1:
        w, h = 1200, 800

    bbox = (x, y, x + w, y + h)
    image = ImageGrab.grab(bbox=bbox)
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, format="PNG")


def setup_title_screen(gui: PlayerGameGUI) -> None:
    """Setup: Title screen (before class selection)."""
    # Already at title screen on init
    pass


def setup_class_selection(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Class selected but not started."""
    gui.select_class(character)


def setup_cave_entrance(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Starting scene (cave entrance)."""
    gui.select_class(character)
    gui.root.update()


def setup_skull_chamber(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Skull chamber scene."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.root.update()


def setup_cave_in(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Cave-in scene."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.handle_consequence("tunnel_collapse")
    gui.root.update()


def setup_primitive_village(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Primitive village scene."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.handle_consequence("tunnel_collapse")
    gui.handle_consequence("escaped_cave_in")
    gui.root.update()


def setup_alley(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Alley scene."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.handle_consequence("tunnel_collapse")
    gui.handle_consequence("escaped_cave_in")
    gui.handle_consequence("followed_creature_to_alley")
    gui.root.update()


def setup_combat(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Combat interface."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.handle_consequence("tunnel_collapse")
    gui.handle_consequence("escaped_cave_in")
    gui.handle_consequence("followed_creature_to_alley")
    gui.handle_consequence("confronted_alley_creature")
    gui.root.update()


def setup_armory(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Armory scene (after winning combat)."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.handle_consequence("tunnel_collapse")
    gui.handle_consequence("escaped_cave_in")
    gui.handle_consequence("followed_creature_to_alley")
    gui.handle_consequence("confronted_alley_creature")
    
    # Win combat quickly
    while gui.game_state == "in_combat" and gui.combat_enemy_health > 0:
        gui.combat_enemy_health = 0  # Cheat to win quickly
        gui.handle_combat_action(1)
    
    gui.handle_consequence("approached_armory")
    gui.root.update()


def setup_chiefs_house(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Chief's house scene (after getting key)."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.handle_consequence("tunnel_collapse")
    gui.handle_consequence("escaped_cave_in")
    gui.handle_consequence("followed_creature_to_alley")
    gui.handle_consequence("confronted_alley_creature")
    
    # Win combat
    while gui.game_state == "in_combat" and gui.combat_enemy_health > 0:
        gui.combat_enemy_health = 0
        gui.handle_combat_action(1)
    
    gui.handle_consequence("approached_armory")
    gui.handle_consequence("used_armory_key")
    gui.handle_consequence("returned_to_village")
    gui.handle_consequence("approached_chiefs_house")
    gui.handle_consequence("used_chiefs_house_key")
    gui.root.update()


def setup_healing_pool(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Healing pool scene."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.handle_consequence("tunnel_collapse")
    gui.handle_consequence("escaped_cave_in")
    gui.handle_consequence("followed_creature_to_alley")
    gui.handle_consequence("confronted_alley_creature")
    
    # Win combat
    while gui.game_state == "in_combat" and gui.combat_enemy_health > 0:
        gui.combat_enemy_health = 0
        gui.handle_combat_action(1)
    
    gui.handle_consequence("approached_armory")
    gui.handle_consequence("used_armory_key")
    gui.handle_consequence("returned_to_village")
    gui.handle_consequence("approached_chiefs_house")
    gui.handle_consequence("used_chiefs_house_key")
    gui.handle_consequence("advanced_to_healing_pool")
    gui.root.update()


def setup_village_changed(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Village changed scene."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.handle_consequence("tunnel_collapse")
    gui.handle_consequence("escaped_cave_in")
    gui.handle_consequence("followed_creature_to_alley")
    gui.handle_consequence("confronted_alley_creature")
    
    # Win combat
    while gui.game_state == "in_combat" and gui.combat_enemy_health > 0:
        gui.combat_enemy_health = 0
        gui.handle_combat_action(1)
    
    gui.handle_consequence("approached_armory")
    gui.handle_consequence("used_armory_key")
    gui.handle_consequence("returned_to_village")
    gui.handle_consequence("approached_chiefs_house")
    gui.handle_consequence("used_chiefs_house_key")
    gui.handle_consequence("advanced_to_healing_pool")
    gui.handle_consequence("advanced_to_village_changed")
    gui.root.update()


def setup_epilogue(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Epilogue scene (after boss victory)."""
    gui.select_class(character)
    gui.handle_consequence("entered_skull_chamber")
    gui.handle_consequence("tunnel_collapse")
    gui.handle_consequence("escaped_cave_in")
    gui.handle_consequence("followed_creature_to_alley")
    gui.handle_consequence("confronted_alley_creature")
    
    # Win alley combat
    while gui.game_state == "in_combat" and gui.combat_enemy_health > 0:
        gui.combat_enemy_health = 0
        gui.handle_combat_action(1)
    
    gui.handle_consequence("approached_armory")
    gui.handle_consequence("used_armory_key")
    gui.handle_consequence("returned_to_village")
    gui.handle_consequence("approached_chiefs_house")
    gui.handle_consequence("used_chiefs_house_key")
    gui.handle_consequence("advanced_to_healing_pool")
    gui.handle_consequence("advanced_to_village_changed")
    gui.handle_consequence("confronted_darkness")
    
    # Win boss combat
    while gui.game_state == "in_combat" and gui.combat_enemy_health > 0:
        gui.combat_enemy_health = 0
        gui.handle_combat_action(1)
    
    gui.root.update()


def setup_inventory_view(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Inventory interface open."""
    gui.select_class(character)
    # Add some items to make it interesting
    gui.inventory = ["Health Potion", "Mana Potion", "Armory Key"]
    gui.show_inventory()
    gui.root.update()


def _build_snapshot_plans(cfg: SnapshotConfig) -> List[SnapshotPlan]:
    """Build a list of all snapshots to capture."""
    plans: List[SnapshotPlan] = []
    
    characters = ["warrior", "rogue", "mage"] if cfg.full_coverage else ["warrior"]
    
    # Title screen (character-independent)
    plans.append(SnapshotPlan(
        name="00_title_screen",
        description="Title screen with class selection",
        setup_fn=setup_title_screen,
        scene="title",
        character=None
    ))
    
    # For each character
    for char in characters:
        char_prefix = f"{char[:3]}"
        
        # Class selected
        plans.append(SnapshotPlan(
            name=f"01_{char_prefix}_class_selected",
            description=f"{char.title()} class selected",
            setup_fn=lambda g, c=char: setup_class_selection(g, c),
            scene="title",
            character=char
        ))
        
        # Cave entrance
        plans.append(SnapshotPlan(
            name=f"02_{char_prefix}_cave_entrance",
            description=f"{char.title()} at cave entrance",
            setup_fn=lambda g, c=char: setup_cave_entrance(g, c),
            scene="cave_entrance",
            character=char
        ))
        
        # Skull chamber
        plans.append(SnapshotPlan(
            name=f"03_{char_prefix}_skull_chamber",
            description=f"{char.title()} in skull chamber",
            setup_fn=lambda g, c=char: setup_skull_chamber(g, c),
            scene="skull_chamber",
            character=char
        ))
        
        # Cave-in
        plans.append(SnapshotPlan(
            name=f"04_{char_prefix}_cave_in",
            description=f"{char.title()} during cave-in",
            setup_fn=lambda g, c=char: setup_cave_in(g, c),
            scene="cave_in",
            character=char
        ))
        
        # Primitive village
        plans.append(SnapshotPlan(
            name=f"05_{char_prefix}_primitive_village",
            description=f"{char.title()} at primitive village",
            setup_fn=lambda g, c=char: setup_primitive_village(g, c),
            scene="primitive_village",
            character=char
        ))
        
        # Alley
        plans.append(SnapshotPlan(
            name=f"06_{char_prefix}_alley",
            description=f"{char.title()} in alley",
            setup_fn=lambda g, c=char: setup_alley(g, c),
            scene="alley",
            character=char
        ))
        
        # Combat
        plans.append(SnapshotPlan(
            name=f"07_{char_prefix}_combat",
            description=f"{char.title()} in combat",
            setup_fn=lambda g, c=char: setup_combat(g, c),
            scene="alley",
            character=char
        ))
        
        # Armory
        plans.append(SnapshotPlan(
            name=f"08_{char_prefix}_armory",
            description=f"{char.title()} at armory",
            setup_fn=lambda g, c=char: setup_armory(g, c),
            scene="armory",
            character=char
        ))
        
        # Chief's house
        plans.append(SnapshotPlan(
            name=f"09_{char_prefix}_chiefs_house",
            description=f"{char.title()} at chief's house",
            setup_fn=lambda g, c=char: setup_chiefs_house(g, c),
            scene="chiefs_house",
            character=char
        ))
        
        # Healing pool
        plans.append(SnapshotPlan(
            name=f"10_{char_prefix}_healing_pool",
            description=f"{char.title()} at healing pool",
            setup_fn=lambda g, c=char: setup_healing_pool(g, c),
            scene="healing_pool",
            character=char
        ))
        
        # Village changed
        plans.append(SnapshotPlan(
            name=f"11_{char_prefix}_village_changed",
            description=f"{char.title()} at changed village",
            setup_fn=lambda g, c=char: setup_village_changed(g, c),
            scene="village_changed",
            character=char
        ))
        
        # Epilogue
        plans.append(SnapshotPlan(
            name=f"12_{char_prefix}_epilogue",
            description=f"{char.title()} at epilogue",
            setup_fn=lambda g, c=char: setup_epilogue(g, c),
            scene="epilogue",
            character=char
        ))
        
        # Inventory view
        plans.append(SnapshotPlan(
            name=f"13_{char_prefix}_inventory",
            description=f"{char.title()} inventory view",
            setup_fn=lambda g, c=char: setup_inventory_view(g, c),
            scene="cave_entrance",
            character=char
        ))
    
    return plans


def generate_snapshots(cfg: SnapshotConfig) -> List[Tuple[Path, str]]:
    """Generate all planned snapshots."""
    plans = _build_snapshot_plans(cfg)
    saved_paths: List[Tuple[Path, str]] = []
    
    total = len(plans)
    print(f"Capturing {total} snapshots...")
    print()
    
    for i, plan in enumerate(plans, 1):
        # Create fresh GUI instance for each snapshot
        gui = PlayerGameGUI()
        gui.root.withdraw()  # Hide during setup
        
        try:
            # Setup the state
            plan.setup_fn(gui)
            time.sleep(cfg.delay_ms / 1000.0)
            
            # Show and capture
            gui.root.deiconify()
            gui.root.update()
            time.sleep(0.1)
            
            filename = f"{plan.name}.png"
            out_path = cfg.output_dir / filename
            _capture_canvas_png(gui, out_path)
            
            print(f"[{i:2d}/{total}] OK {plan.description:45s} -> {filename}")
            saved_paths.append((out_path, plan.description))
            
        except Exception as e:
            print(f"[{i:2d}/{total}] ERR {plan.description:45s} -> ERROR: {e}")
        finally:
            gui.root.destroy()
    
    return saved_paths


def _write_markdown_report(output_dir: Path, saved: List[Tuple[Path, str]]) -> None:
    """Write a markdown report with all snapshots."""
    report_path = output_dir / "player_gui_snapshots.md"
    
    lines = [
        "# PlayerGameGUI Snapshot Report",
        "",
        f"**Total Snapshots:** {len(saved)}",
        "",
        "This report contains screenshots of all major scenes and states in the PlayerGameGUI.",
        "These snapshots allow AI assistants to analyze and modify the game without manual navigation.",
        "",
        "---",
        "",
    ]
    
    for path, description in saved:
        lines.append(f"## {path.stem}")
        lines.append(f"**Description:** {description}")
        lines.append(f"![{description}]({path.name})")
        lines.append("")
    
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nMarkdown report: {report_path}")


def _write_json_index(output_dir: Path, saved: List[Tuple[Path, str]]) -> None:
    """Write a JSON index of all snapshots."""
    import json
    
    index_path = output_dir / "snapshot_index.json"
    
    index_data = {
        "total_snapshots": len(saved),
        "snapshots": [
            {
                "filename": path.name,
                "description": description,
                "path": str(path.relative_to(output_dir))
            }
            for path, description in saved
        ]
    }
    
    index_path.write_text(json.dumps(index_data, indent=2), encoding="utf-8")
    print(f"JSON index: {index_path}")


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture PlayerGameGUI snapshots for AI analysis"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "player_gui_snapshots",
        help="Directory to write snapshots (default: player_gui_snapshots/)",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Capture all scenes with all character classes (warrior, rogue, mage)",
    )
    parser.add_argument(
        "--delay-ms",
        type=int,
        default=200,
        help="Delay after state change before capture (ms)",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    ns = parse_args(argv or sys.argv[1:])
    cfg = SnapshotConfig(
        output_dir=ns.output,
        delay_ms=ns.delay_ms,
        full_coverage=ns.full
    )
    
    print("=" * 70)
    print("SHABUYA Cave Adventure - PlayerGameGUI Snapshot Generator")
    print("=" * 70)
    print(f"Output directory: {cfg.output_dir}")
    print(f"Full coverage: {'Yes (all classes)' if cfg.full_coverage else 'No (warrior only)'}")
    print()
    
    try:
        saved = generate_snapshots(cfg)
        _write_markdown_report(cfg.output_dir, saved)
        _write_json_index(cfg.output_dir, saved)
        
        print()
        print("=" * 70)
        print(f"Snapshot capture complete! {len(saved)} snapshots saved.")
        print("=" * 70)
        return 0
    except Exception as e:
        print(f"\nSnapshot capture failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

