# SHABUYA Cave Adventure - Complete Asset List

## 🎯 **COMPREHENSIVE GRAPHICS ASSET REQUIREMENTS**

Based on codebase analysis, here's the complete list of all sprites and graphics needed for SHABUYA Cave Adventure:

---

## 📦 **CURRENT ASSETS (Already Created)**
✅ **Character Sprites (64x64)**:
- `warrior_sprite.png` - Tank class (brown/gold)
- `rogue_sprite.png` - Agility class (green) 
- `mage_sprite.png` - Magic class (purple)
- ~~`enemy_sprite.png` - Generic enemy (deprecated)~~

✅ **Scene Backgrounds (400x300)**:
- `cave_entrance.png` - Rocky entrance scene
- `skull_chamber.png` - Dark mysterious chamber
- `primitive_village.png` - Village with hut structures  
- `menu.png` - Main menu background

✅ **Icons**:
- `shabuya_icon.png` - Game icon (64x64)
- `shabuya_icon.ico` - Windows format

---

## 🚨 **MISSING ASSETS NEEDED**

### 👾 **Enemy Sprites (64x64 PNG with transparency)**

#### **Primary Enemies:**
1. **`primitive_creature_sprite.png`** 
   - **Description**: Ground-dwelling primitive creature that appears in alley and skull chamber
   - **Appearance**: Small, agile, earth-toned creature with claws that bursts from burrows
   - **AI Prompt**: `pixel art primitive creature sprite, 64x64 pixels, primitive ground-dwelling monster, earth brown colors, burrow creature with claws, RPG enemy sprite, transparent background, retro gaming style`

2. **`divine_heart_sprite.png`** 
   - **Description**: Final boss - cosmic horror entity
   - **Appearance**: Otherworldly, pulsing heart-like entity with cosmic energy
   - **AI Prompt**: `pixel art divine heart boss sprite, 64x64 pixels, cosmic horror final boss, pulsing heart entity, cosmic energy aura, dark purple and red colors, RPG boss sprite, transparent background, retro gaming aesthetic`

#### **Additional Enemy Variants:**
3. **`cave_guardian_sprite.png`**
   - **Description**: Armory guardian/protector enemy
   - **Appearance**: Stone/bone armored guardian
   - **AI Prompt**: `pixel art cave guardian sprite, 64x64 pixels, stone and bone armored guardian, ancient protector, gray and tan colors, RPG guardian enemy, transparent background, retro gaming style`

### 🏞️ **Additional Scene Backgrounds (400x300 PNG)**

#### **Core Missing Scenes:**
5. **`alley.png`**
   - **Description**: Narrow shadowy alley between stone walls (major combat location)
   - **AI Prompt**: `pixel art alley scene, 400x300 resolution, narrow shadowy alley between ancient stone walls, dark atmospheric lighting, medieval cave setting, RPG background, retro gaming style`

6. **`armory.png`**
   - **Description**: Ancient armory with enhanced weapons (major location)
   - **AI Prompt**: `pixel art armory scene, 400x300 resolution, ancient weapon armory chamber, stone walls with weapon racks, medieval fantasy setting, atmospheric lighting, RPG background`

7. **`chief_house.png`**
   - **Description**: Imposing dwelling of tribal chief (major location)
   - **AI Prompt**: `pixel art chief house interior, 400x300 resolution, tribal chief dwelling, primitive hut interior with trophies, bone and hide decorations, RPG background, atmospheric lighting`

8. **`healing_pool.png`**
   - **Description**: Sacred chamber with mystical healing waters
   - **AI Prompt**: `pixel art healing pool chamber, 400x300 resolution, sacred chamber with glowing mystical healing waters, stone architecture, magical atmosphere, RPG background, retro gaming style`

9. **`village_changed.png`**
   - **Description**: Village after cosmic awakening (post-blessing scene)
   - **AI Prompt**: `pixel art transformed village, 400x300 resolution, primitive village after cosmic awakening, mystical energy effects, changed atmosphere, post-blessing scene, RPG background`

### 🎮 **Enhanced UI Elements (Optional but Recommended)**

#### **Weapon Icons (32x32 PNG with transparency):**
10. **`dagger_icon.png`** - Basic rogue weapon
11. **`axe_icon.png`** - Basic warrior weapon  
12. **`wand_icon.png`** - Basic mage weapon
13. **`shadow_blade_icon.png`** - Enhanced dagger
14. **`bone_crusher_icon.png`** - Enhanced axe
15. **`skull_scepter_icon.png`** - Enhanced wand

#### **Item Icons (32x32 PNG with transparency):**
16. **`armory_key_icon.png`** - Key to armory
17. **`town_key_icon.png`** - Key to chief's house
18. **`health_potion_icon.png`** - Healing item

#### **Status Effect Icons (24x24 PNG):**
19. **`level_up_icon.png`** - Level up indicator
20. **`blessing_icon.png`** - Sacred blessing effect
21. **`victory_icon.png`** - Victory celebration

### 🎨 **Battle/Combat Graphics (Optional Enhancement)**

#### **Combat Effect Sprites (64x64 PNG):**
22. **`sword_slash_effect.png`** - Weapon attack effect
23. **`magic_blast_effect.png`** - Magic attack effect
24. **`stealth_strike_effect.png`** - Rogue attack effect
25. **`divine_energy_effect.png`** - Final boss attack effect

#### **Environmental Details (Various sizes):**
26. **`fire_pit_sprite.png`** (32x32) - Village fire pit
27. **`skull_decoration.png`** (48x48) - Skull chamber decoration
28. **`cave_crystal.png`** (24x24) - Healing pool crystals

---

## 🎯 **PRIORITY IMPLEMENTATION ORDER**

### **Phase 1: Critical Missing Assets (High Priority)**
1. `primitive_creature_sprite.png` - Primary enemy (appears in alley and skull chamber)
2. `divine_heart_sprite.png` - Final boss
3. `alley.png` - Major combat scene
4. `armory.png` - Important location
5. `chief_house.png` - Story location

### **Phase 2: Scene Completion (Medium Priority)**
6. `healing_pool.png` - Healing location
7. `village_changed.png` - End game scene
8. `cave_guardian_sprite.png` - Additional enemy

### **Phase 3: UI Enhancement (Lower Priority)**
9. Weapon icons (6 total)
10. Item icons (3 total)
11. Status effect icons (3 total)

### **Phase 4: Visual Polish (Optional)**
12. Combat effect sprites
13. Environmental details
14. Particle effects

---

## 📋 **IMPLEMENTATION WORKFLOW**

### **For Each Asset:**
1. **Generate using AI** with provided prompts
2. **Verify dimensions** (64x64 for sprites, 400x300 for backgrounds)
3. **Test in-game** using `replace_assets.py`
4. **Adjust if needed** for visual consistency
5. **Update asset manifest** when complete

### **Testing Checklist:**
- ✅ Sprite displays correctly in character selection
- ✅ Background shows properly in scene transitions
- ✅ Colors match game aesthetic
- ✅ Transparency works for sprites
- ✅ No visual glitches or artifacts

---

## 📊 **ASSET STATISTICS**

**Total Assets Needed**: 28 (not including current 9)
**Character Sprites**: 4 additional (8 total)
**Scene Backgrounds**: 5 additional (9 total) 
**UI Elements**: 12 additional
**Effects**: 7 additional

**Estimated Generation Time**: 2-3 hours for priority assets
**File Size**: ~200KB total for all assets
**Impact**: Complete visual game experience

---

## 🎨 **STYLE GUIDE**

### **Color Palette:**
- **Earth Tones**: Browns, tans, grays for cave environments
- **Character Classes**: 
  - Warrior: Brown/Gold
  - Rogue: Dark/Light Green  
  - Mage: Purple/Violet
- **Enemies**: Reds, dark grays, earth tones
- **Magic/Divine**: Purple, gold, white energy effects

### **Art Style:**
- **Pixel Art**: 16-bit retro gaming aesthetic
- **Limited Palette**: 8-16 colors per sprite for authentic feel
- **Clean Lines**: Clear, readable details despite small size
- **Consistent Lighting**: Match existing cave/underground theme

This comprehensive list ensures every visual element in the game has proper graphics representation!
