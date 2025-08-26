#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Integrated Asset Management Dashboard
============================================================

Combined interface for:
1. AI prompt generation
2. Asset upload monitoring  
3. Automated processing
4. GUI testing
5. Repository management
"""

import os
import sys
from pathlib import Path
import subprocess

class AssetManagementDashboard:
    """Integrated dashboard for complete asset workflow"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.ai_assets_dir = self.project_root / "ai_generated_assets"
        
    def display_main_dashboard(self):
        """Display the main dashboard"""
        print("🎨 " + "=" * 60)
        print("🎨 SHABUYA INTEGRATED ASSET MANAGEMENT DASHBOARD")
        print("🎨 " + "=" * 60)
        
        # Check current status
        self.display_current_status()
        
        print("\n🎯 WORKFLOW OPTIONS:")
        print("1. 📝 Generate AI Prompts File")
        print("2. 📁 Open Asset Upload Instructions") 
        print("3. 🤖 Run Automated Asset Processor")
        print("4. 👀 Monitor Upload Directories")
        print("5. 🧪 Test Assets in GUI")
        print("6. 📊 View Asset Inventory")
        print("7. 🚀 Complete Workflow Guide")
        print("8. 🔄 Process Single Asset (Manual)")
        print("9. 📋 Generate Processing Report")
        print("10. Exit")
        print()
    
    def display_current_status(self):
        """Show current asset status"""
        print(f"\n📊 CURRENT STATUS:")
        
        # Check for pending uploads
        pending_chars = len(list((self.ai_assets_dir / "characters").glob("*.png"))) if (self.ai_assets_dir / "characters").exists() else 0
        pending_scenes = len(list((self.ai_assets_dir / "scenes").glob("*.png"))) if (self.ai_assets_dir / "scenes").exists() else 0
        
        # Check current game assets
        game_assets_dir = self.project_root / "game_assets"
        current_sprites = len(list((game_assets_dir / "sprites").glob("*.png"))) if (game_assets_dir / "sprites").exists() else 0
        current_backgrounds = len(list((game_assets_dir / "backgrounds").glob("*.png"))) if (game_assets_dir / "backgrounds").exists() else 0
        
        print(f"   🎭 Character sprites: {current_sprites}/6")
        print(f"   🏔️  Scene backgrounds: {current_backgrounds}/9")
        print(f"   📥 Pending characters: {pending_chars}")
        print(f"   📥 Pending scenes: {pending_scenes}")
        
        if pending_chars > 0 or pending_scenes > 0:
            print(f"   ⚡ Ready to process {pending_chars + pending_scenes} new assets!")
        else:
            print(f"   📭 No pending uploads")
    
    def generate_prompts_file(self):
        """Generate the AI prompts file"""
        print("\n🤖 GENERATING AI PROMPTS FILE")
        print("-" * 40)
        
        try:
            from ai_art_generation_system import generate_all_prompts_file
            
            prompts_content = generate_all_prompts_file()
            prompts_file = self.project_root / "COMPLETE_AI_PROMPTS.md"
            
            with open(prompts_file, 'w', encoding='utf-8') as f:
                f.write(prompts_content)
            
            print(f"✅ AI prompts file generated: {prompts_file}")
            print(f"📝 Contains {len(prompts_content.split('Prompt:')) - 1} asset prompts")
            print(f"🎨 Ready for use with DALL-E, Midjourney, Stable Diffusion")
            
        except Exception as e:
            print(f"❌ Error generating prompts: {e}")
    
    def show_upload_instructions(self):
        """Display detailed upload instructions"""
        print("\n📁 AI ASSET UPLOAD INSTRUCTIONS")
        print("-" * 40)
        
        print("🎯 COMPLETE WORKFLOW:")
        print("1. Open COMPLETE_AI_PROMPTS.md for prompts")
        print("2. Generate art with AI tool (DALL-E, Midjourney, etc.)")
        print("3. Download and rename files:")
        print()
        print("   📂 Characters (ai_generated_assets/characters/):")
        print("      • warrior.png - Medieval warrior sprite")
        print("      • rogue.png - Stealthy assassin sprite")
        print("      • mage.png - Mystical wizard sprite")
        print("      • primitive_creature.png - Tribal enemy")
        print("      • divine_heart.png - Mystical heart enemy")
        print("      • cave_guardian.png - Stone guardian boss")
        print()
        print("   📂 Scenes (ai_generated_assets/scenes/):")
        print("      • cave_entrance.png - Cave entrance")
        print("      • skull_chamber.png - Bone chamber")
        print("      • primitive_village.png - Tribal village")
        print("      • alley.png - Village alley")
        print("      • armory.png - Weapon storage")
        print("      • chief_house.png - Leader's dwelling")
        print("      • healing_pool.png - Sacred waters")
        print("      • village_changed.png - Transformed village")
        print("      • menu.png - Main menu background")
        print()
        print("4. Upload files to GitHub repository")
        print("5. Run option 3 (Automated Processor) in this dashboard")
        print("6. Test results with option 5 (GUI Test)")
    
    def run_automated_processor(self):
        """Run the automated asset processor"""
        print("\n🤖 RUNNING AUTOMATED ASSET PROCESSOR")
        print("-" * 40)
        
        try:
            # Import and run the processor
            from automated_asset_processor import AutomatedAssetProcessor
            
            processor = AutomatedAssetProcessor()
            processor.run()
            
        except Exception as e:
            print(f"❌ Error running processor: {e}")
            print("Trying fallback method...")
            try:
                subprocess.run([sys.executable, "automated_asset_processor.py"], check=True)
            except subprocess.CalledProcessError as e2:
                print(f"❌ Fallback also failed: {e2}")
    
    def monitor_uploads(self):
        """Monitor upload directories for new files"""
        print("\n👀 MONITORING UPLOAD DIRECTORIES")
        print("-" * 40)
        
        chars_dir = self.ai_assets_dir / "characters"
        scenes_dir = self.ai_assets_dir / "scenes"
        
        print(f"📁 Characters directory: {chars_dir}")
        if chars_dir.exists():
            char_files = list(chars_dir.glob("*.png"))
            if char_files:
                print(f"   📥 Found {len(char_files)} pending character files:")
                for file in char_files:
                    print(f"      • {file.name}")
            else:
                print(f"   📭 No character files pending")
        else:
            print(f"   ⚠️  Directory doesn't exist")
        
        print(f"\n📁 Scenes directory: {scenes_dir}")
        if scenes_dir.exists():
            scene_files = list(scenes_dir.glob("*.png"))
            if scene_files:
                print(f"   📥 Found {len(scene_files)} pending scene files:")
                for file in scene_files:
                    print(f"      • {file.name}")
            else:
                print(f"   📭 No scene files pending")
        else:
            print(f"   ⚠️  Directory doesn't exist")
        
        total_pending = len(char_files) + len(scene_files) if chars_dir.exists() and scenes_dir.exists() else 0
        if total_pending > 0:
            print(f"\n⚡ {total_pending} files ready for processing!")
            print(f"💡 Run option 3 to process automatically")
    
    def test_gui_assets(self):
        """Test assets in GUI"""
        print("\n🧪 TESTING ASSETS IN GUI")
        print("-" * 40)
        
        try:
            subprocess.run([sys.executable, "gui_diagnostic.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running GUI test: {e}")
            print("💡 Make sure gui_diagnostic.py exists and GUI dependencies are installed")
    
    def view_asset_inventory(self):
        """View complete asset inventory"""
        print("\n📋 COMPLETE ASSET INVENTORY")
        print("-" * 40)
        
        try:
            from asset_management_system import ASSET_CATEGORIES
            
            game_assets_dir = self.project_root / "game_assets"
            
            # Characters
            print("👤 CHARACTER ASSETS:")
            for category, chars in ASSET_CATEGORIES["characters"].items():
                if chars:
                    print(f"  └── {category.replace('_', ' ').title()}:")
                    for char_name, char_data in chars.items():
                        sprite_path = game_assets_dir / "sprites" / char_data["sprite_file"]
                        status = "✅" if sprite_path.exists() else "❌"
                        print(f"      {status} {char_name.replace('_', ' ').title()}")
            
            # Scenes
            print(f"\n🏔️  SCENE ASSETS:")
            for category, scenes in ASSET_CATEGORIES["scenes"].items():
                if scenes:
                    print(f"  └── {category.replace('_', ' ').title()}:")
                    for scene_name, scene_data in scenes.items():
                        bg_path = game_assets_dir / "backgrounds" / scene_data["file"]
                        status = "✅" if bg_path.exists() else "❌"
                        print(f"      {status} {scene_name.replace('_', ' ').title()}")
        
        except Exception as e:
            print(f"❌ Error loading inventory: {e}")
    
    def show_workflow_guide(self):
        """Show complete workflow guide"""
        print("\n🚀 COMPLETE WORKFLOW GUIDE")
        print("-" * 40)
        
        print("📋 STEP-BY-STEP PROCESS:")
        print()
        print("1. 🤖 GENERATE PROMPTS")
        print("   → Run option 1 to create COMPLETE_AI_PROMPTS.md")
        print("   → File contains all asset prompts ready for AI tools")
        print()
        print("2. 🎨 CREATE AI ART")
        print("   → Use DALL-E 3, Midjourney, or Stable Diffusion")
        print("   → Copy prompts exactly from the generated file")
        print("   → Generate 1-3 assets as a test batch")
        print()
        print("3. 📁 UPLOAD TO REPOSITORY")
        print("   → Download images from AI tool")
        print("   → Rename to exact asset names (warrior.png, cave_entrance.png)")
        print("   → Upload to ai_generated_assets/characters/ or /scenes/")
        print("   → Commit and push to GitHub")
        print()
        print("4. 🤖 AUTOMATED PROCESSING")
        print("   → Pull latest changes locally")
        print("   → Run option 3 (Automated Processor)")
        print("   → Script handles resizing, format conversion, placement")
        print()
        print("5. 🧪 TEST RESULTS")
        print("   → Run option 5 (GUI Test)")
        print("   → Verify assets appear correctly")
        print("   → Check visual consistency")
        print()
        print("6. 🔄 ITERATE")
        print("   → Generate more assets based on results")
        print("   → Process in batches for efficiency")
        print("   → Build complete asset library over time")
        print()
        print("🎯 RECOMMENDED FIRST BATCH:")
        print("   • warrior.png (test character)")
        print("   • cave_entrance.png (test scene)")
        print("   → Perfect for testing the complete workflow!")
    
    def run(self):
        """Main dashboard loop"""
        while True:
            self.display_main_dashboard()
            
            try:
                choice = input("Select option (1-10): ").strip()
                
                if choice == "1":
                    self.generate_prompts_file()
                elif choice == "2":
                    self.show_upload_instructions()
                elif choice == "3":
                    self.run_automated_processor()
                elif choice == "4":
                    self.monitor_uploads()
                elif choice == "5":
                    self.test_gui_assets()
                elif choice == "6":
                    self.view_asset_inventory()
                elif choice == "7":
                    self.show_workflow_guide()
                elif choice == "8":
                    print("🚧 Manual processing feature coming soon!")
                elif choice == "9":
                    print("🚧 Report generation feature coming soon!")
                elif choice == "10":
                    print("👋 Goodbye!")
                    break
                else:
                    print("❌ Invalid choice!")
                    
                input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break

if __name__ == "__main__":
    dashboard = AssetManagementDashboard()
    dashboard.run()
