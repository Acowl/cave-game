#!/usr/bin/env python3
"""
Verify project structure after cleanup.
"""
import os, sys
from pathlib import Path

EXPECTED_DIRS = [
    "assets",
    "distribution", 
    "docs",
    "tests",
    "tools",
    "utilities",
    "archive"
]

EXPECTED_FILES = {
    ".": [
        "enhanced_gui_final.py",
        "README.md", 
        "requirements.txt",
        "launch_game.sh",
        "run_player_gui.bat"
    ],
    "assets": [
        "sprites",
        "backgrounds", 
        "icons"
    ],
    "distribution": [
        "main.py",
        "game_refactored.py",
        "combat.py",
        "player.py",
        "item.py",
        "scenes.py",
        "ui.py",
        "config.py",
        "gui.py",
        "launcher.py"
    ],
    "tests": [
        "unit",
        "integration",
        "assets"
    ],
    "tools": [
        "asset_management",
        "build_system", 
        "testing",
        "utilities"
    ]
}

def check_dirs():
    print("\n📁 [Directories]")
    for d in EXPECTED_DIRS:
        exists = Path(d).exists()
        print(("✅" if exists else "❌"), d)
    return all(Path(d).exists() for d in EXPECTED_DIRS)

def check_files():
    print("\n📄 [Files]")
    all_good = True
    for base, names in EXPECTED_FILES.items():
        for name in names:
            p = Path(base) / name
            exists = p.exists()
            print(("✅" if exists else "❌"), str(p))
            if not exists:
                all_good = False
    return all_good

def check_empty_files():
    print("\n🔍 [Empty Files Check]")
    empty_files = []
    for py_file in Path(".").rglob("*.py"):
        if py_file.stat().st_size == 0:
            empty_files.append(str(py_file))
    
    if empty_files:
        print("❌ Found empty files:")
        for f in empty_files:
            print(f"   {f}")
        return False
    else:
        print("✅ No empty files found")
        return True

def check_main_game():
    print("\n🎮 [Main Game Check]")
    main_game = Path("enhanced_gui_final.py")
    if main_game.exists():
        print("✅ Main game file exists")
        try:
            # Try to import the main game
            import enhanced_gui_final
            print("✅ Main game imports successfully")
            return True
        except Exception as e:
            print(f"❌ Main game import failed: {e}")
            return False
    else:
        print("❌ Main game file missing")
        return False

def check_assets():
    print("\n🎨 [Assets Check]")
    assets_dir = Path("assets")
    if not assets_dir.exists():
        print("❌ Assets directory missing")
        return False
    
    sprites = list(assets_dir.glob("sprites/*.png"))
    backgrounds = list(assets_dir.glob("backgrounds/*.png"))
    icons = list(assets_dir.glob("icons/*.png"))
    
    print(f"✅ Sprites: {len(sprites)} files")
    print(f"✅ Backgrounds: {len(backgrounds)} files") 
    print(f"✅ Icons: {len(icons)} files")
    
    return len(sprites) > 0 and len(backgrounds) > 0

def main():
    print("=== VERIFY CLEANUP ===")
    print("Checking cleaned up project structure...")
    
    dirs_ok = check_dirs()
    files_ok = check_files()
    empty_ok = check_empty_files()
    game_ok = check_main_game()
    assets_ok = check_assets()
    
    print("\n" + "="*50)
    print("📊 VERIFICATION SUMMARY")
    print("="*50)
    
    checks = [
        ("Directories", dirs_ok),
        ("Files", files_ok), 
        ("No Empty Files", empty_ok),
        ("Main Game", game_ok),
        ("Assets", assets_ok)
    ]
    
    all_passed = True
    for name, passed in checks:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} {name}")
        if not passed:
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("🎉 ALL CHECKS PASSED - CLEANUP SUCCESSFUL!")
        print("The project structure is clean and ready for development.")
    else:
        print("⚠️  SOME CHECKS FAILED - REVIEW NEEDED")
        print("Please check the failed items above.")
    
    print("="*50)

if __name__ == "__main__":
    main()