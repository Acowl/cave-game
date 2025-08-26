#!/usr/bin/env python3
"""
Cave Game Configuration Module

This module contains all game constants, settings, and configuration values.
Centralizing these values makes the game easier to balance and maintain.

Constants:
    STAT_REQUIREMENT: Minimum stat level needed for legendary actions
    STARTING_STAT_VALUE: Initial value for all player stats
    LEVEL_UP_POINTS: Points gained per level up
    FINAL_BOSS_STAT_REQUIREMENT: Combined stat requirement for final boss
"""

# Combat and Progression Constants
STAT_REQUIREMENT = 8
STARTING_STAT_VALUE = 5
LEVEL_UP_POINTS = 3
FINAL_BOSS_STAT_REQUIREMENT = 5

# Game Balance Settings
STARTING_HEALTH = 100
BASE_DAMAGE_MODIFIER = 1.0
ENHANCED_WEAPON_BONUS = 2.0

# Scene Names (for consistency)
SCENE_NAMES = {
    'CAVE_ENTRANCE': 'Cave Entrance',
    'SKULL_CHAMBER': 'Skull Chamber',
    'PRIMITIVE_VILLAGE': 'Primitive Village',
    'ALLEY': 'Alley',
    'ARMORY': 'Armory',
    'CHIEF_HOUSE': 'Cave People Chief House',
    'HEALING_POOL': 'Healing Pool',
    'VILLAGE_CHANGED': 'Primitive Village Changed'
}

# Game Messages
MESSAGES = {
    'GAME_OVER': "💀 YOU HAVE DIED 💀",
    'VICTORY': "🏆 VICTORY! 🏆",
    'LEVEL_UP': "You feel a surge of power as you level up!",
    'THANKS_PLAYING': "Thanks for playing!",
    'INVALID_OPTION': "Invalid option.",
    'QUIT_PROMPT': "Enter your choice: "
}
