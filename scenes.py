#!/usr/bin/env python3
"""
Cave Game Scene Management Module

This module handles the game world structure including:
- Scene setup and initialization
- Access control and requirements
- Scene navigation and connections
- World state management

The scene system creates an interconnected game world with proper progression gates.
"""

from player import Scene
from config import SCENE_NAMES

def setup_scenes():
    """Set up all game scenes"""
    scenes = {}
    
    # Cave Entrance
    cave_entrance = Scene(SCENE_NAMES['CAVE_ENTRANCE'], "You find yourself in a dark cave with only a crack in the wall visible.")
    scenes[SCENE_NAMES['CAVE_ENTRANCE']] = cave_entrance
    
    # Skull Chamber
    skull_chamber = Scene(SCENE_NAMES['SKULL_CHAMBER'], "A vast chamber dominated by a colossal skull.")
    scenes[SCENE_NAMES['SKULL_CHAMBER']] = skull_chamber
    
    # Primitive Village
    primitive_village = Scene(SCENE_NAMES['PRIMITIVE_VILLAGE'], "The heart of a primitive village with bone and hide huts.")
    scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']] = primitive_village
    
    # Alley
    alley = Scene(SCENE_NAMES['ALLEY'], "A narrow, shadowy alley between ancient stone walls.")
    scenes[SCENE_NAMES['ALLEY']] = alley
    
    # Armory (locked by default)
    armory = Scene(SCENE_NAMES['ARMORY'], "An ancient armory containing enhanced weapons.")
    armory.locked = True
    armory.key = "Armory Key"
    scenes[SCENE_NAMES['ARMORY']] = armory
    
    # Cave People Chief House (locked by default)
    chief_house = Scene(SCENE_NAMES['CHIEF_HOUSE'], "The imposing dwelling of the tribal chief.")
    chief_house.locked = True
    chief_house.key = "Town Key"
    scenes[SCENE_NAMES['CHIEF_HOUSE']] = chief_house
    
    # Healing Pool
    healing_pool = Scene(SCENE_NAMES['HEALING_POOL'], "A sacred chamber with mystical healing waters.")
    scenes[SCENE_NAMES['HEALING_POOL']] = healing_pool
    
    # Primitive Village Changed (post-blessing)
    village_changed = Scene(SCENE_NAMES['VILLAGE_CHANGED'], "The village after the cosmic awakening.")
    scenes[SCENE_NAMES['VILLAGE_CHANGED']] = village_changed
    
    return scenes

def check_scene_access(scene, player):
    """Check if player can access a locked scene"""
    if not getattr(scene, 'locked', False):
        return True
    
    key_name = getattr(scene, 'key', None)
    if key_name and hasattr(player.inventory, 'has_item'):
        return player.inventory.has_item(key_name)
    
    return False

def handle_locked_scene(scene_name, key_name):
    """Handle attempt to access locked scene"""
    print()
    print(f"The {scene_name} is locked. You need the {key_name} to enter.")
    print("You're still in the village.")
    return False
