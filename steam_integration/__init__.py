"""
Steam Integration Module for SHABUYA Cave Adventure
Provides Steam API integration, achievements, and statistics
"""

from .steam_api import SteamIntegration, get_steam_integration

__version__ = "1.0.0"
__all__ = ["SteamIntegration", "get_steam_integration"]
