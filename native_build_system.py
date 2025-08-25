#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - PyInstaller Native Build System
Creates native executables for Steam distribution
"""

import os
import shutil
import subprocess
import platform
from pathlib import Path
from typing import Optional
from typing import Dict, List

class NativeBuildSystem:
    """Build native executables using PyInstaller"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path(__file__).parent
        self.build_dir = self.project_root / "build_native"
        self.dist_dir = self.project_root / "dist_native"
        
    def create_pyinstaller_spec(self, platform_name: str) -> Path:
        """Create PyInstaller spec file for the target platform"""
        
        spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

# SHABUYA Cave Adventure - {platform_name} Build Spec

block_cipher = None

# Data files to include
datas = [
    ('src/', 'src/'),
    ('steam_integration/', 'steam_integration/'),
    ('game_assets/', 'game_assets/'),
    ('README.md', '.'),
    ('LICENSE.txt', '.')
]

# Hidden imports needed by the game
hiddenimports = [
    'tkinter',
    'tkinter.ttk',
    'tkinter.messagebox',
    'tkinter.scrolledtext',
    'PIL',
    'PIL.Image',
    'PIL.ImageTk'
]

a = Analysis(
    ['src/core/game_engine.py'],
    pathex=['{str(self.project_root)}'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'scipy', 'pandas'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SHABUYA',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to False for GUI app
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='game_assets/icons/shabuya.ico'  # Game icon
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SHABUYA'
)

# macOS App Bundle
{"" if platform_name != "macOS" else """
app = BUNDLE(
    coll,
    name='SHABUYA.app',
    icon='game_assets/icons/shabuya.icns',
    bundle_identifier='com.shabuyagames.caveadventure',
    version='1.0.0',
    info_plist={{
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleDisplayName': 'SHABUYA Cave Adventure',
        'CFBundleExecutable': 'SHABUYA',
        'CFBundleName': 'SHABUYA Cave Adventure',
        'NSHighResolutionCapable': True,
        'NSRequiresAquaSystemAppearance': False
    }}
)
"""}
'''
        
        spec_path = self.project_root / f"shabuya_{platform_name.lower()}.spec"
        with open(spec_path, 'w') as f:
            f.write(spec_content)
        
        return spec_path
    
    def build_platform(self, platform_name: str) -> bool:
        """Build native executable for specific platform"""
        
        print(f"🏗️ Building native executable for {platform_name}...")
        
        # Create spec file
        spec_path = self.create_pyinstaller_spec(platform_name)
        
        try:
            # Run PyInstaller
            cmd = [
                "pyinstaller",
                "--clean",
                "--noconfirm", 
                str(spec_path)
            ]
            
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"  ✅ Build completed for {platform_name}")
            
            # Move to organized directory structure
            self._organize_build_output(platform_name)
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Build failed for {platform_name}: {e}")
            print(f"     Output: {e.output}")
            return False
        except FileNotFoundError:
            print(f"  ❌ PyInstaller not found. Install with: pip install pyinstaller")
            return False
    
    def _organize_build_output(self, platform_name: str):
        """Organize build output into Steam-compatible structure"""
        
        source_dir = self.project_root / "dist" / "SHABUYA"
        target_dir = self.dist_dir / platform_name
        
        if target_dir.exists():
            shutil.rmtree(target_dir)
        
        target_dir.mkdir(parents=True, exist_ok=True)
        
        if source_dir.exists():
            # Copy built application
            if platform_name == "macOS" and (source_dir.parent / "SHABUYA.app").exists():
                shutil.copytree(source_dir.parent / "SHABUYA.app", target_dir / "SHABUYA.app")
            else:
                shutil.copytree(source_dir, target_dir / "SHABUYA")
            
            # Add platform-specific files
            self._add_platform_files(target_dir, platform_name)
    
    def _add_platform_files(self, target_dir: Path, platform_name: str):
        """Add platform-specific files and launchers"""
        
        if platform_name == "Windows":
            # Windows-specific files
            launcher_bat = target_dir / "LAUNCH_SHABUYA.bat"
            with open(launcher_bat, 'w') as f:
                f.write('''@echo off
title SHABUYA Cave Adventure
cd /d "%~dp0"
SHABUYA\\SHABUYA.exe
pause
''')
        
        elif platform_name == "Linux":
            # Linux launcher script
            launcher_sh = target_dir / "launch_shabuya.sh"
            with open(launcher_sh, 'w') as f:
                f.write('''#!/bin/bash
cd "$(dirname "$0")"
./SHABUYA/SHABUYA
''')
            os.chmod(launcher_sh, 0o755)
        
        # Steam integration files (all platforms)
        steam_dir = target_dir / "steam_config"
        steam_dir.mkdir(exist_ok=True)
        
        # Copy Steam VDF files
        steam_source = self.project_root / "steam_integration"
        if steam_source.exists():
            for vdf_file in steam_source.glob("*.vdf"):
                shutil.copy2(vdf_file, steam_dir)
    
    def build_all_platforms(self) -> Dict[str, bool]:
        """Build for all supported platforms"""
        
        # Determine available platforms
        current_platform = platform.system()
        
        platforms = {
            "Windows": current_platform == "Windows",
            "Linux": current_platform == "Linux", 
            "macOS": current_platform == "Darwin"
        }
        
        results = {}
        
        for platform_name, can_build in platforms.items():
            if can_build:
                results[platform_name] = self.build_platform(platform_name)
            else:
                print(f"⏭️ Skipping {platform_name} (not available on {current_platform})")
                results[platform_name] = False
        
        return results
    
    def create_steam_ready_build(self) -> Path:
        """Create Steam-ready build directory"""
        
        steam_build_dir = self.project_root / "steam_build"
        if steam_build_dir.exists():
            shutil.rmtree(steam_build_dir)
        
        steam_build_dir.mkdir()
        
        # Copy platform builds
        for platform_dir in self.dist_dir.iterdir():
            if platform_dir.is_dir():
                dest_platform = steam_build_dir / platform_dir.name
                shutil.copytree(platform_dir, dest_platform)
        
        # Create Steam depot structure
        self._create_steam_depots(steam_build_dir)
        
        return steam_build_dir
    
    def _create_steam_depots(self, steam_build_dir: Path):
        """Create Steam depot directory structure"""
        
        depots = {
            "windows_content": "Windows",
            "linux_content": "Linux", 
            "macos_content": "macOS"
        }
        
        for depot_name, platform_name in depots.items():
            depot_dir = steam_build_dir / depot_name
            platform_dir = steam_build_dir / platform_name
            
            if platform_dir.exists():
                # Create depot with platform content
                depot_dir.mkdir(exist_ok=True)
                
                # Copy platform build to depot
                for item in platform_dir.iterdir():
                    if item.is_dir():
                        shutil.copytree(item, depot_dir / item.name)
                    else:
                        shutil.copy2(item, depot_dir)

def main():
    """Build system CLI"""
    import argparse
    
    parser = argparse.ArgumentParser(description="SHABUYA Native Build System")
    parser.add_argument("--platform", choices=["Windows", "Linux", "macOS"], 
                       help="Specific platform to build")
    parser.add_argument("--all", action="store_true", help="Build all available platforms")
    parser.add_argument("--steam", action="store_true", help="Create Steam-ready build")
    
    args = parser.parse_args()
    
    builder = NativeBuildSystem()
    
    if args.platform:
        success = builder.build_platform(args.platform)
        if success:
            print(f"✅ {args.platform} build completed successfully!")
        else:
            print(f"❌ {args.platform} build failed!")
    
    elif args.all:
        results = builder.build_all_platforms()
        successful = sum(results.values())
        total = len(results)
        print(f"\n🏆 Build Summary: {successful}/{total} platforms built successfully")
        
        if args.steam or successful > 0:
            steam_dir = builder.create_steam_ready_build()
            print(f"🎮 Steam build ready: {steam_dir}")
    
    else:
        print("Usage: python native_build_system.py --all [--steam]")
        print("       python native_build_system.py --platform Windows")

if __name__ == "__main__":
    main()
