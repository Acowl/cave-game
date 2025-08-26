#!/usr/bin/env python3
"""
Create the cave guardian sprite based on the user's provided image
"""

from PIL import Image, ImageDraw
from pathlib import Path

def create_cave_guardian_sprite():
    """Create the cave guardian sprite matching the user's design"""
    # Create 64x64 canvas
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colors from the user's design
    dark_brown = (101, 67, 33)
    med_brown = (139, 105, 68)
    light_brown = (165, 124, 82)
    highlight_brown = (180, 140, 100)
    red_eyes = (180, 30, 30)
    red_glow = (220, 60, 60)
    claw_white = (240, 235, 220)
    claw_tip = (200, 190, 170)
    black_outline = (20, 15, 10)
    
    # Main body shape (simplified blob-like creature)
    # Central mass
    draw.ellipse([20, 25, 44, 45], fill=med_brown, outline=black_outline, width=1)
    
    # Body bulk and texture
    draw.ellipse([18, 28, 46, 48], fill=dark_brown, outline=black_outline, width=1)
    
    # Upper body/head area
    draw.ellipse([22, 20, 42, 35], fill=light_brown, outline=black_outline, width=1)
    
    # Add texture spots
    draw.ellipse([25, 22, 28, 25], fill=dark_brown)
    draw.ellipse([35, 24, 38, 27], fill=dark_brown)
    draw.ellipse([28, 30, 31, 33], fill=highlight_brown)
    draw.ellipse([33, 32, 36, 35], fill=highlight_brown)
    
    # Left arm/appendage
    draw.ellipse([12, 32, 22, 40], fill=med_brown, outline=black_outline, width=1)
    
    # Right arm/appendage  
    draw.ellipse([42, 32, 52, 40], fill=med_brown, outline=black_outline, width=1)
    
    # Eyes (glowing red)
    # Left eye
    draw.ellipse([26, 26, 30, 30], fill=red_eyes)
    draw.ellipse([27, 27, 29, 29], fill=red_glow)
    
    # Right eye
    draw.ellipse([34, 26, 38, 30], fill=red_eyes)
    draw.ellipse([35, 27, 37, 29], fill=red_glow)
    
    # Claws - left side
    # Left claw points
    claw_points_left = [(14, 36), (10, 34), (12, 38)]
    draw.polygon(claw_points_left, fill=claw_white, outline=black_outline)
    claw_points_left2 = [(16, 38), (12, 36), (14, 40)]
    draw.polygon(claw_points_left2, fill=claw_white, outline=black_outline)
    claw_points_left3 = [(18, 36), (14, 34), (16, 38)]
    draw.polygon(claw_points_left3, fill=claw_white, outline=black_outline)
    
    # Claws - right side
    claw_points_right = [(50, 36), (54, 34), (52, 38)]
    draw.polygon(claw_points_right, fill=claw_white, outline=black_outline)
    claw_points_right2 = [(48, 38), (52, 36), (50, 40)]
    draw.polygon(claw_points_right2, fill=claw_white, outline=black_outline)
    claw_points_right3 = [(46, 36), (50, 34), (48, 38)]
    draw.polygon(claw_points_right3, fill=claw_white, outline=black_outline)
    
    # Bottom claws/feet
    claw_points_bottom1 = [(26, 46), (24, 50), (28, 48)]
    draw.polygon(claw_points_bottom1, fill=claw_white, outline=black_outline)
    claw_points_bottom2 = [(32, 46), (30, 50), (34, 48)]
    draw.polygon(claw_points_bottom2, fill=claw_white, outline=black_outline)
    claw_points_bottom3 = [(38, 46), (36, 50), (40, 48)]
    draw.polygon(claw_points_bottom3, fill=claw_white, outline=black_outline)
    
    # Add some shading/depth
    draw.arc([20, 25, 44, 45], 180, 360, fill=highlight_brown, width=2)
    
    return img

def save_cave_guardian_sprite():
    """Save the cave guardian sprite to the upload directory"""
    img = create_cave_guardian_sprite()
    
    # Save to upload directory
    upload_dir = Path("ai_generated_assets/characters")
    upload_dir.mkdir(parents=True, exist_ok=True)
    
    sprite_path = upload_dir / "cave_guardian.png"
    img.save(sprite_path)
    
    print(f"✅ Created cave guardian sprite: {sprite_path}")
    print(f"📏 Dimensions: 64x64 pixels")
    print(f"🎨 Format: RGBA (with transparency)")
    print(f"🗿 Style: Earthy creature with glowing red eyes and sharp claws")
    print(f"🎯 Perfect for: Cave encounters, alley ambushes, boss fights")

if __name__ == "__main__":
    save_cave_guardian_sprite()
