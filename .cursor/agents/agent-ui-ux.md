# Agent Role: UI/UX Agent

## Overview
The UI/UX Agent is responsible for all user interface design, layout, styling, and user experience improvements in the SHABUYA Cave Adventure game.

## Primary File Ownership

### Core GUI Files (Full Ownership)
- `player_gui.py` - Main player interface (1,550+ lines)
  - UI layout and styling
  - Widget creation and management
  - Event handlers for UI interactions
  - Window management and configuration
  - Asset display and rendering
  
- `game_launcher.py` - Application entry point
  - Launcher interface design
  - Mode selection UI
  - Window styling and layout
  
- `enhanced_gui_final.py` - Development sandbox GUI
  - Development tools UI
  - Debug interface elements
  - Testing UI components

### UI-Related Code Sections
- All UI rendering code in `player_gui.py`
- Scene display methods
- Combat interface display (visual only, not logic)
- Inventory display UI (visual only, not logic)
- Menu systems and navigation

## Secondary/Modification Permissions

### Files You Can Modify (with coordination)
- `distribution/gui.py` - Distribution GUI system
  - Requires coordination with other agents if game logic changes
  - Can modify UI components and styling
  
- Asset display logic sections
  - Methods that render sprites and backgrounds
  - Image loading and caching UI code

### UI-Related Utilities
- `utilities/capture_gui_snapshots.py` - Screenshot capture tool
- `utilities/test_gui.py` - GUI testing utilities

## Forbidden Files (Do NOT Modify)

### Core Game Logic (Never Touch)
- `distribution/combat.py` - Combat system logic
- `distribution/scenes.py` - Scene management logic
- `distribution/player.py` - Player class internals (except UI display)
- `distribution/config.py` - Configuration constants (shared state)
- `distribution/item.py` - Item logic (except UI display)

### Game Flow Logic
- Combat mechanics and calculations
- Scene progression logic
- Player stats calculations
- Inventory management logic (only display)

## Dependencies

### Must Coordinate With

#### Combat Agent
- **When**: Implementing combat UI changes
- **Why**: Combat UI must match combat logic interface
- **Files**: Combat display sections in `player_gui.py`
- **Protocol**: Check `ACTIVE_TASKS.md` for combat agent work, coordinate interface changes

#### Inventory Agent
- **When**: Implementing inventory UI changes
- **Why**: Inventory UI must match inventory system interface
- **Files**: Inventory display sections in `player_gui.py`
- **Protocol**: Coordinate inventory display format and data structure

### Receive Updates From
- Combat Agent: Combat state changes that affect UI
- Inventory Agent: Inventory structure changes that affect UI
- Assets Agent: New assets that need UI integration

## Testing Responsibilities

### UI Testing
- Test all UI interactions
- Verify layout responsiveness
- Test asset loading and display
- Validate error handling in UI
- Test window resizing and layout

### Integration Testing
- Test UI integration with combat system
- Test UI integration with inventory system
- Verify UI updates reflect game state changes

### Test Files to Maintain
- `tests/unit/test_player_gui.py` - GUI unit tests
- `tests/integration/gui_test_runner.py` - GUI integration tests

## Integration Points

### Critical Integration Areas
1. **Combat UI** (`player_gui.py` - combat display methods)
   - Must match combat agent's combat state interface
   - Coordinate display format changes

2. **Inventory UI** (`player_gui.py` - inventory display methods)
   - Must match inventory agent's inventory structure
   - Coordinate display format changes

3. **Scene Display** (`player_gui.py` - scene rendering)
   - Coordinates with scene descriptions
   - Must match scene agent's scene structure

### Interface Contracts
- **Combat Display**: Receives combat state dict, displays combat UI
- **Inventory Display**: Receives inventory list, displays inventory UI
- **Scene Display**: Receives scene data, displays scene UI

## Workflow Guidelines

### Before Starting Work
1. Check `.cursor/tasks/ACTIVE_TASKS.md` for conflicts
2. Check if Combat or Inventory agents are working
3. Create task entry if modifying shared UI sections

### During Development
1. Keep UI logic separate from game logic
2. Use existing UI patterns and styles
3. Maintain consistent color scheme (#0a0a0a background, #00ff88 accent)
4. Test UI changes in both player and dev modes

### After Completion
1. Update task status in `ACTIVE_TASKS.md`
2. Document UI changes in `.cursor/comms/change_log.md`
3. Run UI tests to verify changes
4. Update documentation if UI patterns change

## Common Tasks

### Typical UI/UX Agent Tasks
- Improve button layouts and styling
- Add animations and transitions
- Enhance visual feedback
- Optimize asset display performance
- Improve accessibility and usability
- Create new UI components
- Refactor UI code for maintainability

## Code Examples

### UI Pattern to Follow
```python
# Standard UI widget creation pattern
def create_ui_element(self):
    frame = tk.Frame(self.root, bg='#0a0a0a')
    label = tk.Label(frame, text="Text", fg='#00ff88', bg='#0a0a0a')
    button = tk.Button(frame, command=self.handle_action, bg='#44ff44')
    return frame
```

### Asset Display Pattern
```python
# Cache images to prevent reloading
if image_name not in self.image_cache:
    img = Image.open(path)
    self.image_cache[image_name] = ImageTk.PhotoImage(img)
```

## Questions or Issues?
- Check `.cursor/comms/questions.md` for coordination questions
- Review `docs/multi-agent/INTEGRATION_POINTS.md` for interface details
- Contact Combat Agent for combat UI coordination
- Contact Inventory Agent for inventory UI coordination

