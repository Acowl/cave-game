#!/usr/bin/env python3
"""
Snapshot analysis tool for AI assistants.

Provides quick analysis of captured GUI snapshots including:
- Snapshot inventory
- Scene coverage
- Missing snapshots
- Quick stats
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Set


def _ensure_import_path() -> None:
    """Ensure the project root is on sys.path."""
    utilities_dir = Path(__file__).resolve().parent
    project_root = utilities_dir.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))


_ensure_import_path()


def analyze_snapshots(snapshot_dir: Path) -> Dict:
    """Analyze snapshot directory and return summary."""
    
    if not snapshot_dir.exists():
        return {
            "error": f"Snapshot directory not found: {snapshot_dir}",
            "exists": False
        }
    
    # Load JSON index if available
    index_path = snapshot_dir / "snapshot_index.json"
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
    else:
        index_data = None
    
    # Count PNG files
    png_files = list(snapshot_dir.glob("*.png"))
    
    # Analyze scenes covered
    scenes = set()
    characters = set()
    
    for png in png_files:
        name = png.stem
        parts = name.split('_')
        
        if len(parts) >= 2:
            # Extract character (war, rog, mag)
            if len(parts) >= 2 and parts[1] in ['war', 'rog', 'mag']:
                characters.add(parts[1])
                # Scene is everything after character
                scene = '_'.join(parts[2:])
                scenes.add(scene)
            else:
                # No character (like title screen)
                scene = '_'.join(parts[1:])
                scenes.add(scene)
    
    # Expected scenes
    expected_scenes = {
        'title_screen',
        'class_selected',
        'cave_entrance',
        'skull_chamber',
        'cave_in',
        'primitive_village',
        'alley',
        'combat',
        'armory',
        'chiefs_house',
        'healing_pool',
        'village_changed',
        'inventory'
    }
    
    missing_scenes = expected_scenes - scenes
    
    # Calculate total file size
    total_size = sum(f.stat().st_size for f in png_files)
    
    return {
        "exists": True,
        "total_snapshots": len(png_files),
        "total_size_mb": round(total_size / (1024 * 1024), 2),
        "scenes_covered": sorted(list(scenes)),
        "scenes_count": len(scenes),
        "characters_covered": sorted(list(characters)),
        "characters_count": len(characters),
        "missing_scenes": sorted(list(missing_scenes)),
        "index_available": index_path.exists(),
        "markdown_available": (snapshot_dir / "player_gui_snapshots.md").exists(),
        "snapshot_files": [f.name for f in sorted(png_files)]
    }


def print_analysis(analysis: Dict) -> None:
    """Pretty-print analysis results."""
    
    if not analysis["exists"]:
        print(f"ERROR: {analysis['error']}")
        print("\nTo generate snapshots, run:")
        print("  python utilities/capture_player_gui_snapshots.py")
        return
    
    print("=" * 70)
    print("SNAPSHOT ANALYSIS")
    print("=" * 70)
    print()
    
    print(f"Total Snapshots: {analysis['total_snapshots']}")
    print(f"Total Size: {analysis['total_size_mb']} MB")
    print(f"Scenes Covered: {analysis['scenes_count']}")
    print(f"Characters: {', '.join(analysis['characters_covered']) if analysis['characters_covered'] else 'None'}")
    print()
    
    print("Available Reports:")
    print(f"  - JSON Index: {'Yes' if analysis['index_available'] else 'No'}")
    print(f"  - Markdown Report: {'Yes' if analysis['markdown_available'] else 'No'}")
    print()
    
    if analysis['scenes_covered']:
        print("Scenes Captured:")
        for scene in analysis['scenes_covered']:
            print(f"  - {scene}")
        print()
    
    if analysis['missing_scenes']:
        print("Missing Scenes:")
        for scene in analysis['missing_scenes']:
            print(f"  - {scene}")
        print()
    
    print("Snapshot Files:")
    for filename in analysis['snapshot_files']:
        print(f"  - {filename}")
    print()
    
    print("=" * 70)
    
    if analysis['missing_scenes']:
        print("NOTE: Some expected scenes are missing.")
        print("Run with --full for complete coverage:")
        print("  python utilities/capture_player_gui_snapshots.py --full")
    else:
        print("All expected scenes captured!")


def get_scene_info(scene_name: str) -> Dict:
    """Get information about a specific scene."""
    try:
        from player_gui import PlayerGameGUI  # type: ignore
        gui = PlayerGameGUI()
        
        info = {
            "scene": scene_name,
            "exists": scene_name in gui.scene_descriptions,
            "description": gui.scene_descriptions.get(scene_name, "Not found"),
            "has_choices": scene_name in gui.scene_choices,
            "choices": gui.scene_choices.get(scene_name, [])
        }
        
        gui.root.destroy()
        return info
        
    except Exception as e:
        return {
            "scene": scene_name,
            "error": str(e)
        }


def list_all_scenes() -> List[str]:
    """List all available scenes from PlayerGameGUI."""
    try:
        from player_gui import PlayerGameGUI  # type: ignore
        gui = PlayerGameGUI()
        scenes = list(gui.scene_descriptions.keys())
        gui.root.destroy()
        return sorted(scenes)
    except Exception as e:
        print(f"Error loading scenes: {e}")
        return []


def main(argv: List[str] | None = None) -> int:
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Analyze GUI snapshots")
    parser.add_argument(
        "--dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "player_gui_snapshots",
        help="Snapshot directory to analyze"
    )
    parser.add_argument(
        "--scene",
        type=str,
        help="Get info about a specific scene"
    )
    parser.add_argument(
        "--list-scenes",
        action="store_true",
        help="List all available scenes"
    )
    
    args = parser.parse_args(argv or sys.argv[1:])
    
    if args.list_scenes:
        print("Available scenes:")
        for scene in list_all_scenes():
            print(f"  - {scene}")
        return 0
    
    if args.scene:
        info = get_scene_info(args.scene)
        if "error" in info:
            print(f"Error: {info['error']}")
            return 1
        
        print(f"Scene: {info['scene']}")
        print(f"Exists: {info['exists']}")
        print(f"Description: {info['description']}")
        print(f"Has Choices: {info['has_choices']}")
        if info['choices']:
            print("Choices:")
            for i, choice in enumerate(info['choices'], 1):
                print(f"  {i}. {choice['text']}")
        return 0
    
    # Default: analyze snapshot directory
    analysis = analyze_snapshots(args.dir)
    print_analysis(analysis)
    
    return 0 if analysis.get("exists", False) else 1


if __name__ == "__main__":
    raise SystemExit(main())

