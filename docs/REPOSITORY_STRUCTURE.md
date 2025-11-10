# Repository Structure - Post-Cleanup

Updated: 2025-01-15

## Overview

This document describes the cleaned and organized repository structure after the multi-agent cleanup initiative.

## Root Directory Structure

```
cave-game/
├── .cursor/                    # Multi-agent coordination files
│   ├── agents/                 # Agent role definitions
│   ├── tasks/                  # Task tracking (ACTIVE, COMPLETED, BLOCKED)
│   ├── COMMUNICATION.md        # Communication protocol
│   └── AGENT_QUICK_REF.md      # Quick reference guide
│
├── .cursorrules                # Project-wide context for agents
│
├── assets/                     # Game assets (optimized)
│   ├── backgrounds/            # Scene backgrounds (400x300 PNG)
│   ├── icons/                  # Game icons
│   └── sprites/                # Character sprites (64x64 PNG)
│
├── distribution/               # Core game modules
│   ├── combat.py               # Combat system
│   ├── config.py               # Game configuration constants
│   ├── game_refactored.py      # Core game engine
│   ├── gui.py                  # Distribution GUI
│   ├── gui_diagnostic.py       # Diagnostic tools
│   ├── item.py                 # Item and inventory system
│   ├── main.py                 # Distribution entry point
│   ├── player.py               # Player character system
│   ├── scenes.py               # Scene management
│   └── ui.py                   # Text-based UI
│
├── docs/                       # Documentation
│   ├── assets/                 # Asset documentation
│   ├── development/            # Development guides
│   ├── distribution/           # Distribution docs
│   ├── gui_snapshots/          # GUI screenshots (moved here)
│   ├── guides/                 # User guides
│   ├── multi-agent/            # Multi-agent workflow docs
│   ├── reports/                # Project reports
│   └── specifications/         # Feature specifications
│
├── tests/                      # Test suite
│   ├── assets/                 # Test data files
│   ├── integration/            # Integration tests
│   └── unit/                   # Unit tests
│
├── utilities/                  # Development utilities
│   ├── analyze_for_cleanup.py  # Cleanup analysis tool
│   ├── autoplay_route.py       # Automated playthrough
│   ├── check_agent_conflicts.py # Conflict detection
│   ├── validate_integration.py # Integration validation
│   └── [other utilities]
│
├── player_gui.py               # Main player GUI (1,550+ lines)
├── game_launcher.py            # Game launcher
├── enhanced_gui_final.py       # Development GUI
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview
├── MVP_ROADMAP.md              # Development roadmap
└── MANUAL_TEST_GUIDE.md        # Testing guide
```

## Key Changes from Cleanup

### Duplicate Files Removed
- ✅ Duplicate background images (6 files removed)
  - `cave entrance.png` → kept `cave_entrance.png`
  - `primitive village.png` → kept `primitive_village.png`
  - `primitive viillage (cosmic).png` → removed
  - `chiefs house.png` → kept `chief_house.png`
  - `healing pool.png` → kept `healing_pool.png`
  - `skull chamber.png` → kept `skull_chamber.png`

### Python Cache Cleaned
- ✅ Removed `__pycache__/` directories
- ✅ `.gitignore` already configured to exclude future cache files

### Organization Improvements
- ✅ Moved `gui_snapshots/` → `docs/gui_snapshots/` (documentation assets)
- ✅ Moved `test_scene_choices.py` → `tests/unit/` (proper test organization)

### Scene System Fixed
- ✅ Added revisit logic (`self.seen_scenes` tracking)
- ✅ Created revisit descriptions for all 9 scenes
- ✅ First-time descriptions now only show once per session

## Module Organization

### No Duplicates Found
Initial analysis suggested duplicate modules between root and `distribution/`, but verification confirms:
- **All core modules exist only in `distribution/`**
- Root-level files are appropriately placed:
  - `player_gui.py` - Main player interface (primary entry point)
  - `game_launcher.py` - Launcher (user-facing entry point)
  - `enhanced_gui_final.py` - Development GUI (dev tool)

This organization is **correct** and requires no consolidation.

## Agent Responsibilities

### File Ownership (Quick Reference)
- **UI Agent**: `player_gui.py`, `game_launcher.py`, `enhanced_gui_final.py`
- **Combat Agent**: `distribution/combat.py`
- **Inventory Agent**: `distribution/item.py`
- **Scene Agent**: `distribution/scenes.py`
- **Testing Agent**: `tests/`, `utilities/` (testing tools)
- **Documentation Agent**: `docs/`, README files
- **Assets Agent**: `assets/` directory

### Shared State Files (Require Coordination)
- `distribution/config.py` - All agents
- `distribution/player.py` - Combat & Inventory agents
- `player_gui.py` (shared sections) - UI, Combat, Inventory agents

## Asset Standards

### Background Images
- Format: 400x300 PNG
- Naming: snake_case (e.g., `cave_entrance.png`)
- Location: `assets/backgrounds/`
- All scenes have valid, non-corrupted backgrounds ✅

### Character Sprites
- Format: 64x64 PNG with transparency
- Naming: `{character}_sprite.png`
- Location: `assets/sprites/`
- 7 sprites available (3 player classes + 4 enemies)

## Documentation Structure

### Multi-Agent Documentation
- `MULTI_AGENT_GUIDE.md` - Comprehensive workflow guide
- `AGENT_ONBOARDING.md` - Quick start for new agents
- `FILE_OWNERSHIP.md` - File ownership matrix
- `DEPENDENCY_MAP.md` - Module dependencies
- `INTEGRATION_POINTS.md` - Interface contracts
- `RESTRUCTURE_PLAN.md` - Restructuring recommendations
- `SCENE_AUDIT.md` - Scene analysis and status

### Development Documentation
- `MVP_ROADMAP.md` - Development priorities
- `MANUAL_TEST_GUIDE.md` - Testing procedures
- `README.md` - Project overview
- `docs/development/` - Development guides

## Build Artifacts

### Excluded from Git
- `__pycache__/` - Python bytecode cache
- `*.pyc` - Compiled Python files
- `.pytest_cache/` - Pytest cache
- Virtual environment directories

### Automation Outputs
- `.cursor/analysis_report.json` - Cleanup analysis results
- `docs/gui_snapshots/` - GUI screenshots for documentation

## Clean State Checklist

- ✅ No duplicate asset files
- ✅ No Python cache directories
- ✅ All scenes have descriptions
- ✅ All scenes have background images
- ✅ Revisit logic implemented
- ✅ Documentation organized under `docs/`
- ✅ Tests organized under `tests/`
- ✅ Clear agent responsibilities defined
- ✅ Conflict detection tools in place
- ✅ Integration validation tools in place

## Next Steps (Optional Enhancements)

1. **Create `src/` Directory (Future)**
   - If project grows significantly, consider moving core code to `src/`
   - Would require updating imports and tooling

2. **Consolidate Launch Scripts**
   - Multiple launch methods exist (`.sh`, `.bat`, Python scripts)
   - Could be unified into a single cross-platform launcher

3. **Asset Metadata File**
   - Create `docs/assets/backgrounds.md` mapping scenes to backgrounds
   - Document scene-to-asset relationships

4. **Automated Cleanup Script**
   - PowerShell/Bash script to clean cache files before packaging
   - Could be run by agents before distribution builds

## Maintenance

### Regular Cleanup Tasks
- Remove `__pycache__/` directories periodically (or rely on `.gitignore`)
- Update `docs/multi-agent/SCENE_AUDIT.md` when scenes change
- Keep `FILE_OWNERSHIP.md` updated when responsibilities shift

### Multi-Agent Coordination
- Check `ACTIVE_TASKS.md` before starting work
- Run `check_agent_conflicts.py` before commits
- Run `validate_integration.py` after changes
- Update `COMPLETED_TASKS.md` when finishing work

## Conclusion

The repository is now well-organized with:
- Clear separation of concerns
- No duplicate or unnecessary files
- Proper documentation organization
- Multi-agent workflow support
- Clean, maintainable structure

All core functionality is preserved while improving organization and enabling efficient parallel development.

