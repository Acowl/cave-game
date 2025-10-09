# SHABUYA Cave Adventure - Quick Reference for AI Assistants

## File Structure

### Main Game Files
- **`player_gui.py`** - Main game implementation (PlayerGameGUI class)
- **`enhanced_gui_final.py`** - Development sandbox GUI (EnhancedGameGUI class)
- **`game_launcher.py`** - Simple launcher script

### Snapshot & Testing Utilities
- **`utilities/capture_player_gui_snapshots.py`** - Generate PlayerGameGUI snapshots
- **`utilities/capture_gui_snapshots.py`** - Generate EnhancedGUI snapshots
- **`utilities/analyze_snapshots.py`** - Analyze snapshot coverage
- **`utilities/autoplay_route.py`** - Automated gameplay testing
- **`utilities/continuity_validator.py`** - Game logic validation
- **`utilities/generate_level_map.py`** - Generate scene graph
- **`utilities/regression.py`** - Full regression suite

### Snapshot Directories
- **`player_gui_snapshots/`** - PlayerGameGUI (actual game) snapshots
- **`gui_snapshots/`** - EnhancedGUI (sandbox) snapshots

### Documentation
- **`AI_SNAPSHOT_GUIDE.md`** - Comprehensive snapshot system guide
- **`QUICK_REFERENCE.md`** - This file
- **`docs/level_map.json`** - Scene graph and relationships
- **`docs/level_map.md`** - Human-readable level map

## Quick Commands

### Generate Snapshots
```bash
# Fast - warrior only (12 snapshots)
python utilities/capture_player_gui_snapshots.py

# Complete - all classes (36+ snapshots)
python utilities/capture_player_gui_snapshots.py --full
```

### Analyze Snapshots
```bash
# View snapshot coverage
python utilities/analyze_snapshots.py

# List all available scenes
python utilities/analyze_snapshots.py --list-scenes

# Get info about a specific scene
python utilities/analyze_snapshots.py --scene primitive_village
```

### Test Game Logic
```bash
# Run automated playthrough
python utilities/autoplay_route.py

# Run full regression suite
python utilities/regression.py
```

### Run the Game
```bash
# Player mode (actual game)
python player_gui.py

# Sandbox mode (development)
python enhanced_gui_final.py

# Via launcher
python game_launcher.py
```

## PlayerGameGUI Structure

### Key Attributes

```python
# Game state
self.player_character        # "warrior", "rogue", or "mage"
self.current_scene          # Current scene name
self.game_state            # "exploring" or "in_combat"
self.player_health         # Current health
self.player_level          # Current level
self.inventory             # List of items

# Combat
self.combat_enemy          # Current enemy name
self.combat_enemy_health   # Enemy health
self.combat_turn          # Turn counter

# Equipment
self.equipped_weapon
self.equipped_armor
self.equipped_accessories
```

### Key Dictionaries

```python
# Scene content
self.scene_descriptions = {
    "cave_entrance": "Description text...",
    "skull_chamber": "Description text...",
    # ... more scenes
}

self.scene_choices = {
    "cave_entrance": [
        {"text": "Choice text", "consequence": "consequence_name"},
        # ... more choices
    ]
}

# Consequence handlers
self.consequences = {
    "consequence_name": {
        "description": "What happens",
        "next_scene": "scene_name",  # Optional
        "combat": "enemy_name",      # Optional
        # ... other effects
    }
}

# Character classes
self.character_classes = {
    "warrior": {
        "health": 120,
        "strength": 15,
        # ... stats
    }
}

# Items and equipment
self.weapons = { ... }
self.items = { ... }
self.enemies = { ... }
```

### Key Methods

```python
# Scene navigation
gui.select_class(character)           # Start game with class
gui.advance_to_scene(scene_name)      # Move to scene
gui.handle_consequence(consequence)   # Trigger consequence

# Combat
gui.start_combat(enemy_name)         # Begin combat
gui.handle_combat_action(choice)     # Take combat action
gui.end_combat()                     # End combat

# Display
gui.show_title_screen()             # Show title screen
gui.show_game_screen()              # Show main game
gui.update_choice_display()         # Refresh choices
```

## Game Flow

### Normal Progression Path

```
Title Screen
    ↓ (select class)
Cave Entrance
    ↓ (enter skull chamber)
Skull Chamber
    ↓ (tunnel collapse)
Cave-in
    ↓ (escape)
Primitive Village
    ↓ (follow creature)
Alley
    ↓ (confront creature)
Combat → Win → Get "Armory Key"
    ↓ (approach armory)
Armory
    ↓ (use armory key)
Get "Chief's House Key"
    ↓ (return to village)
Primitive Village
    ↓ (approach chief's house)
Use "Chief's House Key"
    ↓
Chief's House
    ↓ (advance)
Healing Pool
    ↓ (advance)
Village Changed
```

### Gating System

Some scenes require keys/items:
- **Armory** - Requires "Armory Key" (from alley combat)
- **Chief's House** - Requires "Chief's House Key" (from armory)

The continuity validator checks these gates.

## Common Tasks

### Change Scene Description

```python
# In player_gui.py, find:
self.scene_descriptions = {
    "scene_name": "New description text here",
}
```

### Add New Choice

```python
# In player_gui.py:
self.scene_choices["scene_name"] = [
    {"text": "Choice text", "consequence": "consequence_name"},
    # Add new choice here
]

# Then add the consequence:
self.consequences["consequence_name"] = {
    "description": "What happens",
    "next_scene": "target_scene",  # Optional
}
```

### Modify Enemy Stats

```python
# In player_gui.py:
self.enemies = {
    "Enemy Name": {
        "health": 100,
        "attack": 15,
        "defense": 10,
        "experience": 50,
        "gold": 75
    }
}
```

### Change UI Colors/Layout

```python
# Colors are defined throughout player_gui.py
# Search for hex colors like '#00ff00' to change
# Common color variables:
self.root.configure(bg='#0a0a0a')  # Background
frame.configure(bg='#1a1a1a')      # Frame background
```

## Workflow for AI Assistants

### 1. Understanding Current State

```bash
# Generate snapshots to see current GUI
python utilities/capture_player_gui_snapshots.py

# Analyze what was captured
python utilities/analyze_snapshots.py

# Check the markdown report
# Open: player_gui_snapshots/player_gui_snapshots.md
```

### 2. Making Changes

```python
# Edit player_gui.py
# - Modify scene_descriptions for text changes
# - Modify scene_choices for choice changes
# - Modify consequences for game logic changes
# - Modify class definitions for stats/balance
```

### 3. Verification

```bash
# Regenerate snapshots to see changes
python utilities/capture_player_gui_snapshots.py

# Test gameplay still works
python utilities/autoplay_route.py

# Check for regressions
python utilities/regression.py
```

### 4. Visual Comparison

- Compare old vs new snapshots in `player_gui_snapshots/`
- Check the markdown report for side-by-side view
- Verify all scenes render correctly

## Asset Paths

### Backgrounds
```
assets/backgrounds/
  - cave_entrance.png
  - skull_chamber.png
  - primitive_village.png
  - chiefs_house.png
  - healing_pool.png
  - village_changed.png
  - alley.png
  - armory.png
```

### Sprites
```
assets/sprites/
  - warrior_sprite.png
  - rogue_sprite.png
  - mage_sprite.png
  - primitive_creature_sprite.png
  - cave_guardian_sprite.png
  - ground creature_sprite.png
  - boss_divineheart_sprite.png
```

## Tips for Efficient Development

1. **Always start with snapshots** - See the current state before making changes
2. **Use analyze_snapshots.py** - Quick overview of coverage
3. **Test with autoplay** - Catch logic bugs without manual play
4. **Check level_map.json** - Understand scene relationships
5. **Use --full mode** - When changes affect all character classes
6. **Keep snapshots organized** - Regenerate after each major change
7. **Check the JSON index** - For programmatic access to snapshot data

## Debugging

### Scene Not Displaying Correctly
1. Check `scene_descriptions` for typos
2. Verify asset files exist in correct paths
3. Check console output for loading errors
4. Regenerate snapshots to see current state

### Choices Not Appearing
1. Verify `scene_choices` has entries for the scene
2. Check that consequence names match
3. Ensure `update_choice_display()` is called
4. Use snapshots to verify button rendering

### Navigation Not Working
1. Check `consequences` dictionary
2. Verify `next_scene` points to valid scene
3. Check for gating logic (keys required)
4. Test with autoplay_route.py

### Combat Issues
1. Check `enemies` dictionary
2. Verify combat loop in `handle_combat_action()`
3. Test combat snapshot
4. Check turn counter logic

## Advanced Topics

### Adding New Scenes
1. Add to `scene_descriptions`
2. Add to `scene_choices`
3. Add consequences for navigation
4. Add background image to `assets/backgrounds/`
5. Update snapshot tool if needed
6. Regenerate snapshots to verify

### Modifying Combat System
1. Edit combat-related methods
2. Update enemy definitions
3. Test with combat snapshots
4. Verify with autoplay

### Changing Character Classes
1. Update `character_classes` dict
2. Modify starting equipment
3. Test with snapshots for each class (--full mode)
4. Verify balance with autoplay

## Summary

The snapshot system provides a complete view of the game state without manual navigation. Use it as your primary tool for understanding and modifying the GUI. Always regenerate snapshots after changes to verify your work.

For detailed snapshot system documentation, see `AI_SNAPSHOT_GUIDE.md`.

