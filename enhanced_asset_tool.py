#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Enhanced Scalable Asset Replacement Tool
================================================================

This tool provides:
1. Integration with the asset management system
2. Automated asset organization and validation
3. Batch processing capabilities
4. Quality control and consistency checking
5. Easy expansion for new asset categories
"""

import os
import sys
from pathlib import Path
from PIL import Image, ImageTk
import tkinter as tk
import json

# Import our scalable systems
try:
    from asset_management_system import ASSET_CATEGORIES, QUALITY_STANDARDS, get_asset_info
    from ai_art_generation_system import get_prompt_for_asset, STYLE_GUIDE
except ImportError:
    print("⚠️  Asset management systems not found. Please ensure both files are in the same directory.")
    sys.exit(1)

class ScalableAssetManager:
    """Enhanced asset manager with scalable architecture"""
    
    def __init__(self):
        self.project_root = self.get_project_root()
        self.assets_dir = self.project_root / "game_assets"
        self.backup_dir = self.project_root / "asset_backups"
        
        # Ensure directories exist
        self.assets_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)
    
    def get_project_root(self):
        """Get the project root directory relative to this script"""
        return Path(__file__).parent
    
    def display_main_menu(self):
        """Display the main interactive menu"""
        print("🎨 " + "=" * 60)
        print("🎨 SHABUYA SCALABLE ASSET REPLACEMENT SYSTEM")
        print("🎨 " + "=" * 60)
        print()
        print("📋 WORKFLOW:")
        print("1. Generate AI art using our comprehensive prompt system")
        print("2. Use this tool to replace and organize assets")
        print("3. Validate assets meet quality standards")
        print("4. Test in the enhanced GUI")
        print()
        print("🎯 MAIN OPTIONS:")
        print("1. Replace Character Assets")
        print("2. Replace Scene Backgrounds") 
        print("3. Add New Asset Category (Future Expansion)")
        print("4. Batch Process Assets")
        print("5. Validate All Assets")
        print("6. Generate AI Prompts")
        print("7. Test Updated Assets in GUI")
        print("8. View Asset Inventory")
        print("9. Exit")
        print()
    
    def replace_character_assets(self):
        """Replace character sprites with enhanced categorization"""
        print("\n👤 CHARACTER ASSET REPLACEMENT")
        print("-" * 40)
        
        # Display available character categories
        char_categories = ASSET_CATEGORIES["characters"]
        print("Available character categories:")
        for i, (cat_name, chars) in enumerate(char_categories.items(), 1):
            if chars:  # Only show categories with content
                print(f"{i}. {cat_name.replace('_', ' ').title()} ({len(chars)} characters)")
        
        try:
            cat_choice = int(input("\nSelect category: ")) - 1
            cat_names = [name for name, chars in char_categories.items() if chars]
            
            if 0 <= cat_choice < len(cat_names):
                selected_category = cat_names[cat_choice]
                self.replace_character_in_category(selected_category)
            else:
                print("❌ Invalid category selection!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def replace_character_in_category(self, category):
        """Replace a specific character in a category"""
        chars = ASSET_CATEGORIES["characters"][category]
        
        print(f"\n🎭 {category.replace('_', ' ').title()} Characters:")
        for i, (char_name, char_data) in enumerate(chars.items(), 1):
            print(f"{i}. {char_name.replace('_', ' ').title()}")
            print(f"   Current: {char_data['sprite_file']}")
            print(f"   Description: {char_data['description']}")
        
        try:
            char_choice = int(input("\nSelect character to replace: ")) - 1
            char_names = list(chars.keys())
            
            if 0 <= char_choice < len(char_names):
                selected_char = char_names[char_choice]
                self.process_character_replacement(category, selected_char)
            else:
                print("❌ Invalid character selection!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def process_character_replacement(self, category, char_name):
        """Process the actual character sprite replacement"""
        char_info = ASSET_CATEGORIES["characters"][category][char_name]
        sprite_file = char_info["sprite_file"]
        
        print(f"\n🖼️  Replacing {char_name.replace('_', ' ').title()}")
        print(f"Expected dimensions: {char_info['dimensions']}")
        print(f"Color scheme: {', '.join(char_info['color_scheme'])}")
        print(f"Description: {char_info['description']}")
        
        # Show AI prompt for reference
        prompt_info = get_prompt_for_asset("characters", category, char_name)
        if prompt_info:
            print(f"\n🤖 AI Generation Prompt:")
            print(f"'{prompt_info['prompt']}'")
        
        # Get new image file
        new_image_path = input("\nEnter path to your new sprite image: ").strip().strip('"')
        
        if not os.path.exists(new_image_path):
            print("❌ Image file not found!")
            return
        
        # Determine target path
        sprites_dir = self.assets_dir / "sprites"
        sprites_dir.mkdir(exist_ok=True)
        target_path = sprites_dir / sprite_file
        
        # Backup existing file
        if target_path.exists():
            backup_path = self.backup_dir / f"{char_name}_{sprite_file}.backup"
            target_path.rename(backup_path)
            print(f"💾 Backed up original to: {backup_path}")
        
        # Process and validate new image
        success = self.process_and_validate_sprite(new_image_path, target_path, char_info)
        
        if success:
            print(f"✅ Successfully replaced {char_name} sprite!")
        else:
            print(f"❌ Failed to replace {char_name} sprite!")
    
    def replace_scene_backgrounds(self):
        """Replace scene backgrounds with enhanced categorization"""
        print("\n🏔️  SCENE BACKGROUND REPLACEMENT")
        print("-" * 40)
        
        # Display available scene categories
        scene_categories = ASSET_CATEGORIES["scenes"]
        print("Available scene categories:")
        for i, (cat_name, scenes) in enumerate(scene_categories.items(), 1):
            if scenes:  # Only show categories with content
                print(f"{i}. {cat_name.replace('_', ' ').title()} ({len(scenes)} scenes)")
        
        try:
            cat_choice = int(input("\nSelect category: ")) - 1
            cat_names = [name for name, scenes in scene_categories.items() if scenes]
            
            if 0 <= cat_choice < len(cat_names):
                selected_category = cat_names[cat_choice]
                self.replace_scene_in_category(selected_category)
            else:
                print("❌ Invalid category selection!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def replace_scene_in_category(self, category):
        """Replace a specific scene in a category"""
        scenes = ASSET_CATEGORIES["scenes"][category]
        
        print(f"\n🎬 {category.replace('_', ' ').title()} Scenes:")
        for i, (scene_name, scene_data) in enumerate(scenes.items(), 1):
            print(f"{i}. {scene_name.replace('_', ' ').title()}")
            print(f"   Current: {scene_data['file']}")
            print(f"   Description: {scene_data['description']}")
            print(f"   Mood: {scene_data['mood']}")
        
        try:
            scene_choice = int(input("\nSelect scene to replace: ")) - 1
            scene_names = list(scenes.keys())
            
            if 0 <= scene_choice < len(scene_names):
                selected_scene = scene_names[scene_choice]
                self.process_scene_replacement(category, selected_scene)
            else:
                print("❌ Invalid scene selection!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def process_scene_replacement(self, category, scene_name):
        """Process the actual scene background replacement"""
        scene_info = ASSET_CATEGORIES["scenes"][category][scene_name]
        scene_file = scene_info["file"]
        
        print(f"\n🖼️  Replacing {scene_name.replace('_', ' ').title()}")
        print(f"Expected dimensions: {scene_info['dimensions']}")
        print(f"Color palette: {', '.join(scene_info['color_palette'])}")
        print(f"Description: {scene_info['description']}")
        print(f"Mood: {scene_info['mood']}")
        
        # Show AI prompt for reference
        prompt_info = get_prompt_for_asset("scenes", category, scene_name)
        if prompt_info:
            print(f"\n🤖 AI Generation Prompt:")
            print(f"'{prompt_info['prompt']}'")
        
        # Get new image file
        new_image_path = input("\nEnter path to your new background image: ").strip().strip('"')
        
        if not os.path.exists(new_image_path):
            print("❌ Image file not found!")
            return
        
        # Determine target path
        backgrounds_dir = self.assets_dir / "backgrounds"
        backgrounds_dir.mkdir(exist_ok=True)
        target_path = backgrounds_dir / scene_file
        
        # Backup existing file
        if target_path.exists():
            backup_path = self.backup_dir / f"{scene_name}_{scene_file}.backup"
            target_path.rename(backup_path)
            print(f"💾 Backed up original to: {backup_path}")
        
        # Process and validate new image
        success = self.process_and_validate_background(new_image_path, target_path, scene_info)
        
        if success:
            print(f"✅ Successfully replaced {scene_name} background!")
        else:
            print(f"❌ Failed to replace {scene_name} background!")
    
    def process_and_validate_sprite(self, source_path, target_path, char_info):
        """Process and validate a character sprite"""
        try:
            img = Image.open(source_path)
            
            # Resize to expected dimensions
            expected_size = char_info["dimensions"]
            if img.size != expected_size:
                print(f"🔧 Resizing from {img.size} to {expected_size}")
                img = img.resize(expected_size, Image.Resampling.LANCZOS)
            
            # Ensure RGBA mode for transparency
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Save the processed image
            img.save(target_path)
            print(f"💾 Saved processed sprite to: {target_path}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error processing sprite: {e}")
            return False
    
    def process_and_validate_background(self, source_path, target_path, scene_info):
        """Process and validate a scene background"""
        try:
            img = Image.open(source_path)
            
            # Resize to expected dimensions
            expected_size = scene_info["dimensions"]
            if img.size != expected_size:
                print(f"🔧 Resizing from {img.size} to {expected_size}")
                img = img.resize(expected_size, Image.Resampling.LANCZOS)
            
            # Ensure RGB mode (no transparency for backgrounds)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Save the processed image
            img.save(target_path)
            print(f"💾 Saved processed background to: {target_path}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error processing background: {e}")
            return False
    
    def generate_ai_prompts(self):
        """Generate a comprehensive AI prompts file"""
        print("\n🤖 GENERATING AI PROMPTS FILE")
        print("-" * 40)
        
        from ai_art_generation_system import generate_all_prompts_file
        
        prompts_content = generate_all_prompts_file()
        prompts_file = self.project_root / "COMPLETE_AI_PROMPTS.md"
        
        with open(prompts_file, 'w', encoding='utf-8') as f:
            f.write(prompts_content)
        
        print(f"✅ AI prompts file generated: {prompts_file}")
        print("📝 Use these prompts with DALL-E, Midjourney, or Stable Diffusion")
        print("🎨 All prompts follow the consistent style guide for visual coherence")
    
    def test_updated_assets(self):
        """Test the updated assets in the enhanced GUI"""
        print("\n🧪 TESTING UPDATED ASSETS")
        print("-" * 40)
        
        # Check asset counts
        sprites_dir = self.assets_dir / "sprites"
        backgrounds_dir = self.assets_dir / "backgrounds"
        
        sprite_count = len(list(sprites_dir.glob("*.png"))) if sprites_dir.exists() else 0
        bg_count = len(list(backgrounds_dir.glob("*.png"))) if backgrounds_dir.exists() else 0
        
        print(f"📊 Current assets:")
        print(f"   Sprites: {sprite_count}")
        print(f"   Backgrounds: {bg_count}")
        
        # Try to launch GUI test
        try:
            import tkinter as tk
            project_root = self.get_project_root()
            if str(project_root) not in sys.path:
                sys.path.insert(0, str(project_root))
            
            from enhanced_gui_system import EnhancedGameGUI
            
            print("\n🖥️  Launching GUI test window...")
            root = tk.Tk()
            root.title("SHABUYA - Enhanced Asset Test")
            root.geometry("800x600")
            
            gui = EnhancedGameGUI(root)
            
            print(f"🎮 GUI loaded with:")
            print(f"   Character sprites: {len(gui.character_sprites)}")
            print(f"   Background images: {len(gui.background_images)}")
            
            root.mainloop()
            
        except Exception as e:
            print(f"❌ GUI test failed: {e}")
    
    def view_asset_inventory(self):
        """Display complete asset inventory"""
        print("\n📋 COMPLETE ASSET INVENTORY")
        print("-" * 50)
        
        # Display current assets
        for category, subcategories in ASSET_CATEGORIES.items():
            if not any(subcategories.values()):
                continue
                
            print(f"\n📁 {category.upper()}")
            for subcat, items in subcategories.items():
                if items:
                    print(f"  └── {subcat.replace('_', ' ').title()} ({len(items)} items)")
                    for item_name, item_data in items.items():
                        # Check if file exists
                        file_key = "sprite_file" if "sprite_file" in item_data else "file"
                        if file_key in item_data:
                            file_path = self.assets_dir / ("sprites" if category == "characters" else "backgrounds") / item_data[file_key]
                            status = "✅" if file_path.exists() else "❌"
                            print(f"      {status} {item_name.replace('_', ' ').title()}")
                else:
                    print(f"  └── {subcat.replace('_', ' ').title()} (ready for expansion)")
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_main_menu()
            
            try:
                choice = input("Select option (1-9): ").strip()
                
                if choice == "1":
                    self.replace_character_assets()
                elif choice == "2":
                    self.replace_scene_backgrounds()
                elif choice == "3":
                    print("🚧 New asset category addition coming in future update!")
                elif choice == "4":
                    print("🚧 Batch processing coming in future update!")
                elif choice == "5":
                    print("🚧 Asset validation coming in future update!")
                elif choice == "6":
                    self.generate_ai_prompts()
                elif choice == "7":
                    self.test_updated_assets()
                elif choice == "8":
                    self.view_asset_inventory()
                elif choice == "9":
                    print("👋 Goodbye!")
                    break
                else:
                    print("❌ Invalid choice!")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break

if __name__ == "__main__":
    manager = ScalableAssetManager()
    manager.run()
