"""
SHABUYA Cave Adventure - Scalable AI Art Generation Prompts
==========================================================

Comprehensive prompts for all asset categories with consistent style guide
"""

# Global Style Guide
STYLE_GUIDE = {
    "base_style": "16-bit pixel art, retro gaming aesthetic, detailed sprite work",
    "resolution": "high resolution for sharp details",
    "color_palette": "earthy tones with mystical accents", 
    "lighting": "dramatic shadows and highlights",
    "consistency": "consistent art style across all assets",
    "inspiration": "classic RPG games like Secret of Mana, Chrono Trigger"
}

# Character Asset Prompts
CHARACTER_PROMPTS = {
    "player_classes": {
        "warrior": {
            "prompt": "16-bit pixel art character sprite, medieval warrior, heavy plate armor with bronze trim, large sword and shield, determined expression, brown and bronze color scheme, standing pose facing forward, 64x64 pixels, transparent background, detailed shading, retro RPG game style",
            "variations": [
                "battle stance with sword raised",
                "walking animation frame", 
                "victory pose with arms crossed"
            ]
        },
        "rogue": {
            "prompt": "16-bit pixel art character sprite, stealthy rogue assassin, dark green hooded cloak, leather armor, twin daggers, mysterious shadowed face, dark forest green color scheme, crouched ready stance, 64x64 pixels, transparent background, detailed pixel shading",
            "variations": [
                "sneaking pose low to ground",
                "throwing dagger action",
                "vanishing in shadows effect"
            ]
        },
        "mage": {
            "prompt": "16-bit pixel art character sprite, mystical mage wizard, flowing purple robes with arcane symbols, ornate staff with glowing crystal, wise beard, purple and violet color scheme, spell-casting pose, 64x64 pixels, transparent background, magical aura effect",
            "variations": [
                "reading spellbook pose",
                "staff held high channeling energy",
                "meditation pose with floating runes"
            ]
        }
    },
    
    "enemies": {
        "primitive_creature": {
            "prompt": "16-bit pixel art enemy sprite, primitive tribal humanoid, crude leather clothing, bone jewelry, simple stone axe, wild hair, earthy brown color scheme, aggressive stance, 64x64 pixels, transparent background, detailed tribal markings",
            "variations": [
                "charging attack pose",
                "defensive crouch with weapon",
                "wounded state with battle scars"
            ]
        },
        "divine_heart": {
            "prompt": "16-bit pixel art mystical enemy sprite, floating divine heart, pulsing with golden light, purple mystical energy aura, ornate patterns, ethereal glow effect, purple and gold color scheme, hovering pose, 64x64 pixels, transparent background, magical particles",
            "variations": [
                "power charging with intense glow",
                "healing pulse animation frame",
                "dormant state with dim glow"
            ]
        },
        "cave_guardian": {
            "prompt": "16-bit pixel art boss enemy sprite, ancient stone guardian, weathered rock texture, glowing crystal eyes, moss and mineral deposits, imposing stance, grey stone color scheme, 64x64 pixels, transparent background, detailed rock textures",
            "variations": [
                "awakening with crystal eyes lighting up",
                "defensive wall stance",
                "crumbling damage state"
            ]
        }
    }
}

# Scene/Background Prompts  
SCENE_PROMPTS = {
    "exploration": {
        "cave_entrance": {
            "prompt": "16-bit pixel art background, mysterious cave entrance, rocky cliff face, dark opening with subtle internal glow, ancient stone formations, moss and vines, earthy brown and green color palette, 400x300 pixels, atmospheric perspective, detailed rock textures",
            "mood": "mysterious and inviting danger",
            "time_of_day": "twilight with mysterious cave glow"
        },
        "skull_chamber": {
            "prompt": "16-bit pixel art background, ancient bone chamber, scattered skulls and skeletons, weathered stone walls, dim torchlight casting eerie shadows, dark red and grey color palette, 400x300 pixels, ominous atmosphere, detailed bone textures",
            "mood": "dark and foreboding",
            "lighting": "flickering torchlight with deep shadows"
        },
        "primitive_village": {
            "prompt": "16-bit pixel art background, primitive tribal village, simple thatched huts, wooden fences, campfire smoke, forest surroundings, earthy brown and green color palette, 400x300 pixels, lived-in atmosphere, detailed primitive architecture",
            "mood": "rustic and peaceful",
            "time_of_day": "warm afternoon sunlight"
        }
    },
    
    "social_locations": {
        "alley": {
            "prompt": "16-bit pixel art background, narrow village alley, wooden buildings on both sides, shadowy passage, scattered primitive tools, earthy color palette with deep shadows, 400x300 pixels, cramped intimate atmosphere",
            "mood": "secretive and cramped",
            "lighting": "filtered sunlight through buildings"
        },
        "armory": {
            "prompt": "16-bit pixel art background, primitive weapons storage, stone and wood shelves, various crude weapons displayed, leather armor hanging, torchlit interior, brown and metallic color palette, 400x300 pixels, organized but primitive",
            "mood": "functional and martial",
            "lighting": "steady torch illumination"
        },
        "chief_house": {
            "prompt": "16-bit pixel art background, village leader's dwelling, larger decorated hut, tribal banners, throne of carved wood, ceremonial items, rich earth tones with gold accents, 400x300 pixels, authoritative atmosphere",
            "mood": "important and decorated",
            "details": "tribal ceremonial decorations"
        },
        "healing_pool": {
            "prompt": "16-bit pixel art background, sacred healing waters, crystal clear pool with mystical glow, smooth stone surroundings, soft blue lighting, peaceful atmosphere, blue and white color palette, 400x300 pixels, serene and magical",
            "mood": "peaceful and restorative",
            "lighting": "soft mystical glow from water"
        },
        "village_changed": {
            "prompt": "16-bit pixel art background, mystically transformed village, purple energy effects, altered architecture, floating magical symbols, surreal twisted buildings, purple and dark color palette, 400x300 pixels, supernatural atmosphere",
            "mood": "altered and supernatural",
            "effects": "mystical energy and floating elements"
        }
    },
    
    "ui_scenes": {
        "menu": {
            "prompt": "16-bit pixel art background, main menu scene, atmospheric cave adventure setting, title area space, mystical ambiance, earthy tones with magical accents, 400x300 pixels, welcoming but mysterious, space for UI elements",
            "mood": "welcoming yet adventurous",
            "ui_consideration": "clear space for menu text and buttons"
        }
    }
}

# Future Expansion Prompts (Ready to use)
EXPANSION_PROMPTS = {
    "npcs": {
        "village_elder": {
            "prompt": "16-bit pixel art NPC sprite, wise village elder, aged features, ceremonial robes, staff of wisdom, respectful stance, earth tone colors, 64x64 pixels, transparent background"
        },
        "merchant": {
            "prompt": "16-bit pixel art NPC sprite, traveling merchant, pack full of goods, friendly expression, practical clothing, welcoming pose, varied color scheme, 64x64 pixels"
        }
    },
    
    "items": {
        "healing_potion": {
            "prompt": "16-bit pixel art item icon, healing potion bottle, red liquid with magical sparkles, cork stopper, glass reflection, 32x32 pixels, transparent background"
        },
        "iron_sword": {
            "prompt": "16-bit pixel art weapon icon, iron sword, detailed blade with crossguard, leather-wrapped handle, metallic shine, 32x32 pixels, transparent background"
        }
    },
    
    "effects": {
        "spell_cast": {
            "prompt": "16-bit pixel art spell effect, magical energy burst, swirling particles, glowing center, purple and gold colors, animated frame, 64x64 pixels, transparent background"
        }
    }
}

# AI Art Generation Instructions
GENERATION_INSTRUCTIONS = {
    "tools_recommended": [
        "DALL-E 3 (OpenAI)",
        "Midjourney", 
        "Stable Diffusion",
        "Adobe Firefly"
    ],
    
    "workflow": [
        "1. Use the exact prompt provided for consistency",
        "2. Generate multiple variations if available", 
        "3. Select the best version that matches the style guide",
        "4. Post-process to ensure exact pixel dimensions",
        "5. Validate against quality standards",
        "6. Test in game GUI before finalizing"
    ],
    
    "post_processing": [
        "Resize to exact specifications (64x64 for sprites, 400x300 for backgrounds)",
        "Ensure transparent backgrounds for sprites",
        "Optimize color palette for pixel art aesthetic",
        "Check for visual consistency with existing assets"
    ]
}

def get_prompt_for_asset(category, subcategory, asset_name):
    """Get the complete AI generation prompt for a specific asset"""
    prompts_dict = CHARACTER_PROMPTS if category == "characters" else SCENE_PROMPTS
    
    try:
        asset_data = prompts_dict[subcategory][asset_name]
        base_prompt = asset_data["prompt"]
        
        # Add global style guide elements
        full_prompt = f"{base_prompt}, {STYLE_GUIDE['base_style']}, {STYLE_GUIDE['resolution']}"
        
        return {
            "prompt": full_prompt,
            "variations": asset_data.get("variations", []),
            "mood": asset_data.get("mood", ""),
            "additional_notes": asset_data.get("lighting", "") or asset_data.get("details", "")
        }
    except KeyError:
        return None

def generate_all_prompts_file():
    """Generate a complete prompts file for easy reference"""
    output = []
    output.append("SHABUYA Cave Adventure - Complete AI Art Prompts")
    output.append("=" * 60)
    output.append("")
    
    # Style guide
    output.append("STYLE GUIDE:")
    for key, value in STYLE_GUIDE.items():
        output.append(f"• {key.replace('_', ' ').title()}: {value}")
    output.append("")
    
    # Character prompts
    output.append("CHARACTER SPRITES:")
    output.append("-" * 30)
    for subcat, chars in CHARACTER_PROMPTS.items():
        output.append(f"\n{subcat.replace('_', ' ').title()}:")
        for char_name, char_data in chars.items():
            output.append(f"\n{char_name.replace('_', ' ').title()}:")
            output.append(f"Prompt: {char_data['prompt']}")
            if char_data.get("variations"):
                output.append("Variations:")
                for var in char_data["variations"]:
                    output.append(f"  - {var}")
    
    # Scene prompts
    output.append("\n\nSCENE BACKGROUNDS:")
    output.append("-" * 30)
    for subcat, scenes in SCENE_PROMPTS.items():
        output.append(f"\n{subcat.replace('_', ' ').title()}:")
        for scene_name, scene_data in scenes.items():
            output.append(f"\n{scene_name.replace('_', ' ').title()}:")
            output.append(f"Prompt: {scene_data['prompt']}")
            output.append(f"Mood: {scene_data['mood']}")
    
    return "\n".join(output)

if __name__ == "__main__":
    print("SHABUYA AI Art Generation System")
    print("=" * 50)
    
    # Example usage
    warrior_prompt = get_prompt_for_asset("characters", "player_classes", "warrior")
    if warrior_prompt:
        print("\nExample - Warrior Sprite Prompt:")
        print(warrior_prompt["prompt"])
        print(f"Mood: {warrior_prompt['mood']}")
    
    cave_prompt = get_prompt_for_asset("scenes", "exploration", "cave_entrance") 
    if cave_prompt:
        print("\nExample - Cave Entrance Background Prompt:")
        print(cave_prompt["prompt"])
        print(f"Mood: {cave_prompt['mood']}")
    
    print(f"\nTotal prompts available: {sum(len(chars) for chars in CHARACTER_PROMPTS.values()) + sum(len(scenes) for scenes in SCENE_PROMPTS.values())}")
