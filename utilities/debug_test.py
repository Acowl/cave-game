#!/usr/bin/env python3
"""
Debug test script for SHABUYA Cave Adventure
Tests core functionality and identifies issues
"""

import sys
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent.parent
src_path = project_root / 'src'
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(src_path))

print("🔍 SHABUYA Cave Adventure - Debug Test")
print("=" * 50)

def test_imports():
    """Test all critical imports"""
    print("📦 Testing imports...")
    
    try:
        from src.interfaces.ui import title_screen
        print("  ✅ UI module imported")
        
        from src.core.game_events import start_game
        print("  ✅ Game events module imported")
        
        from src.core.scenes import setup_scenes
        print("  ✅ Scenes module imported")
        
        from src.config import SCENE_NAMES
        print("  ✅ Config module imported")
        
        from src.core.game_engine import main as game_main
        print("  ✅ Game engine imported")
        
        return True
        
    except ImportError as e:
        print(f"  ❌ Import failed: {e}")
        return False

def test_scenes():
    """Test scene setup and basic functionality"""
    print("\n🏗️ Testing scene setup...")
    
    try:
        from src.core.scenes import setup_scenes
        from src.config import SCENE_NAMES
        
        scenes = setup_scenes()
        print(f"  ✅ Created {len(scenes)} scenes")
        
        cave_entrance = scenes[SCENE_NAMES['CAVE_ENTRANCE']]
        print(f"  ✅ Retrieved scene: {cave_entrance.name}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Scene test failed: {e}")
        return False

def test_player_creation():
    """Test player creation and setup"""
    print("\n🧙 Testing player creation...")
    
    try:
        from src.entities.player import Player
        from src.entities.item import Inventory, dagger
        
        player = Player()
        player.inventory = Inventory()
        player.weapon = dagger
        player.character_class = "Rogue"
        
        print(f"  ✅ Player created with {player.character_class} class")
        print(f"  ✅ Weapon: {player.weapon.name}")
        print(f"  ✅ Stats: STR:{player.strength} AGI:{player.agility} INT:{player.intelligence}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Player test failed: {e}")
        return False

def test_launchers():
    """Test launcher availability"""
    print("\n🚀 Testing launchers...")
    
    # Test main launcher
    main_launcher = project_root / "scripts" / "main.py"
    if main_launcher.exists():
        print("  ✅ Main launcher found")
    else:
        print("  ❌ Main launcher missing")
        
    # Test GUI launcher
    gui_launcher = project_root / "scripts" / "launcher.py"
    if gui_launcher.exists():
        print("  ✅ GUI launcher found")
    else:
        print("  ❌ GUI launcher missing")
        
    return main_launcher.exists()

def main():
    """Run all debug tests"""
    print("Starting comprehensive debug test...\n")
    
    results = {
        'imports': test_imports(),
        'scenes': test_scenes(), 
        'player': test_player_creation(),
        'launchers': test_launchers()
    }
    
    print("\n" + "=" * 50)
    print("🏆 DEBUG TEST RESULTS:")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {test_name.capitalize()}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The game should work correctly.")
        print("\n💡 To run the game:")
        print("   python scripts/main.py")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
        print("   The project may need additional setup.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
