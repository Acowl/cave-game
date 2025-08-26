#!/usr/bin/env python3
"""
Project Cleanup and Reorganization Script
Cleans up the cave-game project structure and organizes files properly
"""

import os
import shutil
from pathlib import Path

def cleanup_project():
    """Clean up and reorganize the project structure"""
    base_path = Path("/workspaces/cave-game")
    
    print("🧹 Starting project cleanup and reorganization...")
    
    # Define file movements
    movements = {
        # Test files
        "tests/unit/": [
            "test_*.py"
        ],
        "tests/integration/": [
            "gui_test_runner.py",
            "gui_testing_guide.py"
        ],
        "tests/assets/": [
            "test_input.txt",
            "game_input.txt",
            "quit_input.txt",
            "input.txt"
        ],
        
        # Utility scripts
        "utilities/": [
            "replace_assets.py",
            "create_placeholder_assets.py",
            "verify_asset_tool.py",
            "verify_cleanup.py",
            "verify_phase1_readiness.py",
            "cleanup_final.py",
            "cleanup_project.py",
            "create_basic_graphics.py",
            "generate_enhanced_graphics.py",
            "graphics_status_report.py",
            "debug_enhanced_gui.py",
            "debug_test.py",
            "local_setup_verification.py",
            "build_config.py",
            "build_engine.py",
            "build_installer.py",
            "demo_distribution_system.py",
            "distribution_manager.py",
            "native_build_system.py"
        ],
        
        # Documentation
        "documentation/": [
            "AI_IMAGE_PROMPTS.md",
            "CLEANUP_PLAN.md", 
            "CLEANUP_SUMMARY.md",
            "COMPLETE_ASSET_LIST.md",
            "DEBUG_FIX_REPORT.md",
            "DEVELOPMENT_ROADMAP.md",
            "DISTRIBUTION_SYSTEM.md",
            "ERROR_RESOLUTION_COMPLETE.md",
            "GRAPHICS_INTEGRATION_STRATEGY.md",
            "GRAPHICS_INTEGRATION_SUMMARY.md",
            "PROJECT_MANIFEST.md",
            "TESTING_GUIDE.md",
            "VALIDATION_REPORT.md",
            "VS_CODE_TYPE_CHECKING_SETUP.md"
        ],
        
        # Archive old versions
        "archive/": [
            "game.py",  # old version
            "launcher_fixed.py",
            "gui_diagnostic.py",
            "gui_integrated.py",
            "build_config.json"
        ]
    }
    
    # Execute movements
    for target_dir, file_patterns in movements.items():
        target_path = base_path / target_dir
        target_path.mkdir(parents=True, exist_ok=True)
        
        for pattern in file_patterns:
            if "*" in pattern:
                # Handle glob patterns
                import glob
                matching_files = glob.glob(str(base_path / pattern))
                for file_path in matching_files:
                    file_name = Path(file_path).name
                    if Path(file_path).exists():
                        print(f"  Moving {file_name} -> {target_dir}")
                        shutil.move(file_path, target_path / file_name)
            else:
                # Handle specific files
                source_file = base_path / pattern
                if source_file.exists():
                    print(f"  Moving {pattern} -> {target_dir}")
                    shutil.move(str(source_file), target_path / pattern)
    
    print("\n🗑️  Removing empty/unnecessary directories...")
    
    # Remove empty directories
    dirs_to_remove = ["docs", "releases", "tests/test_data"]
    for dir_name in dirs_to_remove:
        dir_path = base_path / dir_name
        if dir_path.exists():
            try:
                if dir_path.is_dir() and not any(dir_path.iterdir()):
                    print(f"  Removing empty directory: {dir_name}")
                    dir_path.rmdir()
                elif dir_path.is_dir():
                    print(f"  Directory {dir_name} not empty, skipping")
            except Exception as e:
                print(f"  Could not remove {dir_name}: {e}")
    
    # Clean up duplicate files in src/ and scripts/
    print("\n📁 Cleaning up duplicate files...")
    
    # Check src/ contents
    src_dir = base_path / "src"
    if src_dir.exists():
        print("  Analyzing src/ directory...")
        # The src/ directory has an organized structure, but we're using root files
        # Move it to archive since we use the root-level files
        archive_src = base_path / "archive" / "src_structure"
        if not archive_src.exists():
            print("  Moving src/ to archive/src_structure/")
            shutil.move(str(src_dir), str(archive_src))
    
    # Check scripts/ contents  
    scripts_dir = base_path / "scripts"
    if scripts_dir.exists():
        print("  Cleaning scripts/ directory...")
        for script_file in scripts_dir.glob("*.py"):
            # These are likely duplicates, move to archive
            archive_path = base_path / "archive" / "scripts"
            archive_path.mkdir(exist_ok=True)
            print(f"  Moving {script_file.name} to archive/scripts/")
            shutil.move(str(script_file), archive_path / script_file.name)
        
        # Remove empty scripts directory
        if not any(scripts_dir.iterdir()):
            scripts_dir.rmdir()
            print("  Removed empty scripts/ directory")
    
    print("\n✅ Project cleanup completed!")
    print("\n📊 New project structure:")
    show_project_structure()

def show_project_structure():
    """Display the cleaned up project structure"""
    base_path = Path("/workspaces/cave-game")
    
    structure = {
        "Core Game Files": [
            "main.py", "game_refactored.py", "enhanced_gui_system.py",
            "gui.py", "ui.py", "combat.py", "player.py", "item.py", 
            "scenes.py", "game_events.py", "config.py"
        ],
        "Assets": ["game_assets/"],
        "Tests": ["tests/unit/", "tests/integration/", "tests/assets/"],
        "Utilities": ["utilities/"],
        "Documentation": ["documentation/", "README.md"],
        "Distribution": ["distribution/", "requirements.txt", "start_game.sh", "START_GAME.bat"],
        "Steam Integration": ["steam_integration/"],
        "Archive": ["archive/"],
        "Special": ["launcher.py", "SHABUYA-Cave-Adventure-v1.0.zip"]
    }
    
    for category, items in structure.items():
        print(f"\n📂 {category}:")
        for item in items:
            item_path = base_path / item
            if item_path.exists():
                if item_path.is_dir():
                    count = len(list(item_path.rglob("*")))
                    print(f"  ✅ {item} ({count} files)")
                else:
                    print(f"  ✅ {item}")
            else:
                print(f"  ❌ {item} (missing)")

if __name__ == "__main__":
    cleanup_project()
