#!/usr/bin/env python3
"""
Multi-Agent Cleanup and Analysis Script

Analyzes the codebase for:
1. Unnecessary files
2. Duplicate assets
3. Corrupted images
4. Scene description issues
5. Revisiting logic problems
"""

import os
from pathlib import Path
from PIL import Image
import json

REPO_ROOT = Path(__file__).parent.parent

def analyze_files():
    """Analyze repository structure for unnecessary files"""
    print("=" * 60)
    print("FILE ANALYSIS")
    print("=" * 60)
    
    unnecessary_files = []
    
    # Check for duplicate files
    duplicate_patterns = [
        ("cave entrance.png", "cave_entrance.png"),
        ("primitive village.png", "primitive_village.png"),
        ("primitive viillage (cosmic).png", "primitive_village.png"),
        ("chiefs house.png", "chief_house.png"),
        ("healing pool.png", "healing_pool.png"),
        ("skull chamber.png", "skull_chamber.png"),
    ]
    
    backgrounds_dir = REPO_ROOT / "assets" / "backgrounds"
    
    print("\n1. Duplicate Background Files:")
    duplicates_found = []
    for old_name, new_name in duplicate_patterns:
        old_path = backgrounds_dir / old_name
        new_path = backgrounds_dir / new_name
        if old_path.exists() and new_path.exists():
            duplicates_found.append((old_name, new_name))
            print(f"   - {old_name} (can be removed, {new_name} exists)")
    
    if not duplicates_found:
        print("   No duplicates found")
    
    # Check for __pycache__ directories
    print("\n2. Python Cache Directories:")
    pycache_dirs = []
    for root, dirs, files in os.walk(REPO_ROOT):
        if '__pycache__' in dirs:
            pycache_dirs.append(os.path.join(root, '__pycache__'))
    
    if pycache_dirs:
        for cache_dir in pycache_dirs:
            print(f"   - {cache_dir}")
    else:
        print("   No __pycache__ directories found")
    
    return {
        'duplicates': duplicates_found,
        'pycache_dirs': pycache_dirs
    }

def analyze_images():
    """Analyze images for corruption"""
    print("\n" + "=" * 60)
    print("IMAGE ANALYSIS")
    print("=" * 60)
    
    backgrounds_dir = REPO_ROOT / "assets" / "backgrounds"
    corrupted_images = []
    valid_images = []
    
    print("\n1. Background Image Analysis:")
    for img_file in backgrounds_dir.glob("*.png"):
        try:
            img = Image.open(img_file)
            img.verify()
            valid_images.append(img_file.name)
            print(f"   ✓ {img_file.name} - Valid ({img.size[0]}x{img.size[1]})")
        except Exception as e:
            corrupted_images.append((img_file.name, str(e)))
            print(f"   ✗ {img_file.name} - CORRUPTED: {e}")
    
    return {
        'corrupted': corrupted_images,
        'valid': valid_images
    }

def analyze_scenes():
    """Analyze scene descriptions and revisiting logic"""
    print("\n" + "=" * 60)
    print("SCENE ANALYSIS")
    print("=" * 60)
    
    player_gui_file = REPO_ROOT / "player_gui.py"
    
    # Read player_gui.py to analyze scenes
    with open(player_gui_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract scene descriptions
    scene_descriptions = {}
    if 'scene_descriptions = {' in content:
        # Parse scene descriptions
        import re
        desc_match = re.search(r'scene_descriptions = \{([^}]+)\}', content, re.DOTALL)
        if desc_match:
            desc_text = desc_match.group(1)
            # Simple extraction
            for line in desc_text.split('\n'):
                if '":' in line:
                    parts = line.split('":')
                    if len(parts) == 2:
                        scene_name = parts[0].strip().strip('"')
                        description = parts[1].strip().strip(',"')
                        if scene_name:
                            scene_descriptions[scene_name] = description
    
    # Expected scenes from scene_progression
    expected_scenes = [
        "cave_entrance", "skull_chamber", "primitive_village",
        "chiefs_house", "healing_pool", "village_changed",
        "alley", "armory", "cave_in"
    ]
    
    print("\n1. Scene Descriptions:")
    missing_descriptions = []
    for scene in expected_scenes:
        if scene in scene_descriptions:
            desc = scene_descriptions[scene]
            print(f"   ✓ {scene}: {desc[:50]}...")
        else:
            missing_descriptions.append(scene)
            print(f"   ✗ {scene}: MISSING DESCRIPTION")
    
    # Check revisiting logic
    print("\n2. Revisiting Logic Analysis:")
    if 'visited_scenes' in content:
        if 'show_scene_description' in content:
            # Check if show_scene_description checks visited_scenes
            if 'visited_scenes' in content[content.find('show_scene_description'):content.find('show_scene_description')+500]:
                print("   ✓ show_scene_description references visited_scenes")
            else:
                print("   ✗ show_scene_description does NOT check visited_scenes")
                print("   ISSUE: Scene descriptions always shown as first-time")
        else:
            print("   ✗ show_scene_description method not found")
    else:
        print("   ✗ visited_scenes tracking not found")
    
    return {
        'missing_descriptions': missing_descriptions,
        'has_revisiting_logic': 'visited_scenes' in content,
        'revisiting_works': False  # Will be determined by code analysis
    }

def analyze_structure():
    """Analyze folder structure"""
    print("\n" + "=" * 60)
    print("FOLDER STRUCTURE ANALYSIS")
    print("=" * 60)
    
    print("\nCurrent Structure:")
    for root, dirs, files in os.walk(REPO_ROOT):
        level = root.replace(str(REPO_ROOT), '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        
        # Limit depth to avoid too much output
        if level >= 3:
            dirs[:] = []  # Don't recurse deeper
    
    return {}

def main():
    """Run all analyses"""
    print("\n" + "=" * 60)
    print("MULTI-AGENT CLEANUP & ANALYSIS")
    print("=" * 60)
    
    file_analysis = analyze_files()
    image_analysis = analyze_images()
    scene_analysis = analyze_scenes()
    structure_analysis = analyze_structure()
    
    # Generate report
    print("\n" + "=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)
    
    print(f"\nFiles to Remove:")
    print(f"  - Duplicate backgrounds: {len(file_analysis['duplicates'])}")
    print(f"  - __pycache__ directories: {len(file_analysis['pycache_dirs'])}")
    
    print(f"\nImage Issues:")
    print(f"  - Corrupted images: {len(image_analysis['corrupted'])}")
    print(f"  - Valid images: {len(image_analysis['valid'])}")
    
    print(f"\nScene Issues:")
    print(f"  - Missing descriptions: {len(scene_analysis['missing_descriptions'])}")
    print(f"  - Revisiting logic: {'✓' if scene_analysis['has_revisiting_logic'] else '✗'}")
    
    # Save report to file
    report = {
        'file_analysis': file_analysis,
        'image_analysis': image_analysis,
        'scene_analysis': scene_analysis
    }
    
    report_file = REPO_ROOT / ".cursor" / "analysis_report.json"
    report_file.parent.mkdir(exist_ok=True)
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nReport saved to: {report_file}")
    
    return report

if __name__ == "__main__":
    main()

