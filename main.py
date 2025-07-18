#!/usr/bin/env python3
"""
Cave Game Launcher
Run this file to start the Cave Game.
"""

if __name__ == "__main__":
    try:
        from game_refactored import main
        main()
    except ImportError as e:
        print(f"Error importing game modules: {e}")
        print("Please ensure all game files are in the same directory.")
    except KeyboardInterrupt:
        print("\nGame interrupted by user. Thanks for playing!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please report this issue if it persists.")
