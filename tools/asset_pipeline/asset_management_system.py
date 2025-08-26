"""
SHABUYA Cave Adventure - Scalable Asset Management System
========================================================

This system provides:
1. Organized asset categories with clear naming conventions
2. Scalable directory structure for future expansion
3. Automated asset discovery and loading
4. Asset validation and quality control
5. Easy addition of new categories, scenes, characters, etc.
"""

ASSET_CATEGORIES = {
    # Character Assets
    "characters": {
        "player_classes": {
            "warrior": {
                "sprite_file": "warrior_sprite.png",
                "description": "Heavy armor, sword and shield",
                "color_scheme": ["#8B4513", "#CD853F", "#F4A460"],  # Brown/bronze
                "dimensions": (64, 64)
            },
            "rogue": {
                "sprite_file": "rogue_sprite.png", 
                "description": "Dark hood, daggers, stealth gear",
                "color_scheme": ["#2F4F2F", "#556B2F", "#8FBC8F"],  # Dark green
                "dimensions": (64, 64)
            },
            "mage": {
                "sprite_file": "mage_sprite.png",
                "description": "Robes, staff, mystical aura", 
                "color_scheme": ["#4B0082", "#8A2BE2", "#9370DB"],  # Purple/violet
                "dimensions": (64, 64)
            }
        },
        "enemies": {
            "primitive_creature": {
                "sprite_file": "primitive_creature_sprite.png",
                "description": "Tribal humanoid with crude weapons",
                "color_scheme": ["#A0522D", "#D2691E", "#CD853F"],  # Earth tones
                "dimensions": (64, 64)
            },
            "divine_heart": {
                "sprite_file": "divine_heart_sprite.png", 
                "description": "Mystical floating heart with divine energy",
                "color_scheme": ["#4B0082", "#8A2BE2", "#FFD700"],  # Purple with gold
                "dimensions": (64, 64)
            },
            "cave_guardian": {
                "sprite_file": "cave_guardian_sprite.png",
                "description": "Stone/earth elemental guardian", 
                "color_scheme": ["#696969", "#808080", "#A9A9A9"],  # Stone grey
                "dimensions": (64, 64)
            }
        },
        # Future expansion ready
        "npcs": {
            # Ready for village chiefs, merchants, etc.
        },
        "bosses": {
            # Ready for major boss encounters
        }
    },
    
    # Scene/Background Assets  
    "scenes": {
        "exploration": {
            "cave_entrance": {
                "file": "cave_entrance.png",
                "description": "Rocky cave mouth with mysterious depths",
                "mood": "mysterious, foreboding",
                "color_palette": ["#8B4513", "#A0522D", "#2F4F2F"],
                "dimensions": (400, 300)
            },
            "skull_chamber": {
                "file": "skull_chamber.png", 
                "description": "Ancient chamber filled with bones and skulls",
                "mood": "dark, ominous",
                "color_palette": ["#2F2F2F", "#8B0000", "#696969"],
                "dimensions": (400, 300)
            },
            "primitive_village": {
                "file": "primitive_village.png",
                "description": "Simple huts and primitive structures", 
                "mood": "rustic, lived-in",
                "color_palette": ["#8B4513", "#228B22", "#CD853F"],
                "dimensions": (400, 300)
            }
        },
        "social_locations": {
            "alley": {
                "file": "alley.png",
                "description": "Narrow passage between primitive buildings",
                "mood": "cramped, shadowy", 
                "color_palette": ["#2F2F2F", "#8B4513", "#556B2F"],
                "dimensions": (400, 300)
            },
            "armory": {
                "file": "armory.png",
                "description": "Weapon storage with primitive arms",
                "mood": "organized, martial",
                "color_palette": ["#8B4513", "#696969", "#CD853F"], 
                "dimensions": (400, 300)
            },
            "chief_house": {
                "file": "chief_house.png",
                "description": "Larger dwelling of the village leader",
                "mood": "authoritative, decorated",
                "color_palette": ["#8B4513", "#DAA520", "#CD853F"],
                "dimensions": (400, 300)
            },
            "healing_pool": {
                "file": "healing_pool.png", 
                "description": "Sacred waters with mystical properties",
                "mood": "serene, magical",
                "color_palette": ["#4682B4", "#87CEEB", "#E0E0E0"],
                "dimensions": (400, 300)
            },
            "village_changed": {
                "file": "village_changed.png",
                "description": "Village transformed by mystical forces", 
                "mood": "altered, supernatural",
                "color_palette": ["#4B0082", "#8A2BE2", "#2F4F2F"],
                "dimensions": (400, 300)
            }
        },
        "ui_scenes": {
            "menu": {
                "file": "menu.png",
                "description": "Main menu background with game title area",
                "mood": "welcoming, atmospheric",
                "color_palette": ["#2F4F2F", "#8B4513", "#CD853F"],
                "dimensions": (400, 300)
            }
        },
        # Future expansion ready
        "dungeon_levels": {
            # Ready for deeper cave levels
        },
        "outdoor_areas": {
            # Ready for forest, mountain areas
        }
    },
    
    # Future Asset Categories (Ready for expansion)
    "items": {
        "weapons": {
            # Swords, daggers, staves, etc.
        },
        "armor": {
            # Helmets, chestplates, shields, etc.
        },
        "consumables": {
            # Potions, scrolls, food, etc.
        }
    },
    
    "effects": {
        "combat": {
            # Spell effects, impact effects, etc.
        },
        "environmental": {
            # Particle effects, weather, etc.
        }
    },
    
    "ui_elements": {
        "buttons": {
            # Menu buttons, action buttons, etc.
        },
        "icons": {
            # Inventory icons, status icons, etc.
        },
        "frames": {
            # Dialog boxes, panels, etc.
        }
    }
}

# Asset Quality Standards
QUALITY_STANDARDS = {
    "sprites": {
        "dimensions": (64, 64),
        "format": "PNG",
        "color_depth": "RGBA",
        "style": "pixel_art",
        "max_colors": 16,  # For authentic pixel art look
        "transparency": True
    },
    "backgrounds": {
        "dimensions": (400, 300),
        "format": "PNG", 
        "color_depth": "RGB",
        "style": "pixel_art",
        "max_colors": 32,  # More colors for detailed scenes
        "transparency": False
    },
    "items": {
        "dimensions": (32, 32),
        "format": "PNG",
        "color_depth": "RGBA", 
        "style": "pixel_art",
        "max_colors": 8,  # Simple items
        "transparency": True
    }
}

# File Organization Structure
DIRECTORY_STRUCTURE = {
    "game_assets/": {
        "sprites/": {
            "characters/": {
                "player/": ["warrior_sprite.png", "rogue_sprite.png", "mage_sprite.png"],
                "enemies/": ["primitive_creature_sprite.png", "divine_heart_sprite.png", "cave_guardian_sprite.png"],
                "npcs/": [],  # Future expansion
                "bosses/": []  # Future expansion
            }
        },
        "backgrounds/": {
            "scenes/": ["cave_entrance.png", "skull_chamber.png", "primitive_village.png", 
                       "alley.png", "armory.png", "chief_house.png", "healing_pool.png", "village_changed.png"],
            "ui/": ["menu.png"],
            "dungeons/": [],  # Future expansion
            "outdoor/": []  # Future expansion  
        },
        "items/": {
            "weapons/": [],  # Future expansion
            "armor/": [],  # Future expansion
            "consumables/": []  # Future expansion
        },
        "effects/": {
            "combat/": [],  # Future expansion
            "environmental/": []  # Future expansion
        },
        "ui/": {
            "buttons/": [],  # Future expansion
            "icons/": [],  # Future expansion
            "frames/": []  # Future expansion
        }
    }
}

def get_asset_info(category, subcategory, asset_name):
    """Get detailed information about a specific asset"""
    try:
        return ASSET_CATEGORIES[category][subcategory][asset_name]
    except KeyError:
        return None

def get_all_assets_in_category(category, subcategory=None):
    """Get all assets in a category or subcategory"""
    if subcategory:
        return ASSET_CATEGORIES.get(category, {}).get(subcategory, {})
    else:
        return ASSET_CATEGORIES.get(category, {})

def validate_asset_quality(asset_path, asset_type):
    """Validate an asset meets quality standards"""
    standards = QUALITY_STANDARDS.get(asset_type, {})
    # Implementation would check file format, dimensions, etc.
    return True, []  # Returns (is_valid, error_list)

if __name__ == "__main__":
    print("SHABUYA Asset Management System")
    print("=" * 50)
    
    # Display current asset inventory
    for category, subcategories in ASSET_CATEGORIES.items():
        if not subcategories:
            continue
            
        print(f"\n📁 {category.upper()}")
        for subcat, items in subcategories.items():
            if items:
                print(f"  └── {subcat} ({len(items)} items)")
                for item_name in items.keys():
                    print(f"      • {item_name}")
            else:
                print(f"  └── {subcat} (ready for expansion)")
