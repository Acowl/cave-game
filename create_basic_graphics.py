#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Basic Graphics Asset Creator
Creates simple programmer art for the core demo
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os

def create_character_sprites():
    """Create basic character class sprites (64x64)"""
    sprite_dir = Path("game_assets/sprites")
    sprite_dir.mkdir(parents=True, exist_ok=True)
    
    # Character sprite configurations
    sprite_configs = {
        'warrior': {
            'primary_color': '#8B4513',    # Brown
            'secondary_color': '#FFD700',   # Gold
            'symbol': '🛡️',
            'description': 'Tank class with high defense'
        },
        'rogue': {
            'primary_color': '#2F4F2F',    # Dark green
            'secondary_color': '#90EE90',   # Light green
            'symbol': '🗡️',
            'description': 'Fast class with high agility'
        },
        'mage': {
            'primary_color': '#4B0082',    # Indigo
            'secondary_color': '#DA70D6',   # Orchid
            'symbol': '🔮',
            'description': 'Magic class with high intelligence'
        },
        'enemy': {
            'primary_color': '#8B0000',    # Dark red
            'secondary_color': '#FF6B6B',   # Light red
            'symbol': '👹',
            'description': 'Generic enemy'
        }
    }
    
    print("🎨 Creating character sprites...")
    
    for name, config in sprite_configs.items():
        # Create 64x64 sprite
        img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Main body circle
        draw.ellipse([8, 16, 56, 56], fill=config['primary_color'])
        
        # Detail circle (armor/equipment indicator)
        draw.ellipse([20, 8, 44, 32], fill=config['secondary_color'])
        
        # Simple border for definition
        draw.ellipse([8, 16, 56, 56], outline='#000000', width=2)
        draw.ellipse([20, 8, 44, 32], outline='#000000', width=1)
        
        # Save sprite
        sprite_path = sprite_dir / f"{name}_sprite.png"
        img.save(sprite_path)
        print(f"  ✅ Created {name} sprite: {sprite_path}")
    
    return len(sprite_configs)

def create_scene_backgrounds():
    """Create basic scene background images (400x300)"""
    bg_dir = Path("game_assets/backgrounds")
    bg_dir.mkdir(parents=True, exist_ok=True)
    
    # Scene background configurations
    scene_configs = {
        'cave_entrance': {
            'gradient_start': (40, 20, 10),    # Dark brown
            'gradient_end': (80, 60, 40),      # Light brown
            'accent_color': (160, 140, 120),    # Tan
            'description': 'Rocky cave entrance'
        },
        'skull_chamber': {
            'gradient_start': (20, 20, 40),    # Dark blue-gray
            'gradient_end': (60, 40, 40),      # Reddish gray
            'accent_color': (100, 80, 80),      # Light gray-red
            'description': 'Ominous chamber'
        },
        'primitive_village': {
            'gradient_start': (40, 60, 20),    # Dark green
            'gradient_end': (80, 120, 60),     # Light green
            'accent_color': (120, 80, 40),      # Brown (huts)
            'description': 'Village with huts'
        },
        'menu': {
            'gradient_start': (20, 10, 40),    # Dark purple
            'gradient_end': (60, 40, 80),      # Light purple
            'accent_color': (200, 180, 120),    # Gold
            'description': 'Main menu background'
        }
    }
    
    print("🖼️ Creating scene backgrounds...")
    
    for scene_name, config in scene_configs.items():
        # Create 400x300 background
        img = Image.new('RGB', (400, 300))
        draw = ImageDraw.Draw(img)
        
        # Create vertical gradient
        for y in range(300):
            ratio = y / 300
            r = int(config['gradient_start'][0] * (1-ratio) + config['gradient_end'][0] * ratio)
            g = int(config['gradient_start'][1] * (1-ratio) + config['gradient_end'][1] * ratio)
            b = int(config['gradient_start'][2] * (1-ratio) + config['gradient_end'][2] * ratio)
            draw.line([(0, y), (400, y)], fill=(r, g, b))
        
        # Add simple environmental details
        if scene_name == 'cave_entrance':
            # Add rock formations
            draw.ellipse([50, 200, 150, 280], fill=config['accent_color'])
            draw.ellipse([250, 180, 350, 270], fill=config['accent_color'])
            
        elif scene_name == 'skull_chamber':
            # Add mysterious shapes
            draw.rectangle([150, 100, 250, 200], fill=config['accent_color'])
            draw.ellipse([170, 120, 230, 180], fill=config['gradient_start'])
            
        elif scene_name == 'primitive_village':
            # Add hut shapes
            draw.rectangle([80, 200, 140, 260], fill=config['accent_color'])
            draw.polygon([(80, 200), (110, 160), (140, 200)], fill=(100, 60, 20))
            draw.rectangle([260, 190, 320, 250], fill=config['accent_color'])
            draw.polygon([(260, 190), (290, 150), (320, 190)], fill=(100, 60, 20))
            
        elif scene_name == 'menu':
            # Add decorative elements
            draw.ellipse([50, 50, 100, 100], outline=config['accent_color'], width=3)
            draw.ellipse([300, 200, 350, 250], outline=config['accent_color'], width=3)
        
        # Save background
        bg_path = bg_dir / f"{scene_name}.png"
        img.save(bg_path)
        print(f"  ✅ Created {scene_name} background: {bg_path}")
    
    return len(scene_configs)

def create_game_icon():
    """Create a simple game icon"""
    icon_dir = Path("game_assets/icons")
    icon_dir.mkdir(parents=True, exist_ok=True)
    
    # Create 64x64 icon
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Mountain/cave shape
    draw.polygon([(10, 50), (32, 10), (54, 50)], fill='#8B4513')  # Brown mountain
    draw.ellipse([20, 35, 44, 55], fill='#000000')  # Cave opening
    
    # Border
    draw.polygon([(10, 50), (32, 10), (54, 50)], outline='#000000', width=2)
    
    # Save icon
    icon_path = icon_dir / "shabuya_icon.png"
    img.save(icon_path)
    print(f"  ✅ Created game icon: {icon_path}")
    
    # Also create Windows ICO format
    try:
        img.save(icon_dir / "shabuya_icon.ico", format='ICO', sizes=[(32, 32), (64, 64)])
        print(f"  ✅ Created ICO format: {icon_dir}/shabuya_icon.ico")
    except:
        print("  ⚠️ Could not create ICO format (PIL limitation)")
    
    return True

def create_asset_manifest():
    """Create a manifest of all created assets"""
    manifest = {
        "asset_creation_info": {
            "created_date": "2025-08-25",
            "style": "Simple Programmer Art",
            "resolution": "64x64 sprites, 400x300 backgrounds",
            "format": "PNG with transparency support"
        },
        "sprites": {
            "warrior_sprite.png": "Tank class - brown/gold color scheme",
            "rogue_sprite.png": "Agility class - green color scheme", 
            "mage_sprite.png": "Magic class - purple color scheme",
            "enemy_sprite.png": "Generic enemy - red color scheme"
        },
        "backgrounds": {
            "cave_entrance.png": "Rocky entrance with stone formations",
            "skull_chamber.png": "Dark mysterious chamber",
            "primitive_village.png": "Village with hut structures",
            "menu.png": "Main menu decorative background"
        },
        "icons": {
            "shabuya_icon.png": "Game icon - mountain with cave opening",
            "shabuya_icon.ico": "Windows format game icon"
        },
        "usage_notes": [
            "All sprites are 64x64 PNG with transparency",
            "All backgrounds are 400x300 PNG without transparency",
            "Colors chosen for good contrast and readability",
            "Assets can be easily replaced with higher quality art later",
            "Compatible with enhanced_gui_system.py loading functions"
        ]
    }
    
    import json
    manifest_path = Path("game_assets/asset_manifest.json")
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"📋 Created asset manifest: {manifest_path}")
    return manifest_path

def main():
    """Create all basic graphics assets"""
    print("🎨 SHABUYA Cave Adventure - Basic Graphics Creator")
    print("=" * 60)
    
    try:
        # Create all asset types
        sprite_count = create_character_sprites()
        bg_count = create_scene_backgrounds()
        icon_created = create_game_icon()
        manifest_path = create_asset_manifest()
        
        print("\n" + "=" * 60)
        print("✅ GRAPHICS CREATION COMPLETE!")
        print(f"📊 Summary:")
        print(f"  • {sprite_count} character sprites created")
        print(f"  • {bg_count} scene backgrounds created")
        print(f"  • Game icon created: {icon_created}")
        print(f"  • Asset manifest: {manifest_path}")
        
        print(f"\n🎮 Next Steps:")
        print(f"  1. Test enhanced GUI: python enhanced_gui_system.py")
        print(f"  2. View assets in: game_assets/ directory")
        print(f"  3. Replace with better art as needed")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating graphics: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    main()
