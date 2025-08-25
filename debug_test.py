#!/usr/bin/env python3
"""
Debug test script to isolate the hanging issue
"""

print("Starting debug test...")

try:
    print("Testing imports...")
    from ui import title_screen
    from game_events import start_game
    from scenes import setup_scenes
    from config import SCENE_NAMES
    print("All imports successful")
    
    print("Testing title screen...")
    # Don't actually call it, just check it exists
    print("Title screen function exists")
    
    print("Testing scenes setup...")
    scenes = setup_scenes()
    current_scene = scenes[SCENE_NAMES['CAVE_ENTRANCE']]
    print(f"Scene created: {current_scene.name}")
    
    print("Testing scene enter...")
    current_scene.enter(None)
    print("Scene enter completed")
    
    print("All tests passed!")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
