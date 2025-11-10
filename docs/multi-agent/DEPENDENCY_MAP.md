# Module Dependency Map

This document visualizes module dependencies and critical integration points to help agents understand how their work connects and where coordination is needed.

## Dependency Graph

```
player_gui.py (UI Agent)
├── distribution/combat.py (Combat Agent)
│   ├── distribution/config.py (SHARED - requires coordination)
│   ├── distribution/item.py (Inventory Agent)
│   └── distribution/player.py (SHARED - requires coordination)
├── distribution/scenes.py (Scene Agent)
│   ├── distribution/config.py (SHARED - requires coordination)
│   └── distribution/player.py (SHARED - requires coordination)
├── distribution/item.py (Inventory Agent)
│   └── distribution/player.py (SHARED - requires coordination)
└── assets/ (Assets Agent)

distribution/combat.py (Combat Agent)
├── distribution/config.py (SHARED - requires coordination)
├── distribution/item.py (Inventory Agent)
│   └── distribution/player.py (SHARED - requires coordination)
└── distribution/player.py (SHARED - requires coordination)

distribution/item.py (Inventory Agent)
└── distribution/player.py (SHARED - requires coordination)

distribution/scenes.py (Scene Agent)
├── distribution/config.py (SHARED - requires coordination)
└── distribution/player.py (SHARED - requires coordination)

distribution/player.py (SHARED STATE - all agents)
├── Used by: Combat Agent, Inventory Agent, Scene Agent, UI Agent
└── Modifications require coordination

distribution/config.py (SHARED STATE - all agents)
├── Used by: Combat Agent, Scene Agent, UI Agent
└── Modifications require coordination
```

## Critical Integration Points

### 1. player_gui.py - Central Integration Hub
**Location**: Root directory
**Agent**: UI Agent (primary), Combat Agent (secondary), Inventory Agent (secondary)

**Dependencies**:
- Imports combat functions from `distribution/combat.py`
- Uses player state from `distribution/player.py`
- Uses items from `distribution/item.py`
- Displays scenes from scene data

**Coordination Required**:
- UI Agent must coordinate with Combat Agent for combat UI changes
- UI Agent must coordinate with Inventory Agent for inventory UI changes
- Changes to player_gui.py structure affect multiple agents

**Interface Contracts**:
- Combat state dict structure (UI ↔ Combat)
- Inventory structure (UI ↔ Inventory)
- Player state structure (all agents)

### 2. distribution/config.py - Shared Configuration
**Location**: `distribution/config.py`
**Agent**: All agents (SHARED STATE - requires coordination)

**Constants Defined**:
- `STAT_REQUIREMENT` - Used by Combat Agent
- `STARTING_STAT_VALUE` - Used by Player initialization
- `LEVEL_UP_POINTS` - Used by progression system
- `FINAL_BOSS_STAT_REQUIREMENT` - Used by Combat Agent
- `SCENE_NAMES` - Used by Scene Agent
- `MESSAGES` - Used by UI Agent

**Coordination Required**:
- ANY changes to config.py require coordination with ALL agents
- Must document changes in `.cursor/comms/change_log.md`
- Must update all affected modules

**Interface Contracts**:
- Config constants must remain consistent
- New constants must be documented
- Removed constants must be coordinated

### 3. distribution/player.py - Shared Player State
**Location**: `distribution/player.py`
**Agent**: Combat Agent (modify), Inventory Agent (modify), UI Agent (read)

**Player Attributes**:
- `health` - Modified by Combat Agent
- `strength`, `agility`, `intelligence` - Modified by Combat Agent
- `level` - Modified by progression system
- `inventory` - Modified by Inventory Agent
- `weapon` - Modified by Inventory Agent

**Coordination Required**:
- Combat Agent modifications must coordinate with Inventory Agent
- Inventory Agent modifications must coordinate with Combat Agent
- UI Agent only reads player state (no modifications)

**Interface Contracts**:
- Player class structure must remain consistent
- Attribute changes must be coordinated
- Method signatures must not break

### 4. distribution/combat.py - Combat System
**Location**: `distribution/combat.py`
**Agent**: Combat Agent (primary)

**Dependencies**:
- `distribution/config.py` - Stat requirements
- `distribution/item.py` - Weapon definitions
- `distribution/player.py` - Player stats

**Exports**:
- `execute_weapon_attack(player, weapon)` - Used by UI Agent
- `execute_class_ability_final_boss(player)` - Used by UI Agent
- `check_weapon_effectiveness(player, weapon)` - Used by UI Agent

**Coordination Required**:
- Function signature changes must coordinate with UI Agent
- Weapon stat changes must coordinate with Inventory Agent
- Player stat changes must coordinate with other agents

**Interface Contracts**:
- Combat functions return (success: bool, message: str)
- Damage calculations use player stats and weapon stats
- Combat state structure must match UI expectations

### 5. distribution/item.py - Item System
**Location**: `distribution/item.py`
**Agent**: Inventory Agent (primary)

**Dependencies**:
- `distribution/player.py` - Player type checking

**Exports**:
- `Weapon` class - Used by Combat Agent
- `Inventory` class - Used by Scene Agent and UI Agent
- Weapon instances (dagger, axe, wand, enhanced versions)

**Coordination Required**:
- Weapon stat changes must coordinate with Combat Agent
- Inventory structure changes must coordinate with UI Agent
- Item placement changes must coordinate with Scene Agent

**Interface Contracts**:
- Weapon.get_damage(player) returns int
- Inventory.has_item(name) returns bool
- Inventory.add_item(item) modifies inventory

### 6. distribution/scenes.py - Scene System
**Location**: `distribution/scenes.py`
**Agent**: Scene Agent (primary), Inventory Agent (secondary)

**Dependencies**:
- `distribution/config.py` - Scene names
- `distribution/player.py` - Player inventory for keys

**Exports**:
- `Scene` class - Used by game engine
- `setup_scenes()` - Used by game initialization

**Coordination Required**:
- Item placement in scenes must coordinate with Inventory Agent
- Scene progression must coordinate with game flow
- Key requirements must coordinate with Inventory Agent

**Interface Contracts**:
- Scene.enter(player) returns bool
- Scene.unlock(player) modifies scene state
- Scene.exits dict structure must remain consistent

## Import Hierarchy

### Top Level (player_gui.py)
```
player_gui.py
├── tkinter (UI framework)
├── PIL (Image processing)
├── distribution/combat (combat functions)
├── distribution/item (item definitions)
└── distribution/player (player state)
```

### Distribution Modules
```
distribution/combat.py
├── config (constants)
├── item (weapon definitions)
└── player (player stats)

distribution/item.py
└── player (type checking)

distribution/scenes.py
├── config (scene names)
└── player (inventory checking)

distribution/player.py
└── item (type checking)
```

## Shared State Locations

### Critical Shared State Files

1. **distribution/config.py**
   - Status: SHARED STATE
   - Requires: Coordination with ALL agents
   - Contains: Game constants, stat requirements, scene names
   - Lock: Use coordination lock before modifying

2. **distribution/player.py**
   - Status: SHARED STATE
   - Requires: Coordination between Combat and Inventory agents
   - Contains: Player class with stats and inventory
   - Lock: Use coordination lock before modifying

3. **player_gui.py**
   - Status: INTEGRATION POINT
   - Requires: Coordination between UI, Combat, and Inventory agents
   - Contains: Main game loop and UI integration
   - Lock: Check ACTIVE_TASKS.md before modifying

## Coordination Points

### Lock Files or Coordination Points

1. **distribution/config.py**
   - Lock required: Yes
   - Coordination: All agents
   - Check: `.cursor/shared/coordination_locks.json`

2. **distribution/player.py**
   - Lock required: Yes
   - Coordination: Combat Agent, Inventory Agent
   - Check: `.cursor/shared/coordination_locks.json`

3. **player_gui.py**
   - Lock required: Yes (for shared sections)
   - Coordination: UI Agent, Combat Agent, Inventory Agent
   - Check: `.cursor/tasks/ACTIVE_TASKS.md`

## Module Dependencies Summary

### By Agent

**UI Agent**:
- Reads: `player_gui.py`, `distribution/player.py`, `distribution/config.py`
- Modifies: `player_gui.py` (UI sections)
- Coordinates: Combat Agent, Inventory Agent

**Combat Agent**:
- Reads: `distribution/combat.py`, `distribution/item.py`, `distribution/player.py`, `distribution/config.py`
- Modifies: `distribution/combat.py`, `distribution/player.py` (stats)
- Coordinates: UI Agent, Inventory Agent

**Inventory Agent**:
- Reads: `distribution/item.py`, `distribution/player.py`, `distribution/scenes.py`
- Modifies: `distribution/item.py`, `distribution/player.py` (inventory), `distribution/scenes.py` (item placement)
- Coordinates: UI Agent, Combat Agent

**Scene Agent** (if separate):
- Reads: `distribution/scenes.py`, `distribution/config.py`, `distribution/player.py`
- Modifies: `distribution/scenes.py`
- Coordinates: Inventory Agent

**Assets Agent**:
- Reads: `assets/` directory
- Modifies: `assets/` directory
- Coordinates: UI Agent (for asset format)

**Testing Agent**:
- Reads: All files (for testing)
- Modifies: `tests/` directory
- Coordinates: All agents (for test updates)

## Dependency Rules

### Safe to Modify Independently
- `utilities/` - Each utility is independent
- `tests/unit/` - Unit tests are independent
- `assets/` - Assets are independent (format coordination only)
- `docs/` - Documentation is independent

### Requires Coordination
- `distribution/config.py` - ALL agents
- `distribution/player.py` - Combat & Inventory agents
- `player_gui.py` - UI, Combat, Inventory agents (for shared sections)

### Requires Task Entry
- Any file listed in ACTIVE_TASKS.md
- Shared state files (config.py, player.py)
- Integration point files (player_gui.py)

## Validation Points

### Integration Validation
- Check imports after changes
- Validate shared interfaces haven't changed
- Run tests for affected modules
- Check configuration consistency

### Conflict Detection
- Check ACTIVE_TASKS.md before modifying files
- Check coordination locks for shared state files
- Validate dependencies are met

## Best Practices

1. **Before Modifying Shared Files**:
   - Check ACTIVE_TASKS.md
   - Check coordination locks
   - Create task entry
   - Coordinate with affected agents

2. **When Modifying Dependencies**:
   - Update all dependent modules
   - Run integration validation
   - Update tests
   - Document changes

3. **After Modifying Shared Files**:
   - Update ACTIVE_TASKS.md
   - Release coordination locks
   - Run integration validation
   - Notify affected agents

