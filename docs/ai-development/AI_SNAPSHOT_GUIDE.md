# AI Assistant Snapshot System Guide

## Overview

This guide explains how AI assistants can use the automated snapshot system to analyze and modify the SHABUYA Cave Adventure GUI without manually playing through the game.

## Quick Start

### Generate Fresh Snapshots

```bash
# Generate snapshots for warrior class only (fast, ~13 snapshots)
python utilities/capture_player_gui_snapshots.py

# Generate snapshots for all classes (comprehensive, ~37 snapshots)
python utilities/capture_player_gui_snapshots.py --full
```

### View Snapshots

After generation, snapshots are saved to:
- **Directory:** `player_gui_snapshots/`
- **Report:** `player_gui_snapshots/player_gui_snapshots.md` (markdown with embedded images)
- **Index:** `player_gui_snapshots/snapshot_index.json` (machine-readable index)

## What Gets Captured

The snapshot tool captures every major scene and game state:

### Scenes Captured
1. **Title Screen** - Class selection interface
2. **Cave Entrance** - Starting location
3. **Skull Chamber** - First exploration area
4. **Cave-in** - Action sequence
5. **Primitive Village** - Main hub area
6. **Alley** - Side area with encounters
7. **Combat** - Battle interface
8. **Armory** - Loot/equipment area
9. **Chief's House** - Story progression
10. **Healing Pool** - Special location
11. **Village Changed** - Late-game state

### For Each Scene
- Full window capture showing layout
- UI elements in their actual state
- Character sprites rendered
- Background images loaded
- All text and dialogue visible
- Stats and inventory displayed

## Using Snapshots for Development

### For UI/UX Changes

1. **Review the snapshots** to see current state
2. **Identify the issue** (layout, colors, text, etc.)
3. **Make changes** to `player_gui.py`
4. **Re-generate snapshots** to verify changes
5. **Compare before/after** using the markdown reports

### For Content Changes

1. **Find the relevant scene** in snapshots
2. **Locate the code** in `player_gui.py`:
   - Scene descriptions: `self.scene_descriptions` dict
   - Choices: `self.scene_choices` dict
   - Consequences: `self.consequences` dict
3. **Make changes** to text, choices, or logic
4. **Re-generate snapshots** to verify

### For Bug Fixes

1. **Reproduce the bug** using autoplay: `python utilities/autoplay_route.py`
2. **Check snapshots** for the problematic state
3. **Fix the code** in `player_gui.py`
4. **Verify with snapshots** and autoplay

## Snapshot File Naming Convention

Files are named with a pattern: `{sequence}_{character}_{scene}.png`

Examples:
- `00_title_screen.png` - Title screen (no character yet)
- `02_war_cave_entrance.png` - Warrior at cave entrance
- `07_war_combat.png` - Warrior in combat
- `05_rog_primitive_village.png` - Rogue at primitive village (full mode)

**Character abbreviations:**
- `war` = Warrior
- `rog` = Rogue
- `mag` = Mage

## Advanced Usage

### Custom Snapshot Sets

You can modify `utilities/capture_player_gui_snapshots.py` to add custom snapshots:

```python
def setup_custom_state(gui: PlayerGameGUI, character: str) -> None:
    """Setup: Your custom game state."""
    gui.select_class(character)
    # Add your navigation logic here
    gui.handle_consequence("some_consequence")
    gui.root.update()
```

Then add it to `_build_snapshot_plans()`.

### Automated Testing

Combine snapshots with the autoplay system:

```bash
# Run autoplay to test game progression
python utilities/autoplay_route.py

# Generate snapshots to verify visual state
python utilities/capture_player_gui_snapshots.py

# Run regression tests
python utilities/regression.py
```

### CI/CD Integration

Snapshots can be generated automatically in CI/CD pipelines:

```yaml
# Example: .github/workflows/regression.yml
- name: Generate GUI Snapshots
  run: python utilities/capture_player_gui_snapshots.py
  
- name: Upload Snapshots
  uses: actions/upload-artifact@v3
  with:
    name: gui-snapshots
    path: player_gui_snapshots/
```

## Snapshot Output Reference

### Markdown Report (`player_gui_snapshots.md`)

Contains:
- Total snapshot count
- Description of each snapshot
- Embedded images for easy viewing
- Organized by sequence number

### JSON Index (`snapshot_index.json`)

Machine-readable index with:
```json
{
  "total_snapshots": 12,
  "snapshots": [
    {
      "filename": "00_title_screen.png",
      "description": "Title screen with class selection",
      "path": "00_title_screen.png"
    }
  ]
}
```

## Tips for AI Assistants

1. **Always generate fresh snapshots** when starting work on GUI changes
2. **Check multiple scenes** - a change in one place may affect others
3. **Use the JSON index** for programmatic access to snapshot data
4. **Compare snapshots** before and after changes to verify improvements
5. **Use full mode** (`--full`) when making changes that affect all character classes
6. **Regenerate after major changes** to catch unintended side effects

## Troubleshooting

### Snapshot generation fails
- Ensure you have Pillow installed: `pip install Pillow`
- Check that you have a display (required for ImageGrab)
- On headless systems, use `xvfb-run` (Linux) or similar

### Snapshots look wrong
- Increase `--delay-ms` to allow more time for rendering
- Check that assets (backgrounds, sprites) are properly loaded
- Verify `player_gui.py` has no errors before capturing

### Missing scenes
- Check that the scene exists in `player_gui.py`
- Verify the navigation path in setup functions
- Add debug print statements if needed

## Related Tools

- **`autoplay_route.py`** - Automated gameplay testing
- **`continuity_validator.py`** - Game logic validation
- **`generate_level_map.py`** - Scene graph generation
- **`regression.py`** - Full regression test suite

## Example Workflow

Here's a complete workflow for making UI changes:

```bash
# 1. Generate baseline snapshots
python utilities/capture_player_gui_snapshots.py

# 2. Make your changes to player_gui.py
# (edit the file as needed)

# 3. Generate new snapshots
python utilities/capture_player_gui_snapshots.py

# 4. Compare the markdown reports
# Open player_gui_snapshots/player_gui_snapshots.md in a browser

# 5. Test gameplay still works
python utilities/autoplay_route.py

# 6. Run full regression if needed
python utilities/regression.py
```

## Summary

The snapshot system provides:
- **No manual navigation** required - automated state setup
- **Complete coverage** - all scenes, all characters (in full mode)
- **Visual verification** - actual rendered output
- **Fast iteration** - regenerate in seconds
- **AI-friendly** - structured output for analysis

This allows AI assistants to work on the GUI confidently without needing to manually play through the game to reach each state.

