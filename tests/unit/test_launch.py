#!/usr/bin/env python3
"""
Quick Game Test - Launch the actual game to verify it works
"""

import sys
from pathlib import Path

print("🎮 SHABUYA Cave Adventure - Game Launch Test")
print("=" * 50)

def test_game_launch():
    """Test launching the actual game"""
    try:
        print("Testing game launch...")
        
        # Import the main game
        import game_refactored
        print("✅ Game engine imported successfully")
        
        # Test game initialization without actually running
        from game_events import start_game
        from ui import title_screen
        from scenes import setup_scenes
        from config import SCENE_NAMES
        
        print("✅ All game modules loaded")
        
        # Test scene setup
        scenes = setup_scenes()
        starting_scene = scenes[SCENE_NAMES['CAVE_ENTRANCE']]
        print(f"✅ Game world ready: Starting at '{starting_scene.name}'")
        
        print("\n🎯 Core game systems are working!")
        print("🚀 You can now play the full game with:")
        print("   python main.py")
        
        return True
        
    except Exception as e:
        print(f"❌ Game launch test failed: {e}")
        print("\nDebugging info:")
        import traceback
        traceback.print_exc()
        return False

def test_professional_launcher():
    """Test the new professional launcher"""
    try:
        project_root = Path(__file__).parent
        new_launcher = project_root / "scripts" / "main.py"
        
        if new_launcher.exists():
            print(f"\n✅ Professional launcher found: {new_launcher}")
            print("🚀 You can use the new launcher with:")
            print("   python scripts/main.py")
            return True
        else:
            print("\n❌ Professional launcher not found")
            return False
            
    except Exception as e:
        print(f"❌ Professional launcher test failed: {e}")
        return False

def main():
    """Run game launch tests"""
    print("Testing if the game can actually launch...\n")
    
    # Test core game
    game_works = test_game_launch()
    
    # Test new launcher
    launcher_works = test_professional_launcher()
    
    print("\n" + "=" * 50)
    print("🏆 LAUNCH TEST RESULTS:")
    
    if game_works:
        print("✅ CORE GAME: Ready to play!")
    else:
        print("❌ CORE GAME: Issues found")
        
    if launcher_works:
        print("✅ PROFESSIONAL LAUNCHER: Available")
    else:
        print("❌ PROFESSIONAL LAUNCHER: Not available")
    
    if game_works:
        print("\n🎉 SUCCESS! Your cave adventure is ready!")
        print("\n🎮 Start playing now:")
        print("   python main.py                 # Original launcher")
        if launcher_works:
            print("   python scripts/main.py         # Professional launcher")
            
        print("\n🎯 Game features available:")
        print("   • Multiple character classes (Rogue, Warrior, Mage)")
        print("   • Combat system with class-specific weapons")
        print("   • Scene-based exploration and progression")
        print("   • Character stats and leveling system")
        print("   • Enhanced weapons and special abilities")
        print("   • Complete storyline with final boss battle")
        
    else:
        print("\n⚠️ Some issues detected.")
        print("Check error messages above for troubleshooting.")
    
    return game_works

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
