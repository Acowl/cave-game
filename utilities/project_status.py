#!/usr/bin/env python3
"""
Quick project status overview
"""

from pathlib import Path

def show_clean_structure():
    """Display the cleaned project structure"""
    base_path = Path("/workspaces/cave-game")
    
    print("🎮 SHABUYA Cave Adventure - Clean Project")
    print("=" * 50)
    
    # Core files check
    core_files = [
        "main.py", "game_refactored.py", "enhanced_gui_system.py", 
        "launcher.py", "combat.py", "player.py", "item.py", 
        "scenes.py", "game_events.py", "config.py", "gui.py", "ui.py"
    ]
    
    print("\n🎯 CORE GAME FILES:")
    for file in core_files:
        status = "✅" if (base_path / file).exists() else "❌"
        print(f"  {status} {file}")
    
    # Directory overview
    directories = {
        "🎨 game_assets": "game_assets",
        "🧪 tests": "tests", 
        "🔧 utilities": "utilities",
        "📚 documentation": "documentation",
        "📦 distribution": "distribution",
        "🎮 steam_integration": "steam_integration",
        "📁 archive": "archive"
    }
    
    for label, dir_name in directories.items():
        dir_path = base_path / dir_name
        if dir_path.exists():
            file_count = len(list(dir_path.rglob("*")))
            print(f"  ✅ {label}: {file_count} files")
        else:
            print(f"  ❌ {label}: missing")
    
    # Asset status
    print("\n🎨 ASSET STATUS:")
    sprites_dir = base_path / "game_assets" / "sprites"
    if sprites_dir.exists():
        sprites = list(sprites_dir.glob("*.png"))
        print(f"  Sprites: {len(sprites)} files")
        for sprite in sorted(sprites):
            print(f"    - {sprite.name}")
    
    backgrounds_dir = base_path / "game_assets" / "backgrounds" 
    if backgrounds_dir.exists():
        backgrounds = list(backgrounds_dir.glob("*.png"))
        print(f"  Backgrounds: {len(backgrounds)} files")
        for bg in sorted(backgrounds):
            print(f"    - {bg.name}")
    
    print(f"\n📊 TOTAL PROJECT FILES: {len(list(base_path.rglob('*')))}")
    print("🎉 Project structure cleaned and organized!")

if __name__ == "__main__":
    show_clean_structure()
