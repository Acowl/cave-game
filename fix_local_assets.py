#!/usr/bin/env python3
"""
Fix Local Asset Issues - Run this to sync your local assets with the repository
"""

import os
from pathlib import Path
import shutil

def fix_local_assets():
    print("🔧 FIXING LOCAL ASSET ISSUES")
    print("=" * 50)
    
    # Check current directory
    if not Path("game_assets").exists():
        print("❌ Error: Not in cave-game directory")
        print("Please run this script from your cave-game folder")
        return
    
    print("1️⃣ REMOVING OLD ENEMY SPRITE")
    print("-" * 30)
    
    enemy_sprite_path = Path("game_assets/sprites/enemy_sprite.png")
    if enemy_sprite_path.exists():
        print(f"🗑️  Removing old enemy_sprite.png...")
        enemy_sprite_path.unlink()
        print("✅ enemy_sprite.png deleted")
    else:
        print("✅ enemy_sprite.png already removed")
    
    print("\n2️⃣ CHECKING SPRITE FILES")
    print("-" * 30)
    
    sprites_dir = Path("game_assets/sprites")
    expected_sprites = [
        "warrior_sprite.png",
        "rogue_sprite.png", 
        "mage_sprite.png",
        "primitive_creature_sprite.png",
        "divine_heart_sprite.png",
        "cave_guardian_sprite.png"
    ]
    
    for sprite in expected_sprites:
        sprite_path = sprites_dir / sprite
        status = "✅ EXISTS" if sprite_path.exists() else "❌ MISSING"
        print(f"   {sprite}: {status}")
    
    print("\n3️⃣ CHECKING BACKGROUND FILES")
    print("-" * 30)
    
    backgrounds_dir = Path("game_assets/backgrounds")
    expected_backgrounds = [
        "cave_entrance.png",
        "skull_chamber.png", 
        "primitive_village.png",
        "menu.png",
        "alley.png",
        "armory.png", 
        "chief_house.png",
        "healing_pool.png",
        "village_changed.png"
    ]
    
    missing_backgrounds = []
    for bg in expected_backgrounds:
        bg_path = backgrounds_dir / bg
        if bg_path.exists():
            print(f"   {bg}: ✅ EXISTS")
        else:
            print(f"   {bg}: ❌ MISSING")
            missing_backgrounds.append(bg)
    
    if missing_backgrounds:
        print(f"\n4️⃣ CREATING MISSING BACKGROUNDS")
        print("-" * 30)
        create_missing_backgrounds(backgrounds_dir, missing_backgrounds)
    
    print("\n5️⃣ FINAL ASSET COUNT")
    print("-" * 30)
    
    sprite_count = len(list(sprites_dir.glob("*.png")))
    bg_count = len(list(backgrounds_dir.glob("*.png")))
    
    print(f"📊 Sprites: {sprite_count}/6 {'✅' if sprite_count == 6 else '❌'}")
    print(f"📊 Backgrounds: {bg_count}/9 {'✅' if bg_count == 9 else '❌'}")
    
    if sprite_count == 6 and bg_count == 9:
        print("\n🎉 LOCAL ASSETS FIXED!")
        print("Now run: python gui_diagnostic.py")
    else:
        print("\n⚠️  Some issues remain - check the output above")

def create_missing_backgrounds(bg_dir, missing_list):
    """Create placeholder backgrounds for missing scenes"""
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        bg_configs = {
            'alley': [(15, 15, 15), (35, 35, 35)], # Dark grey gradient
            'armory': [(30, 30, 40), (50, 50, 60)], # Blue-grey
            'chief_house': [(40, 25, 10), (60, 45, 30)], # Brown hut
            'healing_pool': [(10, 30, 50), (30, 50, 70)], # Blue healing
            'village_changed': [(25, 15, 35), (45, 35, 55)], # Purple mystical
            'cave_entrance': [(20, 10, 5), (60, 40, 20)],  # Brown gradient
            'skull_chamber': [(40, 20, 20), (20, 10, 10)], # Dark red
            'primitive_village': [(10, 40, 10), (30, 60, 30)], # Green
            'menu': [(10, 10, 20), (30, 20, 40)] # Purple
        }
        
        scene_labels = {
            'alley': 'ALLEY SCENE',
            'armory': 'ARMORY SCENE', 
            'chief_house': 'CHIEF HOUSE',
            'healing_pool': 'HEALING POOL',
            'village_changed': 'VILLAGE CHANGED',
            'cave_entrance': 'CAVE ENTRANCE',
            'skull_chamber': 'SKULL CHAMBER',
            'primitive_village': 'PRIMITIVE VILLAGE',
            'menu': 'MAIN MENU'
        }
        
        for bg_name in missing_list:
            print(f"   🎨 Creating {bg_name}...")
            
            if bg_name in bg_configs:
                colors = bg_configs[bg_name]
                img = Image.new('RGB', (400, 300))
                draw = ImageDraw.Draw(img)
                
                # Create gradient
                start_color, end_color = colors
                for y in range(300):
                    ratio = y / 299.0
                    r = int(start_color[0] + ratio * (end_color[0] - start_color[0]))
                    g = int(start_color[1] + ratio * (end_color[1] - start_color[1]))
                    b = int(start_color[2] + ratio * (end_color[2] - start_color[2]))
                    draw.line([(0, y), (400, y)], fill=(r, g, b))
                
                # Add text label
                if bg_name in scene_labels:
                    text = scene_labels[bg_name]
                    try:
                        font = ImageFont.truetype("arial.ttf", 24)
                        bbox = draw.textbbox((0, 0), text, font=font)
                    except:
                        font = ImageFont.load_default()
                        bbox = draw.textbbox((0, 0), text, font=font)
                    
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]
                    x = (400 - text_width) // 2
                    y = (300 - text_height) // 2
                    
                    # Add shadow
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx != 0 or dy != 0:
                                draw.text((x+dx, y+dy), text, fill='black', font=font)
                    draw.text((x, y), text, fill='white', font=font)
                
                img.save(bg_dir / f"{bg_name}.png")
                print(f"     ✅ {bg_name}.png created")
            
    except ImportError:
        print("   ⚠️  PIL not available - creating simple placeholder files")
        for bg_name in missing_list:
            placeholder_path = bg_dir / f"{bg_name}.png"
            # Create empty file as placeholder
            placeholder_path.touch()
            print(f"     📝 {bg_name}.png placeholder created")

if __name__ == "__main__":
    fix_local_assets()
