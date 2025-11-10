# File Ownership Matrix

This document shows which agent owns or modifies each file and identifies conflict zones where coordination is required.

## Legend

- **Primary Owner**: Agent has full ownership and can modify freely
- **Secondary**: Agent can modify with coordination
- **Read Only**: Agent can read but not modify
- **Conflict Zone**: File requires coordination between multiple agents
- **Forbidden**: Agent should not modify this file

## Core Game Files

| File | UI Agent | Combat Agent | Inventory Agent | Testing Agent | Documentation Agent | Assets Agent |
|------|----------|--------------|-----------------|---------------|---------------------|--------------|
| `player_gui.py` | **Primary** | Secondary (combat logic) | Secondary (inventory logic) | Read Only | Read Only | Read Only |
| `game_launcher.py` | **Primary** | Forbidden | Forbidden | Read Only | Read Only | Read Only |
| `enhanced_gui_final.py` | **Primary** | Forbidden | Forbidden | Read Only | Read Only | Read Only |

## Distribution Module Files

| File | UI Agent | Combat Agent | Inventory Agent | Testing Agent | Documentation Agent | Assets Agent |
|------|----------|--------------|-----------------|---------------|---------------------|--------------|
| `distribution/combat.py` | Read Only | **Primary** | Read Only | Read Only | Read Only | Forbidden |
| `distribution/player.py` | Read Only | Secondary (stats) | Secondary (inventory) | Read Only | Read Only | Forbidden |
| `distribution/item.py` | Read Only | Read Only | **Primary** | Read Only | Read Only | Forbidden |
| `distribution/scenes.py` | Read Only | Secondary (combat triggers) | Secondary (item placement) | Read Only | Read Only | Forbidden |
| `distribution/config.py` | **CONFLICT ZONE** | **CONFLICT ZONE** | **CONFLICT ZONE** | Read Only | Read Only | Forbidden |
| `distribution/gui.py` | Secondary | Forbidden | Forbidden | Read Only | Read Only | Read Only |
| `distribution/ui.py` | Read Only | Read Only | Read Only | Read Only | Read Only | Forbidden |
| `distribution/main.py` | Read Only | Read Only | Read Only | Read Only | Read Only | Forbidden |

## Asset Files

| File/Directory | UI Agent | Combat Agent | Inventory Agent | Testing Agent | Documentation Agent | Assets Agent |
|----------------|----------|--------------|-----------------|---------------|---------------------|--------------|
| `assets/sprites/` | Read Only | Forbidden | Forbidden | Read Only | Read Only | **Primary** |
| `assets/backgrounds/` | Read Only | Forbidden | Forbidden | Read Only | Read Only | **Primary** |
| `assets/icons/` | Read Only | Forbidden | Forbidden | Read Only | Read Only | **Primary** |

## Test Files

| File/Directory | UI Agent | Combat Agent | Inventory Agent | Testing Agent | Documentation Agent | Assets Agent |
|----------------|----------|--------------|-----------------|---------------|---------------------|--------------|
| `tests/unit/` | Forbidden | Forbidden | Forbidden | **Primary** | Read Only | Forbidden |
| `tests/integration/` | Forbidden | Forbidden | Forbidden | **Primary** | Read Only | Forbidden |
| `tests/assets/` | Forbidden | Forbidden | Forbidden | **Primary** | Read Only | Forbidden |

## Utility Files

| File | UI Agent | Combat Agent | Inventory Agent | Testing Agent | Documentation Agent | Assets Agent |
|------|----------|--------------|-----------------|---------------|---------------------|--------------|
| `utilities/capture_gui_snapshots.py` | Secondary | Forbidden | Forbidden | Read Only | Read Only | **Primary** |
| `utilities/test_gui.py` | Read Only | Forbidden | Forbidden | **Primary** | Read Only | Forbidden |
| `utilities/verify_cleanup.py` | Forbidden | Forbidden | Forbidden | **Primary** | Read Only | Forbidden |
| `utilities/check_agent_conflicts.py` | Read Only | Read Only | Read Only | **Primary** | Read Only | Forbidden |
| `utilities/validate_integration.py` | Read Only | Read Only | Read Only | **Primary** | Read Only | Forbidden |
| `utilities/continuity_validator.py` | Forbidden | Forbidden | Forbidden | **Primary** | Read Only | Forbidden |
| `utilities/autoplay_route.py` | Forbidden | Forbidden | Forbidden | **Primary** | Read Only | Forbidden |
| `utilities/regression.py` | Forbidden | Forbidden | Forbidden | **Primary** | Read Only | Forbidden |
| `utilities/validate_scene_choices.py` | Forbidden | Forbidden | Forbidden | **Primary** | Read Only | Forbidden |

## Documentation Files

| File/Directory | UI Agent | Combat Agent | Inventory Agent | Testing Agent | Documentation Agent | Assets Agent |
|----------------|----------|--------------|-----------------|---------------|---------------------|--------------|
| `README.md` | Read Only | Read Only | Read Only | Read Only | **Primary** | Read Only |
| `MVP_ROADMAP.md` | Read Only | Read Only | Read Only | Read Only | **Primary** | Read Only |
| `MANUAL_TEST_GUIDE.md` | Read Only | Read Only | Read Only | Read Only | **Primary** | Read Only |
| `docs/` | Read Only | Read Only | Read Only | Read Only | **Primary** | Read Only |
| `docs/multi-agent/` | Read Only | Read Only | Read Only | Read Only | **Primary** | Read Only |
| `docs/assets/` | Read Only | Forbidden | Forbidden | Read Only | **Primary** | Secondary |

## Configuration Files

| File | UI Agent | Combat Agent | Inventory Agent | Testing Agent | Documentation Agent | Assets Agent |
|------|----------|--------------|-----------------|---------------|---------------------|--------------|
| `.cursorrules` | Read Only | Read Only | Read Only | Read Only | **Primary** | Read Only |
| `.cursor/agents/` | Read Only | Read Only | Read Only | Read Only | **Primary** | Read Only |
| `.cursor/tasks/` | Read Only | Read Only | Read Only | Read Only | **Primary** | Read Only |
| `requirements.txt` | Read Only | Read Only | Read Only | Read Only | **Primary** | Read Only |

## Conflict Zones

### High Priority Conflict Zones

**1. `distribution/config.py`**
- **Status**: SHARED STATE - Requires coordination
- **Agents**: All agents (UI, Combat, Inventory)
- **Rules**: 
  - Check ACTIVE_TASKS.md before modifying
  - Create task entry before modifying
  - Document changes in change log
  - Coordinate with all affected agents

**2. `distribution/player.py`**
- **Status**: SHARED STATE - Requires coordination
- **Agents**: Combat Agent, Inventory Agent
- **Rules**:
  - Check ACTIVE_TASKS.md before modifying
  - Create task entry before modifying
  - Coordinate stat modifications with Inventory Agent
  - Coordinate inventory modifications with Combat Agent

**3. `player_gui.py`**
- **Status**: INTEGRATION POINT - Requires coordination
- **Agents**: UI Agent (primary), Combat Agent (secondary), Inventory Agent (secondary)
- **Rules**:
  - UI Agent owns UI sections
  - Combat Agent coordinates for combat logic sections
  - Inventory Agent coordinates for inventory logic sections
  - Check ACTIVE_TASKS.md before modifying shared sections

### Medium Priority Conflict Zones

**4. `distribution/scenes.py`**
- **Status**: Requires coordination
- **Agents**: Scene Agent (primary), Inventory Agent (secondary for item placement)
- **Rules**:
  - Coordinate item placement with Inventory Agent
  - Coordinate combat triggers with Combat Agent

**5. `distribution/item.py`**
- **Status**: Requires coordination
- **Agents**: Inventory Agent (primary), Combat Agent (secondary for weapon stats)
- **Rules**:
  - Coordinate weapon stat changes with Combat Agent
  - Coordinate inventory structure with UI Agent

## Safe Zones (Independent Modification)

### UI Agent Safe Zone
- `game_launcher.py` (UI sections only)
- `enhanced_gui_final.py` (UI sections only)
- UI rendering code in `player_gui.py` (non-integration sections)

### Combat Agent Safe Zone
- `distribution/combat.py` (combat logic, not function signatures)
- Combat calculations and formulas
- Enemy definitions

### Inventory Agent Safe Zone
- `distribution/item.py` (item definitions, not Weapon interface)
- Inventory management logic
- Item creation functions

### Testing Agent Safe Zone
- `tests/` directory (all test files)
- Test utilities
- Test fixtures

### Documentation Agent Safe Zone
- `docs/` directory (all documentation)
- `README.md`
- `MVP_ROADMAP.md`
- Documentation updates

### Assets Agent Safe Zone
- `assets/` directory (all asset files)
- Asset processing utilities
- Asset documentation

## Coordination Requirements

### Before Modifying Files

**Primary Ownership Files**:
- Check ACTIVE_TASKS.md for conflicts
- Create task entry if modifying shared sections
- Proceed with modification

**Secondary Ownership Files**:
- Check ACTIVE_TASKS.md for conflicts
- Create task entry
- Coordinate with primary owner
- Get approval before modifying

**Conflict Zone Files**:
- Check ACTIVE_TASKS.md for conflicts
- Create task entry
- Coordinate with ALL affected agents
- Get approval from all agents
- Document changes in change log

**Forbidden Files**:
- Do NOT modify
- Read only access
- Contact owner agent if changes needed

## File Modification Checklist

Before modifying any file:

- [ ] Check this matrix for ownership
- [ ] Check ACTIVE_TASKS.md for conflicts
- [ ] Identify if file is in conflict zone
- [ ] Create task entry if needed
- [ ] Coordinate with affected agents if needed
- [ ] Get approval if required
- [ ] Proceed with modification
- [ ] Update task status after completion

## Questions or Issues?

- Check `.cursor/comms/questions.md` for coordination questions
- Review `docs/multi-agent/INTEGRATION_POINTS.md` for interface details
- Contact file owner agent for modification requests
- Update this matrix if ownership changes

