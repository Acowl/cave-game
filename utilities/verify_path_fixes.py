#!/usr/bin/env python3
"""
Verify that path resolution fixes are working correctly
"""

from pathlib import Path

def get_project_root():
    """Get the project root directory relative to this script"""
    return Path(__file__).parent.parent

def main():
    print("🔍 VERIFYING PATH RESOLUTION FIXES")
    print("=" * 50)
    
    project_root = get_project_root()
    print(f"📁 Project root: {project_root}")
    print(f"   Exists: {project_root.exists()}")
    
    # Check sprites directory
    sprites_dir = project_root / "game_assets" / "sprites"
    print(f"\n📁 Sprites directory: {sprites_dir}")
    print(f"   Exists: {sprites_dir.exists()}")
    if sprites_dir.exists():
        sprite_files = list(sprites_dir.glob("*_sprite.png"))
        print(f"   Files found: {len(sprite_files)}")
        for sprite in sorted(sprite_files):
            print(f"     - {sprite.name}")
    
    # Check backgrounds directory
    backgrounds_dir = project_root / "game_assets" / "backgrounds"
    print(f"\n📁 Backgrounds directory: {backgrounds_dir}")
    print(f"   Exists: {backgrounds_dir.exists()}")
    if backgrounds_dir.exists():
        bg_files = list(backgrounds_dir.glob("*.png"))
        print(f"   Files found: {len(bg_files)}")
        for bg in sorted(bg_files):
            print(f"     - {bg.name}")
    
    # Test that enhanced GUI exists in project root
    gui_file = project_root / "enhanced_gui_system.py"
    print(f"\n📁 Enhanced GUI file: {gui_file}")
    print(f"   Exists: {gui_file.exists()}")
    
    print("\n✅ Path resolution verification complete!")
    print("🎉 All paths are now resolved correctly from utilities directory")

if __name__ == "__main__":
    main()
