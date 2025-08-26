# ��‍☠️ SHABUYA Cave Adventure

A Python adventure game with an enhanced GUI system featuring 7 character sprites, 15+ dynamic backgrounds, and professional game interface.

## ✨ Features

### 🎮 Enhanced GUI System
- **Visual Game Interface**: 1200x800 professional gaming interface
- **7 Character Sprites**: Warrior, Rogue, Mage, Boss, Guardian, and Creatures
- **15+ Dynamic Backgrounds**: Cave entrance, Chief's house, Healing pool, Villages, and more
- **Scene-Dependent Display**: Backgrounds and characters change based on game state
- **Real-Time Controls**: Dropdown menus for instant character/scene/state switching
- **Combat Visualization**: Enemy sprites appear automatically in combat mode
- **Quick Test Scenarios**: Preset combat, treasure, and boss fight tests

### 🎯 Game Mechanics  
- **Multiple Character Classes**: Each with unique sprites and abilities
- **Dynamic Combat System**: Visual turn-based combat with positioning
- **Rich Inventory System**: Weapons, armor, and magical items
- **Multiple Game Scenes**: Explore diverse locations with unique atmospheres
- **State-Dependent Gameplay**: Exploring, Combat, Talking, Inventory modes

## 🚀 Quick Start

### Prerequisites
```bash
# Install required Python packages
pip install -r requirements.txt
```

### Launch Enhanced GUI
```bash
# Option 1: Easy launcher with system checks
./launch_game.sh

# Option 2: Direct launch
python3 enhanced_gui_final.py

# Option 3: Validate system first
python3 validate_system.py
```

## 🧪 Testing Guide

### 1. Character Sprite Testing
1. Launch the Enhanced GUI
2. Use the **Character dropdown** to select different characters:
   - **Warrior** → `warrior_sprite.png`
   - **Rogue** → `rogue_sprite.png`  
   - **Mage** → `mage_sprite.png`
   - **Boss Divine Heart** → `boss_divineheart_sprite.png`
   - **Cave Guardian** → `cave_guardian_sprite.png`
   - **Ground Creature** → `ground creature_sprite.png`
   - **Primitive Creature** → `primitive_creature_sprite.png`
3. Verify each character sprite displays correctly with proper sizing and positioning

### 2. Background Scene Testing
1. Use the **Scene dropdown** to cycle through all available scenes:
   - `cave_entrance` → Cave entrance background
   - `chiefs_house` → Chief's house interior
   - `healing_pool` → Mystical healing pool
   - `primitive_village` → Village scene
   - `primitive_village_cosmic` → Cosmic village variant
   - `skull_chamber` → Dark skull chamber
   - `village_changed` → Modified village
   - And 8+ additional scenes
2. Verify backgrounds load properly and fit the canvas correctly
3. Check image quality and visual consistency

### 3. Game State Testing
1. Use the **State dropdown** to switch between game modes:
   - **Exploring**: Character centered, no enemies visible
   - **In Combat**: Character on left, enemy on right
   - **Talking**: Character positioned for dialogue
   - **Inventory**: Character centered with inventory focus
2. Verify sprite positioning changes appropriately for each state
3. Confirm enemy sprites appear only during combat

### 4. Quick Test Scenarios
Use the preset test buttons to validate complete functionality:

#### ⚔️ Combat Test
- **Scenario**: Warrior vs enemies in skull chamber
- **Expected**: Warrior sprite on left, enemy sprite on right, skull chamber background
- **Verify**: Combat positioning, enemy visibility, scene atmosphere

#### 💰 Treasure Test
- **Scenario**: Rogue exploring chief's house
- **Expected**: Rogue sprite centered, chief's house background, exploration mode
- **Verify**: Exploration positioning, no enemies, treasure hunt atmosphere

#### 🐉 Boss Test
- **Scenario**: Mage vs Divine Heart in cosmic village
- **Expected**: Mage on left, Divine Heart boss on right, cosmic village background
- **Verify**: Boss combat layout, special background, epic battle setup

## 📁 Project Structure

```
cave-game/
├── enhanced_gui_final.py          # Main Enhanced GUI System
├── launch_game.sh                 # Easy launcher with system checks
├── validate_system.py             # System validation tool
├── requirements.txt               # Python dependencies
├── LAUNCH_AND_TEST_GUIDE.md       # Detailed testing instructions
├── assets/                        # All game assets
│   ├── sprites/                   # Character sprite images
│   └── backgrounds/              # Scene background images
├── src/                          # Source code modules
│   ├── core/                     # Game engine components
│   ├── entities/                 # Game objects (player, items)
│   └── interfaces/               # UI components
├── tests/                        # Testing scripts
├── tools/                        # Development utilities
├── docs/                         # Documentation
└── build/                        # Build artifacts
```

## 🎮 Usage Instructions

### Enhanced GUI Controls

**Character Selection**
- Use the Character dropdown to choose your player character
- Each character has a unique sprite and visual style
- Character choice affects combat positioning and abilities

**Scene Selection**  
- Use the Scene dropdown to change the current location
- Each scene has a unique background image and atmosphere
- Scene choice affects available enemies and interactions

**Game State Control**
- Use the State dropdown to switch between game modes
- **Exploring**: Standard adventure mode with centered character
- **In Combat**: Battle mode with character and enemy positioning  
- **Talking**: Dialogue mode with appropriate character placement
- **Inventory**: Item management mode

**Quick Test Buttons**
- **Combat Test**: Instantly set up a warrior vs enemy battle
- **Treasure Test**: Set up a rogue treasure hunting scenario
- **Boss Test**: Launch an epic mage vs boss battle

### Asset Information Panel
The right sidebar displays:
- Current configuration (scene/character/state)
- Expected asset files for current setup
- Total loaded assets count
- Asset loading status and confirmations

## 🔧 Technical Details

### Requirements
- **Python 3.8+**
- **tkinter** (GUI framework)
- **Pillow (PIL)** (Image processing)
- **All dependencies in requirements.txt**

### Asset Specifications
- **Sprite Images**: 150x150 pixels, PNG format
- **Background Images**: 900x650 pixels, PNG format  
- **File Naming**: Descriptive names with underscores
- **Asset Loading**: Automatic with error handling

### Performance Notes
- Assets are cached in memory for fast switching
- Image resizing is handled automatically
- GUI updates are optimized for smooth transitions
- Error handling prevents crashes from missing assets

## 🏆 Current Status

**✅ FULLY IMPLEMENTED:**
- All 7 character sprites integrated and functional
- 15+ background scenes processed and available
- Enhanced GUI with professional interface design
- Scene-dependent sprite and background display
- Combat and exploration mode visualization
- Real-time asset information and status display
- Comprehensive testing framework
- Professional project organization

**🎯 READY FOR:** Complete gameplay testing and player use

## 🚀 Launch Commands

```bash
# Easy launcher (recommended)
./launch_game.sh

# Direct launch
python3 enhanced_gui_final.py

# System validation
python3 validate_system.py
```

## 📊 Testing Checklist

- [ ] All 7 character sprites load correctly
- [ ] All 15+ background scenes display properly
- [ ] Character/scene dropdown menus work
- [ ] Game state changes affect sprite positioning
- [ ] Combat mode shows both player and enemy
- [ ] Quick test buttons function correctly
- [ ] Asset info panel updates in real-time
- [ ] Console shows successful asset loading

## 🎉 Success!

**INTEGRATION COMPLETE** - All systems operational and ready for gameplay testing!

---

**👑 Status**: READY FOR COMPLETE GAMEPLAY TESTING!
