#!/usr/bin/env python3
"""
Quick verification script to check asset replacement tool options
"""

def check_asset_options():
    """Display what the asset tool should show"""
    print("🔍 EXPECTED CHARACTER SPRITE OPTIONS:")
    print("=== PLAYER CHARACTERS ===")
    print("- warrior")
    print("- rogue")
    print("- mage")
    print("=== ENEMIES ===")
    print("- enemy (generic)")
    print("- alley_creature")
    print("- divine_heart")
    print("- primitive_creature")
    print("- cave_guardian")
    
    print("\n🔍 EXPECTED SCENE BACKGROUND OPTIONS:")
    print("=== CURRENT SCENES ===")
    print("- cave_entrance")
    print("- skull_chamber")
    print("- primitive_village")
    print("- menu")
    print("=== MISSING SCENES (High Priority) ===")
    print("- alley")
    print("- armory")
    print("- chief_house")
    print("- healing_pool")
    print("- village_changed")
    
    # Check if replace_assets.py has the correct content
    try:
        with open("replace_assets.py", "r") as f:
            content = f.read()
            
        if "alley_creature" in content:
            print("\n✅ replace_assets.py contains new enemy options!")
        else:
            print("\n❌ replace_assets.py missing new enemy options!")
            
        if "village_changed" in content:
            print("✅ replace_assets.py contains new scene options!")
        else:
            print("❌ replace_assets.py missing new scene options!")
            
    except FileNotFoundError:
        print("\n❌ replace_assets.py not found!")

if __name__ == "__main__":
    check_asset_options()
