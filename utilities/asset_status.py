#!/usr/bin/env python3
"""
Simple asset status check for users
"""

from pathlib import Path
import os

def check_asset_status():
    """Check current asset status from any directory"""
    
    # Find the project root (look for main.py)
    current_dir = Path.cwd()
    project_root = None
    
    # Check if we're already in project root
    if (current_dir / 'main.py').exists():
        project_root = current_dir
    # Check if we're in utilities subdirectory
    elif (current_dir.parent / 'main.py').exists():
        project_root = current_dir.parent
    # Search upward for project root
    else:
        check_dir = current_dir
        for _ in range(5):  # Don't search too far up
            if (check_dir / 'main.py').exists():
                project_root = check_dir
                break
            check_dir = check_dir.parent
    
    if not project_root:
        print("❌ Could not find SHABUYA project root directory")
        return
    
    print(f"🎮 SHABUYA Cave Adventure - Asset Status")
    print(f"📁 Project root: {project_root}")
    print("=" * 50)
    
    # Check sprites
    sprites_dir = project_root / 'game_assets' / 'sprites'
    print(f"\n👾 CHARACTER SPRITES:")
    
    expected_sprites = [
        ('warrior_sprite.png', '🛡️ Warrior'),
        ('rogue_sprite.png', '🗡️ Rogue'),
        ('mage_sprite.png', '🔮 Mage'),
        ('primitive_creature_sprite.png', '🦎 Primitive Creature'),
        ('divine_heart_sprite.png', '💜 Divine Heart Boss'),
        ('cave_guardian_sprite.png', '🗿 Cave Guardian')
    ]
    
    for filename, description in expected_sprites:
        path = sprites_dir / filename
        if path.exists():
            size_kb = round(path.stat().st_size / 1024, 1)
            print(f"  ✅ {description}: {size_kb}KB")
        else:
            print(f"  ❌ {description}: MISSING")
    
    # Check backgrounds  
    bg_dir = project_root / 'game_assets' / 'backgrounds'
    print(f"\n🏞️ SCENE BACKGROUNDS:")
    
    expected_backgrounds = [
        ('cave_entrance.png', '🕳️ Cave Entrance'),
        ('skull_chamber.png', '💀 Skull Chamber'), 
        ('primitive_village.png', '🏘️ Primitive Village'),
        ('menu.png', '🎮 Menu Background'),
        ('alley.png', '🏚️ Alley Scene'),
        ('armory.png', '⚔️ Armory'),
        ('chief_house.png', '🏠 Chief House'),
        ('healing_pool.png', '💧 Healing Pool'),
        ('village_changed.png', '🌟 Village Changed')
    ]
    
    for filename, description in expected_backgrounds:
        path = bg_dir / filename
        if path.exists():
            size_kb = round(path.stat().st_size / 1024, 1)
            print(f"  ✅ {description}: {size_kb}KB")
        else:
            print(f"  ❌ {description}: MISSING")
    
    print(f"\n🎯 NEXT STEPS:")
    print(f"1. Generate AI images using prompts from documentation/COMPLETE_ASSET_LIST.md")
    print(f"2. Navigate to utilities/: cd utilities/")
    print(f"3. Run replacement tool: python replace_assets.py") 
    print(f"4. Test your assets: select option 3 in the tool")

if __name__ == "__main__":
    check_asset_status()
