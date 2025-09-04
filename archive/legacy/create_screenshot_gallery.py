#!/usr/bin/env python3
"""
Screenshot Gallery Generator
===========================
Creates an HTML gallery of GUI screenshots for easy viewing and AI analysis.
"""

import os
from pathlib import Path
import base64
import time

def create_html_gallery():
    """Create an HTML gallery of screenshots."""
    
    snapshot_dir = Path("gui_snapshots")
    gallery_file = snapshot_dir / "gallery.html"
    
    # Get all PNG files
    png_files = sorted(list(snapshot_dir.glob("*.png")))
    
    if not png_files:
        print("❌ No PNG files found in gui_snapshots/")
        return
    
    # Create HTML content
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHABUYA Cave Adventure - GUI Screenshots</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #1e1e1e, #2a2a2a);
            color: white;
        }}
        h1 {{
            text-align: center;
            color: #FFD700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            margin-bottom: 10px;
        }}
        .subtitle {{
            text-align: center;
            color: #CCCCCC;
            margin-bottom: 30px;
        }}
        .gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .screenshot {{
            background: #2a2a2a;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            transition: transform 0.2s ease;
        }}
        .screenshot:hover {{
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.4);
        }}
        .screenshot img {{
            width: 100%;
            height: auto;
            border-radius: 5px;
            border: 2px solid #444;
        }}
        .screenshot h3 {{
            color: #FFD700;
            margin: 15px 0 10px 0;
            font-size: 18px;
        }}
        .screenshot p {{
            color: #CCCCCC;
            margin: 0;
            font-size: 14px;
            line-height: 1.4;
        }}
        .stats {{
            text-align: center;
            margin: 30px 0;
            padding: 20px;
            background: #333;
            border-radius: 10px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }}
        .download-links {{
            text-align: center;
            margin: 20px 0;
        }}
        .download-links a {{
            color: #FFD700;
            text-decoration: none;
            margin: 0 10px;
            padding: 8px 16px;
            border: 1px solid #FFD700;
            border-radius: 5px;
            transition: all 0.2s ease;
        }}
        .download-links a:hover {{
            background: #FFD700;
            color: #1e1e1e;
        }}
    </style>
</head>
<body>
    <h1>🏴‍☠️ SHABUYA Cave Adventure</h1>
    <p class="subtitle">GUI Screenshot Gallery - Generated {time.strftime('%B %d, %Y at %I:%M %p')}</p>
    
    <div class="stats">
        <h3>📊 Gallery Statistics</h3>
        <p><strong>{len(png_files)}</strong> screenshots captured</p>
        <p><strong>{sum(f.stat().st_size for f in png_files) // 1024}</strong> KB total size</p>
        <p>Ready for AI analysis and review</p>
    </div>
    
    <div class="download-links">
        <a href="screenshot_report.md" target="_blank">📋 View Report</a>
        <a href="." target="_blank">📁 Browse Files</a>
    </div>
    
    <div class="gallery">
"""
    
    # Screenshot descriptions
    descriptions = {
        "01_title_screen": "Main title screen with character class selection. Shows the game branding and initial player choice interface.",
        "02_class_selected": "Character class selection confirmation. Demonstrates the selection feedback and transition state.",
        "03_main_game_scene": "Core gameplay interface with scene rendering, player stats, NPCs, and dialogue system.",
        "04_shop_interface": "Village armory shop showing item listings, prices, and merchant interaction interface.",
        "05_combat_interface": "Battle system with player vs enemy combat, health bars, and action selection buttons.",
        "06_inventory_interface": "Character inventory management with items, equipment, and detailed player statistics."
    }
    
    # Add each screenshot
    for i, png_file in enumerate(png_files):
        # Convert image to base64 for embedding
        with open(png_file, 'rb') as f:
            img_data = base64.b64encode(f.read()).decode('utf-8')
        
        # Extract description key
        desc_key = png_file.stem.split('_')[1:3]  # Get parts like "title_screen"
        desc_key = '_'.join(desc_key) if len(desc_key) > 1 else desc_key[0] if desc_key else "screenshot"
        
        description = descriptions.get(desc_key, "Game interface screenshot captured during automated testing.")
        
        file_size_kb = png_file.stat().st_size // 1024
        
        html_content += f"""
        <div class="screenshot">
            <img src="data:image/png;base64,{img_data}" alt="{png_file.name}">
            <h3>📷 {png_file.stem.replace('_', ' ').title()}</h3>
            <p>{description}</p>
            <p style="margin-top: 10px; font-size: 12px; color: #888;">
                <strong>File:</strong> {png_file.name} ({file_size_kb} KB)
            </p>
        </div>
        """
    
    html_content += """
    </div>
    
    <div style="text-align: center; margin-top: 40px; padding: 20px; color: #888; font-size: 12px;">
        <p>Generated by SHABUYA Cave Adventure Screenshot System</p>
        <p>All images embedded as base64 for offline viewing</p>
    </div>
    
</body>
</html>
"""
    
    # Save the HTML file
    with open(gallery_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ HTML gallery created: {gallery_file}")
    print(f"📁 Gallery size: {gallery_file.stat().st_size // 1024} KB")
    print(f"🌐 Open in browser: file://{gallery_file.absolute()}")
    
    return str(gallery_file.absolute())

def create_screenshot_summary():
    """Create a text summary of screenshots for AI analysis."""
    
    snapshot_dir = Path("gui_snapshots") 
    summary_file = snapshot_dir / "ai_analysis_summary.txt"
    
    png_files = sorted(list(snapshot_dir.glob("*.png")))
    
    with open(summary_file, 'w') as f:
        f.write("SHABUYA CAVE ADVENTURE - GUI SCREENSHOT ANALYSIS SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Screenshots: {len(png_files)}\n")
        f.write(f"Total Size: {sum(f.stat().st_size for f in png_files) // 1024} KB\n\n")
        
        f.write("SCREENSHOT INVENTORY:\n")
        f.write("-" * 30 + "\n")
        
        for i, png_file in enumerate(png_files, 1):
            size_kb = png_file.stat().st_size // 1024
            f.write(f"{i}. {png_file.name}\n")
            f.write(f"   Size: {size_kb} KB\n")
            f.write(f"   Path: {png_file.absolute()}\n\n")
        
        f.write("INTERFACE ANALYSIS CHECKLIST:\n")
        f.write("-" * 35 + "\n")
        f.write("□ Title screen layout and branding\n")
        f.write("□ Character selection user experience\n") 
        f.write("□ Main game scene composition\n")
        f.write("□ Dialogue system readability\n")
        f.write("□ Shop interface usability\n")
        f.write("□ Combat system clarity\n")
        f.write("□ Inventory organization\n")
        f.write("□ Color scheme consistency\n")
        f.write("□ Button placement and sizing\n")
        f.write("□ Text legibility across interfaces\n")
        f.write("□ Overall visual polish\n\n")
        
        f.write("READY FOR AI ANALYSIS:\n")
        f.write("-" * 25 + "\n")
        f.write("All PNG files are ready for upload to AI systems for:\n")
        f.write("- Visual design feedback\n")
        f.write("- UI/UX improvement suggestions\n") 
        f.write("- Layout optimization recommendations\n")
        f.write("- Accessibility assessment\n")
        f.write("- Player experience evaluation\n")
    
    print(f"✅ Analysis summary created: {summary_file}")
    return str(summary_file)

def main():
    print("🎨 Creating GUI Screenshot Gallery...")
    
    try:
        # Create HTML gallery
        gallery_path = create_html_gallery()
        
        # Create AI analysis summary
        summary_path = create_screenshot_summary()
        
        print(f"\n🎯 RESULTS:")
        print(f"  📱 HTML Gallery: {gallery_path}")
        print(f"  📋 AI Summary: {summary_path}")
        print(f"  📁 All files in: gui_snapshots/")
        
        print(f"\n💡 NEXT STEPS:")
        print(f"  1. Open the HTML gallery in your browser")
        print(f"  2. Share PNG files with AI for visual analysis") 
        print(f"  3. Use summary checklist for systematic review")
        
    except Exception as e:
        print(f"❌ Error creating gallery: {e}")

if __name__ == "__main__":
    main()
