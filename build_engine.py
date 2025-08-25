#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Universal Build Engine
Scalable build system for multiple distribution channels including Steam
"""

import os
import shutil
import zipfile
import json
from pathlib import Path
from typing import List, Dict, Optional, Set
import tempfile
import subprocess
import fnmatch

from build_config import BuildConfiguration, BuildTarget, STEAM_CONFIG


class UniversalBuilder:
    """Universal build engine for multiple distribution targets"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path(__file__).parent
        self.config = BuildConfiguration(self.project_root)
        self.build_output = self.project_root / "build_output"
        
    def build_target(self, target_name: str, clean: bool = True) -> Path:
        """Build a specific distribution target"""
        target = self.config.get_target(target_name)
        
        print(f"🏗️ Building {target.name}...")
        print(f"📋 {target.description}")
        
        if clean and self.build_output.exists():
            shutil.rmtree(self.build_output)
        
        self.build_output.mkdir(exist_ok=True)
        
        # Create target-specific output directory
        output_name = target.get_output_name(
            self.config.metadata.short_name,
            self.config.metadata.version
        )
        target_dir = self.build_output / output_name
        target_dir.mkdir(exist_ok=True)
        
        # Copy files based on patterns
        self._copy_files(target, target_dir)
        
        # Create launchers
        self._create_launchers(target, target_dir)
        
        # Create platform-specific assets
        if target.steam_ready:
            self._create_steam_assets(target, target_dir)
        
        if target.store_assets:
            self._create_store_assets(target, target_dir)
        
        # Create documentation
        self._create_documentation(target, target_dir)
        
        # Package the build
        package_path = None
        if target.create_zip:
            package_path = self._create_zip_package(target, target_dir)
        
        if target.create_installer:
            self._create_installer(target, target_dir)
        
        print(f"✅ Build complete: {target_dir}")
        if package_path:
            print(f"📦 Package created: {package_path}")
            
        return package_path or target_dir
    
    def _copy_files(self, target: BuildTarget, target_dir: Path):
        """Copy files based on include/exclude patterns"""
        print("📂 Copying files...")
        
        copied_files = set()
        
        # Process include patterns
        for pattern in target.include_patterns:
            matches = list(self.project_root.glob(pattern))
            for match in matches:
                if match.is_file():
                    # Check if excluded
                    if self._is_excluded(match, target.exclude_patterns):
                        continue
                    
                    # Calculate relative path and copy
                    rel_path = match.relative_to(self.project_root)
                    dest_path = target_dir / rel_path
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    shutil.copy2(match, dest_path)
                    copied_files.add(str(rel_path))
                    print(f"  ✅ {rel_path}")
        
        print(f"📁 Copied {len(copied_files)} files")
        return copied_files
    
    def _is_excluded(self, file_path: Path, exclude_patterns: List[str]) -> bool:
        """Check if file matches any exclude pattern"""
        rel_path = str(file_path.relative_to(self.project_root))
        
        for pattern in exclude_patterns:
            if fnmatch.fnmatch(rel_path, pattern):
                return True
        return False
    
    def _create_launchers(self, target: BuildTarget, target_dir: Path):
        """Create platform-specific launchers"""
        print("🚀 Creating launchers...")
        
        launchers = target.launchers
        metadata = self.config.metadata
        
        # Python launcher (universal)
        if launchers.get("python", False):
            self._create_python_launcher(target_dir, metadata)
        
        # Windows batch launcher  
        if launchers.get("batch", False):
            self._create_batch_launcher(target_dir, metadata)
        
        # Unix shell launcher
        if launchers.get("shell", False):
            self._create_shell_launcher(target_dir, metadata)
        
        # Desktop launcher (Linux)
        if launchers.get("desktop", False):
            self._create_desktop_launcher(target_dir, metadata)
        
        # GUI launcher
        if launchers.get("gui_launcher", False):
            self._create_gui_launcher(target_dir, metadata)
        
        # Steam launcher
        if launchers.get("steam", False):
            self._create_steam_launcher(target_dir, metadata)
    
    def _create_python_launcher(self, target_dir: Path, metadata):
        """Create universal Python launcher"""
        launcher_content = f'''#!/usr/bin/env python3
"""
{metadata.name} - Universal Launcher
{metadata.tagline}
"""

import sys
import os
from pathlib import Path

# Setup paths
game_root = Path(__file__).parent
sys.path.insert(0, str(game_root))
if (game_root / "src").exists():
    sys.path.insert(0, str(game_root / "src"))

def main():
    """Main launcher entry point"""
    try:
        # Import the main game function
        if (game_root / "src" / "core" / "game_engine.py").exists():
            from src.core.game_engine import main as game_main
        elif (game_root / "scripts" / "main.py").exists():
            from scripts.main import main as game_main
        else:
            from main import main as game_main
        
        # Launch the game
        game_main()
        
    except ImportError as e:
        print(f"❌ Error importing game: {{e}}")
        print("📁 Please ensure all game files are present")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"❌ Error running game: {{e}}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
'''
        
        launcher_path = target_dir / "launch_game.py"
        with open(launcher_path, 'w') as f:
            f.write(launcher_content)
        
        # Make executable on Unix systems
        os.chmod(launcher_path, 0o755)
        print(f"  ✅ Python launcher: {launcher_path.name}")
    
    def _create_batch_launcher(self, target_dir: Path, metadata):
        """Create Windows batch launcher"""
        batch_content = f'''@echo off
title {metadata.name} Launcher
echo.
echo {"="*60}
echo.
echo        {metadata.name.upper()}
echo        {metadata.tagline}
echo.
echo {"="*60}
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found!
    echo.
    echo Please install Python 3.7+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

REM Launch the game
echo 🚀 Starting {metadata.name}...
echo.

REM Try different launch methods
if exist "launch_game.py" (
    python launch_game.py
) else if exist "scripts\\main.py" (
    python scripts\\main.py
) else if exist "main.py" (
    python main.py
) else (
    echo ❌ Game launcher not found!
    echo Please ensure all game files are present.
    pause
    exit /b 1
)

REM Handle errors
if errorlevel 1 (
    echo.
    echo ❌ Game exited with an error.
    echo.
    echo Troubleshooting tips:
    echo 1. Make sure Python 3.7+ is installed
    echo 2. Check that all game files are present
    echo 3. Try running: python launch_game.py
    echo.
    pause
)
'''
        
        batch_path = target_dir / "LAUNCH_GAME.bat"
        with open(batch_path, 'w') as f:
            f.write(batch_content)
        print(f"  ✅ Windows launcher: {batch_path.name}")
    
    def _create_shell_launcher(self, target_dir: Path, metadata):
        """Create Unix shell launcher"""
        shell_content = f'''#!/bin/bash

# {metadata.name} - Unix Launcher
# {metadata.tagline}

echo "{"="*60}"
echo ""
echo "        {metadata.name.upper()}"
echo "        {metadata.tagline}" 
echo ""
echo "{"="*60}"
echo ""

# Function to find Python
find_python() {{
    if command -v python3 &> /dev/null; then
        echo "python3"
    elif command -v python &> /dev/null; then
        echo "python"
    else
        echo ""
    fi
}}

# Check for Python
PYTHON_CMD=$(find_python)

if [ -z "$PYTHON_CMD" ]; then
    echo "❌ Python not found!"
    echo ""
    echo "Please install Python 3.7+ from https://python.org"
    echo ""
    echo "Installation commands by distro:"
    echo "  Ubuntu/Debian: sudo apt-get install python3"
    echo "  CentOS/RHEL:   sudo yum install python3"
    echo "  Fedora:        sudo dnf install python3"
    echo "  Arch Linux:    sudo pacman -S python"
    echo "  macOS:         brew install python"
    echo ""
    exit 1
fi

echo "🐍 Using Python: $($PYTHON_CMD --version 2>&1)"
echo ""

# Launch the game
echo "🚀 Starting {metadata.name}..."
echo ""

# Try different launch methods
if [ -f "launch_game.py" ]; then
    $PYTHON_CMD launch_game.py
elif [ -f "scripts/main.py" ]; then
    $PYTHON_CMD scripts/main.py
elif [ -f "main.py" ]; then
    $PYTHON_CMD main.py
else
    echo "❌ Game launcher not found!"
    echo "Please ensure all game files are present."
    exit 1
fi

# Handle errors
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Game exited with an error."
    echo ""
    echo "Troubleshooting tips:"
    echo "1. Make sure Python 3.7+ is installed"
    echo "2. Check that all game files are present"
    echo "3. Try running: $PYTHON_CMD launch_game.py"
    echo ""
fi
'''
        
        shell_path = target_dir / "launch_game.sh"
        with open(shell_path, 'w') as f:
            f.write(shell_content)
        
        # Make executable
        os.chmod(shell_path, 0o755)
        print(f"  ✅ Unix launcher: {shell_path.name}")
    
    def _create_steam_launcher(self, target_dir: Path, metadata):
        """Create Steam-specific launcher"""
        steam_launcher = f'''#!/usr/bin/env python3
"""
{metadata.name} - Steam Integration Launcher
Handles Steam-specific initialization and features
"""

import sys
import os
from pathlib import Path

# Steam integration (when available)
try:
    # This will be available when running through Steam
    import steam
    STEAM_AVAILABLE = True
except ImportError:
    STEAM_AVAILABLE = False

def initialize_steam_features():
    """Initialize Steam-specific features"""
    if not STEAM_AVAILABLE:
        return False
    
    try:
        # Initialize Steam API (placeholder - implement when ready)
        # steam.initialize()
        print("🎮 Steam features initialized")
        return True
    except Exception as e:
        print(f"⚠️ Steam initialization warning: {{e}}")
        return False

def main():
    """Steam launcher main function"""
    # Initialize Steam features if available
    steam_ready = initialize_steam_features()
    
    # Setup game paths
    game_root = Path(__file__).parent
    sys.path.insert(0, str(game_root))
    if (game_root / "src").exists():
        sys.path.insert(0, str(game_root / "src"))
    
    try:
        # Import and run the game
        from src.core.game_engine import main as game_main
        
        # Pass Steam context to game if available
        if steam_ready:
            # In the future, we can pass Steam context
            game_main()
        else:
            game_main()
            
    except Exception as e:
        print(f"❌ Game error: {{e}}")
        if STEAM_AVAILABLE:
            # In Steam, we might want to report errors differently
            pass
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
'''
        
        steam_path = target_dir / "steam_launcher.py"
        with open(steam_path, 'w') as f:
            f.write(steam_launcher)
        print(f"  ✅ Steam launcher: {steam_path.name}")
    
    def _create_steam_assets(self, target: BuildTarget, target_dir: Path):
        """Create Steam-specific assets and configuration"""
        print("🎮 Creating Steam assets...")
        
        steam_dir = target_dir / "steam_config"
        steam_dir.mkdir(exist_ok=True)
        
        # App build VDF (Steam configuration)
        app_build_vdf = f'''
"AppBuild"
{{
    "AppID"         "{STEAM_CONFIG['app_build']['appid']}"
    "Desc"          "{STEAM_CONFIG['app_build']['desc']}"
    
    "ContentRoot"   "{STEAM_CONFIG['app_build']['contentroot']}"
    "BuildOutput"   "{STEAM_CONFIG['app_build']['buildoutput']}"
    
    "Depots"
    {{
        "{STEAM_CONFIG['depots']['windows']['depot_id']}" "depot_build_windows.vdf"
        "{STEAM_CONFIG['depots']['linux']['depot_id']}"  "depot_build_linux.vdf"
        "{STEAM_CONFIG['depots']['macos']['depot_id']}"  "depot_build_macos.vdf"
    }}
}}
'''
        
        with open(steam_dir / "app_build.vdf", 'w') as f:
            f.write(app_build_vdf)
        
        # Depot configurations for each platform
        for platform, depot_config in STEAM_CONFIG['depots'].items():
            depot_vdf = f'''
"DepotBuild"
{{
    "DepotID" "{depot_config['depot_id']}"
    
    "FileMapping"
    {{
        "LocalPath"     "{depot_config['file_mapping']['LocalPath']}"
        "DepotPath"     "{depot_config['file_mapping']['DepotPath']}"
        "Recursive"     "{depot_config['file_mapping']['recursive']}"
    }}
}}
'''
            
            with open(steam_dir / f"depot_build_{platform}.vdf", 'w') as f:
                f.write(depot_vdf)
        
        print(f"  ✅ Steam configuration files created")
    
    def _create_documentation(self, target: BuildTarget, target_dir: Path):
        """Create target-specific documentation"""
        print("📚 Creating documentation...")
        
        metadata = self.config.metadata
        
        # Create comprehensive README
        readme_content = f"""# {metadata.name}

{metadata.description}

## Quick Start

### Windows Users
1. **Double-click `LAUNCH_GAME.bat`**
2. The game will start automatically

### Linux/macOS Users  
1. **Open terminal in this folder**
2. **Run: `./launch_game.sh`**
3. Or run: `python3 launch_game.py`

## Game Information

- **Version**: {metadata.version}
- **Developer**: {metadata.developer}
- **Genre**: {metadata.genre_primary}
- **Python Version Required**: {metadata.python_min_version[0]}.{metadata.python_min_version[1]}+

## Features

{chr(10).join([f'- {feature}' for feature in metadata.tags])}

## System Requirements

### Minimum Requirements
- **OS**: Windows 10, macOS 10.12, or Ubuntu 18.04 LTS
- **Python**: {metadata.python_min_version[0]}.{metadata.python_min_version[1]} or higher
- **Memory**: 50 MB available space
- **Additional**: No additional packages required

### Recommended
- **Python**: 3.9 or higher for best performance
- **Display**: Any resolution (GUI mode adapts automatically)

## Troubleshooting

### "Python not found" Error
1. Install Python from https://python.org
2. During installation, check "Add Python to PATH"
3. Restart your computer
4. Test by opening terminal/command prompt and typing: `python --version`

### Game Won't Start
1. Make sure all files are in the same folder
2. Try running: `python3 launch_game.py`
3. Check that Python 3.7+ is installed

## Support

- **Found a bug?** Please report it on our GitHub repository
- **Need help?** Check the troubleshooting section above
- **Want to contribute?** Pull requests are welcome!

---

**Enjoy your adventure in the caves of Mount Shabuya!** 🗻⚔️

© {metadata.copyright_year} {metadata.developer}. All rights reserved.
"""
        
        with open(target_dir / "README.md", 'w') as f:
            f.write(readme_content)
        
        # Create LICENSE file
        license_content = f"""MIT License

Copyright (c) {metadata.copyright_year} {metadata.developer}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
        
        with open(target_dir / "LICENSE.txt", 'w') as f:
            f.write(license_content)
        
        print(f"  ✅ Documentation created")
    
    def _create_zip_package(self, target: BuildTarget, target_dir: Path) -> Path:
        """Create ZIP package for distribution"""
        print("📦 Creating ZIP package...")
        
        output_name = target.get_output_name(
            self.config.metadata.short_name,
            self.config.metadata.version
        )
        zip_path = self.build_output / f"{output_name}.zip"
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
            for file_path in target_dir.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(target_dir)
                    zipf.write(file_path, arcname)
        
        # Calculate size
        size_mb = zip_path.stat().st_size / (1024 * 1024)
        print(f"  ✅ ZIP created: {zip_path.name} ({size_mb:.1f} MB)")
        
        return zip_path
    
    def _create_desktop_launcher(self, target_dir: Path, metadata):
        """Create desktop launcher files (.desktop for Linux)"""
        if os.name == 'posix':  # Linux/Unix
            desktop_file = target_dir / f"{metadata.name}.desktop"
            with open(desktop_file, 'w') as f:
                f.write(f"""[Desktop Entry]
Type=Application
Name={metadata.name}
Comment={metadata.description}
Exec={target_dir}/start_game.sh
Icon={target_dir}/game_icon.png
Terminal=false
Categories=Game;
""")
            # Make executable
            os.chmod(desktop_file, 0o755)
            print(f"  ✅ Created desktop launcher: {desktop_file.name}")
    
    def _create_gui_launcher(self, target_dir: Path, metadata):
        """Create GUI launcher wrapper"""
        gui_launcher = target_dir / "start_gui.py"
        with open(gui_launcher, 'w') as f:
            f.write(f'''#!/usr/bin/env python3
"""
GUI Launcher for {metadata.name}
Auto-detects and launches the best available interface
"""
import sys
import os
from pathlib import Path

def main():
    """Launch the best available GUI"""
    # Add current directory to path
    sys.path.insert(0, str(Path(__file__).parent))
    
    try:
        # Try enhanced GUI first
        from enhanced_gui_system import main as enhanced_main
        print("🚀 Starting Enhanced GUI...")
        enhanced_main()
    except ImportError:
        try:
            # Fall back to basic GUI
            from gui import main as basic_main
            print("🎮 Starting Basic GUI...")
            basic_main()
        except ImportError:
            try:
                # Fall back to text mode
                from main import main as text_main
                print("📝 Starting Text Mode...")
                text_main()
            except ImportError as e:
                print(f"❌ Could not start game: {{e}}")
                input("Press Enter to exit...")
                sys.exit(1)

if __name__ == "__main__":
    main()
''')
        os.chmod(gui_launcher, 0o755)
        print(f"  ✅ Created GUI launcher: {gui_launcher.name}")
    
    def _create_store_assets(self, target: BuildTarget, target_dir: Path):
        """Create store-specific assets and metadata"""
        if target.name == "steam":
            # Steam store assets
            self._create_steam_assets(target, target_dir)
        elif target.name == "itch":
            # Itch.io assets
            self._create_itch_assets(target, target_dir)
        elif "store" in target.name.lower():
            # Generic store assets
            self._create_generic_store_assets(target, target_dir)
    
    def _create_itch_assets(self, target: BuildTarget, target_dir: Path):
        """Create Itch.io specific assets"""
        assets_dir = target_dir / "itch_assets"
        assets_dir.mkdir(exist_ok=True)
        
        # Create itch.io metadata
        itch_metadata = {
            "name": self.config.metadata.name,
            "description": self.config.metadata.description,
            "version": self.config.metadata.version,
            "tags": ["rpg", "adventure", "indie", "text-based", "cave"],
            "pricing": "pay_what_you_want",
            "min_price": 0
        }
        
        with open(assets_dir / "itch_metadata.json", 'w') as f:
            json.dump(itch_metadata, f, indent=2)
        
        print(f"  ✅ Created Itch.io assets in: {assets_dir}")
    
    def _create_generic_store_assets(self, target: BuildTarget, target_dir: Path):
        """Create generic store assets"""
        assets_dir = target_dir / "store_assets"
        assets_dir.mkdir(exist_ok=True)
        
        # Create generic store metadata
        store_metadata = {
            "name": self.config.metadata.name,
            "description": self.config.metadata.description,
            "version": self.config.metadata.version,
            "screenshots": [],
            "features": [
                "Single-player RPG experience",
                "Multiple character classes",
                "Cave exploration adventure", 
                "Cross-platform compatibility"
            ]
        }
        
        with open(assets_dir / "store_metadata.json", 'w') as f:
            json.dump(store_metadata, f, indent=2)
        
        print(f"  ✅ Created generic store assets in: {assets_dir}")
    
    def _create_installer(self, target: BuildTarget, target_dir: Path):
        """Create platform-specific installer"""
        if os.name == 'nt':  # Windows
            self._create_windows_installer(target, target_dir)
        elif os.name == 'posix':  # Linux/macOS
            self._create_unix_installer(target, target_dir)
    
    def _create_windows_installer(self, target: BuildTarget, target_dir: Path):
        """Create Windows installer script"""
        installer_script = target_dir / "install.bat"
        with open(installer_script, 'w') as f:
            f.write(f'''@echo off
echo Installing {self.config.metadata.name}...
echo.

REM Create desktop shortcut if requested
set /p create_shortcut="Create desktop shortcut? (y/n): "
if /i "%create_shortcut%"=="y" (
    echo Creating desktop shortcut...
    copy "{self.config.metadata.name}.lnk" "%USERPROFILE%\\Desktop\\" 2>nul
)

REM Create start menu entry
mkdir "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\{self.config.metadata.name}" 2>nul
copy "start_game.bat" "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\{self.config.metadata.name}\\" 2>nul

echo.
echo Installation complete!
echo You can now run the game from the Start Menu or desktop shortcut.
pause
''')
        print(f"  ✅ Created Windows installer: {installer_script.name}")
    
    def _create_unix_installer(self, target: BuildTarget, target_dir: Path):
        """Create Unix installer script"""
        installer_script = target_dir / "install.sh"
        with open(installer_script, 'w') as f:
            f.write(f'''#!/bin/bash
echo "Installing {self.config.metadata.name}..."
echo

# Make scripts executable
chmod +x start_game.sh
chmod +x start_gui.py

# Offer to create desktop entry
read -p "Create desktop entry? (y/n): " create_desktop
if [[ "$create_desktop" =~ ^[Yy]$ ]]; then
    mkdir -p ~/.local/share/applications
    cp {self.config.metadata.name}.desktop ~/.local/share/applications/ 2>/dev/null || true
    echo "Desktop entry created"
fi

# Offer to add to PATH
read -p "Add to PATH? (y/n): " add_path  
if [[ "$add_path" =~ ^[Yy]$ ]]; then
    echo "export PATH=\\"\\$PATH:$(pwd)\\"" >> ~/.bashrc
    echo "Added to PATH (restart terminal or run 'source ~/.bashrc')"
fi

echo
echo "Installation complete!"
echo "Run './start_game.sh' to play"
''')
        os.chmod(installer_script, 0o755)
        print(f"  ✅ Created Unix installer: {installer_script.name}")
    
    def build_all_targets(self):
        """Build all configured targets"""
        print("🏭 Building all distribution targets...")
        
        results = {}
        for target_name in self.config.list_targets():
            try:
                result = self.build_target(target_name, clean=False)
                results[target_name] = result
                print(f"✅ {target_name}: {result}")
            except Exception as e:
                print(f"❌ {target_name}: {e}")
                results[target_name] = None
        
        return results

def main():
    """Build system CLI"""
    import argparse
    
    parser = argparse.ArgumentParser(description="SHABUYA Universal Build System")
    parser.add_argument("target", nargs="?", help="Build target (or 'all' for all targets)")
    parser.add_argument("--list", action="store_true", help="List available targets")
    parser.add_argument("--clean", action="store_true", help="Clean before building")
    
    args = parser.parse_args()
    
    builder = UniversalBuilder()
    
    if args.list:
        print("Available build targets:")
        for target_name in builder.config.list_targets():
            target = builder.config.get_target(target_name)
            print(f"  • {target_name}: {target.description}")
        return
    
    if not args.target:
        print("Usage: python build_engine.py <target> [options]")
        print("Use --list to see available targets")
        return
    
    if args.target == "all":
        builder.build_all_targets()
    else:
        builder.build_target(args.target, clean=args.clean)

if __name__ == "__main__":
    main()
