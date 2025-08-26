#!/usr/bin/env python3
"""
Diagnostic script to check what assets the enhanced GUI can actually see
"""

import sys
from pathlib import Path

def check_asset_loading():
    """Check what assets the enhanced GUI system can see"""
    print("🔍 ENHANCED GUI ASSET DIAGNOSTIC")
    print("=" * 50)
    
    # Check what the enhanced GUI sprite loading code would see
    sprite_dir = Path("game_assets/sprites")
    print(f"📁 Sprite directory: {sprite_dir}")
    print(f"   Exists: {sprite_dir.exists()}")
    
    if sprite_dir.exists():
        print("   Files found:")
        for sprite_file in sorted(sprite_dir.glob("*.png")):
            print(f"     - {sprite_file.name}")
    
    # Check what sprite files the enhanced GUI expects
    expected_sprites = {
        'warrior': 'warrior_sprite.png',
        'rogue': 'rogue_sprite.png', 
        'mage': 'mage_sprite.png',
        'primitive_creature': 'primitive_creature_sprite.png',
        'divine_heart': 'divine_heart_sprite.png',
        'cave_guardian': 'cave_guardian_sprite.png'
    }
    
    print(f"\n🎯 Expected sprite mapping:")
    for sprite_name, filename in expected_sprites.items():
        sprite_path = sprite_dir / filename
        status = "✅ EXISTS" if sprite_path.exists() else "❌ MISSING"
        print(f"   {sprite_name} -> {filename}: {status}")
    
    # Check backgrounds
    bg_dir = Path("game_assets/backgrounds")
    print(f"\n📁 Background directory: {bg_dir}")
    print(f"   Exists: {bg_dir.exists()}")
    
    if bg_dir.exists():
        print("   Files found:")
        for bg_file in sorted(bg_dir.glob("*.png")):
            print(f"     - {bg_file.name}")
    
    # Check what background files the enhanced GUI expects
    expected_backgrounds = {
        'cave_entrance': 'cave_entrance.png',
        'skull_chamber': 'skull_chamber.png',
        'primitive_village': 'primitive_village.png',
        'menu': 'menu.png',
        'alley': 'alley.png',
        'armory': 'armory.png',
        'chief_house': 'chief_house.png',
        'healing_pool': 'healing_pool.png',
        'village_changed': 'village_changed.png'
    }
    
    print(f"\n🎯 Expected background mapping:")
    for bg_name, filename in expected_backgrounds.items():
        bg_path = bg_dir / filename
        status = "✅ EXISTS" if bg_path.exists() else "❌ MISSING"
        print(f"   {bg_name} -> {filename}: {status}")
    
    # Check for any old enemy sprite files
    print(f"\n🔍 Checking for old enemy files:")
    old_enemy_path = sprite_dir / "enemy_sprite.png"
    if old_enemy_path.exists():
        print(f"   ❌ OLD enemy_sprite.png still exists - SHOULD BE REMOVED")
    else:
        print(f"   ✅ enemy_sprite.png correctly removed")
    
    # Check enhanced GUI system file
    gui_file = Path("enhanced_gui_system.py")
    print(f"\n📄 Enhanced GUI file: {gui_file}")
    print(f"   Exists: {gui_file.exists()}")
    if gui_file.exists():
        print(f"   Size: {gui_file.stat().st_size} bytes")
        print(f"   Modified: {gui_file.stat().st_mtime}")
    
    print(f"\n✅ Asset diagnostic complete!")

if __name__ == "__main__":
    check_asset_loading()
