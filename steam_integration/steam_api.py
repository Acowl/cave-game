#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Steam Integration Module
Future-ready Steam integration for when the game is published on Steam

This module provides:
- Steam API integration (when available)  
- Achievement system
- Steam Cloud save support
- Steam Workshop integration (for future content)
- Steam overlay compatibility
"""

import sys
import json
from pathlib import Path
from typing import Optional, Dict, List, Any
from dataclasses import dataclass

# Steam integration status
STEAM_AVAILABLE = False
try:
    # This will be available when the Steamworks SDK is integrated
    # import steamworks
    # STEAM_AVAILABLE = True
    pass
except ImportError:
    STEAM_AVAILABLE = False

@dataclass
class Achievement:
    """Steam achievement definition"""
    id: str
    name: str
    description: str
    hidden: bool = False
    progress_stat: Optional[str] = None

@dataclass
class Statistic:
    """Steam statistic definition"""
    id: str
    name: str
    type: str = "int"  # int, float, avgrate
    default_value: Any = 0

class SteamIntegration:
    """Steam integration manager"""
    
    def __init__(self, app_id: Optional[int] = None):
        self.app_id = app_id
        self.initialized = False
        self.achievements: Dict[str, Achievement] = {}
        self.statistics: Dict[str, Statistic] = {}
        self._setup_achievements()
        self._setup_statistics()
    
    def initialize(self) -> bool:
        """Initialize Steam API"""
        if not STEAM_AVAILABLE:
            print("🎮 Steam API not available - running in standalone mode")
            return False
        
        try:
            # Initialize Steamworks SDK when available
            # steamworks.initialize(self.app_id)
            self.initialized = True
            print("🎮 Steam API initialized successfully")
            return True
        except Exception as e:
            print(f"⚠️ Steam initialization failed: {e}")
            return False
    
    def _setup_achievements(self):
        """Define game achievements for Steam"""
        achievements = [
            Achievement(
                id="FIRST_STEPS",
                name="First Steps", 
                description="Started your first adventure in the caves"
            ),
            Achievement(
                id="CLASS_MASTER",
                name="Class Master",
                description="Played as all three character classes"
            ),
            Achievement(
                id="WARRIOR_VICTORY",
                name="Mighty Warrior",
                description="Completed the game as a Warrior"
            ),
            Achievement(
                id="ROGUE_VICTORY", 
                name="Shadow Walker",
                description="Completed the game as a Rogue"
            ),
            Achievement(
                id="MAGE_VICTORY",
                name="Arcane Master", 
                description="Completed the game as a Mage"
            ),
            Achievement(
                id="WEAPON_COLLECTOR",
                name="Weapon Collector",
                description="Found all enhanced weapons"
            ),
            Achievement(
                id="EXPLORATION_MASTER",
                name="Master Explorer", 
                description="Visited every scene in the game"
            ),
            Achievement(
                id="BOSS_SLAYER",
                name="Boss Slayer",
                description="Defeated the final boss"
            ),
            Achievement(
                id="STAT_MAXED",
                name="Peak Performance",
                description="Reached maximum stats in all categories"
            ),
            Achievement(
                id="SPEED_RUN",
                name="Swift Adventurer",
                description="Completed the game in under 30 minutes",
                hidden=True
            ),
            Achievement(
                id="PACIFIST_RUN",
                name="Peaceful Soul",
                description="Completed the game without fighting optional enemies",
                hidden=True
            ),
            Achievement(
                id="HARDCORE_VICTORY",
                name="Legendary Adventurer", 
                description="Completed the game on the hardest difficulty",
                hidden=True
            )
        ]
        
        for achievement in achievements:
            self.achievements[achievement.id] = achievement
    
    def _setup_statistics(self):
        """Define game statistics for Steam"""
        statistics = [
            Statistic("games_played", "Games Played"),
            Statistic("games_won", "Games Won"),
            Statistic("total_playtime", "Total Play Time", "int"),
            Statistic("enemies_defeated", "Enemies Defeated"),
            Statistic("scenes_visited", "Scenes Visited"),
            Statistic("deaths", "Deaths"),
            Statistic("items_collected", "Items Collected"),
            Statistic("level_ups", "Level Ups"),
            Statistic("fastest_completion", "Fastest Completion Time", "int"),
            Statistic("warrior_victories", "Warrior Victories"),
            Statistic("rogue_victories", "Rogue Victories"),
            Statistic("mage_victories", "Mage Victories")
        ]
        
        for stat in statistics:
            self.statistics[stat.id] = stat
    
    def unlock_achievement(self, achievement_id: str) -> bool:
        """Unlock a Steam achievement"""
        if not self.initialized or achievement_id not in self.achievements:
            return False
        
        achievement = self.achievements[achievement_id]
        
        try:
            # Unlock achievement via Steam API when available
            # steamworks.unlock_achievement(achievement_id)
            print(f"🏆 Achievement unlocked: {achievement.name}")
            return True
        except Exception as e:
            print(f"⚠️ Failed to unlock achievement {achievement_id}: {e}")
            return False
    
    def set_statistic(self, stat_id: str, value: Any) -> bool:
        """Set a Steam statistic value"""
        if not self.initialized or stat_id not in self.statistics:
            return False
        
        try:
            # Set statistic via Steam API when available  
            # steamworks.set_stat(stat_id, value)
            return True
        except Exception as e:
            print(f"⚠️ Failed to set statistic {stat_id}: {e}")
            return False
    
    def increment_statistic(self, stat_id: str, increment: int = 1) -> bool:
        """Increment a Steam statistic"""
        if not self.initialized or stat_id not in self.statistics:
            return False
        
        try:
            # Increment statistic via Steam API when available
            # current_value = steamworks.get_stat(stat_id)
            # steamworks.set_stat(stat_id, current_value + increment)
            return True
        except Exception as e:
            print(f"⚠️ Failed to increment statistic {stat_id}: {e}")
            return False
    
    def store_statistics(self) -> bool:
        """Store statistics to Steam"""
        if not self.initialized:
            return False
        
        try:
            # Store stats via Steam API when available
            # steamworks.store_stats()
            return True
        except Exception as e:
            print(f"⚠️ Failed to store statistics: {e}")
            return False
    
    def is_achievement_unlocked(self, achievement_id: str) -> bool:
        """Check if achievement is unlocked"""
        if not self.initialized or achievement_id not in self.achievements:
            return False
        
        try:
            # Check achievement status via Steam API when available
            # return steamworks.is_achievement_unlocked(achievement_id)
            return False
        except Exception:
            return False
    
    def get_statistic_value(self, stat_id: str) -> Any:
        """Get current value of a statistic"""
        if not self.initialized or stat_id not in self.statistics:
            return None
        
        try:
            # Get statistic value via Steam API when available
            # return steamworks.get_stat(stat_id)
            return None
        except Exception:
            return None
    
    def enable_steam_cloud(self) -> bool:
        """Enable Steam Cloud save synchronization"""
        if not self.initialized:
            return False
        
        # Steam Cloud is typically handled automatically by Steam
        # but games can use the API to manage cloud files explicitly
        return True
    
    def shutdown(self):
        """Shutdown Steam API"""
        if self.initialized:
            try:
                # Shutdown Steam API when available
                # steamworks.shutdown()
                self.initialized = False
                print("🎮 Steam API shutdown")
            except Exception as e:
                print(f"⚠️ Steam shutdown error: {e}")

class SteamGameIntegration:
    """Game-specific Steam integration"""
    
    def __init__(self):
        self.steam = SteamIntegration()
        self.session_stats = {
            'start_time': None,
            'enemies_defeated': 0,
            'scenes_visited': set(),
            'items_collected': 0,
            'level_ups': 0
        }
    
    def on_game_start(self, player_class: str):
        """Called when a new game starts"""
        import time
        self.session_stats['start_time'] = time.time()
        
        # Track first game
        if not self.steam.is_achievement_unlocked("FIRST_STEPS"):
            self.steam.unlock_achievement("FIRST_STEPS")
        
        # Increment games played
        self.steam.increment_statistic("games_played")
    
    def on_game_complete(self, player_class: str, victory: bool = True):
        """Called when game is completed"""
        import time
        
        if not victory:
            return
        
        # Calculate completion time
        if self.session_stats['start_time']:
            completion_time = int(time.time() - self.session_stats['start_time'])
            
            # Check for speed run achievement (30 minutes = 1800 seconds)
            if completion_time < 1800:
                self.steam.unlock_achievement("SPEED_RUN")
            
            # Update fastest completion time
            current_best = self.steam.get_statistic_value("fastest_completion")
            if current_best is None or completion_time < current_best:
                self.steam.set_statistic("fastest_completion", completion_time)
        
        # Class-specific achievements
        class_achievements = {
            "Warrior": "WARRIOR_VICTORY",
            "Rogue": "ROGUE_VICTORY", 
            "Mage": "MAGE_VICTORY"
        }
        
        if player_class in class_achievements:
            achievement_id = class_achievements[player_class]
            self.steam.unlock_achievement(achievement_id)
            
            # Track class victories
            stat_id = f"{player_class.lower()}_victories"
            self.steam.increment_statistic(stat_id)
        
        # Check if played as all classes
        warrior_wins = self.steam.get_statistic_value("warrior_victories") or 0
        rogue_wins = self.steam.get_statistic_value("rogue_victories") or 0
        mage_wins = self.steam.get_statistic_value("mage_victories") or 0
        
        if warrior_wins > 0 and rogue_wins > 0 and mage_wins > 0:
            self.steam.unlock_achievement("CLASS_MASTER")
        
        # General completion tracking
        self.steam.unlock_achievement("BOSS_SLAYER")
        self.steam.increment_statistic("games_won")
    
    def on_enemy_defeated(self, enemy_name: str):
        """Called when an enemy is defeated"""
        self.session_stats['enemies_defeated'] += 1
        self.steam.increment_statistic("enemies_defeated")
    
    def on_scene_visited(self, scene_name: str):
        """Called when a new scene is visited"""
        self.session_stats['scenes_visited'].add(scene_name)
        self.steam.increment_statistic("scenes_visited")
        
        # Check for exploration achievement (assuming 8 total scenes)
        if len(self.session_stats['scenes_visited']) >= 8:
            self.steam.unlock_achievement("EXPLORATION_MASTER")
    
    def on_item_collected(self, item_name: str):
        """Called when an item is collected"""
        self.session_stats['items_collected'] += 1
        self.steam.increment_statistic("items_collected")
    
    def on_level_up(self, new_level: int):
        """Called when player levels up"""
        self.session_stats['level_ups'] += 1
        self.steam.increment_statistic("level_ups")
    
    def on_enhanced_weapon_collected(self, weapon_count: int):
        """Called when enhanced weapons are collected"""
        if weapon_count >= 3:  # All enhanced weapons
            self.steam.unlock_achievement("WEAPON_COLLECTOR")
    
    def on_stats_maxed(self, all_stats_maxed: bool):
        """Called when checking if stats are maxed"""
        if all_stats_maxed:
            self.steam.unlock_achievement("STAT_MAXED")

# Global Steam integration instance
steam_integration = SteamGameIntegration()

def get_steam_integration() -> SteamGameIntegration:
    """Get the global Steam integration instance"""
    return steam_integration

def initialize_steam(app_id: Optional[int] = None) -> bool:
    """Initialize Steam integration"""
    return steam_integration.steam.initialize()

def shutdown_steam():
    """Shutdown Steam integration"""
    steam_integration.steam.shutdown()

# Export functions for game integration
__all__ = [
    'SteamIntegration',
    'SteamGameIntegration', 
    'get_steam_integration',
    'initialize_steam',
    'shutdown_steam',
    'STEAM_AVAILABLE'
]
