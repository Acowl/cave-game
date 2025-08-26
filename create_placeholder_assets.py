#!/usr/bin/env python3
"""
Create placeholder assets for immediate viewing after replacement
Ensures all missing sprites and backgrounds have default graphics
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def create_placeholder_sprites():
    """Create placeholder sprites for missing enemy types"""
    sprite_dir = Path("game_assets/sprites")
    sprite_dir.mkdir(parents=True, exist_ok=True)
    
    sprite_configs = {
        'primitive_creature_sprite.png': {'color': '#A0522D', 'text': 'PRIMITIVE\nCREATURE'},
        'divine_heart_sprite.png': {'color': '#4B0082', 'text': 'DIVINE\nHEART'},
        'cave_guardian_sprite.png': {'color': '#696969', 'text': 'CAVE\nGUARDIAN'}
    }
    
    for filename, config in sprite_configs.items():
        sprite_path = sprite_dir / filename
        if not sprite_path.exists():
            # Create 64x64 placeholder sprite
            img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Background circle
            draw.ellipse([4, 4, 60, 60], fill=config['color'], outline='white', width=2)
            
            # Add text
            try:
                # Try to use a small font
                font = ImageFont.load_default()
                text_lines = config['text'].split('\n')
                y_offset = 20 if len(text_lines) == 2 else 28
                
                for i, line in enumerate(text_lines):
                    bbox = draw.textbbox((0, 0), line, font=font)
                    text_width = bbox[2] - bbox[0]
                    x = (64 - text_width) // 2
                    y = y_offset + (i * 12)
                    draw.text((x, y), line, fill='white', font=font)
                    
            except Exception:
                # Fallback to simple text
                draw.text((16, 28), config['text'].replace('\n', ' '), fill='white')
            
            img.save(sprite_path)
            print(f"✅ Created placeholder: {filename}")

def create_placeholder_backgrounds():
    """Create placeholder backgrounds for missing scenes"""
    bg_dir = Path("game_assets/backgrounds")
    bg_dir.mkdir(parents=True, exist_ok=True)
    
    bg_configs = {
        'alley.png': {'colors': [(15, 15, 15), (35, 35, 35)], 'text': 'ALLEY SCENE'},
        'armory.png': {'colors': [(30, 30, 40), (50, 50, 60)], 'text': 'ARMORY SCENE'},
        'chief_house.png': {'colors': [(40, 25, 10), (60, 45, 30)], 'text': 'CHIEF HOUSE'},
        'healing_pool.png': {'colors': [(10, 30, 50), (30, 50, 70)], 'text': 'HEALING POOL'},
        'village_changed.png': {'colors': [(25, 15, 35), (45, 35, 55)], 'text': 'VILLAGE CHANGED'}
    }
    
    for filename, config in bg_configs.items():
        bg_path = bg_dir / filename
        if not bg_path.exists():
            # Create 400x300 placeholder background
            img = Image.new('RGB', (400, 300))
            draw = ImageDraw.Draw(img)
            
            # Gradient background
            color1, color2 = config['colors']
            for y in range(300):
                ratio = y / 300
                r = int(color1[0] * (1-ratio) + color2[0] * ratio)
                g = int(color1[1] * (1-ratio) + color2[1] * ratio)
                b = int(color1[2] * (1-ratio) + color2[2] * ratio)
                draw.line([(0, y), (400, y)], fill=(r, g, b))
            
            # Add centered text
            try:
                font = ImageFont.load_default()
                text = config['text']
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                x = (400 - text_width) // 2
                y = (300 - text_height) // 2
                
                # Text with outline for visibility
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx or dy:
                            draw.text((x+dx, y+dy), text, fill='black', font=font)
                draw.text((x, y), text, fill='white', font=font)
                
            except Exception:
                # Fallback text
                draw.text((150, 140), config['text'], fill='white')
            
            img.save(bg_path)
            print(f"✅ Created placeholder: {filename}")

def main():
    """Create all placeholder assets"""
    print("🎨 Creating placeholder assets for immediate viewing...")
    print()
    
    print("👾 Creating enemy sprite placeholders...")
    create_placeholder_sprites()
    
    print("\n🏞️ Creating scene background placeholders...")
    create_placeholder_backgrounds()
    
    print("\n✅ All placeholder assets created!")
    print("💡 Now you can test them in the GUI before replacing with AI-generated assets.")

if __name__ == "__main__":
    main()
