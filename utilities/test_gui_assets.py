#!/usr/bin/env python3
"""
Quick test to verify GUI asset loading
"""

import sys
import os
sys.path.append('/workspaces/cave-game')

try:
    import tkinter as tk
    from enhanced_gui_system import EnhancedGameGUI
    
    print("🧪 Testing Enhanced GUI Asset Loading...")
    
    # Create test GUI instance
    root = tk.Tk()
    root.withdraw()  # Hide the window
    
    gui = EnhancedGameGUI(root)
    gui.setup_graphics()
    
    print(f"\n📊 RESULTS:")
    print(f"Character Sprites Loaded: {len(gui.character_sprites)}")
    print("Sprites:")
    for name in sorted(gui.character_sprites.keys()):
        print(f"  ✅ {name}")
    
    print(f"\nScene Backgrounds Loaded: {len(gui.background_images)}")
    print("Backgrounds:")
    for name in sorted(gui.background_images.keys()):
        print(f"  ✅ {name}")
    
    # Check for expected counts
    expected_sprites = 6  # warrior, rogue, mage, primitive_creature, divine_heart, cave_guardian
    expected_backgrounds = 9  # all 9 scenes
    
    if len(gui.character_sprites) == expected_sprites:
        print(f"\n✅ CHARACTER SPRITES: Perfect! {expected_sprites}/{expected_sprites}")
    else:
        print(f"\n⚠️ CHARACTER SPRITES: {len(gui.character_sprites)}/{expected_sprites} (missing some)")
    
    if len(gui.background_images) == expected_backgrounds:
        print(f"✅ SCENE BACKGROUNDS: Perfect! {expected_backgrounds}/{expected_backgrounds}")
    else:
        print(f"⚠️ SCENE BACKGROUNDS: {len(gui.background_images)}/{expected_backgrounds} (missing some)")
    
    root.destroy()
    print("\n🎉 Test completed!")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
