#!/usr/bin/env python3
"""
Cave Game Combat System

This module handles all combat-related functionality including:
- Weapon availability checking
- Combat effectiveness calculations  
- Attack execution for different character classes
- Enhanced weapon mechanics

The combat system provides class-specific attacks and weapon scaling.
"""

from config import STAT_REQUIREMENT, FINAL_BOSS_STAT_REQUIREMENT
from ui import get_user_choice

def get_available_weapons(player):
    """Get list of weapons available to the player's class"""
    from item import dagger, axe, wand
    
    if player.character_class == "Rogue":
        return [dagger]
    elif player.character_class == "Warrior":
        return [axe]
    elif player.character_class == "Mage":
        return [wand]
    else:
        return []

def check_weapon_effectiveness(player, weapon):
    """Check if player meets weapon requirements"""
    if weapon.scale_attr == "agility" and player.agility >= STAT_REQUIREMENT:
        return True, "Your agility makes this weapon highly effective!"
    elif weapon.scale_attr == "strength" and player.strength >= STAT_REQUIREMENT:
        return True, "Your strength makes this weapon devastating!"
    elif weapon.scale_attr == "intelligence" and player.intelligence >= STAT_REQUIREMENT:
        return True, "Your intelligence unlocks this weapon's true potential!"
    else:
        return False, f"You need {STAT_REQUIREMENT} {weapon.scale_attr} to use this weapon effectively."

def execute_weapon_attack(player, weapon):
    """Execute a weapon-based attack with damage calculation"""
    damage = weapon.get_damage(player)
    effective, message = check_weapon_effectiveness(player, weapon)
    
    if effective:
        return True, f"You attack with {weapon.name} for {damage} damage! {message}"
    else:
        return False, f"Your attack with {weapon.name} is ineffective. {message}"

def execute_rogue_attack(player):
    """Execute Rogue-specific attack"""
    if player.agility >= STAT_REQUIREMENT:
        return True, "You slip into the shadows and strike with deadly precision! The creature staggers back, wounded."
    else:
        return False, "You attempt to move stealthily, but your movements are clumsy. The creature notices and counterattacks!"

def execute_warrior_attack(player):
    """Execute Warrior-specific attack"""
    if player.strength >= STAT_REQUIREMENT:
        return True, "You charge forward with overwhelming force! Your powerful blow sends the creature reeling."
    else:
        return False, "You swing your weapon with all your might, but lack the strength to break through the creature's defenses!"

def execute_mage_attack(player):
    """Execute Mage-specific attack"""
    if player.intelligence >= STAT_REQUIREMENT:
        return True, "You weave complex magical energies and unleash a devastating spell! Arcane power overwhelms your foe."
    else:
        return False, "You attempt to cast a spell, but your understanding of magic is insufficient. The spell fizzles out harmlessly!"

def execute_class_ability_final_boss(player):
    """Execute class-specific ability against final boss"""
    if player.character_class == "Rogue" and player.agility >= FINAL_BOSS_STAT_REQUIREMENT:
        return True, "🌟 SHADOW STRIKE MASTERY! 🌟\nYou become one with the darkness, striking with supernatural speed and precision!"
    elif player.character_class == "Warrior" and player.strength >= FINAL_BOSS_STAT_REQUIREMENT:
        return True, "🌟 BERSERKER'S FURY! 🌟\nYour strength transcends mortal limits as you unleash devastating attacks!"
    elif player.character_class == "Mage" and player.intelligence >= FINAL_BOSS_STAT_REQUIREMENT:
        return True, "🌟 ARCANE MASTERY! 🌟\nYou channel the fundamental forces of magic with perfect understanding!"
    else:
        return False, f"You need {FINAL_BOSS_STAT_REQUIREMENT} in your primary stat to use this legendary ability!"
