#!/usr/bin/env python3
"""
Test script to verify GUI functionality
"""
import sys
import os
from pathlib import Path

def test_gui_import():
    """Test if the GUI can be imported"""
    try:
        import enhanced_gui_final
        print("✅ GUI module imports successfully")
        return True
    except Exception as e:
        print(f"❌ GUI import failed: {e}")
        return False

def test_assets_exist():
    """Test if required assets exist"""
    assets_dir = Path("assets")
    sprites_dir = assets_dir / "sprites"
    backgrounds_dir = assets_dir / "backgrounds"
    
    if not assets_dir.exists():
        print("❌ Assets directory missing")
        return False
    
    if not sprites_dir.exists():
        print("❌ Sprites directory missing")
        return False
    
    if not backgrounds_dir.exists():
        print("❌ Backgrounds directory missing")
        return False
    
    sprites = list(sprites_dir.glob("*.png"))
    backgrounds = list(backgrounds_dir.glob("*.png"))
    
    print(f"✅ Found {len(sprites)} sprites")
    print(f"✅ Found {len(backgrounds)} backgrounds")
    
    return len(sprites) > 0 and len(backgrounds) > 0

def test_pillow():
    """Test if Pillow is available"""
    try:
        from PIL import Image, ImageTk
        print("✅ Pillow (PIL) available")
        return True
    except ImportError:
        print("❌ Pillow not installed. Run: pip install Pillow")
        return False

def test_tkinter():
    """Test if Tkinter is available"""
    try:
        import tkinter as tk
        print("✅ Tkinter available")
        return True
    except ImportError:
        print("❌ Tkinter not available")
        return False

def main():
    print("=== GUI FUNCTIONALITY TEST ===")
    
    tests = [
        ("Tkinter", test_tkinter),
        ("Pillow", test_pillow),
        ("Assets", test_assets_exist),
        ("GUI Import", test_gui_import)
    ]
    
    all_passed = True
    for name, test_func in tests:
        print(f"\n--- Testing {name} ---")
        if not test_func():
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
        print("The GUI should work properly.")
        print("\nTo run the game:")
        print("  python enhanced_gui_final.py")
    else:
        print("⚠️  SOME TESTS FAILED")
        print("Please fix the issues above before running the GUI.")
    
    print("="*50)

if __name__ == "__main__":
    main()
