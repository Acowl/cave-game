# Agent Onboarding Guide

Quick start guide for new agents joining the SHABUYA Cave Adventure multi-agent development workflow.

## Welcome!

This guide will help you get started quickly with the multi-agent workflow system. Follow these steps to begin contributing effectively.

## Step 1: Identify Your Agent Role (5 minutes)

### Find Your Role

1. Navigate to `.cursor/agents/` directory
2. Review available agent role files:
   - `agent-ui-ux.md` - UI/UX development
   - `agent-combat.md` - Combat system
   - `agent-inventory.md` - Inventory/items
   - `agent-testing.md` - Testing/QA
   - `agent-documentation.md` - Documentation
   - `agent-assets.md` - Asset management

3. Identify which role matches your assigned work
4. Read your agent role definition file thoroughly

### Understand Your Scope

From your agent role file, note:
- **Primary Files**: Files you own and can modify freely
- **Secondary Files**: Files you can modify with coordination
- **Forbidden Files**: Files you should never modify
- **Dependencies**: Which agents you need to coordinate with

## Step 2: Review Project Context (10 minutes)

### Read Essential Files

1. **`.cursorrules`** - Project-wide context and guidelines
   - Code style guidelines
   - Architecture principles
   - Testing requirements

2. **`docs/multi-agent/FILE_OWNERSHIP.md`** - File ownership matrix
   - See which agent owns which files
   - Identify conflict zones
   - Understand coordination requirements

3. **`docs/multi-agent/INTEGRATION_POINTS.md`** - Integration points
   - Understand where agents' work connects
   - Learn interface contracts
   - Know coordination requirements

## Step 3: Check Current Work (5 minutes)

### Review Active Tasks

1. Open `.cursor/tasks/ACTIVE_TASKS.md`
2. Check for conflicts with your planned work
3. Identify if files you need are already in use
4. Note any dependencies or blocking tasks

### Check for Conflicts

Run conflict detection:
```bash
python utilities/check_agent_conflicts.py
```

This will show if your planned files conflict with active tasks.

## Step 4: Understand Your Files (10 minutes)

### Primary Files

Review your primary files:
- Understand their structure
- Note key functions and classes
- Identify integration points

### Secondary Files

Review files you can modify with coordination:
- Understand what sections you can modify
- Note coordination requirements
- Identify affected agents

### Forbidden Files

Understand files you cannot modify:
- Know why they're forbidden
- Understand who owns them
- Know how to request changes if needed

## Step 5: Create Your First Task (5 minutes)

### Task Template

Use `.cursor/tasks/task_template.md` as a template:

1. **Task ID**: Generate unique ID (TASK-001, TASK-002, etc.)
2. **Assigned Agent**: Your agent name
3. **Status**: Set to `pending` or `in_progress`
4. **Description**: Clear description of what you'll do
5. **Files Affected**: List files you'll modify
6. **Dependencies**: Any dependencies or coordination needs

### Add to Active Tasks

1. Open `.cursor/tasks/ACTIVE_TASKS.md`
2. Add your task entry at the top
3. Follow the template format
4. Update status as you work

## Step 6: Coordinate If Needed (as needed)

### When Coordination is Required

Coordinate if you're:
- Modifying shared state files (`config.py`, `player.py`)
- Modifying integration points (`player_gui.py` shared sections)
- Changing interface contracts
- Modifying files owned by another agent

### Coordination Steps

1. **Check Active Tasks**: Review ACTIVE_TASKS.md
2. **Create Task Entry**: Document your planned work
3. **Contact Agents**: Notify affected agents
4. **Discuss Changes**: Coordinate interface changes
5. **Get Approval**: Obtain approval before modifying
6. **Proceed**: Make changes with coordination

## Step 7: Start Development

### Before Making Changes

- [ ] Check ACTIVE_TASKS.md for conflicts
- [ ] Create task entry if modifying shared files
- [ ] Coordinate with affected agents if needed
- [ ] Understand interface contracts

### During Development

- [ ] Follow code style guidelines (`.cursorrules`)
- [ ] Maintain interface contracts
- [ ] Update task progress regularly
- [ ] Test your changes

### After Completing

- [ ] Run integration validation
- [ ] Test affected modules
- [ ] Update documentation if needed
- [ ] Move task to COMPLETED_TASKS.md
- [ ] Notify affected agents

## Essential Commands

### Conflict Detection
```bash
python utilities/check_agent_conflicts.py
```

### Integration Validation
```bash
python utilities/validate_integration.py
```

### Run Tests
```bash
python -m pytest tests/ -v
```

### Run Specific Tests
```bash
python -m pytest tests/unit/test_player_gui.py -v
```

## Quick Reference

### Essential Files

| File | Purpose |
|------|---------|
| `.cursorrules` | Project-wide context |
| `.cursor/agents/agent-*.md` | Your agent role definition |
| `.cursor/tasks/ACTIVE_TASKS.md` | Active tasks |
| `docs/multi-agent/FILE_OWNERSHIP.md` | File ownership |
| `docs/multi-agent/INTEGRATION_POINTS.md` | Integration points |
| `docs/multi-agent/DEPENDENCY_MAP.md` | Dependencies |

### Task Status Values

- `pending` - Task created but not started
- `in_progress` - Task currently being worked on
- `blocked` - Task waiting on dependency
- `review` - Task completed, awaiting review
- `completed` - Task finished

### Common Workflows

**Starting New Work**:
1. Check ACTIVE_TASKS.md
2. Create task entry
3. Coordinate if needed
4. Start development

**Modifying Shared Files**:
1. Check ACTIVE_TASKS.md
2. Create task entry
3. Coordinate with affected agents
4. Get approval
5. Make changes
6. Validate integration

**Completing Work**:
1. Run integration validation
2. Test changes
3. Update documentation
4. Move task to COMPLETED_TASKS.md

## Common Scenarios

### Scenario 1: Working on Primary Files

**What to do**:
1. Check ACTIVE_TASKS.md for conflicts
2. Create task entry
3. Start development
4. Test changes
5. Complete task

**No coordination needed** if files are truly yours.

### Scenario 2: Modifying Shared Files

**What to do**:
1. Check ACTIVE_TASKS.md for conflicts
2. Create task entry
3. Coordinate with affected agents
4. Get approval
5. Make changes
6. Validate integration
7. Complete task

**Coordination required** for shared files.

### Scenario 3: Task Blocked

**What to do**:
1. Move task to BLOCKED_TASKS.md
2. Document blocking reason
3. Coordinate with blocking agent
4. Wait for dependency resolution
5. Move back to ACTIVE_TASKS.md when unblocked

### Scenario 4: Conflict Detected

**What to do**:
1. Review conflict details
2. Contact conflicting agent
3. Discuss resolution
4. Coordinate changes
5. Update tasks
6. Resolve conflict

## Getting Help

### Documentation

- **Full Guide**: `docs/multi-agent/MULTI_AGENT_GUIDE.md`
- **Best Practices**: `docs/multi-agent/BEST_PRACTICES.md`
- **Quick Reference**: `.cursor/AGENT_QUICK_REF.md`

### Communication

- **Questions**: `.cursor/comms/questions.md`
- **Change Log**: `.cursor/comms/change_log.md`
- **Tasks**: `.cursor/tasks/ACTIVE_TASKS.md`

### Troubleshooting

- Check documentation first
- Review examples in completed tasks
- Ask questions in questions.md
- Contact relevant agents

## Next Steps

1. **Complete Onboarding**: Finish reading this guide
2. **Review Role**: Read your agent role definition thoroughly
3. **Check Tasks**: Review ACTIVE_TASKS.md
4. **Create Task**: Create your first task entry
5. **Start Work**: Begin your assigned work

## Tips for Success

1. **Check Before Starting**: Always check ACTIVE_TASKS.md first
2. **Coordinate Early**: Coordinate before modifying shared files
3. **Update Regularly**: Update task status and progress regularly
4. **Test Thoroughly**: Test your changes before completing
5. **Document Changes**: Document significant changes
6. **Follow Protocols**: Follow coordination protocols consistently

## Welcome Aboard!

You're now ready to contribute to the multi-agent workflow. Remember:
- Check ACTIVE_TASKS.md before starting
- Create task entries for shared files
- Coordinate with affected agents
- Test your changes thoroughly
- Update documentation when needed

Good luck with your contributions!

