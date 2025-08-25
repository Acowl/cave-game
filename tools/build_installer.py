#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Professional Build Script
Creates distributable package for desktop installation
"""

import os
import shutil
from pathlib import Path
import sys
import zipfile


def build_distribution():
    """Create a professional distribution package"""
    
    project_root = Path(__file__).parent.parent
    dist_dir = project_root / "dist"
    
    print("🏗️ Building SHABUYA Cave Adventure Distribution...")
    
    # Clean and create dist directory
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    print(f"📁 Creating distribution in: {dist_dir}")
    
    # Files and directories to include
    include_items = [
        "src/",
        "scripts/",
        "README.md",
        "requirements.txt"
    ]
    
    # Copy items to distribution
    for item_name in include_items:
        src_path = project_root / item_name
        if src_path.exists():
            dest_path = dist_dir / item_name
            
            if src_path.is_dir():
                print(f"  Copying directory: {item_name}")
                shutil.copytree(src_path, dest_path)
            else:
                print(f"  Copying file: {item_name}")
                shutil.copy2(src_path, dest_path)
        else:
            print(f"  ⚠️  Warning: {item_name} not found")
    
    # Create distribution-specific launcher
    create_dist_launchers(dist_dir)
    
    # Create zip package
    create_zip_package(project_root, dist_dir)
    
    print("✅ Distribution build completed!")
    print(f"📦 Files available in: {dist_dir}")


def create_dist_launchers(dist_dir):
    """Create distribution-specific launcher files"""
    
    # Main Python launcher
    main_launcher = '''#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Distribution Launcher
"""
import sys
from pathlib import Path

# Add src to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))

# Import and run
from scripts.main import main

if __name__ == "__main__":
    main()
'''
    
    launcher_path = dist_dir / "shabuya_launcher.py"
    with open(launcher_path, 'w') as f:
        f.write(main_launcher)
    
    # Windows batch file
    windows_launcher = '''@echo off
echo Starting SHABUYA Cave Adventure...
python shabuya_launcher.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error: Python not found or game failed to start.
    echo Please ensure Python 3.7+ is installed.
    pause
)
'''
    
    bat_path = dist_dir / "START_GAME.bat"
    with open(bat_path, 'w') as f:
        f.write(windows_launcher)
    
    # Unix shell script
    unix_launcher = '''#!/bin/bash
echo "Starting SHABUYA Cave Adventure..."
python3 shabuya_launcher.py
if [ $? -ne 0 ]; then
    echo
    echo "Error: Python 3 not found or game failed to start."
    echo "Please ensure Python 3.7+ is installed."
    echo "Press Enter to exit."
    read
fi
'''
    
    sh_path = dist_dir / "start_game.sh"
    with open(sh_path, 'w') as f:
        f.write(unix_launcher)
    
    # Make executable
    try:
        os.chmod(sh_path, 0o755)
    except:
        pass
    
    print("  ✅ Created distribution launchers")


def create_zip_package(project_root, dist_dir):
    """Create a ZIP package of the distribution"""
    
    zip_path = project_root / "SHABUYA-Cave-Adventure-v1.0-Professional.zip"
    
    print(f"📦 Creating ZIP package: {zip_path.name}")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dist_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(dist_dir)
                zipf.write(file_path, arcname)
    
    file_size = zip_path.stat().st_size / 1024 / 1024  # MB
    print(f"  ✅ Created {zip_path.name} ({file_size:.1f} MB)")


if __name__ == "__main__":
    build_distribution()
