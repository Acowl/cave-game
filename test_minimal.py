#!/usr/bin/env python3
"""
Minimal game test to identify the hanging issue
"""

from ui import title_screen, get_user_choice
from game_events import start_game
from scenes import setup_scenes
from config import SCENE_NAMES

def test_minimal_game():
    """Test minimal game flow"""
    print("Testing minimal game flow...")
    
    # Skip title screen for now
    print("Creating player...")
    
    # Mock player creation without input
    from player import Player
    from item import Inventory, dagger
    
    player = Player()
    player.inventory = Inventory()
    player.weapon = dagger
    print("Player created successfully")
    
    print("Setting up scenes...")
    scenes = setup_scenes()
    current_scene = scenes[SCENE_NAMES['CAVE_ENTRANCE']]
    print("Scenes setup complete")
    
    print("Entering first scene...")
    current_scene.enter(None)
    print("First scene entered")
    
    print("Testing choice prompt...")
    print("What do you want to do?")
    print("1: Go through the crack")
    print("2: Sit and cry") 
    print("3: Look around")
    print("4: Quit")
    
    # Test with automated choice
    choice = "4"  # Quit immediately
    print(f"Automated choice: {choice}")
    
    if choice == "4":
        print("Game quit successfully")
        return True
    
    print("Test completed")
    return True

if __name__ == "__main__":
    test_minimal_game()
