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

from typing import Optional, Dict
from config import SCENE_NAMES


class Scene:
    """
    Represents a game location with navigation and access control.
    
    Attributes:
        name (str): Display name of the scene
        description (str): Descriptive text for the location
        exits (Dict[str, str]): Available exits mapping directions to scene names
        locked (bool): Whether this scene requires a key
        key (Optional[str]): Name of the key item required for access
    """
    def __init__(self, name: str, description: str, exits: Optional[Dict[str, str]] = None, 
                 locked: bool = False, key: Optional[str] = None) -> None:
        self.name = name
        self.description = description
        self.exits = exits or {}  # e.g., {'north': 'Engineering Bay'}
        self.locked = locked
        self.key = key  # name of key that unlocks

    def enter(self, player) -> bool:
        """Attempt to enter the scene, checking for locks and keys."""
        if self.locked and not player.inventory.has_item(self.key):
            print("The door is locked. You need the key.")
            return False
        print(f"You enter the {self.name}. {self.description}")
        return True
        
    def unlock(self, player) -> None:
        """Unlock the scene if player has the required key."""
        if self.locked and player.inventory.has_item(self.key):
            self.locked = False
            print(f"You unlock the {self.name} with the {self.key}.")
        else:
            print("You can't unlock this door.")

def setup_scenes():
    """Set up all game scenes with proper exits and connections"""
    scenes = {}
    
    # Cave Entrance
    cave_entrance = Scene(
        name=SCENE_NAMES['CAVE_ENTRANCE'], 
        description="You find yourself in a dark cave with only a crack in the wall visible.",
        exits={'north': SCENE_NAMES['SKULL_CHAMBER']}
    )
    scenes[SCENE_NAMES['CAVE_ENTRANCE']] = cave_entrance
    
    # Skull Chamber
    skull_chamber = Scene(
        name=SCENE_NAMES['SKULL_CHAMBER'], 
        description="A vast chamber dominated by a colossal skull.",
        exits={
            'south': SCENE_NAMES['CAVE_ENTRANCE'],
            'west': SCENE_NAMES['PRIMITIVE_VILLAGE']
        }
    )
    scenes[SCENE_NAMES['SKULL_CHAMBER']] = skull_chamber
    
    # Primitive Village
    primitive_village = Scene(
        name=SCENE_NAMES['PRIMITIVE_VILLAGE'], 
        description="The heart of a primitive village with bone and hide huts.",
        exits={
            'east': SCENE_NAMES['SKULL_CHAMBER'],
            'north': SCENE_NAMES['ALLEY'],
            'south': SCENE_NAMES['CHIEF_HOUSE'],
            'west': SCENE_NAMES['ARMORY']
        }
    )
    scenes[SCENE_NAMES['PRIMITIVE_VILLAGE']] = primitive_village
    
    # Alley
    alley = Scene(
        name=SCENE_NAMES['ALLEY'], 
        description="A narrow, shadowy alley between ancient stone walls.",
        exits={'south': SCENE_NAMES['PRIMITIVE_VILLAGE']}
    )
    scenes[SCENE_NAMES['ALLEY']] = alley
    
    # Armory (locked by default)
    armory = Scene(
        name=SCENE_NAMES['ARMORY'], 
        description="An ancient armory containing enhanced weapons.",
        exits={'east': SCENE_NAMES['PRIMITIVE_VILLAGE']},
        locked=True,
        key="Armory Key"
    )
    scenes[SCENE_NAMES['ARMORY']] = armory
    
    # Cave People Chief House (locked by default)
    chief_house = Scene(
        name=SCENE_NAMES['CHIEF_HOUSE'], 
        description="The imposing dwelling of the tribal chief.",
        exits={
            'north': SCENE_NAMES['PRIMITIVE_VILLAGE'],
            'south': SCENE_NAMES['HEALING_POOL']
        },
        locked=True,
        key="Town Key"
    )
    scenes[SCENE_NAMES['CHIEF_HOUSE']] = chief_house
    
    # Healing Pool
    healing_pool = Scene(
        name=SCENE_NAMES['HEALING_POOL'], 
        description="A sacred chamber with mystical healing waters.",
        exits={
            'north': SCENE_NAMES['CHIEF_HOUSE'],
            'south': SCENE_NAMES['VILLAGE_CHANGED']
        }
    )
    scenes[SCENE_NAMES['HEALING_POOL']] = healing_pool
    
    # Primitive Village Changed (post-blessing)
    village_changed = Scene(
        name=SCENE_NAMES['VILLAGE_CHANGED'], 
        description="The village after the cosmic awakening.",
        exits={'north': SCENE_NAMES['HEALING_POOL']}
    )
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
