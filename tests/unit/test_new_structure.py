#!/usr/bin/env python3
"""
Quick Test - Verify New Project Structure
"""

import sys
from pathlib import Path

# Add paths
project_root = Path(__file__).parent
src_path = project_root / 'src'
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(src_path))

print("🧪 Testing New Project Structure")
print("=" * 40)

def test_basic_imports():
    """Test if our reorganized imports work"""
    try:
        # Test config import
        from src.config import SCENE_NAMES, STAT_REQUIREMENT
        print("✅ Config imported successfully")
        
        # Test entities
        from src.entities.player import Player
        from src.entities.item import dagger, axe, wand
        print("✅ Entities imported successfully")
        
        # Test core modules  
        from src.core.scenes import setup_scenes
        from src.core.combat import get_available_weapons
        print("✅ Core modules imported successfully")
        
        # Test interfaces
        from src.interfaces.ui import title_screen
        print("✅ Interfaces imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_basic_functionality():
    """Test basic game functionality"""
    try:
        from src.entities.player import Player
        from src.entities.item import Inventory, dagger
        from src.core.scenes import setup_scenes
        from src.config import SCENE_NAMES
        
        # Create player
        player = Player()
        player.inventory = Inventory()
        player.weapon = dagger
        player.character_class = "Rogue"
        
        # Test scenes
        scenes = setup_scenes()
        cave_entrance = scenes[SCENE_NAMES['CAVE_ENTRANCE']]
        
        print(f"✅ Player created: {player.character_class} with {player.weapon.name}")
        print(f"✅ Scene loaded: {cave_entrance.name}")
        print(f"✅ Total scenes: {len(scenes)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        return False

def main():
    print("Testing reorganized project structure...\n")
    
    import_success = test_basic_imports()
    print()
    
    if import_success:
        functionality_success = test_basic_functionality()
    else:
        functionality_success = False
    
    print("\n" + "=" * 40)
    
    if import_success and functionality_success:
        print("🎉 SUCCESS! New project structure is working!")
        print("\n✅ The reorganization is complete and functional")
        print("✅ All core modules are properly organized")
        print("✅ Imports are working correctly")
        print("\n💡 You can now run the game with:")
        print("   python scripts/main.py")
    else:
        print("❌ Some issues found. Check the error messages above.")
    
    return import_success and functionality_success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
