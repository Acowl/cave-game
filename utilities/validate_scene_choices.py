#!/usr/bin/env python3
"""
Scene Choice Validator for SHABUYA Cave Adventure.

Validates that all player choices in each scene have properly defined consequences
and that the consequences lead to the intended outcomes.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Tuple


def _ensure_import_path() -> None:
    utilities_dir = Path(__file__).resolve().parent
    project_root = utilities_dir.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))


_ensure_import_path()

try:
    from player_gui import PlayerGameGUI
except Exception as e:
    print(f"ERROR: Failed to import PlayerGameGUI: {e}")
    sys.exit(1)


def analyze_scene(scene_name: str, gui: PlayerGameGUI) -> Dict:
    """Analyze a single scene's choices and consequences."""
    
    if scene_name not in gui.scene_choices:
        return {
            "scene": scene_name,
            "error": "No choices defined for this scene",
            "valid": False
        }
    
    choices = gui.scene_choices[scene_name]
    analysis = {
        "scene": scene_name,
        "description": gui.scene_descriptions.get(scene_name, "No description"),
        "total_choices": len(choices),
        "choices": [],
        "issues": [],
        "valid": True
    }
    
    for i, choice in enumerate(choices, 1):
        choice_analysis = {
            "number": i,
            "text": choice.get("text", ""),
            "consequence": choice.get("consequence", ""),
            "has_consequence": choice.get("consequence", "") in gui.consequences,
            "consequence_details": {}
        }
        
        consequence_name = choice.get("consequence", "")
        if consequence_name in gui.consequences:
            cons_data = gui.consequences[consequence_name]
            choice_analysis["consequence_details"] = {
                "text": cons_data.get("text", ""),
                "has_effect": cons_data.get("effect") is not None
            }
        else:
            analysis["issues"].append(
                f"Choice {i} ('{choice['text']}') references undefined consequence: '{consequence_name}'"
            )
            analysis["valid"] = False
        
        analysis["choices"].append(choice_analysis)
    
    return analysis


def print_scene_analysis(analysis: Dict) -> None:
    """Pretty-print scene analysis."""
    
    scene = analysis["scene"]
    print(f"\n{'='*80}")
    print(f"SCENE: {scene.upper().replace('_', ' ')}")
    print(f"{'='*80}")
    
    if "error" in analysis:
        print(f"ERROR: {analysis['error']}")
        return
    
    print(f"\nDescription:")
    print(f"  {analysis['description'][:150]}...")
    print(f"\nTotal Choices: {analysis['total_choices']}")
    
    for choice in analysis["choices"]:
        print(f"\n  [{choice['number']}] {choice['text']}")
        print(f"      Consequence: {choice['consequence']}")
        
        if choice["has_consequence"]:
            print(f"      Status: OK")
            print(f"      Effect Text: {choice['consequence_details']['text']}")
        else:
            print(f"      Status: MISSING CONSEQUENCE")
    
    if analysis["issues"]:
        print(f"\nISSUES FOUND:")
        for issue in analysis["issues"]:
            print(f"  - {issue}")
    else:
        print(f"\nStatus: ALL CHOICES VALID")


def analyze_all_scenes(gui: PlayerGameGUI) -> List[Dict]:
    """Analyze all scenes."""
    results = []
    
    for scene_name in gui.scene_choices.keys():
        analysis = analyze_scene(scene_name, gui)
        results.append(analysis)
    
    return results


def generate_choice_flowchart(gui: PlayerGameGUI) -> None:
    """Generate a text-based flowchart of all choices and their consequences."""
    
    print("\n" + "="*80)
    print("COMPLETE GAME FLOW - SCENE BY SCENE")
    print("="*80)
    
    # Define the main progression path
    main_path = [
        "cave_entrance",
        "skull_chamber",
        "cave_in",
        "primitive_village",
        "alley",
        "armory",
        "chiefs_house",
        "healing_pool",
        "village_changed"
    ]
    
    for scene_name in main_path:
        if scene_name not in gui.scene_choices:
            continue
            
        print(f"\n{'='*80}")
        print(f"SCENE: {scene_name.upper().replace('_', ' ')}")
        print(f"{'='*80}")
        print(f"Description: {gui.scene_descriptions.get(scene_name, 'N/A')[:100]}...")
        print(f"\nPlayer Choices:")
        
        choices = gui.scene_choices[scene_name]
        for i, choice in enumerate(choices, 1):
            print(f"\n  [{i}] {choice['text']}")
            
            consequence_name = choice.get("consequence", "")
            if consequence_name in gui.consequences:
                cons = gui.consequences[consequence_name]
                print(f"      -> Consequence: {cons['text']}")
                
                # Try to determine what happens next
                try:
                    # Check if it advances to another scene
                    if "advance_to_scene" in cons['text'].lower() or "emerged" in cons['text'].lower():
                        words = cons['text'].split()
                        for word in ["primitive_village", "skull_chamber", "armory", "chiefs_house", 
                                   "healing_pool", "village_changed", "alley", "cave_in"]:
                            if word in cons['text'].lower():
                                print(f"      -> Next Scene: {word.replace('_', ' ').title()}")
                                break
                    
                    # Check if it starts combat
                    if "combat" in cons['text'].lower():
                        print(f"      -> Initiates: COMBAT")
                    
                    # Check if it's gated
                    if "key" in cons['text'].lower() and "need" in cons['text'].lower():
                        print(f"      -> Gated: Requires key")
                    
                    # Check if it gives items
                    if "find" in cons['text'].lower() or "discover" in cons['text'].lower():
                        print(f"      -> Reward: Items/Experience")
                        
                except Exception as e:
                    pass
            else:
                print(f"      -> ERROR: Undefined consequence '{consequence_name}'")


def validate_consequence_chains(gui: PlayerGameGUI) -> List[str]:
    """Validate that consequence chains make sense."""
    issues = []
    
    # Check for orphaned consequences (defined but never used)
    used_consequences = set()
    for scene_choices in gui.scene_choices.values():
        for choice in scene_choices:
            used_consequences.add(choice.get("consequence", ""))
    
    defined_consequences = set(gui.consequences.keys())
    orphaned = defined_consequences - used_consequences
    
    if orphaned:
        issues.append(f"Orphaned consequences (defined but never used): {sorted(orphaned)}")
    
    # Check for missing consequences (used but not defined)
    missing = used_consequences - defined_consequences
    missing.discard("")  # Remove empty string
    
    if missing:
        issues.append(f"Missing consequences (used but not defined): {sorted(missing)}")
    
    return issues


def main() -> int:
    """Main entry point."""
    print("="*80)
    print("SHABUYA CAVE ADVENTURE - SCENE CHOICE VALIDATOR")
    print("="*80)
    
    # Initialize GUI to load game data
    gui = PlayerGameGUI()
    gui.root.withdraw()  # Hide window
    
    # Validate consequence chains
    print("\n>>> VALIDATING CONSEQUENCE CHAINS...\n")
    chain_issues = validate_consequence_chains(gui)
    
    if chain_issues:
        print("ISSUES FOUND:")
        for issue in chain_issues:
            print(f"  - {issue}")
    else:
        print("All consequence chains are valid!")
    
    # Analyze all scenes
    print("\n>>> ANALYZING ALL SCENES...\n")
    results = analyze_all_scenes(gui)
    
    # Print each scene analysis
    for result in results:
        print_scene_analysis(result)
    
    # Generate flowchart
    generate_choice_flowchart(gui)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    total_scenes = len(results)
    valid_scenes = sum(1 for r in results if r.get("valid", False))
    total_choices = sum(r.get("total_choices", 0) for r in results)
    total_issues = sum(len(r.get("issues", [])) for r in results)
    
    print(f"Total Scenes: {total_scenes}")
    print(f"Valid Scenes: {valid_scenes}/{total_scenes}")
    print(f"Total Choices: {total_choices}")
    print(f"Total Issues: {total_issues}")
    
    if total_issues == 0 and not chain_issues:
        print("\nSTATUS: ALL SCENES AND CHOICES ARE VALID!")
        status_code = 0
    else:
        print("\nSTATUS: ISSUES FOUND - REVIEW REQUIRED")
        status_code = 1
    
    gui.root.destroy()
    return status_code


if __name__ == "__main__":
    raise SystemExit(main())

