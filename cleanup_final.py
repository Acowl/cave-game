#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Project Cleanup and Reorganization Script
Automated cleanup to transform the project into a professional structure
"""

import os
import shutil
from pathlib import Path

def cleanup_project():
    """Execute the complete project cleanup and reorganization"""
    
    project_root = Path(__file__).parent
    print(f"🧹 Starting cleanup of: {project_root}")
    
    # Files to move to tests/
    test_files = [
        'test_gui_integration.py',
        'test_full_main.py', 
        'test_game.py',
        'test_minimal.py',
        'test_main_text_mode.py',
        'test_text_mode.py',
        'debug_test.py'
    ]
    
    # Input files to move to tests/test_data/
    test_data_files = [
        'gui_input.txt',
        'game_input.txt', 
        'test_input.txt',
        'alley_battle_input.txt'
    ]
    
    # Files to move to tools/
    tool_files = [
        'gui_diagnostic.py',
        'build_installer.py'
    ]
    
    # Files to move to docs/
    doc_files = [
        'VALIDATION_REPORT.md',
        'VS_CODE_TYPE_CHECKING_SETUP.md',
        'PROJECT_MANIFEST.md',
        'CLEANUP_PLAN.md'
    ]
    
    # Files to delete (empty, redundant, or temporary)
    files_to_delete = [
        'game.py',  # Empty file
        'launcher_fixed.py',  # Superseded
        'cleanup_project.py',  # This script itself after completion
    ]
    
    # Directories to clean up
    dirs_to_delete = [
        '__pycache__'
    ]
    
    print("📁 Moving test files...")
    for file_name in test_files:
        src_path = project_root / file_name
        if src_path.exists():
            dest_path = project_root / 'tests' / file_name
            print(f"  Moving {file_name} → tests/")
            try:
                shutil.move(str(src_path), str(dest_path))
            except Exception as e:
                print(f"    Warning: Could not move {file_name}: {e}")
    
    print("📊 Moving test data files...")
    for file_name in test_data_files:
        src_path = project_root / file_name
        if src_path.exists():
            dest_path = project_root / 'tests' / 'test_data' / file_name
            print(f"  Moving {file_name} → tests/test_data/")
            try:
                shutil.move(str(src_path), str(dest_path))
            except Exception as e:
                print(f"    Warning: Could not move {file_name}: {e}")
    
    print("🔧 Moving tool files...")
    for file_name in tool_files:
        src_path = project_root / file_name
        if src_path.exists():
            dest_path = project_root / 'tools' / file_name
            print(f"  Moving {file_name} → tools/")
            try:
                shutil.move(str(src_path), str(dest_path))
            except Exception as e:
                print(f"    Warning: Could not move {file_name}: {e}")
    
    print("📚 Moving documentation files...")
    for file_name in doc_files:
        src_path = project_root / file_name
        if src_path.exists():
            dest_path = project_root / 'docs' / file_name
            print(f"  Moving {file_name} → docs/")
            try:
                shutil.move(str(src_path), str(dest_path))
            except Exception as e:
                print(f"    Warning: Could not move {file_name}: {e}")
    
    print("🗑️ Removing temporary files...")
    for file_name in files_to_delete:
        file_path = project_root / file_name
        if file_path.exists():
            print(f"  Deleting {file_name}")
            try:
                file_path.unlink()
            except Exception as e:
                print(f"    Warning: Could not delete {file_name}: {e}")
    
    print("🗂️ Removing temporary directories...")
    for dir_name in dirs_to_delete:
        dir_path = project_root / dir_name
        if dir_path.exists():
            print(f"  Removing {dir_name}/")
            try:
                shutil.rmtree(str(dir_path))
            except Exception as e:
                print(f"    Warning: Could not remove {dir_name}: {e}")
    
    # Create new launcher scripts for cross-platform compatibility
    create_launcher_scripts(project_root)
    
    # Create a professional README
    create_new_readme(project_root)
    
    # Create .gitignore
    create_gitignore(project_root)
    
    print("✅ Cleanup completed successfully!")
    print("\n📂 New project structure:")
    print_directory_structure(project_root)
    
    print("\n🎯 Next steps:")
    print("  1. Test the new structure: python scripts/main.py")
    print("  2. Update import statements in remaining old files if needed")
    print("  3. Update distribution folder with new structure")
    print("  4. Commit changes to version control")

def create_launcher_scripts(project_root):
    """Create cross-platform launcher scripts"""
    
    # Windows batch file
    bat_content = '''@echo off
echo Starting SHABUYA Cave Adventure...
python scripts/main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error running the game. Press any key to exit.
    pause >nul
)
'''
    bat_path = project_root / 'scripts' / 'START_GAME.bat'
    print(f"  Creating {bat_path.name}")
    with open(bat_path, 'w') as f:
        f.write(bat_content)
    
    # Unix shell script
    sh_content = '''#!/bin/bash
echo "Starting SHABUYA Cave Adventure..."
cd "$(dirname "$0")/.."
python3 scripts/main.py
if [ $? -ne 0 ]; then
    echo
    echo "Error running the game. Press Enter to exit."
    read
fi
'''
    sh_path = project_root / 'scripts' / 'start_game.sh'
    print(f"  Creating {sh_path.name}")
    with open(sh_path, 'w') as f:
        f.write(sh_content)
    
    # Make shell script executable
    try:
        os.chmod(sh_path, 0o755)
    except Exception as e:
        print(f"    Warning: Could not make {sh_path.name} executable: {e}")

def create_new_readme(project_root):
    """Create a professional README.md"""
    readme_content = '''# 🗻 SHABUYA - Cave Adventure

A professionally crafted text-based adventure game featuring multiple character classes, combat systems, and an immersive storyline.

## 🎮 Features

- **Multiple Character Classes**: Choose from Rogue, Warrior, or Mage
- **Combat System**: Class-specific weapons and abilities
- **Progressive Story**: Navigate through interconnected scenes
- **Character Development**: Upgrade stats and unlock new abilities
- **Enhanced Weapons**: Discover powerful artifacts
- **Cross-Platform**: Runs on Windows, macOS, and Linux

## 🚀 Quick Start

### Option 1: Simple Launch
```bash
python scripts/main.py
```

### Option 2: GUI Launcher
```bash
python scripts/launcher.py
```

### Option 3: Platform Scripts
- **Windows**: Double-click `scripts/START_GAME.bat`
- **Unix/Linux/macOS**: Run `scripts/start_game.sh`

## 🎯 Gameplay

1. **Choose Your Class**
   - **Rogue**: Agility-based stealth attacks
   - **Warrior**: Strength-based powerful melee
   - **Mage**: Intelligence-based magical abilities

2. **Explore the World**
   - Navigate through mysterious caves and ancient villages
   - Discover hidden areas and secrets
   - Interact with various characters and environments

3. **Combat & Progression**
   - Battle creatures using class-specific weapons
   - Level up and allocate attribute points
   - Find enhanced weapons with special properties

4. **Complete Your Quest**
   - Progress through challenging scenes
   - Defeat bosses and overcome obstacles
   - Reach the final confrontation with the Divine Heart

## 📋 Requirements

- Python 3.7 or higher
- tkinter (for GUI mode, usually included with Python)

## 🏗️ Project Structure

```
cave-game/
├── src/                    # Core game source code
│   ├── core/              # Game engine and logic
│   ├── entities/          # Player, items, and game objects
│   ├── interfaces/        # UI components (GUI and console)
│   └── config.py          # Game configuration
├── scripts/               # Launch scripts and utilities
├── tests/                 # Test files and test data
├── tools/                 # Development tools
├── docs/                  # Documentation
├── dist/                  # Distribution files
└── README.md              # This file
```

## 🎨 Game Modes

### Text Mode (Default)
Full interactive console experience with rich text output.

### GUI Mode
Simplified desktop interface with launch options and basic information.

## 🏆 Development

This project demonstrates professional Python development practices:

- **Clean Architecture**: Modular design with separated concerns
- **Professional Structure**: Industry-standard project organization
- **Cross-Platform Support**: Works on all major operating systems
- **Comprehensive Testing**: Test suite for quality assurance
- **Documentation**: Clear documentation and code comments
- **Version Control**: Git-ready project structure

## 📄 License

This project is developed for educational and portfolio purposes.

---

**Have fun exploring the caves!** 🗻✨
'''
    
    readme_path = project_root / 'README.md'
    print(f"  Creating professional {readme_path.name}")
    with open(readme_path, 'w') as f:
        f.write(readme_content)

def create_gitignore(project_root):
    """Create a .gitignore file"""
    gitignore_content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Game specific
*.log
debug_*.txt
temp_*.py
'''
    
    gitignore_path = project_root / '.gitignore'
    print(f"  Creating {gitignore_path.name}")
    with open(gitignore_path, 'w') as f:
        f.write(gitignore_content)

def print_directory_structure(root_path, prefix="", max_depth=3, current_depth=0):
    """Print the directory structure"""
    if current_depth >= max_depth:
        return
        
    try:
        items = sorted(root_path.iterdir())
        dirs = [item for item in items if item.is_dir() and not item.name.startswith('.')]
        files = [item for item in items if item.is_file() and not item.name.startswith('.')]
        
        # Print directories first
        for i, dir_path in enumerate(dirs):
            is_last_dir = (i == len(dirs) - 1) and len(files) == 0
            print(f"{prefix}{'└── ' if is_last_dir else '├── '}{dir_path.name}/")
            
            extension = "    " if is_last_dir else "│   "
            print_directory_structure(dir_path, prefix + extension, max_depth, current_depth + 1)
        
        # Print files
        for i, file_path in enumerate(files[:5]):  # Limit to first 5 files
            is_last = i == len(files) - 1 or i == 4
            print(f"{prefix}{'└── ' if is_last else '├── '}{file_path.name}")
            
        if len(files) > 5:
            print(f"{prefix}└── ... ({len(files) - 5} more files)")
            
    except PermissionError:
        print(f"{prefix}└── [Permission Denied]")

if __name__ == "__main__":
    cleanup_project()
