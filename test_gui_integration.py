#!/usr/bin/env python3
"""
Quick GUI test to verify game integration
"""

try:
    print("Testing GUI imports...")
    
    # Test imports
    from distribution.gui import CaveGameGUI
    print("✅ GUI class imported successfully")
    
    from distribution.game_refactored import play_game
    print("✅ Game engine imported successfully")
    
    from distribution.game_events import start_game  
    print("✅ Game events imported successfully")
    
    print("\n🎮 GUI should work! Try these steps:")
    print("1. Open the GUI")
    print("2. Type 'start' in the command box")
    print("3. Press Enter")
    print("4. Or click the '🎯 New Game' button")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("The GUI might not have the game integration.")
    
except Exception as e:
    print(f"❌ Other error: {e}")
