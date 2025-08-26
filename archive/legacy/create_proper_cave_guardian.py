#!/usr/bin/env python3
"""
Create the proper cave guardian sprite based on the user's provided image
"""

from PIL import Image, ImageDraw
from pathlib import Path

def create_cave_guardian_sprite():
    """Create the cave guardian sprite matching the user's design"""
    # Create 64x64 canvas
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colors from the user's design
    dark_stone = (60, 60, 65)
    med_stone = (80, 80, 85)
    light_stone = (100, 100, 105)
    highlight_stone = (120, 120, 125)
    bone_color = (180, 160, 140)
    bone_tip = (200, 180, 160)
    skull_dark = (40, 35, 35)
    brown_leather = (90, 70, 50)
    dark_brown = (60, 45, 30)
    black_outline = (20, 20, 25)
    
    # Main body structure - massive stone form
    # Central torso
    draw.rectangle([22, 30, 42, 55], fill=med_stone, outline=black_outline, width=1)
    
    # Chest plate area
    draw.rectangle([20, 25, 44, 45], fill=light_stone, outline=black_outline, width=1)
    
    # Shoulder areas
    draw.rectangle([15, 20, 25, 35], fill=med_stone, outline=black_outline, width=1)
    draw.rectangle([39, 20, 49, 35], fill=med_stone, outline=black_outline, width=1)
    
    # Head/helmet area with skull
    draw.rectangle([26, 12, 38, 28], fill=dark_stone, outline=black_outline, width=1)
    
    # Skull face in the helmet
    # Eye sockets
    draw.ellipse([28, 16, 31, 19], fill=skull_dark)
    draw.ellipse([33, 16, 36, 19], fill=skull_dark)
    # Nasal cavity
    draw.rectangle([31, 20, 33, 24], fill=skull_dark)
    
    # Massive arms
    # Left arm
    draw.rectangle([10, 25, 20, 50], fill=med_stone, outline=black_outline, width=1)
    # Right arm  
    draw.rectangle([44, 25, 54, 50], fill=med_stone, outline=black_outline, width=1)
    
    # Legs
    draw.rectangle([24, 50, 32, 62], fill=med_stone, outline=black_outline, width=1)
    draw.rectangle([32, 50, 40, 62], fill=med_stone, outline=black_outline, width=1)
    
    # Bone spikes protruding from body
    # Shoulder spikes
    spike_points_1 = [(15, 18), (12, 12), (18, 15)]
    draw.polygon(spike_points_1, fill=bone_color, outline=black_outline)
    spike_points_2 = [(20, 16), (17, 10), (23, 13)]
    draw.polygon(spike_points_2, fill=bone_color, outline=black_outline)
    
    # Right shoulder spikes
    spike_points_3 = [(49, 18), (52, 12), (46, 15)]
    draw.polygon(spike_points_3, fill=bone_color, outline=black_outline)
    spike_points_4 = [(44, 16), (47, 10), (41, 13)]
    draw.polygon(spike_points_4, fill=bone_color, outline=black_outline)
    
    # Arm spikes
    # Left arm spikes
    spike_points_5 = [(8, 30), (5, 26), (11, 28)]
    draw.polygon(spike_points_5, fill=bone_color, outline=black_outline)
    spike_points_6 = [(9, 38), (6, 34), (12, 36)]
    draw.polygon(spike_points_6, fill=bone_color, outline=black_outline)
    
    # Right arm spikes
    spike_points_7 = [(56, 30), (59, 26), (53, 28)]
    draw.polygon(spike_points_7, fill=bone_color, outline=black_outline)
    spike_points_8 = [(55, 38), (58, 34), (52, 36)]
    draw.polygon(spike_points_8, fill=bone_color, outline=black_outline)
    
    # Chest/torso spikes
    spike_points_9 = [(22, 32), (19, 28), (25, 30)]
    draw.polygon(spike_points_9, fill=bone_color, outline=black_outline)
    spike_points_10 = [(42, 32), (45, 28), (39, 30)]
    draw.polygon(spike_points_10, fill=bone_color, outline=black_outline)
    
    # Leg spikes
    spike_points_11 = [(26, 58), (23, 54), (29, 56)]
    draw.polygon(spike_points_11, fill=bone_color, outline=black_outline)
    spike_points_12 = [(38, 58), (41, 54), (35, 56)]
    draw.polygon(spike_points_12, fill=bone_color, outline=black_outline)
    
    # Add brown leather/strap details
    draw.rectangle([30, 35, 34, 45], fill=brown_leather, outline=black_outline)
    
    # Stone texture details
    draw.rectangle([17, 27, 19, 29], fill=highlight_stone)
    draw.rectangle([45, 27, 47, 29], fill=highlight_stone)
    draw.rectangle([25, 40, 27, 42], fill=dark_stone)
    draw.rectangle([37, 40, 39, 42], fill=dark_stone)
    
    # Additional skull detail in chest
    draw.ellipse([30, 38, 34, 42], fill=skull_dark)
    
    return img

def save_proper_cave_guardian_sprite():
    """Save the proper cave guardian sprite to the upload directory"""
    img = create_cave_guardian_sprite()
    
    # Save to upload directory
    upload_dir = Path("ai_generated_assets/characters")
    upload_dir.mkdir(parents=True, exist_ok=True)
    
    sprite_path = upload_dir / "cave_guardian.png"
    img.save(sprite_path)
    
    print(f"✅ Created PROPER cave guardian sprite: {sprite_path}")
    print(f"📏 Dimensions: 64x64 pixels")
    print(f"🎨 Format: RGBA (with transparency)")
    print(f"🗿 Style: Massive stone golem with bone spikes and skull motifs")
    print(f"💀 Features: Bone spikes, skull helmet, imposing fortress-like build")
    print(f"🎯 Perfect for: Boss encounters, final guardian battles")

if __name__ == "__main__":
    save_proper_cave_guardian_sprite()
