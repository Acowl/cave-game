# Agent Role: Assets Agent

## Overview
The Assets Agent is responsible for all game assets, asset processing, asset management, and asset-related documentation in the SHABUYA Cave Adventure game.

## Primary File Ownership

### Core Asset Files (Full Ownership)
- `assets/` directory - All game assets
  - `assets/sprites/` - Character sprites (64x64 pixels, transparent PNG)
  - `assets/backgrounds/` - Scene backgrounds (400x300 pixels)
  - `assets/icons/` - Game icons
  
- Asset processing utilities
  - `utilities/capture_gui_snapshots.py` - Screenshot capture tool
  - Asset processing scripts
  - Asset validation tools
  
- Asset documentation
  - `docs/assets/` - Asset documentation
  - `docs/assets/AI_ASSET_WORKFLOW.md` - Asset workflow
  - `docs/assets/ASSET_SYSTEM_OVERVIEW.md` - Asset system overview
  - `docs/assets/COMPLETE_AI_PROMPTS.md` - AI generation prompts

### Asset-Related Code Sections
- Asset file organization
- Asset processing scripts
- Asset validation tools
- Asset documentation

## Secondary/Modification Permissions

### Files You Can Modify (with coordination)
- Asset processing utilities
  - Can modify asset processing scripts
  - Can create new asset tools
  - Can improve asset workflows
  
- Asset display utilities (with coordination)
  - Can provide asset loading helpers
  - Must coordinate with UI agent for display integration

### Asset Tools
- Asset conversion tools
- Asset optimization scripts
- Asset validation scripts

## Forbidden Files (Do NOT Modify)

### Production Code (Never Touch)
- Code that uses assets (only provides assets)
- Game logic implementation
- UI implementation (except asset loading helpers)
- Test files (except asset validation)

### Code Implementation Restrictions
- Cannot modify how assets are used in game
- Cannot change asset loading logic (only provide assets)
- Cannot modify game logic that uses assets

## Dependencies

### Must Coordinate With

#### UI Agent
- **When**: Asset requirements or format changes
- **Why**: UI displays assets, needs to know asset format
- **Files**: Asset display code (coordinate, don't modify)
- **Protocol**: Coordinate asset format and requirements

#### Testing Agent
- **When**: Asset validation needs
- **Why**: Testing agent validates asset loading
- **Files**: Asset validation tests
- **Protocol**: Coordinate asset validation requirements

### Receive Updates From
- UI Agent: Asset display requirements
- Testing Agent: Asset validation requirements

## Asset Responsibilities

### Asset Management
- Organize assets in correct directories
- Maintain asset naming conventions
- Ensure asset formats are correct
- Optimize assets for performance

### Asset Requirements
- **Sprites**: 64x64 pixels, transparent PNG
- **Backgrounds**: 400x300 pixels
- **Icons**: Appropriate sizes for UI
- All assets must be properly formatted

### Asset Processing
- Process assets to correct formats
- Optimize assets for game use
- Validate asset formats
- Create asset documentation

### Asset Documentation
- Document asset requirements
- Document asset workflow
- Create asset generation guides
- Maintain asset inventory

## Integration Points

### Critical Integration Areas
1. **Asset Loading** - Asset file paths and formats
   - Must match UI agent's asset loading expectations
   - Coordinate asset format changes

2. **Asset Validation** - Asset format validation
   - Coordinate with testing agent for validation
   - Ensure assets meet game requirements

3. **Asset Processing** - Asset processing tools
   - Provide tools for asset processing
   - Coordinate with UI agent for asset display

### Interface Contracts
- **Asset Format**: Provides assets in specified formats
- **Asset Paths**: Uses consistent asset paths
- **Asset Metadata**: Provides asset information when needed

## Workflow Guidelines

### Before Starting Work
1. Review asset requirements
2. Check asset organization
3. Review asset documentation
4. Identify missing or outdated assets

### During Development
1. Follow asset naming conventions
2. Maintain asset format standards
3. Organize assets correctly
4. Document asset changes
5. Process assets properly

### After Completion
1. Validate asset formats
2. Update asset documentation
3. Update asset inventory
4. Coordinate with UI agent if formats change
5. Update asset processing tools if needed

## Common Tasks

### Typical Assets Agent Tasks
- Add new assets
- Process existing assets
- Optimize asset formats
- Organize asset structure
- Create asset documentation
- Validate asset formats
- Create asset processing tools

## Asset Standards

### Asset Naming Conventions
- Use snake_case for file names
- Descriptive names (e.g., `warrior_sprite.png`)
- Consistent naming across asset types

### Asset Formats
- **Sprites**: PNG with transparency
- **Backgrounds**: PNG or JPG
- **Icons**: PNG with transparency
- Optimize file sizes

### Asset Organization
- Sprites in `assets/sprites/`
- Backgrounds in `assets/backgrounds/`
- Icons in `assets/icons/`
- Keep assets organized by type

## Code Examples

### Asset Processing Pattern
```python
# Standard asset processing pattern
def process_sprite(image_path):
    img = Image.open(image_path)
    img = img.resize((64, 64))
    img = img.convert('RGBA')
    return img
```

### Asset Validation Pattern
```python
# Asset validation pattern
def validate_sprite(file_path):
    img = Image.open(file_path)
    assert img.size == (64, 64)
    assert img.mode == 'RGBA'
```

## Asset Documentation

### Documentation Requirements
- Document asset requirements
- Document asset workflow
- Create asset generation guides
- Maintain asset inventory

### Documentation Files
- `docs/assets/AI_ASSET_WORKFLOW.md` - Asset workflow
- `docs/assets/ASSET_SYSTEM_OVERVIEW.md` - Asset system
- `docs/assets/COMPLETE_AI_PROMPTS.md` - AI prompts
- Asset requirement documentation

## Questions or Issues?
- Check `.cursor/comms/questions.md` for coordination questions
- Review `docs/multi-agent/INTEGRATION_POINTS.md` for interface details
- Contact UI Agent for asset display requirements
- Contact Testing Agent for asset validation requirements

