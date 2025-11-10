# Agent Role: Combat System Agent

## Overview
The Combat System Agent is responsible for all combat mechanics, enemy definitions, damage calculations, and combat-related game logic in the SHABUYA Cave Adventure game.

## Primary File Ownership

### Core Combat Files (Full Ownership)
- `distribution/combat.py` - Combat system implementation
  - Combat mechanics and turn-based logic
  - Damage calculation formulas
  - Enemy attack patterns
  - Combat resolution logic
  
- Combat flow logic in `player_gui.py`
  - Combat state management
  - Combat turn handling
  - Combat outcome processing
  - NOT the UI rendering (that's UI agent's job)

### Combat-Related Code Sections
- Enemy definitions and stats
- Damage calculation formulas
- Combat skill/ability system
- Turn-based combat flow
- Combat-related scene triggers

## Secondary/Modification Permissions

### Files You Can Modify (with coordination)
- `distribution/player.py` - Player stats related to combat
  - Health modifications
  - Combat-related stat changes
  - Level-up combat bonuses
  - Requires coordination with Inventory agent for equipment stats
  
- `distribution/scenes.py` - Combat-related scene triggers
  - Combat encounter setup
  - Scene combat outcomes
  - Combat gating and prerequisites

### Combat Configuration
- Combat constants in `distribution/config.py`
  - Requires coordination - this is shared state
  - Document all changes in change log

## Forbidden Files (Do NOT Modify)

### UI Code (Never Touch)
- UI rendering code in `player_gui.py`
- Widget creation and styling
- Window management
- Asset display code
- Button layout and styling

### Other Systems
- `distribution/item.py` - Item logic (coordinate for weapon stats)
- `game_launcher.py` - Launcher interface
- Asset loading code

## Dependencies

### Must Coordinate With

#### UI Agent
- **When**: Combat interface changes affect UI
- **Why**: UI must display combat state correctly
- **Files**: Combat display sections in `player_gui.py`
- **Protocol**: Document combat state structure, coordinate UI updates

#### Inventory Agent
- **When**: Weapon/equipment stats affect combat
- **Why**: Equipment affects damage calculations
- **Files**: `distribution/item.py`, equipment stats
- **Protocol**: Coordinate weapon stat changes, document equipment effects

### Receive Updates From
- Inventory Agent: Weapon stat changes, equipment effects
- Assets Agent: New enemy sprites (for reference)

## Testing Responsibilities

### Combat Testing
- Test all combat scenarios
- Verify damage calculations
- Test enemy AI and attack patterns
- Validate combat progression
- Test class-specific combat abilities

### Balance Testing
- Test combat difficulty balance
- Verify stat requirements
- Test weapon effectiveness
- Validate level-up progression

### Test Files to Maintain
- `tests/unit/test_game.py` - Combat logic tests
- `tests/integration/` - Combat integration tests
- Create tests for new combat features

## Integration Points

### Critical Integration Areas
1. **Combat State** (`player_gui.py` - combat state management)
   - Provides combat state to UI agent
   - Must maintain consistent state structure

2. **Player Stats** (`distribution/player.py`)
   - Modifies player health/stats during combat
   - Coordinates with Inventory agent for equipment stats

3. **Weapon System** (`distribution/item.py`)
   - Uses weapon stats for damage calculations
   - Must coordinate weapon stat changes with Inventory agent

4. **Scene Combat** (`distribution/scenes.py`)
   - Sets up combat encounters in scenes
   - Handles combat outcomes and scene progression

### Interface Contracts
- **Combat State**: Provides dict with combat state (health, enemy, turn, etc.)
- **Damage Calculation**: Receives player stats, weapon stats, returns damage
- **Combat Resolution**: Returns combat outcome dict

## Workflow Guidelines

### Before Starting Work
1. Check `.cursor/tasks/ACTIVE_TASKS.md` for conflicts
2. Check if UI or Inventory agents are working
3. Create task entry if modifying shared files
4. Review `docs/multi-agent/INTEGRATION_POINTS.md` for interface details

### During Development
1. Keep combat logic separate from UI code
2. Use existing combat patterns
3. Maintain balance with existing stats
4. Document damage calculation formulas
5. Test combat scenarios thoroughly

### After Completion
1. Update task status in `ACTIVE_TASKS.md`
2. Document combat changes in `.cursor/comms/change_log.md`
3. Run combat tests to verify changes
4. Update UI agent if combat state structure changes
5. Update documentation

## Common Tasks

### Typical Combat Agent Tasks
- Add new enemy types
- Implement new combat abilities
- Balance damage calculations
- Add combat-related scene events
- Improve combat AI
- Add special combat mechanics
- Refactor combat code

## Code Examples

### Combat Pattern to Follow
```python
# Standard damage calculation pattern
def calculate_damage(player_stats, weapon_stats, enemy_defense):
    base_damage = player_stats['strength'] + weapon_stats['damage']
    final_damage = max(1, base_damage - enemy_defense)
    return final_damage
```

### Combat State Pattern
```python
# Combat state structure (shared with UI agent)
combat_state = {
    'player_health': 100,
    'enemy_health': 50,
    'enemy_name': 'Cave Guardian',
    'turn': 'player',
    'available_actions': ['attack', 'defend', 'special']
}
```

## Combat Balance Guidelines

### Stat Requirements
- Check `distribution/config.py` for stat constants
- Maintain balance with existing values
- Coordinate stat changes with other agents

### Damage Formula Guidelines
- Base damage should scale with player level
- Weapon bonuses should be meaningful but not overpowered
- Enemy difficulty should progress logically

## Questions or Issues?
- Check `.cursor/comms/questions.md` for coordination questions
- Review `docs/multi-agent/INTEGRATION_POINTS.md` for interface details
- Contact UI Agent for combat display coordination
- Contact Inventory Agent for weapon stat coordination

