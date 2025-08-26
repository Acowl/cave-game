#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Headless Graphics Test
Test graphics integration without GUI display
"""

import sys
import os
import json
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_assets_exist():
    """Test if all graphics assets exist"""
    print("Testing asset existence...")
    
    assets_dir = Path("game_assets")
    
    if not assets_dir.exists():
        return False, "game_assets directory missing"
    
    # Check manifest
    manifest_path = assets_dir / "asset_manifest.json"
    if not manifest_path.exists():
        return False, "Asset manifest missing"
    
    # Load and check manifest
    try:
        with open(manifest_path) as f:
            manifest = json.load(f)
        
        # Check sprites
        sprites_dir = assets_dir / "sprites"
        sprites_data = manifest.get("sprites", {})
        if isinstance(sprites_data, dict):
            for filename in sprites_data.keys():
                sprite_path = sprites_dir / filename
                if not sprite_path.exists():
                    return False, f"Missing sprite: {sprite_path}"
        
        # Check backgrounds
        backgrounds_dir = assets_dir / "backgrounds"
        backgrounds_data = manifest.get("backgrounds", {})
        if isinstance(backgrounds_data, dict):
            for filename in backgrounds_data.keys():
                bg_path = backgrounds_dir / filename
                if not bg_path.exists():
                    return False, f"Missing background: {bg_path}"
        
        # Check icons
        icons_dir = assets_dir / "icons"
        icon_files = ["shabuya_icon.png", "shabuya_icon.ico"]
        for icon_file in icon_files:
            icon_path = icons_dir / icon_file
            if not icon_path.exists():
                return False, f"Missing icon: {icon_path}"
        
        sprite_count = len(manifest.get("sprites", {}))
        bg_count = len(manifest.get("backgrounds", {}))
        
        return True, f"All assets exist: {sprite_count} sprites, {bg_count} backgrounds, 2 icons"
        
    except Exception as e:
        return False, f"Manifest read error: {e}"

def test_pil_loading():
    """Test if PIL can load the created assets"""
    print("Testing PIL asset loading...")
    
    try:
        from PIL import Image
    except ImportError:
        return False, "PIL not available"
    
    assets_dir = Path("game_assets")
    loaded_count = 0
    errors = []
    
    # Test sprites
    sprites_dir = assets_dir / "sprites"
    if sprites_dir.exists():
        for sprite_file in sprites_dir.glob("*.png"):
            try:
                with Image.open(sprite_file) as img:
                    # Verify it's a valid image
                    width, height = img.size
                    if width > 0 and height > 0:
                        loaded_count += 1
                    else:
                        errors.append(f"Invalid sprite dimensions: {sprite_file}")
            except Exception as e:
                errors.append(f"Could not load sprite {sprite_file}: {e}")
    
    # Test backgrounds
    backgrounds_dir = assets_dir / "backgrounds"
    if backgrounds_dir.exists():
        for bg_file in backgrounds_dir.glob("*.png"):
            try:
                with Image.open(bg_file) as img:
                    # Verify it's a valid image
                    width, height = img.size
                    if width > 0 and height > 0:
                        loaded_count += 1
                    else:
                        errors.append(f"Invalid background dimensions: {bg_file}")
            except Exception as e:
                errors.append(f"Could not load background {bg_file}: {e}")
    
    # Test icon
    icons_dir = assets_dir / "icons"
    icon_path = icons_dir / "shabuya_icon.png"
    if icon_path.exists():
        try:
            with Image.open(icon_path) as img:
                width, height = img.size
                if width > 0 and height > 0:
                    loaded_count += 1
                else:
                    errors.append(f"Invalid icon dimensions: {icon_path}")
        except Exception as e:
            errors.append(f"Could not load icon: {e}")
    
    if errors:
        return False, f"PIL loading errors: {'; '.join(errors)}"
    
    return True, f"PIL loaded {loaded_count} assets successfully"

def test_enhanced_gui_class():
    """Test if EnhancedGameGUI class can be imported and has graphics methods"""
    print("Testing Enhanced GUI class...")
    
    try:
        from enhanced_gui_system import EnhancedGameGUI
        
        # Check if class has required graphics methods
        required_methods = [
            'setup_graphics',
            'load_character_sprites',
            'load_background_images',
            'update_character_sprite',
            'update_scene_background',
            'add_background_display'
        ]
        
        missing_methods = []
        for method in required_methods:
            if not hasattr(EnhancedGameGUI, method):
                missing_methods.append(method)
        
        if missing_methods:
            return False, f"Missing methods: {', '.join(missing_methods)}"
        
        return True, f"Enhanced GUI class ready with {len(required_methods)} graphics methods"
        
    except ImportError as e:
        return False, f"Import error: {e}"
    except Exception as e:
        return False, f"Unexpected error: {e}"

def test_asset_specifications():
    """Test if assets meet the required specifications"""
    print("Testing asset specifications...")
    
    try:
        from PIL import Image
        
        assets_dir = Path("game_assets")
        spec_violations = []
        
        # Test sprite specifications (should be 64x64)
        sprites_dir = assets_dir / "sprites"
        if sprites_dir.exists():
            for sprite_file in sprites_dir.glob("*_sprite.png"):
                with Image.open(sprite_file) as img:
                    width, height = img.size
                    if width != 64 or height != 64:
                        spec_violations.append(f"Sprite {sprite_file.name} is {width}x{height}, should be 64x64")
        
        # Test background specifications (should be 400x300)
        backgrounds_dir = assets_dir / "backgrounds"
        if backgrounds_dir.exists():
            for bg_file in backgrounds_dir.glob("*.png"):
                with Image.open(bg_file) as img:
                    width, height = img.size
                    if width != 400 or height != 300:
                        spec_violations.append(f"Background {bg_file.name} is {width}x{height}, should be 400x300")
        
        if spec_violations:
            return False, f"Specification violations: {'; '.join(spec_violations)}"
        
        return True, "All assets meet specifications (sprites: 64x64, backgrounds: 400x300)"
        
    except Exception as e:
        return False, f"Specification test error: {e}"

def main():
    """Run headless graphics integration test"""
    print("=" * 70)
    print("SHABUYA CAVE ADVENTURE - HEADLESS GRAPHICS INTEGRATION TEST")
    print("=" * 70)
    
    tests = [
        ("Asset Existence Check", test_assets_exist),
        ("PIL Asset Loading", test_pil_loading),
        ("Enhanced GUI Class", test_enhanced_gui_class),
        ("Asset Specifications", test_asset_specifications),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 50)
        
        try:
            success, message = test_func()
            results.append((test_name, success, message))
            
            if success:
                print(f"✅ PASS: {message}")
            else:
                print(f"❌ FAIL: {message}")
                
        except Exception as e:
            results.append((test_name, False, f"Test crashed: {e}"))
            print(f"💥 CRASH: {e}")
    
    print("\n" + "=" * 70)
    print("HEADLESS TEST SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for _, success, _ in results if success)
    total = len(results)
    
    for test_name, success, message in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} | {test_name}")
    
    print(f"\nResult: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL HEADLESS TESTS PASSED!")
        print("Graphics integration is ready for GUI testing.")
        print("\nNext steps:")
        print("1. Run in environment with display: python enhanced_gui_system.py")
        print("2. Test interactive features manually")
        print("3. Integrate with main game loop")
    else:
        print(f"\n⚠️  {total - passed} tests failed. Fix issues before proceeding.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
