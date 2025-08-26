#!/usr/bin/env python3
"""
Comprehensive GUI Asset Diagnostic - Run this locally to debug GUI issues
"""

import tkinter as tk
import sys
from pathlib import Path

def main():
    print("🔍 SHABUYA GUI ASSET DIAGNOSTIC")
    print("=" * 60)
    
    # Test 1: Check file system assets
    print("\n1️⃣ CHECKING FILE SYSTEM ASSETS")
    print("-" * 40)
    
    sprite_dir = Path("game_assets/sprites")
    print(f"📁 Sprite directory: {sprite_dir}")
    print(f"   Exists: {sprite_dir.exists()}")
    
    if sprite_dir.exists():
        sprite_files = list(sprite_dir.glob("*.png"))
        print(f"   Sprite files found: {len(sprite_files)}")
        for sprite in sorted(sprite_files):
            print(f"     - {sprite.name}")
    
    bg_dir = Path("game_assets/backgrounds")
    print(f"\n📁 Background directory: {bg_dir}")
    print(f"   Exists: {bg_dir.exists()}")
    
    if bg_dir.exists():
        bg_files = list(bg_dir.glob("*.png"))
        print(f"   Background files found: {len(bg_files)}")
        for bg in sorted(bg_files):
            print(f"     - {bg.name}")
    
    # Test 2: Import and create GUI instance
    print("\n2️⃣ TESTING GUI IMPORT AND INITIALIZATION")
    print("-" * 40)
    
    try:
        from enhanced_gui_system import EnhancedGameGUI
        print("✅ Enhanced GUI system imported successfully")
    except ImportError as e:
        print(f"❌ Enhanced GUI import failed: {e}")
        return
    
    # Test 3: Create GUI instance and check asset loading
    print("\n3️⃣ CREATING GUI INSTANCE AND LOADING ASSETS")
    print("-" * 40)
    
    try:
        # Create root window
        root = tk.Tk()
        root.title("SHABUYA Asset Diagnostic")
        root.geometry("800x600")
        
        # Create GUI instance
        print("Creating Enhanced GUI instance...")
        gui = EnhancedGameGUI(root)
        
        # Check what was actually loaded
        print(f"\n📊 ASSET LOADING RESULTS:")
        print(f"   Graphics system loaded: {gui.graphics_loaded}")
        print(f"   Character sprites loaded: {len(gui.character_sprites)}")
        
        if gui.character_sprites:
            print("   Loaded sprites:")
            for sprite_name in sorted(gui.character_sprites.keys()):
                print(f"     ✅ {sprite_name}")
        
        print(f"   Background images loaded: {len(gui.background_images)}")
        if gui.background_images:
            print("   Loaded backgrounds:")
            for bg_name in sorted(gui.background_images.keys()):
                print(f"     ✅ {bg_name}")
        
        # Test 4: Check for any issues
        print(f"\n4️⃣ DIAGNOSTIC CHECKS")
        print("-" * 40)
        
        # Check if old enemy sprite is somehow still loaded
        if 'enemy' in gui.character_sprites:
            print("   ❌ Generic 'enemy' sprite found - THIS SHOULD NOT EXIST")
        else:
            print("   ✅ No generic 'enemy' sprite found")
        
        # Check expected counts
        expected_sprites = 6  # warrior, rogue, mage, primitive_creature, divine_heart, cave_guardian
        expected_backgrounds = 9  # all 9 scene backgrounds
        
        if len(gui.character_sprites) == expected_sprites:
            print(f"   ✅ Correct number of sprites ({expected_sprites})")
        else:
            print(f"   ⚠️  Expected {expected_sprites} sprites, got {len(gui.character_sprites)}")
        
        if len(gui.background_images) == expected_backgrounds:
            print(f"   ✅ Correct number of backgrounds ({expected_backgrounds})")
        else:
            print(f"   ⚠️  Expected {expected_backgrounds} backgrounds, got {len(gui.background_images)}")
        
        # Test 5: Create a test window to visually inspect
        print(f"\n5️⃣ VISUAL TEST WINDOW")
        print("-" * 40)
        print("Creating visual test window...")
        print("Check the window that opens to see:")
        print("- Character sprites (should be 6 colored circles, no red enemy)")
        print("- Background cycling (should show all 9 backgrounds)")
        print("Close the window when done inspecting.")
        
        # Create visual test panel
        test_frame = tk.Frame(root, bg='white')
        test_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(test_frame, text="SHABUYA Asset Visual Test", 
                              font=('Arial', 16, 'bold'), bg='white')
        title_label.pack(pady=(0, 20))
        
        # Sprite test section
        sprite_frame = tk.Frame(test_frame, bg='white')
        sprite_frame.pack(fill=tk.X, pady=(0, 20))
        
        sprite_title = tk.Label(sprite_frame, text="Character Sprites:", 
                               font=('Arial', 12, 'bold'), bg='white')
        sprite_title.pack()
        
        sprite_display = tk.Frame(sprite_frame, bg='white')
        sprite_display.pack()
        
        # Display all loaded sprites
        for i, (sprite_name, sprite_img) in enumerate(gui.character_sprites.items()):
            sprite_container = tk.Frame(sprite_display, bg='white')
            sprite_container.pack(side=tk.LEFT, padx=10)
            
            sprite_label = tk.Label(sprite_container, image=sprite_img, bg='white')
            sprite_label.pack()
            
            name_label = tk.Label(sprite_container, text=sprite_name, 
                                 font=('Arial', 8), bg='white')
            name_label.pack()
        
        # Background test section
        bg_frame = tk.Frame(test_frame, bg='white')
        bg_frame.pack(fill=tk.BOTH, expand=True)
        
        bg_title = tk.Label(bg_frame, text="Background Images:", 
                           font=('Arial', 12, 'bold'), bg='white')
        bg_title.pack()
        
        # Background display canvas
        bg_canvas = tk.Canvas(bg_frame, width=400, height=300, bg='gray')
        bg_canvas.pack(pady=10)
        
        # Background cycling
        bg_names = list(gui.background_images.keys())
        current_bg_index = 0
        
        def cycle_background():
            nonlocal current_bg_index
            if bg_names and current_bg_index < len(bg_names):
                bg_name = bg_names[current_bg_index]
                bg_img = gui.background_images[bg_name]
                bg_canvas.delete("all")
                bg_canvas.create_image(200, 150, image=bg_img)
                bg_canvas.create_text(200, 280, text=f"{bg_name} ({current_bg_index + 1}/{len(bg_names)})",
                                     fill='white', font=('Arial', 12, 'bold'))
                current_bg_index = (current_bg_index + 1) % len(bg_names)
            root.after(2000, cycle_background)  # Change every 2 seconds
        
        # Start background cycling
        cycle_background()
        
        # Instructions
        instructions = tk.Label(test_frame, 
                               text="Backgrounds will cycle automatically. Close window when done.",
                               font=('Arial', 10), bg='white')
        instructions.pack(pady=(10, 0))
        
        print("\n✅ DIAGNOSTIC COMPLETE - Check the visual test window!")
        print("Report back what you see:")
        print("1. How many character sprites are shown?")
        print("2. Are any of them red circles?")
        print("3. How many different backgrounds cycle through?")
        print("4. Do all 9 backgrounds appear?")
        
        # Start the GUI
        root.mainloop()
        
    except Exception as e:
        print(f"❌ GUI creation failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
