#!/usr/bin/env python3
"""
Test asset loading without GUI display
"""

import sys
from pathlib import Path
sys.path.append('/workspaces/cave-game')

def test_asset_files():
    """Test that all required asset files exist"""
    print("🧪 Testing Asset Files...")
    
    base_path = Path('/workspaces/cave-game')
    
    # Expected sprites (6 total - no more generic enemy)
    expected_sprites = [
        'warrior_sprite.png', 'rogue_sprite.png', 'mage_sprite.png',
        'primitive_creature_sprite.png', 'divine_heart_sprite.png', 'cave_guardian_sprite.png'
    ]
    
    # Expected backgrounds (9 total)
    expected_backgrounds = [
        'cave_entrance.png', 'skull_chamber.png', 'primitive_village.png', 'menu.png',
        'alley.png', 'armory.png', 'chief_house.png', 'healing_pool.png', 'village_changed.png'
    ]
    
    sprites_dir = base_path / 'game_assets' / 'sprites'
    backgrounds_dir = base_path / 'game_assets' / 'backgrounds'
    
    print(f"\n📊 CHARACTER SPRITES ({len(expected_sprites)} expected):")
    sprite_count = 0
    for sprite in expected_sprites:
        sprite_path = sprites_dir / sprite
        if sprite_path.exists():
            print(f"  ✅ {sprite}")
            sprite_count += 1
        else:
            print(f"  ❌ {sprite} - MISSING")
    
    print(f"\n📊 SCENE BACKGROUNDS ({len(expected_backgrounds)} expected):")
    background_count = 0
    for background in expected_backgrounds:
        bg_path = backgrounds_dir / background
        if bg_path.exists():
            print(f"  ✅ {background}")
            background_count += 1
        else:
            print(f"  ❌ {background} - MISSING")
    
    # Check for unwanted files
    print(f"\n🔍 CHECKING FOR UNWANTED FILES:")
    if (sprites_dir / 'enemy_sprite.png').exists():
        print("  ❌ enemy_sprite.png - SHOULD BE REMOVED")
    else:
        print("  ✅ enemy_sprite.png - correctly removed")
    
    print(f"\n📈 SUMMARY:")
    print(f"Character Sprites: {sprite_count}/{len(expected_sprites)}")
    print(f"Scene Backgrounds: {background_count}/{len(expected_backgrounds)}")
    
    if sprite_count == len(expected_sprites) and background_count == len(expected_backgrounds):
        print("🎉 All assets present and correct!")
        return True
    else:
        print("⚠️ Some assets missing or incorrect")
        return False

if __name__ == "__main__":
    test_asset_files()
