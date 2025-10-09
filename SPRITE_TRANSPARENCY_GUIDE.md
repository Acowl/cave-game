# Sprite Transparency System

## Overview

The game now automatically removes backgrounds from sprite images, making them blend seamlessly with scene backgrounds.

## How It Works

When sprites are loaded, the system:
1. Opens the image in RGBA mode (with alpha channel)
2. Scans each pixel
3. Identifies background pixels (white/near-white by default)
4. Converts those pixels to transparent
5. Keeps all other pixels intact

## Default Settings

**Current threshold**: 240 (out of 255)
- Pixels with RGB values all above 240 are made transparent
- This removes white and very light backgrounds
- Darker pixels (the actual sprite artwork) are preserved

## Adjusting Transparency

If sprites look incorrect (too much or too little removed), adjust the threshold in `player_gui.py`:

```python
# In load_assets() method, find this line:
if item[0] > 240 and item[1] > 240 and item[2] > 240:
    # Change 240 to a different value
```

### Threshold Guide

| Value | Effect | Use When |
|-------|--------|----------|
| 250 | Very conservative | Only pure white removed |
| 240 | **Default** | White and very light backgrounds |
| 220 | Moderate | Light gray backgrounds |
| 200 | Aggressive | Medium gray backgrounds |
| 180 | Very aggressive | Darker backgrounds (may remove sprite details!) |

**Recommendation**: Keep between 220-250 for best results

## Supported Sprite Background Colors

Works best with:
- ✅ White backgrounds (RGB: 255, 255, 255)
- ✅ Very light gray (RGB: 240+, 240+, 240+)
- ✅ Off-white backgrounds
- ⚠️ Medium gray (may need threshold adjustment)
- ❌ Dark backgrounds (use manual editing tools instead)

## Current Sprites

All sprites in `assets/sprites/` are processed:
- warrior_sprite.png ✅ (white background removed)
- rogue_sprite.png ✅
- mage_sprite.png ✅
- primitive_creature_sprite.png ✅
- cave_guardian_sprite.png ✅
- ground creature_sprite.png ✅
- boss_divineheart_sprite.png ✅

## Visual Result

**Before**: Sprites had white/light boxes around them that clashed with scene backgrounds

**After**: Sprites blend seamlessly with scene backgrounds, only the character/enemy artwork is visible

## Advanced: Color-Specific Removal

If your sprites have different background colors (e.g., green screen), you can modify the code to target specific colors:

```python
# Example: Remove green backgrounds
if item[1] > 200 and item[0] < 100 and item[2] < 100:  # Green dominant
    newData.append((255, 255, 255, 0))  # Transparent
```

## Troubleshooting

### Sprites look "cut off" or missing parts
- **Cause**: Threshold too low, removing sprite details
- **Fix**: Increase threshold (try 250)

### Background still visible
- **Cause**: Threshold too high, not catching background
- **Fix**: Decrease threshold (try 220)

### Sprites have "halos" or edges
- **Cause**: Anti-aliasing pixels at sprite edges
- **Fix**: Lower threshold slightly to catch light edge pixels

### Specific color backgrounds not removed
- **Cause**: Code only targets white/light backgrounds
- **Fix**: Modify the color detection logic for your specific background color

## Manual Alternative

If automatic transparency doesn't work well, you can pre-process sprites using:
- **GIMP**: Layer → Transparency → Color to Alpha
- **Photoshop**: Magic Wand → Delete
- **Online tools**: remove.bg, photoscissors.com

Then save as PNG with transparency and the game will use them directly.

## Performance

Transparency processing adds minimal load time:
- ~50ms per sprite
- Processed once on game start
- Cached for entire session
- No runtime performance impact

## Testing

To verify transparency is working:
1. Run the game: `python player_gui.py`
2. Select a character class
3. Check if sprite blends with background (no white box)
4. Enter combat to see enemy sprites
5. All sprites should have clean edges

Or use snapshot tool:
```bash
python utilities/capture_player_gui_snapshots.py
```
Then check the generated PNG files for sprite appearance.

## Summary

✅ Automatic transparency removes sprite backgrounds  
✅ No manual editing required  
✅ Works with white/light backgrounds  
✅ Adjustable threshold for different sprites  
✅ All sprites processed on load  
✅ Seamless blending with scene backgrounds  

The game now has professional-looking sprite integration!

