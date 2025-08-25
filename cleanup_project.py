#!/usr/bin/env python3
"""
Project cleanup script - removes temporary and redundant files
"""

import os
import shutil
from pathlib import Path

def cleanup_project():
    """Clean up the project directory"""
    
    # Files to remove from root directory
    cleanup_files = [
        # Test files (keep functionality but move to tests/)
        'test_gui_integration.py',
        'test_full_main.py', 
        'test_minimal.py',
        'test_main_text_mode.py',
        'test_text_mode.py',
        'debug_test.py',
        
        # Temporary input files
        'game_input.txt',
        'input.txt',
        'quit_input.txt', 
        'test_input.txt',
        
        # Redundant files
        'game.py',  # Empty file
        'launcher_fixed.py',  # Superseded by improved main.py
        'gui_diagnostic.py',  # Move to tools/
        
        # Old validation files (keep in docs/ if needed)
        'VALIDATION_REPORT.md',
        'VS_CODE_TYPE_CHECKING_SETUP.md',
        'PROJECT_MANIFEST.md',
        
        # Build artifacts
        'build_installer.py',  # Move to tools/
    ]
    
    # Clean up files
    removed_files = []
    for file in cleanup_files:
        if os.path.exists(file):
            print(f"🗑️  Removing: {file}")
            os.remove(file)
            removed_files.append(file)
    
    # Clean up __pycache__ directories
    for root, dirs, files in os.walk('.'):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            print(f"🗑️  Removing: {pycache_path}")
            shutil.rmtree(pycache_path)
    
    return removed_files

if __name__ == "__main__":
    print("🧹 SHABUYA Project Cleanup")
    print("=" * 40)
    
    removed = cleanup_project()
    
    print(f"\n✅ Cleanup complete! Removed {len(removed)} files/directories.")
    print("\n📁 Recommended new structure:")
    print("""
    cave-game/
    ├── src/                    # Core game files
    │   ├── game_refactored.py
    │   ├── combat.py
    │   ├── scenes.py
    │   ├── player.py
    │   ├── item.py
    │   ├── ui.py
    │   ├── config.py
    │   └── game_events.py
    ├── gui/                    # GUI components  
    │   ├── gui.py
    │   └── launcher.py
    ├── scripts/               # Launch scripts
    │   ├── START_GAME.bat
    │   ├── start_game.sh
    │   └── main.py
    ├── tests/                 # Test files
    ├── tools/                 # Development tools
    ├── docs/                  # Documentation
    ├── distribution/          # Release package
    └── README.md
    """)
