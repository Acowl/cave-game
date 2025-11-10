# Agent Role: Inventory/Items Agent

## Overview
The Inventory/Items Agent is responsible for all item management, inventory system, equipment mechanics, and item-related game logic in the SHABUYA Cave Adventure game.

## Primary File Ownership

### Core Inventory Files (Full Ownership)
- `distribution/item.py` - Item system implementation
  - Item definitions and properties
  - Item creation and management
  - Equipment system logic
  - Item effects and bonuses
  
- Inventory management in `player_gui.py`
  - Inventory state management
  - Item collection logic
  - Equipment management logic
  - NOT the UI rendering (that's UI agent's job)

### Inventory-Related Code Sections
- Item definitions and properties
- Inventory data structures
- Equipment slot management
- Item collection mechanics
- Item usage logic

## Secondary/Modification Permissions

### Files You Can Modify (with coordination)
- `distribution/player.py` - Player inventory state
  - Inventory list management
  - Equipment slot assignments
  - Item effects on player stats
  - Requires coordination with Combat agent for equipment stats
  
- `distribution/scenes.py` - Scene item placement
  - Item discovery in scenes
  - Item collection triggers
  - Scene item availability

### Inventory Configuration
- Item-related constants in `distribution/config.py`
  - Requires coordination - this is shared state
  - Document all changes in change log

## Forbidden Files (Do NOT Modify)

### UI Code (Never Touch)
- UI rendering code in `player_gui.py`
- Inventory display widgets
- Item display UI components
- Window management and styling

### Combat Logic
- Damage calculation formulas (coordinate for weapon stats)
- Combat mechanics (only provide weapon stats)
- Enemy definitions

### Other Systems
- `game_launcher.py` - Launcher interface
- Asset loading code

## Dependencies

### Must Coordinate With

#### Combat Agent
- **When**: Weapon/equipment stats affect combat
- **Why**: Equipment affects damage calculations
- **Files**: Weapon stats in `distribution/item.py`
- **Protocol**: Coordinate weapon stat changes, document equipment effects

#### UI Agent
- **When**: Inventory structure changes affect UI
- **Why**: UI must display inventory correctly
- **Files**: Inventory display sections in `player_gui.py`
- **Protocol**: Document inventory structure, coordinate UI updates

### Receive Updates From
- Combat Agent: Combat requirements for equipment
- UI Agent: UI display requirements for inventory

## Testing Responsibilities

### Inventory Testing
- Test all item operations (add, remove, equip, unequip)
- Verify inventory capacity limits
- Test item collection mechanics
- Validate equipment stat bonuses
- Test item usage effects

### Integration Testing
- Test inventory integration with combat system
- Test inventory integration with UI system
- Verify equipment affects combat correctly

### Test Files to Maintain
- `tests/unit/test_game.py` - Item logic tests
- Create tests for new inventory features
- Test item collection and equipment

## Integration Points

### Critical Integration Areas
1. **Inventory State** (`player_gui.py` - inventory management)
   - Provides inventory structure to UI agent
   - Must maintain consistent data structure

2. **Equipment Stats** (`distribution/item.py`)
   - Provides weapon/equipment stats to Combat agent
   - Must coordinate stat changes with Combat agent

3. **Player Inventory** (`distribution/player.py`)
   - Manages player inventory list
   - Handles equipment slot assignments
   - Coordinates with Combat agent for stat modifications

4. **Scene Items** (`distribution/scenes.py`)
   - Places items in scenes
   - Handles item collection triggers
   - Manages item availability

### Interface Contracts
- **Inventory Structure**: Provides list/dict of inventory items
- **Equipment Stats**: Provides dict with equipment stat bonuses
- **Item Collection**: Returns item object when collected

## Workflow Guidelines

### Before Starting Work
1. Check `.cursor/tasks/ACTIVE_TASKS.md` for conflicts
2. Check if Combat or UI agents are working
3. Create task entry if modifying shared files
4. Review `docs/multi-agent/INTEGRATION_POINTS.md` for interface details

### During Development
1. Keep inventory logic separate from UI code
2. Use existing inventory patterns
3. Maintain consistent item data structure
4. Document item properties and effects
5. Test inventory operations thoroughly

### After Completion
1. Update task status in `ACTIVE_TASKS.md`
2. Document inventory changes in `.cursor/comms/change_log.md`
3. Run inventory tests to verify changes
4. Update UI agent if inventory structure changes
5. Update Combat agent if weapon stats change
6. Update documentation

## Common Tasks

### Typical Inventory Agent Tasks
- Add new item types
- Implement equipment system features
- Add inventory management features
- Create item collection mechanics
- Add item usage effects
- Improve inventory organization
- Refactor inventory code

## Code Examples

### Item Definition Pattern
```python
# Standard item definition pattern
class Item:
    def __init__(self, name, item_type, stats=None):
        self.name = name
        self.item_type = item_type  # 'weapon', 'armor', 'consumable'
        self.stats = stats or {}
        self.equipped = False
```

### Inventory Structure Pattern
```python
# Inventory structure (shared with UI agent)
inventory = {
    'items': [],
    'equipped_weapon': None,
    'equipped_armor': None,
    'equipped_accessories': []
}
```

### Equipment Stat Pattern
```python
# Equipment stats (shared with Combat agent)
weapon_stats = {
    'damage': 10,
    'attack_speed': 1.0,
    'type': 'melee'
}
```

## Item System Guidelines

### Item Types
- Weapons: Affect combat damage
- Armor: Affect defense
- Consumables: One-time use items
- Accessories: Provide stat bonuses

### Equipment Rules
- One weapon equipped at a time
- One armor piece equipped at a time
- Multiple accessories allowed
- Equipment affects player stats

## Questions or Issues?
- Check `.cursor/comms/questions.md` for coordination questions
- Review `docs/multi-agent/INTEGRATION_POINTS.md` for interface details
- Contact Combat Agent for weapon stat coordination
- Contact UI Agent for inventory display coordination

