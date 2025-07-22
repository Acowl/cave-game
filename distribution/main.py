#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Main Entry Point
Launch point for the complete cave adventure game
"""

import sys
import os
from pathlib import Path

def main():
    """Main entry point for SHABUYA Cave Adventure"""
    
    print("🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻")
    print("🗻                                           🗻")
    print("🗻        SHABUYA - CAVE ADVENTURE          🗻")
    print("🗻              Loading Game...             🗻")
    print("🗻                                           🗻")
    print("🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻")
    print()
    
    # Check command line arguments
    force_text = '--text' in sys.argv or '--debug' in sys.argv
    debug_mode = '--debug' in sys.argv
    
    if debug_mode:
        print("🐛 DEBUG MODE ENABLED")
        print(f"📁 Current directory: {os.getcwd()}")
        print(f"📄 Available files: {list(Path('.').glob('*.py'))}")
        print()
    
    # Try to import and start the game
    try:
        # First, try to import the main game module
        if Path('game_refactored.py').exists():
            if debug_mode:
                print("✅ Found game_refactored.py - importing...")
            
            import game_refactored
            
            # Start the game properly
            if hasattr(game_refactored, 'main'):
                if debug_mode:
                    print("🎮 Starting game via game_refactored.main()...")
                game_refactored.main()
            elif hasattr(game_refactored, 'Game'):
                if debug_mode:
                    print("🎮 Starting game via Game class...")
                game = game_refactored.Game()
                game.start()
            else:
                print("❌ Error: Could not find main() function or Game class in game_refactored.py")
                print("Available functions:", dir(game_refactored))
                
        else:
            print("❌ Error: game_refactored.py not found!")
            print("Available files:", list(Path('.').glob('*.py')))
            return
            
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Make sure all game files are in the same directory.")
        return
    except Exception as e:
        print(f"❌ Game Error: {e}")
        if debug_mode:
            import traceback
            traceback.print_exc()
        return

if __name__ == "__main__":
    main()
