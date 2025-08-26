#!/usr/bin/env python3
"""
Create the divine heart sprite based on the user's provided image
"""

from PIL import Image, ImageDraw
from pathlib import Path
import math

def create_divine_heart_sprite():
    """Create the divine heart sprite matching the user's design"""
    # Create 64x64 canvas
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colors from the user's design
    dark_purple = (45, 20, 60)
    med_purple = (80, 40, 100) 
    bright_purple = (120, 60, 140)
    heart_purple = (100, 50, 120)
    red_glow = (180, 40, 80)
    bright_red = (220, 60, 100)
    
    # Create outer energy aura (larger circle)
    for r in range(32, 20, -1):
        alpha = int((32-r) * 8)
        color = dark_purple + (alpha,)
        draw.ellipse([32-r, 32-r, 32+r, 32+r], fill=color)
    
    # Create energy rays (simplified)
    center_x, center_y = 32, 32
    for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
        rad = math.radians(angle)
        x1 = center_x + int(15 * math.cos(rad))
        y1 = center_y + int(15 * math.sin(rad))
        x2 = center_x + int(25 * math.cos(rad))
        y2 = center_y + int(25 * math.sin(rad))
        draw.line([(x1, y1), (x2, y2)], fill=red_glow, width=2)
    
    # Create heart shape (simplified pixel art heart)
    # Heart body
    heart_points = [
        # Left lobe
        (25, 28), (27, 26), (30, 26), (32, 28),
        # Right lobe  
        (32, 28), (34, 26), (37, 26), (39, 28),
        # Point
        (32, 38)
    ]
    
    draw.polygon(heart_points, fill=heart_purple)
    
    # Heart highlight
    draw.polygon([(26, 28), (28, 27), (30, 27), (32, 29)], fill=bright_purple)
    
    # Inner glow
    draw.ellipse([28, 30, 36, 36], fill=red_glow + (100,))
    
    return img

def save_divine_heart_sprite():
    """Save the divine heart sprite to the upload directory"""
    img = create_divine_heart_sprite()
    
    # Save to upload directory
    upload_dir = Path("ai_generated_assets/characters")
    upload_dir.mkdir(parents=True, exist_ok=True)
    
    sprite_path = upload_dir / "divine_heart.png"
    img.save(sprite_path)
    
    print(f"✅ Created divine heart sprite: {sprite_path}")
    print(f"📏 Dimensions: 64x64 pixels")
    print(f"🎨 Format: RGBA (with transparency)")
    print(f"🔮 Style: Mystical heart with purple/red energy aura")

if __name__ == "__main__":
    save_divine_heart_sprite()
