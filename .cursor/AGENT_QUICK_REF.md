# Agent Quick Reference

One-page reference for agent roles, conflict checking, and common commands.

## Agent Roles

| Agent | Primary Files | Key Focus |
|-------|--------------|-----------|
| **UI/UX** | `player_gui.py`, `game_launcher.py` | UI layout, styling, UX |
| **Combat** | `distribution/combat.py` | Combat mechanics, damage |
| **Inventory** | `distribution/item.py` | Items, inventory, equipment |
| **Testing** | `tests/`, `utilities/` | Tests, validation, QA |
| **Documentation** | `docs/`, `README.md` | Docs, guides, API refs |
| **Assets** | `assets/` | Sprites, backgrounds, icons |

## Conflict Zones

**High Priority** (Require coordination):
- `distribution/config.py` - ALL agents
- `distribution/player.py` - Combat & Inventory agents
- `player_gui.py` - UI, Combat, Inventory agents

**Check Before Modifying**:
1. `.cursor/tasks/ACTIVE_TASKS.md`
2. `docs/multi-agent/FILE_OWNERSHIP.md`
3. `python utilities/check_agent_conflicts.py`

## Quick Conflict Check

```bash
# Check for conflicts
python utilities/check_agent_conflicts.py

# Validate integration
python utilities/validate_integration.py

# Run tests
python -m pytest tests/ -v
```

## Essential Files

| File | Purpose |
|------|---------|
| `.cursorrules` | Project context |
| `.cursor/agents/agent-*.md` | Your role definition |
| `.cursor/tasks/ACTIVE_TASKS.md` | Active tasks |
| `docs/multi-agent/FILE_OWNERSHIP.md` | File ownership |
| `docs/multi-agent/INTEGRATION_POINTS.md` | Integration points |

## Task Workflow

**Before Starting**:
1. Check ACTIVE_TASKS.md
2. Create task entry (if shared files)
3. Coordinate if needed

**While Working**:
- Update task progress
- Update status if blocked

**After Completing**:
1. Run integration validation
2. Test changes
3. Move to COMPLETED_TASKS.md

## Coordination Contacts

**For Shared Files**:
- `config.py` → All agents
- `player.py` → Combat & Inventory agents
- `player_gui.py` → UI, Combat, Inventory agents

**Check**: `.cursor/tasks/ACTIVE_TASKS.md` for active work

## Emergency Procedures

**Conflict Detected**:
1. Check ACTIVE_TASKS.md
2. Contact conflicting agent
3. Coordinate resolution
4. Update tasks

**Integration Failure**:
1. Check INTEGRATION_POINTS.md
2. Verify interface contracts
3. Coordinate with affected agents
4. Fix breaking changes

## Common Commands

```bash
# Conflict detection
python utilities/check_agent_conflicts.py

# Integration validation
python utilities/validate_integration.py --files file1.py file2.py

# Run specific tests
python -m pytest tests/unit/test_player_gui.py -v

# Check active tasks
cat .cursor/tasks/ACTIVE_TASKS.md
```

## Quick Checklist

Before modifying files:
- [ ] Check ACTIVE_TASKS.md
- [ ] Check FILE_OWNERSHIP.md
- [ ] Create task entry if needed
- [ ] Coordinate if required

After completing work:
- [ ] Run integration validation
- [ ] Test changes
- [ ] Update documentation
- [ ] Move task to COMPLETED_TASKS.md

## Getting Help

- **Full Guide**: `docs/multi-agent/MULTI_AGENT_GUIDE.md`
- **Onboarding**: `docs/multi-agent/AGENT_ONBOARDING.md`
- **Questions**: `.cursor/comms/questions.md`

