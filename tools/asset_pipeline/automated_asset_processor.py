#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Automated Asset Processing System
=========================================================

This system automatically processes AI-generated assets from the repository:
1. Scans ai_generated_assets/ directory for new images
2. Automatically identifies asset type and category
3. Processes, resizes, and validates images
4. Moves them to correct game_assets/ locations
5. Creates backups of replaced assets
6. Generates processing reports

Usage:
1. Upload AI-generated images to ai_generated_assets/ folders
2. Run this script to automatically process all new assets
3. Test in GUI to see results
"""

import os
import sys
import shutil
from pathlib import Path
from PIL import Image
import json
from datetime import datetime

# Import our scalable systems
try:
    from asset_management_system import ASSET_CATEGORIES, QUALITY_STANDARDS
    from ai_art_generation_system import get_prompt_for_asset
except ImportError:
    print("⚠️  Asset management systems not found. Please ensure both files are in the same directory.")
    sys.exit(1)

class AutomatedAssetProcessor:
    """Automated asset processing from repository uploads"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.ai_assets_dir = self.project_root / "ai_generated_assets"
        self.game_assets_dir = self.project_root / "game_assets"
        self.backup_dir = self.project_root / "asset_backups"
        self.processed_dir = self.project_root / "ai_generated_assets" / "processed"
        
        # Ensure directories exist
        self.ai_assets_dir.mkdir(exist_ok=True)
        self.game_assets_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)
        self.processed_dir.mkdir(exist_ok=True)
        
        # Asset mapping for automatic identification
        self.asset_mapping = self.build_asset_mapping()
        
    def build_asset_mapping(self):
        """Build mapping from file names to asset categories"""
        mapping = {}
        
        # Character assets
        for category, chars in ASSET_CATEGORIES["characters"].items():
            for char_name, char_data in chars.items():
                # Map both the character name and sprite file name
                mapping[char_name] = {
                    "type": "character",
                    "category": category,
                    "name": char_name,
                    "file": char_data["sprite_file"],
                    "target_dir": "sprites",
                    "dimensions": char_data["dimensions"]
                }
                mapping[char_data["sprite_file"].replace("_sprite.png", "")] = mapping[char_name]
        
        # Scene assets
        for category, scenes in ASSET_CATEGORIES["scenes"].items():
            for scene_name, scene_data in scenes.items():
                mapping[scene_name] = {
                    "type": "scene",
                    "category": category, 
                    "name": scene_name,
                    "file": scene_data["file"],
                    "target_dir": "backgrounds",
                    "dimensions": scene_data["dimensions"]
                }
                mapping[scene_data["file"].replace(".png", "")] = mapping[scene_name]
        
        return mapping
    
    def scan_for_new_assets(self):
        """Scan ai_generated_assets directory for new images"""
        new_assets = []
        
        # Scan character uploads
        char_dir = self.ai_assets_dir / "characters"
        if char_dir.exists():
            for img_file in char_dir.glob("*.png"):
                asset_info = self.identify_asset(img_file)
                if asset_info:
                    new_assets.append(asset_info)
        
        # Scan scene uploads
        scenes_dir = self.ai_assets_dir / "scenes"
        if scenes_dir.exists():
            for img_file in scenes_dir.glob("*.png"):
                asset_info = self.identify_asset(img_file)
                if asset_info:
                    new_assets.append(asset_info)
        
        return new_assets
    
    def identify_asset(self, image_path):
        """Automatically identify what asset type an image is"""
        file_name = image_path.stem.lower()
        
        # Try exact matches first
        if file_name in self.asset_mapping:
            mapping = self.asset_mapping[file_name]
            return {
                "source_path": image_path,
                "asset_type": mapping["type"],
                "category": mapping["category"],
                "name": mapping["name"],
                "target_file": mapping["file"],
                "target_dir": mapping["target_dir"],
                "dimensions": mapping["dimensions"]
            }
        
        # Try partial matches
        for key, mapping in self.asset_mapping.items():
            if key in file_name or file_name in key:
                return {
                    "source_path": image_path,
                    "asset_type": mapping["type"],
                    "category": mapping["category"],
                    "name": mapping["name"],
                    "target_file": mapping["file"],
                    "target_dir": mapping["target_dir"],
                    "dimensions": mapping["dimensions"]
                }
        
        # If no match found, try to guess from directory
        parent_dir = image_path.parent.name
        if parent_dir == "characters":
            return {
                "source_path": image_path,
                "asset_type": "character",
                "category": "unknown",
                "name": file_name,
                "target_file": f"{file_name}_sprite.png",
                "target_dir": "sprites",
                "dimensions": (64, 64)
            }
        elif parent_dir == "scenes":
            return {
                "source_path": image_path,
                "asset_type": "scene",
                "category": "unknown", 
                "name": file_name,
                "target_file": f"{file_name}.png",
                "target_dir": "backgrounds",
                "dimensions": (400, 300)
            }
        
        return None
    
    def process_asset(self, asset_info):
        """Process a single asset"""
        print(f"\n🖼️  Processing {asset_info['name']}...")
        print(f"   Type: {asset_info['asset_type']} ({asset_info['category']})")
        print(f"   Source: {asset_info['source_path']}")
        
        try:
            # Load and process image
            img = Image.open(asset_info["source_path"])
            original_size = img.size
            
            # Resize if needed
            target_size = asset_info["dimensions"]
            if img.size != target_size:
                print(f"   🔧 Resizing from {original_size} to {target_size}")
                img = img.resize(target_size, Image.Resampling.LANCZOS)
            
            # Set correct mode
            if asset_info["asset_type"] == "character":
                # Characters need transparency
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
            else:
                # Backgrounds don't need transparency
                if img.mode != 'RGB':
                    img = img.convert('RGB')
            
            # Determine target path
            target_dir = self.game_assets_dir / asset_info["target_dir"]
            target_dir.mkdir(exist_ok=True)
            target_path = target_dir / asset_info["target_file"]
            
            # Backup existing file
            if target_path.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_path = self.backup_dir / f"{asset_info['name']}_{timestamp}.backup.png"
                shutil.copy2(target_path, backup_path)
                print(f"   💾 Backed up original to: {backup_path.name}")
            
            # Save processed image
            img.save(target_path)
            print(f"   ✅ Saved to: {target_path}")
            
            # Move source to processed directory
            processed_path = self.processed_dir / asset_info["source_path"].name
            shutil.move(asset_info["source_path"], processed_path)
            print(f"   📁 Moved source to: processed/{processed_path.name}")
            
            return True, None
            
        except Exception as e:
            error_msg = f"Error processing {asset_info['name']}: {e}"
            print(f"   ❌ {error_msg}")
            return False, error_msg
    
    def generate_processing_report(self, processed_assets, failed_assets):
        """Generate a report of processed assets"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = []
        report.append("SHABUYA Asset Processing Report")
        report.append("=" * 50)
        report.append(f"Generated: {timestamp}")
        report.append("")
        
        if processed_assets:
            report.append(f"✅ SUCCESSFULLY PROCESSED ({len(processed_assets)} assets):")
            report.append("-" * 40)
            for asset in processed_assets:
                report.append(f"• {asset['name']} ({asset['asset_type']})")
                report.append(f"  Source: {asset['source_path'].name}")
                report.append(f"  Target: {asset['target_file']}")
                report.append("")
        
        if failed_assets:
            report.append(f"❌ FAILED TO PROCESS ({len(failed_assets)} assets):")
            report.append("-" * 40)
            for asset, error in failed_assets:
                report.append(f"• {asset['name']} ({asset['asset_type']})")
                report.append(f"  Error: {error}")
                report.append("")
        
        if not processed_assets and not failed_assets:
            report.append("📭 No new assets found to process.")
            report.append("")
            report.append("To add assets:")
            report.append("1. Upload AI-generated images to ai_generated_assets/characters/")
            report.append("2. Upload AI-generated images to ai_generated_assets/scenes/")
            report.append("3. Name files using asset names (e.g., warrior.png, cave_entrance.png)")
            report.append("4. Run this script again")
        
        # Save report
        report_content = "\n".join(report)
        report_file = self.project_root / "asset_processing_report.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return report_content, report_file
    
    def run(self):
        """Main processing routine"""
        print("🤖 AUTOMATED ASSET PROCESSING SYSTEM")
        print("=" * 50)
        
        # Scan for new assets
        print("\n1️⃣ SCANNING FOR NEW ASSETS")
        print("-" * 30)
        new_assets = self.scan_for_new_assets()
        
        if not new_assets:
            print("📭 No new assets found in ai_generated_assets/")
            print("\n💡 To add assets:")
            print("   1. Upload images to ai_generated_assets/characters/")
            print("   2. Upload images to ai_generated_assets/scenes/")
            print("   3. Name files using asset names (e.g., warrior.png)")
            print("   4. Run this script again")
            return
        
        print(f"🎯 Found {len(new_assets)} new assets to process:")
        for asset in new_assets:
            print(f"   • {asset['name']} ({asset['asset_type']})")
        
        # Process each asset
        print(f"\n2️⃣ PROCESSING ASSETS")
        print("-" * 30)
        
        processed_assets = []
        failed_assets = []
        
        for asset_info in new_assets:
            success, error = self.process_asset(asset_info)
            if success:
                processed_assets.append(asset_info)
            else:
                failed_assets.append((asset_info, error))
        
        # Generate report
        print(f"\n3️⃣ GENERATING REPORT")
        print("-" * 30)
        
        report_content, report_file = self.generate_processing_report(processed_assets, failed_assets)
        print(f"📋 Report saved to: {report_file}")
        
        # Summary
        print(f"\n🎉 PROCESSING COMPLETE!")
        print(f"   ✅ Processed: {len(processed_assets)} assets")
        print(f"   ❌ Failed: {len(failed_assets)} assets")
        
        if processed_assets:
            print(f"\n🧪 Next steps:")
            print(f"   1. Run: python gui_diagnostic.py")
            print(f"   2. Test the updated assets in the GUI")
            print(f"   3. Commit and push changes if satisfied")

if __name__ == "__main__":
    processor = AutomatedAssetProcessor()
    processor.run()
