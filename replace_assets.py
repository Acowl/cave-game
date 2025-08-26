#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Asset Replacement Helper
Easy workflow for replacing placeholder graphics with AI-generated assets
"""

import os
import shutil
from pathlib import Path
from PIL import Image

def validate_and_resize_image(image_path, target_size, output_path):
    """Validate and resize image to exact target size"""
    try:
        with Image.open(image_path) as img:
            print(f"  Original size: {img.size}")
            
            # Resize to exact target size
            resized = img.resize(target_size, Image.Resampling.LANCZOS)
            
            # Ensure RGBA for sprites (transparency support)
            if target_size == (64, 64):
                resized = resized.convert('RGBA')
            else:
                resized = resized.convert('RGB')
            
            # Save to target location
            resized.save(output_path)
            print(f"  ✅ Saved as: {output_path}")
            return True
            
    except Exception as e:
        print(f"  ❌ Error processing {image_path}: {e}")
        return False

def replace_character_sprite(sprite_name, new_image_path):
    """Replace a character sprite with AI-generated version"""
    print(f"\n🧙 Replacing {sprite_name} sprite...")
    
    # Define target path
    target_path = Path(f"game_assets/sprites/{sprite_name}_sprite.png")
    
    # Create backup
    if target_path.exists():
        backup_path = Path(f"game_assets/sprites/backup_{sprite_name}_sprite.png")
        shutil.copy2(target_path, backup_path)
        print(f"  💾 Backed up original to: {backup_path}")
    
    # Process and replace
    success = validate_and_resize_image(new_image_path, (64, 64), target_path)
    
    if success:
        print(f"  🎉 {sprite_name} sprite updated successfully!")
        return True
    return False

def replace_scene_background(scene_name, new_image_path):
    """Replace a scene background with AI-generated version"""
    print(f"\n🏔️  Replacing {scene_name} background...")
    
    # Define target path
    target_path = Path(f"game_assets/backgrounds/{scene_name}.png")
    
    # Create backup
    if target_path.exists():
        backup_path = Path(f"game_assets/backgrounds/backup_{scene_name}.png")
        shutil.copy2(target_path, backup_path)
        print(f"  💾 Backed up original to: {backup_path}")
    
    # Process and replace
    success = validate_and_resize_image(new_image_path, (400, 300), target_path)
    
    if success:
        print(f"  🎉 {scene_name} background updated successfully!")
        return True
    return False

def test_updated_assets():
    """Test the updated assets in the enhanced GUI"""
    print(f"\n🧪 Testing updated assets...")
    
    try:
        import tkinter as tk
        from enhanced_gui_system import EnhancedGameGUI
        
        print("  Creating test window...")
        root = tk.Tk()
        root.title("SHABUYA - Asset Test")
        root.geometry("700x500")
        
        gui = EnhancedGameGUI(root)
        gui.setup_graphics()
        
        # Show asset counts
        sprite_count = len(gui.character_sprites)
        bg_count = len(gui.background_images)
        
        print(f"  ✅ Loaded {sprite_count} character sprites")
        print(f"  ✅ Loaded {bg_count} backgrounds")
        
        # Add test interface
        tk.Label(root, text="🎨 Updated Assets Test", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        tk.Label(root, text=f"Sprites: {sprite_count} | Backgrounds: {bg_count}",
                font=("Arial", 12)).pack()
        
        tk.Button(root, text="Open Graphics Demo", 
                 command=gui.create_demo_graphics_test,
                 bg="#8B4513", fg="white", font=("Arial", 12)).pack(pady=20)
        
        tk.Button(root, text="Close Test", 
                 command=root.destroy,
                 bg="#654321", fg="white", font=("Arial", 12)).pack()
        
        print("  🖥️  Test window opened - check the graphics!")
        root.mainloop()
        
        return True
        
    except Exception as e:
        print(f"  ❌ Asset test failed: {e}")
        return False

def interactive_asset_replacement():
    """Interactive workflow for replacing assets"""
    print("🎨 " + "=" * 60)
    print("🎨 SHABUYA ASSET REPLACEMENT WORKFLOW")
    print("🎨 " + "=" * 60)
    
    print("\n📋 WORKFLOW STEPS:")
    print("1. Generate AI images using the prompts in AI_IMAGE_PROMPTS.md")
    print("2. Save images to a temporary folder on your computer")
    print("3. Use this script to replace the placeholder assets")
    print("4. Test the updated graphics in the enhanced GUI")
    
    while True:
        print("\n🎯 REPLACEMENT OPTIONS:")
        print("1. Replace character sprite")
        print("2. Replace scene background")  
        print("3. Test updated assets")
        print("4. View current assets")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            print("\nAvailable character sprites:")
            print("=== PLAYER CHARACTERS ===")
            print("- warrior")
            print("- rogue")
            print("- mage")
            print("=== ENEMIES ===")
            print("- enemy (generic)")
            print("- primitive_creature")
            print("- divine_heart")
            print("- cave_guardian")
            
            sprite_name = input("Enter sprite name: ").strip().lower()
            valid_sprites = ["warrior", "rogue", "mage", "enemy", "primitive_creature", 
                           "divine_heart", "cave_guardian"]
            
            if sprite_name in valid_sprites:
                image_path = input("Enter path to your AI-generated sprite image: ").strip()
                if os.path.exists(image_path):
                    replace_character_sprite(sprite_name, image_path)
                else:
                    print("❌ Image file not found!")
            else:
                print("❌ Invalid sprite name!")
                
        elif choice == "2":
            print("\nAvailable scene backgrounds:")
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
            
            scene_name = input("Enter scene name: ").strip().lower()
            valid_scenes = ["cave_entrance", "skull_chamber", "primitive_village", "menu",
                          "alley", "armory", "chief_house", "healing_pool", "village_changed"]
            
            if scene_name in valid_scenes:
                image_path = input("Enter path to your AI-generated background image: ").strip()
                if os.path.exists(image_path):
                    replace_scene_background(scene_name, image_path)
                else:
                    print("❌ Image file not found!")
            else:
                print("❌ Invalid scene name!")
                
        elif choice == "3":
            test_updated_assets()
            
        elif choice == "4":
            print(f"\n📁 Current assets:")
            sprites_dir = Path("game_assets/sprites")
            if sprites_dir.exists():
                print("  Character sprites:")
                for sprite in sprites_dir.glob("*_sprite.png"):
                    print(f"    - {sprite.name}")
            
            bg_dir = Path("game_assets/backgrounds")  
            if bg_dir.exists():
                print("  Scene backgrounds:")
                for bg in bg_dir.glob("*.png"):
                    print(f"    - {bg.name}")
                    
        elif choice == "5":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    interactive_asset_replacement()
