#!/bin/bash
echo "🏴‍☠️ SHABUYA Cave Adventure - Enhanced GUI v2.0"
echo "=============================================="
echo ""
echo "🔍 Checking system requirements..."
python_version=$(python3 --version 2>&1)
echo "   $python_version"
echo ""
echo "🎨 Checking game assets..."
sprite_count=$(find assets/sprites -name "*.png" 2>/dev/null | wc -l)
bg_count=$(find assets/backgrounds -name "*.png" 2>/dev/null | wc -l)
echo "   📸 Character Sprites: $sprite_count found"
echo "   🌄 Background Scenes: $bg_count found"
echo ""
echo "🚀 Launching Enhanced GUI..."
echo "   (If GUI doesn't appear, you're in a container environment)"
echo ""
python3 enhanced_gui_final.py
echo ""
echo "👋 Enhanced GUI session ended. Thanks for testing!"
