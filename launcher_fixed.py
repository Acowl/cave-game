#!/usr/bin/env python3
"""
🗻 SHABUYA - Cave Adventure 🗻
WORKING GAME LAUNCHER

This launcher ensures the game always starts properly.
"""

def main():
    """Simple, reliable game launcher"""
    print("🗻" + "="*60 + "🗻")
    print("🗻" + " "*18 + "SHABUYA - CAVE ADVENTURE" + " "*18 + "🗻")
    print("🗻" + " "*15 + "A Thrilling Text-Based RPG" + " "*16 + "🗻") 
    print("🗻" + "="*60 + "🗻")
    print()
    
    try:
        # Import and run the game
        from game_refactored import main as game_main
        game_main()
    except ImportError as e:
        print(f"❌ Error importing game: {e}")
        print("📁 Please ensure all game files are present")
    except Exception as e:
        print(f"❌ Error running game: {e}")

if __name__ == "__main__":
    main()
