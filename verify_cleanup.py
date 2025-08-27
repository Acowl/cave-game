#!/usr/bin/env python3
"""
Verify project structure after cleanup.
"""
import os, sys
from pathlib import Path

EXPECTED_DIRS = [
    "src",
    "src/core",
    "src/interfaces",
    "tests",
    "scripts",
    "tools",
    "docs"
]

EXPECTED_FILES = {
    "src/core": ["game_refactored.py","scenes.py","game_events.py","player.py","item.py","config.py","ui.py"],
    "src/interfaces": ["gui.py"],
    "scripts": ["start_game.py","launcher.py"],
    ".": ["README.md"]
}

def add_src_to_path():
    p = Path("src")
    if p.exists():
        sys.path.insert(0, str(p))

def check_dirs():
    print("\n[Dirs]")
    for d in EXPECTED_DIRS:
        print(("✅" if Path(d).exists() else "❌"), d)

def check_files():
    print("\n[Files]")
    for base, names in EXPECTED_FILES.items():
        for n in names:
            p = Path(base) / n
            ok = p.exists()
            print(("✅" if ok else "❌"), str(p))

def test_imports():
    print("\n[Imports]")
    add_src_to_path()
    modules = ["core.game_refactored","core.scenes","core.game_events","core.player","core.item","core.config","core.ui"]
    for m in modules:
        try:
            __import__(f"{m}")
            print("✅", m)
        except Exception as e:
            print("❌", m, "-", e.__class__.__name__, e)

def main():
    print("=== VERIFY CLEANUP ===")
    check_dirs()
    check_files()
    test_imports()
    print("\nDone.")

if __name__ == "__main__":
    main()