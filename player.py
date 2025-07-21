#!/usr/bin/env python3
"""
Cave Game Player and Scene Classes

This module defines the core game entities:
- Player: Character with stats, inventory, and progression
- Scene: Game world locations with connections and access control
"""

from typing import Optional, Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from item import Inventory, Weapon


class Player:
    """
    Represents the player character with stats, inventory, and progression.
    
    Attributes:
        health (int): Current health points
        strength (int): Physical combat effectiveness  
        intelligence (int): Magical combat effectiveness
        agility (int): Stealth and speed effectiveness
        level (int): Current character level
        inventory (Inventory): Items and keys collected
        weapon (Optional[Weapon]): Currently equipped weapon
    """
    def __init__(self) -> None:
        self.health: int = 100
        self.strength: int = 5
        self.intelligence: int = 5
        self.agility: int = 5
        self.level: int = 1
        self.inventory: 'Inventory' = None  # Will be set in game initialization
        self.weapon: Optional['Weapon'] = None
    
    def level_up(self) -> None:
        """Increase player level and provide attribute upgrade options."""
        self.level += 1
        print("You leveled up! Choose an attribute to increase.")
        # logic for increasing attributes

    def attack(self) -> None:
        """Execute an attack using the equipped weapon."""
        # damage = base + scaling
        pass


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
    def __init__(self, name: str, description: str, exits: Dict[str, str], 
                 locked: bool = False, key: Optional[str] = None) -> None:
        self.name = name
        self.description = description
        self.exits = exits  # e.g., {'north': 'Engineering Bay'}
        self.locked = locked
        self.key = key  # name of key that unlocks

    def enter(self, player: Player) -> None:
        if self.locked and not player.inventory.has_item(self.key):
            print("The door is locked. You need the key.")
            return False
        print(f"You enter the {self.name}. {self.description}")
        return True
    def unlock(self, player):
        if self.locked and player.inventory.has_item(self.key):
            self.locked = False
            print(f"You unlock the {self.name} with the {self.key}.")
        else:
            print("You can't unlock this door.")
