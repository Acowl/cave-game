#!/usr/bin/env python3
"""
Diagnostic script for GUI issues
Run this in your game directory to check what's wrong
"""

import sys
import os
import traceback

def test_imports():
    """Test if all game modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import tkinter
        print("✅ tkinter - GUI framework available")
    except ImportError:
        print("❌ tkinter - GUI framework MISSING")
        return False
    
    try:
        from game_refactored import play_game
        print("✅ game_refactored - Main game engine")
    except ImportError as e:
        print(f"❌ game_refactored - FAILED: {e}")
    
    try:
        from game_events import start_game
        print("✅ game_events - Game initialization")  
    except ImportError as e:
        print(f"❌ game_events - FAILED: {e}")
        
    try:
        from scenes import setup_scenes
        print("✅ scenes - Game world")
    except ImportError as e:
        print(f"❌ scenes - FAILED: {e}")
        
    return True

def test_gui_class():
    """Test if the GUI class works"""
    print("\n🎮 Testing GUI class...")
    
    try:
        from gui import CaveGameGUI
        print("✅ CaveGameGUI class imported")
        
        # Test creating instance (without running mainloop)
        app = CaveGameGUI()
        print("✅ GUI instance created")
        
        # Check initial state
        print(f"📊 Initial game_state: {app.game_state}")
        
        # Test command processing without GUI
        print("\n🧪 Testing command processing...")
        
        # Simulate the new_game setup
        app.game_state = "menu"
        
        # Test menu command
        response = app.handle_game_command("1")
        print(f"✅ Command '1' response: {response[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ GUI test failed: {e}")
        traceback.print_exc()
        return False

def main():
    print("🗻 SHABUYA GUI Diagnostic Tool 🗻")
    print("=" * 50)
    
    print(f"📁 Current directory: {os.getcwd()}")
    print(f"🐍 Python version: {sys.version}")
    
    # Check if we're in the right directory
    if not os.path.exists("gui.py"):
        print("❌ gui.py not found! Make sure you're in the game directory.")
        return
    
    if not os.path.exists("main.py"):
        print("❌ main.py not found! Make sure you're in the game directory.")
        return
        
    print("✅ Game files found")
    
    # Test imports
    if not test_imports():
        print("\n❌ Critical imports failed!")
        return
        
    # Test GUI
    if test_gui_class():
        print("\n✅ GUI integration appears to be working!")
        print("\n🎯 Try this:")
        print("1. Open the GUI launcher")
        print("2. Look for the welcome message in the main text area")
        print("3. Type '1' in the command box at the bottom")
        print("4. Press Enter")
        print("5. You should see class selection options")
    else:
        print("\n❌ GUI has issues - try text mode instead:")
        print("   python main.py --text")

if __name__ == "__main__":
    main()
