#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Direct Sprite Integration Tool
======================================================

This tool processes sprites shared by the user and integrates them directly
into the repository without requiring local file management.
"""

import base64
from pathlib import Path
from PIL import Image
import io

class DirectSpriteIntegrator:
    """Tool for direct sprite integration from user uploads"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.ai_assets_dir = self.project_root / "ai_generated_assets"
        self.game_assets_dir = self.project_root / "game_assets"
        
        # Asset mapping
        self.sprite_specs = {
            "warrior": {"file": "warrior_sprite.png", "size": (64, 64), "category": "player"},
            "rogue": {"file": "rogue_sprite.png", "size": (64, 64), "category": "player"},
            "mage": {"file": "mage_sprite.png", "size": (64, 64), "category": "player"},
            "primitive_creature": {"file": "primitive_creature_sprite.png", "size": (64, 64), "category": "enemy"},
            "divine_heart": {"file": "divine_heart_sprite.png", "size": (64, 64), "category": "enemy"},
            "cave_guardian": {"file": "cave_guardian_sprite.png", "size": (64, 64), "category": "enemy"}
        }
        
        self.scene_specs = {
            "cave_entrance": {"file": "cave_entrance.png", "size": (400, 300), "category": "exploration"},
            "skull_chamber": {"file": "skull_chamber.png", "size": (400, 300), "category": "exploration"},
            "primitive_village": {"file": "primitive_village.png", "size": (400, 300), "category": "exploration"},
            "alley": {"file": "alley.png", "size": (400, 300), "category": "social"},
            "armory": {"file": "armory.png", "size": (400, 300), "category": "social"},
            "chief_house": {"file": "chief_house.png", "size": (400, 300), "category": "social"},
            "healing_pool": {"file": "healing_pool.png", "size": (400, 300), "category": "social"},
            "village_changed": {"file": "village_changed.png", "size": (400, 300), "category": "social"},
            "menu": {"file": "menu.png", "size": (400, 300), "category": "ui"}
        }
    
    def process_base64_image(self, base64_data, asset_name, asset_type="sprite"):
        """Process a base64 encoded image and save it as an asset"""
        try:
            # Decode base64 image
            image_data = base64.b64decode(base64_data)
            img = Image.open(io.BytesIO(image_data))
            
            # Get asset specifications
            if asset_type == "sprite":
                specs = self.sprite_specs.get(asset_name)
                target_dir = self.ai_assets_dir / "characters"
            else:
                specs = self.scene_specs.get(asset_name) 
                target_dir = self.ai_assets_dir / "scenes"
            
            if not specs:
                print(f"❌ Unknown asset: {asset_name}")
                return False
            
            # Ensure directory exists
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # Process image
            target_size = specs["size"]
            if img.size != target_size:
                print(f"🔧 Resizing {asset_name} from {img.size} to {target_size}")
                img = img.resize(target_size, Image.Resampling.LANCZOS)
            
            # Set proper format
            if asset_type == "sprite":
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
            else:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
            
            # Save to upload directory
            target_path = target_dir / f"{asset_name}.png"
            img.save(target_path)
            
            print(f"✅ Saved {asset_name} to {target_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error processing {asset_name}: {e}")
            return False
    
    def add_sprite_from_attachment(self, sprite_name, description=""):
        """Add a sprite from user attachment"""
        print(f"🎨 PROCESSING SPRITE: {sprite_name}")
        print("-" * 40)
        
        if sprite_name in self.sprite_specs:
            specs = self.sprite_specs[sprite_name]
            print(f"Asset: {sprite_name}")
            print(f"File: {specs['file']}")
            print(f"Size: {specs['size']}")
            print(f"Category: {specs['category']}")
            if description:
                print(f"Description: {description}")
            
            # Create placeholder for now (will be replaced with actual processing)
            target_dir = self.ai_assets_dir / "characters"
            target_dir.mkdir(parents=True, exist_ok=True)
            target_path = target_dir / f"{sprite_name}.png"
            
            # For now, create a marker file
            with open(target_path, 'w') as f:
                f.write(f"Sprite: {sprite_name}\nDescription: {description}\nReady for processing")
            
            print(f"✅ Prepared for: {sprite_name}")
            print(f"📁 Location: {target_path}")
            print(f"🔄 Ready for automated processing")
            
            return True
        else:
            print(f"❌ Unknown sprite: {sprite_name}")
            return False

def main():
    integrator = DirectSpriteIntegrator()
    
    print("🎨 DIRECT SPRITE INTEGRATION TOOL")
    print("=" * 50)
    print()
    print("Available sprites to process:")
    
    for sprite_name, specs in integrator.sprite_specs.items():
        print(f"• {sprite_name} - {specs['category']} character ({specs['size'][0]}x{specs['size'][1]})")
    
    print()
    print("Available scenes to process:")
    
    for scene_name, specs in integrator.scene_specs.items():
        print(f"• {scene_name} - {specs['category']} scene ({specs['size'][0]}x{specs['size'][1]})")

if __name__ == "__main__":
    main()
