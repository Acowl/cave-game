# PlayerGameGUI Snapshots

This directory contains automated screenshots of all major scenes and states in the SHABUYA Cave Adventure PlayerGameGUI.

## Quick Start

### Generate Snapshots

**Windows:**
```cmd
capture_snapshots.bat
```

**Linux/Mac:**
```bash
./capture_snapshots.sh
```

**Direct command:**
```bash
# Fast (warrior only)
python utilities/capture_player_gui_snapshots.py

# Complete (all classes)
python utilities/capture_player_gui_snapshots.py --full
```

### View Snapshots

- **Markdown Report:** Open `player_gui_snapshots.md` in your browser
- **JSON Index:** Use `snapshot_index.json` for programmatic access
- **PNG Files:** All snapshots are saved as PNG images

## Files in This Directory

- **`player_gui_snapshots.md`** - Markdown report with embedded images
- **`snapshot_index.json`** - Machine-readable snapshot index
- **`*.png`** - Individual screenshot files

## Snapshot Naming

Files follow the pattern: `{sequence}_{character}_{scene}.png`

Examples:
- `00_title_screen.png` - Title screen (no character)
- `02_war_cave_entrance.png` - Warrior at cave entrance
- `07_war_combat.png` - Warrior in combat
- `05_rog_primitive_village.png` - Rogue at primitive village

**Character codes:**
- `war` = Warrior
- `rog` = Rogue  
- `mag` = Mage

## Purpose

These snapshots enable:

1. **Visual QA** - Review all game states without manual navigation
2. **AI Assistance** - AI tools can analyze the GUI without playing
3. **Regression Testing** - Compare before/after when making changes
4. **Documentation** - Visual reference for all game scenes
5. **Bug Reporting** - Share exact state when issues occur

## Analyze Snapshots

```bash
# View coverage summary
python utilities/analyze_snapshots.py

# List all scenes
python utilities/analyze_snapshots.py --list-scenes

# Get scene info
python utilities/analyze_snapshots.py --scene primitive_village
```

## For More Information

- **`AI_SNAPSHOT_GUIDE.md`** - Comprehensive guide for AI assistants
- **`QUICK_REFERENCE.md`** - Quick reference for development
- **`utilities/capture_player_gui_snapshots.py`** - Source code

## Regeneration

Snapshots should be regenerated whenever:
- The GUI layout changes
- Scene descriptions are modified
- New scenes are added
- Visual elements are updated
- Before major releases

Simply run the capture script again - it will overwrite existing snapshots.

