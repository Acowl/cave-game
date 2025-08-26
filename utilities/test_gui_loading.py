#!/usr/bin/env python3
"""
Direct test of Enhanced GUI asset loading
Run this from the utilities directory
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

def test_enhanced_gui_loading():
    """Test the enhanced GUI loading without display"""
    
    print("🔍 Testing Enhanced GUI Asset Loading Logic...")
    
    # Import the GUI class
    try:
        from enhanced_gui_system import EnhancedGameGUI
        print("✅ Successfully imported EnhancedGameGUI")
    except ImportError as e:
        print(f"❌ Failed to import EnhancedGameGUI: {e}")
        return
    
    # Test the loading logic without tkinter
    class MockGUI:
        def __init__(self):
            self.character_sprites = {}
            self.background_images = {}
            
        def setup_graphics(self):
            # Simulate the loading process
            self.load_character_sprites()
            self.load_background_images()
            
        def load_character_sprites(self):
            """Simulate sprite loading logic"""
            sprite_dir = Path("../game_assets/sprites")
            
            sprite_files = {
                'warrior': 'warrior_sprite.png',
                'rogue': 'rogue_sprite.png', 
                'mage': 'mage_sprite.png',
                'primitive_creature': 'primitive_creature_sprite.png',
                'divine_heart': 'divine_heart_sprite.png',
                'cave_guardian': 'cave_guardian_sprite.png'
            }
            
            for sprite_name, filename in sprite_files.items():
                sprite_path = sprite_dir / filename
                if sprite_path.exists():
                    self.character_sprites[sprite_name] = f"mock_{sprite_name}"
                    print(f"  ✅ Would load sprite: {sprite_name}")
                else:
                    print(f"  ❌ Missing sprite: {sprite_name} ({filename})")
            
        def load_background_images(self):
            """Simulate background loading logic"""
            bg_dir = Path("../game_assets/backgrounds")
            
            background_files = {
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
            
            for bg_name, filename in background_files.items():
                bg_path = bg_dir / filename
                if bg_path.exists():
                    self.background_images[bg_name] = f"mock_{bg_name}"
                    print(f"  ✅ Would load background: {bg_name}")
                else:
                    print(f"  ❌ Missing background: {bg_name} ({filename})")
    
    # Test the mock loading
    print("\n🎮 Testing Asset Loading Logic...")
    mock_gui = MockGUI()
    mock_gui.setup_graphics()
    
    print(f"\n📊 Results:")
    print(f"Character Sprites: {len(mock_gui.character_sprites)}/6")
    print(f"Scene Backgrounds: {len(mock_gui.background_images)}/9")
    
    if len(mock_gui.character_sprites) == 6 and len(mock_gui.background_images) == 9:
        print("\n🎉 All assets should load correctly!")
    else:
        print("\n⚠️ Some assets missing - GUI won't load them all")

if __name__ == "__main__":
    test_enhanced_gui_loading()
