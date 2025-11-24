# 🎨 SHABUYA AI Asset Generation & Processing Workflow

This guide explains how to generate AI art and automatically process it in the repository without manual file management.

## 📁 Directory Structure

```
cave-game/
├── ai_generated_assets/          # Upload AI-generated images here
│   ├── characters/              # Character sprites go here
│   ├── scenes/                  # Background scenes go here
│   ├── items/                   # Future: Item icons
│   ├── effects/                 # Future: Spell/combat effects
│   └── processed/               # Auto-moved after processing
├── game_assets/                 # Final processed game assets
│   ├── sprites/                 # Character sprites (64x64)
│   └── backgrounds/             # Scene backgrounds (400x300)
├── COMPLETE_AI_PROMPTS.md       # All AI generation prompts
└── automated_asset_processor.py # Automated processing script
```

## 🚀 Complete Workflow

### Step 1: Generate AI Art

1. **Open `COMPLETE_AI_PROMPTS.md`** in the repository
2. **Choose an asset to generate** (warrior, cave_entrance, etc.)
3. **Copy the full prompt** for your chosen asset
4. **Use with your preferred AI tool:**
   - DALL-E 3 (OpenAI)
   - Midjourney
   - Stable Diffusion
   - Adobe Firefly

### Step 2: Upload to Repository

1. **Download the generated image** from your AI tool
2. **Rename the file** to match the asset name:
   - Character: `warrior.png`, `rogue.png`, `mage.png`, etc.
   - Scene: `cave_entrance.png`, `skull_chamber.png`, etc.
3. **Upload to the correct folder:**
   - Characters → `ai_generated_assets/characters/`
   - Scenes → `ai_generated_assets/scenes/`

### Step 3: Automatic Processing

1. **Run the automated processor:**
   ```bash
   python automated_asset_processor.py
   ```

2. **The script will automatically:**
   - ✅ Find your uploaded images
   - ✅ Identify what asset they represent
   - ✅ Resize to correct dimensions
   - ✅ Convert to proper format (RGBA/RGB)
   - ✅ Backup any existing assets
   - ✅ Move to correct game directories
   - ✅ Generate a processing report

### Step 4: Test Results

1. **Run the GUI diagnostic:**
   ```bash
   python gui_diagnostic.py
   ```

2. **Check that your new assets appear correctly**

3. **If satisfied, commit the changes:**
   ```bash
   git add .
   git commit -m "🎨 Updated assets with AI-generated art"
   git push origin main
   ```

## 📝 Asset Naming Guide

For automatic recognition, name your files exactly as follows:

### Character Assets (upload to `ai_generated_assets/characters/`)
- `warrior.png` - Medieval warrior sprite
- `rogue.png` - Stealthy assassin sprite  
- `mage.png` - Mystical wizard sprite
- `primitive_creature.png` - Tribal enemy
- `divine_heart.png` - Mystical floating heart
- `cave_guardian.png` - Stone guardian boss

### Scene Assets (upload to `ai_generated_assets/scenes/`)
- `cave_entrance.png` - Cave mouth entrance
- `skull_chamber.png` - Ancient bone chamber
- `primitive_village.png` - Tribal village
- `alley.png` - Village alley passage
- `armory.png` - Weapons storage area
- `chief_house.png` - Village leader's dwelling
- `healing_pool.png` - Sacred healing waters
- `village_changed.png` - Mystically transformed village
- `menu.png` - Main menu background

## 🎯 AI Prompt Examples

### Character Example (Warrior):
```
16-bit pixel art character sprite, medieval warrior, heavy plate armor with bronze trim, large sword and shield, determined expression, brown and bronze color scheme, standing pose facing forward, 64x64 pixels, transparent background, detailed shading, retro RPG game style
```

### Scene Example (Cave Entrance):
```
16-bit pixel art background, mysterious cave entrance, rocky cliff face, dark opening with subtle internal glow, ancient stone formations, moss and vines, earthy brown and green color palette, 400x300 pixels, atmospheric perspective, detailed rock textures
```

## 🔧 Troubleshooting

### If asset isn't recognized:
1. Check the filename matches exactly (case-insensitive)
2. Ensure file is in the correct directory
3. Make sure file is PNG format
4. Run the processor again

### If processing fails:
1. Check the `asset_processing_report.md` for error details
2. Verify image file isn't corrupted
3. Ensure image has reasonable dimensions
4. Try re-uploading the file

### If GUI doesn't show updates:
1. Ensure you're running from the correct directory
2. Check that files exist in `game_assets/sprites/` or `game_assets/backgrounds/`
3. Try force-refreshing by restarting the GUI diagnostic

## 🚀 Future Expansion

This system is ready for expansion with:
- **NPCs**: Village elders, merchants, guards
- **Items**: Weapons, armor, potions, scrolls  
- **Effects**: Spell animations, impact effects
- **UI Elements**: Buttons, icons, frames

Simply add prompts to the system and upload to the appropriate directories!

## 📊 Processing Reports

Each run generates `asset_processing_report.md` with:
- ✅ Successfully processed assets
- ❌ Failed processing attempts with error details
- 📁 Where files were moved
- 💾 Backup information

## 🎮 Testing Workflow

1. **Generate 1-2 key assets** (warrior + cave_entrance recommended)
2. **Upload and process** using the automated system
3. **Test in GUI diagnostic** to see visual improvement
4. **Generate remaining assets** based on results
5. **Process in batches** for efficiency

This workflow eliminates manual file management and ensures consistent, automated asset integration!
