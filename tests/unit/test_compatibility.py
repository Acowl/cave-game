#!/usr/bin/env python3
"""
Simple Test - Verify Basic Game Functionality
Test the core game without complex imports
"""

import sys
from pathlib import Path

print("🧪 SHABUYA Cave Adventure - Basic Test")
print("=" * 40)

def test_original_files():
    """Test if original files work"""
    try:
        # Test basic imports from root
        import config
        import ui
        import combat
        import scenes
        import item
        import player
        import game_events
        
        print("✅ All original modules imported successfully")
        
        # Test basic functionality
        from config import SCENE_NAMES, STAT_REQUIREMENT
        from item import dagger, axe, wand
        from player import Player
        
        print(f"✅ Scene names loaded: {len(SCENE_NAMES)} scenes")
        print(f"✅ Stat requirement: {STAT_REQUIREMENT}")
        print(f"✅ Weapons available: {dagger.name}, {axe.name}, {wand.name}")
        
        # Test player creation
        test_player = Player()
        print(f"✅ Player created with {test_player.health} health")
        
        # Test scenes
        from scenes import setup_scenes
        game_scenes = setup_scenes()
        print(f"✅ Game world created with {len(game_scenes)} scenes")
        
        return True
        
    except Exception as e:
        print(f"❌ Original files test failed: {e}")
        return False

def test_new_structure():
    """Test new structure files"""
    try:
        # Add src to path
        project_root = Path(__file__).parent
        src_path = project_root / 'src'
        sys.path.insert(0, str(src_path))
        
        # Test new structure
        from src.config import SCENE_NAMES as NEW_SCENES
        print(f"✅ New config loaded: {len(NEW_SCENES)} scenes")
        
        from src.entities.player import Player as NewPlayer
        from src.entities.item import dagger as new_dagger
        
        new_player = NewPlayer()
        print(f"✅ New player class: {new_player.health} health, {new_player.level} level")
        print(f"✅ New item system: {new_dagger.name}")
        
        return True
        
    except Exception as e:
        print(f"❌ New structure test failed: {e}")
        return False

def test_launchers():
    """Test if launcher files exist and are accessible"""
    project_root = Path(__file__).parent
    
    launchers = [
        ("Original main.py", "main.py"),
        ("New main launcher", "scripts/main.py"), 
        ("GUI launcher", "scripts/launcher.py"),
        ("Windows batch", "scripts/START_GAME.bat" if (project_root / "scripts/START_GAME.bat").exists() else "START_GAME.bat"),
        ("Unix shell", "start_game.sh")
    ]
    
    found = 0
    for name, path in launchers:
        if (project_root / path).exists():
            print(f"✅ {name}: {path}")
            found += 1
        else:
            print(f"❌ {name}: {path} (not found)")
    
    return found >= 2  # At least 2 launchers should exist

def main():
    """Run all tests"""
    print("Running comprehensive compatibility test...\n")
    
    # Test original system
    print("1. Testing Original Files:")
    original_works = test_original_files()
    
    print("\n2. Testing New Structure:")
    new_structure_works = test_new_structure()
    
    print("\n3. Testing Launchers:")
    launchers_work = test_launchers()
    
    print("\n" + "=" * 40)
    print("🏆 TEST RESULTS:")
    
    results = {
        "Original Files": original_works,
        "New Structure": new_structure_works, 
        "Launchers": launchers_work
    }
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} test categories passed")
    
    if passed >= 2:
        print("\n🎉 GREAT! The game is ready to play!")
        print("\n🚀 Try these launch options:")
        if original_works:
            print("   python main.py                 # Original launcher")
        if (Path(__file__).parent / "scripts/main.py").exists():
            print("   python scripts/main.py         # New professional launcher")
        if (Path(__file__).parent / "scripts/launcher.py").exists():
            print("   python scripts/launcher.py     # GUI launcher")
    else:
        print("\n⚠️ Some issues found, but you can likely still play with:")
        print("   python main.py")
    
    return passed >= 2

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
