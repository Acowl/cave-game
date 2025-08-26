#!/usr/bin/env python3
"""
Check path resolution from utilities directory
"""

import os
from pathlib import Path

def check_paths():
    print("🔍 Path Resolution Check")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Script location: {__file__}")
    print(f"Script directory: {os.path.dirname(__file__)}")
    
    # Test different path approaches
    approaches = [
        ("../game_assets/sprites", Path("../game_assets/sprites")),
        ("Absolute path", Path("/workspaces/cave-game/game_assets/sprites")),  
        ("From script dir", Path(os.path.dirname(__file__)).parent / "game_assets" / "sprites"),
        ("Join approach", Path(os.path.join(os.path.dirname(__file__), "..", "game_assets", "sprites")))
    ]
    
    for name, path in approaches:
        print(f"\n{name}: {path}")
        print(f"  Exists: {path.exists()}")
        if path.exists():
            files = list(path.glob("*.png"))
            print(f"  Files found: {len(files)}")
            for f in files[:3]:  # Show first 3
                print(f"    - {f.name}")

if __name__ == "__main__":
    check_paths()
