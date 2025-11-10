# Integration Points

This document details where agents' work connects and defines the interface contracts that must be maintained for proper integration.

## Overview

Integration points are locations in the codebase where multiple agents' work must connect seamlessly. These points require:
- Clear interface contracts
- Coordination between agents
- Consistent data structures
- Validation of changes

## Critical Integration Points

### 1. player_gui.py - Combat UI Integration

**Location**: `player_gui.py` (combat display methods)

**Agents Involved**:
- UI Agent (primary) - Renders combat UI
- Combat Agent (secondary) - Provides combat state

**Interface Contract**:

**Combat State Structure** (Combat Agent → UI Agent):
```python
combat_state = {
    'player_health': int,          # Current player health
    'enemy_health': int,           # Current enemy health
    'enemy_name': str,             # Enemy display name
    'turn': str,                   # 'player' or 'enemy'
    'available_actions': List[str], # ['attack', 'defend', 'special']
    'combat_message': str           # Current combat message
}
```

**Combat Functions** (Combat Agent → UI Agent):
```python
# Function signature must remain consistent
def execute_weapon_attack(player, weapon) -> Tuple[bool, str]:
    """
    Returns:
        (success: bool, message: str)
    """
    pass

def execute_class_ability_final_boss(player) -> Tuple[bool, str]:
    """
    Returns:
        (success: bool, message: str)
    """
    pass
```

**Coordination Protocol**:
1. Combat Agent: Document combat state structure changes
2. UI Agent: Update UI to match new combat state structure
3. Both: Test integration after changes
4. Update: Document changes in `.cursor/comms/change_log.md`

**Breaking Changes**:
- Changing combat state structure requires UI Agent coordination
- Changing function signatures requires UI Agent coordination
- Adding new combat actions requires UI Agent coordination

### 2. player_gui.py - Inventory UI Integration

**Location**: `player_gui.py` (inventory display methods)

**Agents Involved**:
- UI Agent (primary) - Renders inventory UI
- Inventory Agent (secondary) - Provides inventory structure

**Interface Contract**:

**Inventory Structure** (Inventory Agent → UI Agent):
```python
inventory = {
    'items': List[Item],              # List of all items
    'equipped_weapon': Optional[Weapon], # Currently equipped weapon
    'equipped_armor': Optional[Armor],   # Currently equipped armor
    'equipped_accessories': List[Accessory] # Equipped accessories
}

# Item structure
class Item:
    name: str
    description: str
    item_type: str  # 'weapon', 'armor', 'consumable', 'key'
```

**Player Inventory Access** (Inventory Agent → UI Agent):
```python
# Player.inventory structure must remain consistent
player.inventory.items: List[Item]
player.inventory.has_item(name: str) -> bool
player.inventory.add_item(item: Item) -> None
player.inventory.remove_item(name: str) -> bool
```

**Coordination Protocol**:
1. Inventory Agent: Document inventory structure changes
2. UI Agent: Update UI to match new inventory structure
3. Both: Test integration after changes
4. Update: Document changes in `.cursor/comms/change_log.md`

**Breaking Changes**:
- Changing inventory structure requires UI Agent coordination
- Changing Item class structure requires UI Agent coordination
- Adding new item types requires UI Agent coordination

### 3. Combat System - Weapon Integration

**Location**: `distribution/combat.py` (weapon usage)

**Agents Involved**:
- Combat Agent (primary) - Uses weapons in combat
- Inventory Agent (secondary) - Defines weapon stats

**Interface Contract**:

**Weapon Interface** (Inventory Agent → Combat Agent):
```python
class Weapon:
    name: str
    description: str
    base_damage: int
    scale_attr: str  # 'agility', 'strength', 'intelligence'
    
    def get_damage(self, player: Player) -> int:
        """
        Calculate damage based on player stats.
        Must use player.{scale_attr} for scaling.
        """
        pass
```

**Weapon Usage** (Combat Agent):
```python
# Combat agent uses weapon.get_damage(player)
damage = weapon.get_damage(player)

# Combat agent checks weapon effectiveness
effective, message = check_weapon_effectiveness(player, weapon)
```

**Coordination Protocol**:
1. Inventory Agent: Document weapon stat changes
2. Combat Agent: Update damage calculations if needed
3. Both: Test weapon effectiveness in combat
4. Update: Document changes in `.cursor/comms/change_log.md`

**Breaking Changes**:
- Changing Weapon.get_damage() signature requires Combat Agent coordination
- Changing weapon stat structure requires Combat Agent coordination
- Adding new weapon attributes requires Combat Agent coordination

### 4. Player State - Shared Attributes

**Location**: `distribution/player.py` (Player class)

**Agents Involved**:
- Combat Agent (modify stats)
- Inventory Agent (modify inventory)
- UI Agent (read state)

**Interface Contract**:

**Player Class Structure**:
```python
class Player:
    # Combat Agent modifies these
    health: int
    strength: int
    agility: int
    intelligence: int
    vitality: int
    level: int
    
    # Inventory Agent modifies these
    inventory: Inventory
    weapon: Optional[Weapon]
    
    # Methods used by both agents
    def level_up(self) -> None:
        """Increase level and provide stat upgrades."""
        pass
```

**Coordination Protocol**:
1. Combat Agent: Coordinate stat modifications with Inventory Agent
2. Inventory Agent: Coordinate inventory modifications with Combat Agent
3. UI Agent: Read-only access, no modifications
4. Both: Test integration after changes
5. Update: Document changes in `.cursor/comms/change_log.md`

**Breaking Changes**:
- Changing Player attribute names requires all agents coordination
- Changing Player method signatures requires all agents coordination
- Adding new Player attributes requires all agents coordination

### 5. Configuration Constants

**Location**: `distribution/config.py`

**Agents Involved**:
- All agents (shared state)

**Interface Contract**:

**Configuration Constants**:
```python
# Combat constants
STAT_REQUIREMENT = int
FINAL_BOSS_STAT_REQUIREMENT = int
STARTING_STAT_VALUE = int
LEVEL_UP_POINTS = int

# Scene constants
SCENE_NAMES = Dict[str, str]

# Message constants
MESSAGES = Dict[str, str]
```

**Usage Pattern**:
```python
from distribution.config import STAT_REQUIREMENT, SCENE_NAMES
```

**Coordination Protocol**:
1. Any agent: Check ACTIVE_TASKS.md before modifying
2. Any agent: Create task entry before modifying
3. Any agent: Document changes in `.cursor/comms/change_log.md`
4. All agents: Update affected modules after changes
5. All agents: Test integration after changes

**Breaking Changes**:
- Changing constant names requires all agents coordination
- Changing constant values requires affected agents coordination
- Removing constants requires all agents coordination

### 6. Scene System - Item Placement

**Location**: `distribution/scenes.py` (Scene class)

**Agents Involved**:
- Scene Agent (primary) - Places items in scenes
- Inventory Agent (secondary) - Defines items

**Interface Contract**:

**Scene Item Placement**:
```python
class Scene:
    # Inventory Agent provides items
    items: List[Item]  # Items available in this scene
    
    # Scene Agent manages item collection
    def collect_item(self, item_name: str, player: Player) -> bool:
        """Add item to player inventory if available."""
        pass
```

**Coordination Protocol**:
1. Inventory Agent: Define items for scenes
2. Scene Agent: Place items in appropriate scenes
3. Both: Test item collection mechanics
4. Update: Document changes in `.cursor/comms/change_log.md`

**Breaking Changes**:
- Changing item collection interface requires Scene Agent coordination
- Changing item structure requires Scene Agent coordination

## Interface Contracts Summary

### Data Structures

**Combat State** (Combat → UI):
```python
{
    'player_health': int,
    'enemy_health': int,
    'enemy_name': str,
    'turn': str,
    'available_actions': List[str],
    'combat_message': str
}
```

**Inventory Structure** (Inventory → UI):
```python
{
    'items': List[Item],
    'equipped_weapon': Optional[Weapon],
    'equipped_armor': Optional[Armor],
    'equipped_accessories': List[Accessory]
}
```

**Player State** (All agents):
```python
Player {
    health: int,
    strength: int,
    agility: int,
    intelligence: int,
    level: int,
    inventory: Inventory,
    weapon: Optional[Weapon]
}
```

### Function Signatures

**Combat Functions**:
```python
execute_weapon_attack(player: Player, weapon: Weapon) -> Tuple[bool, str]
execute_class_ability_final_boss(player: Player) -> Tuple[bool, str]
check_weapon_effectiveness(player: Player, weapon: Weapon) -> Tuple[bool, str]
```

**Inventory Functions**:
```python
Inventory.add_item(item: Item) -> None
Inventory.remove_item(name: str) -> bool
Inventory.has_item(name: str) -> bool
Weapon.get_damage(player: Player) -> int
```

**Scene Functions**:
```python
Scene.enter(player: Player) -> bool
Scene.unlock(player: Player) -> None
```

## Coordination Checklist

Before modifying an integration point:

- [ ] Check ACTIVE_TASKS.md for conflicts
- [ ] Review interface contract in this document
- [ ] Create task entry if modifying shared files
- [ ] Coordinate with affected agents
- [ ] Document planned changes
- [ ] Test integration after changes
- [ ] Update this document if interface changes
- [ ] Update affected agents

## Validation Requirements

After modifying an integration point:

- [ ] Run integration validation script
- [ ] Test affected modules
- [ ] Verify interface contracts still work
- [ ] Update documentation
- [ ] Notify affected agents
- [ ] Move task to COMPLETED_TASKS.md

## Breaking Change Protocol

If breaking changes are necessary:

1. **Proposal**: Document proposed changes in `.cursor/comms/questions.md`
2. **Coordination**: Discuss with affected agents
3. **Timeline**: Plan coordinated update timeline
4. **Implementation**: Implement changes together
5. **Testing**: Test integration thoroughly
6. **Documentation**: Update all interface contracts

## Questions or Issues?

- Check `.cursor/comms/questions.md` for coordination questions
- Review `docs/multi-agent/DEPENDENCY_MAP.md` for dependency details
- Contact relevant agents for interface questions
- Update this document when interfaces change

