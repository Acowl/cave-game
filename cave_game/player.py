#!/usr/bin/env python3
"""
Cave Game Player Class

This module defines the core game entities:
- Player: Character with stats, inventory, and progression
"""

from typing import Optional, TYPE_CHECKING

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
