# Multi-Agent Workflow Guide

This comprehensive guide explains how to use the multi-agent workflow system for efficient parallel development in the SHABUYA Cave Adventure project.

## Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Agent Roles](#agent-roles)
4. [Task Management](#task-management)
5. [Coordination Protocols](#coordination-protocols)
6. [Conflict Resolution](#conflict-resolution)
7. [Integration Workflow](#integration-workflow)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

## Overview

The multi-agent workflow system enables multiple Cursor agents to work efficiently in parallel on different aspects of the codebase while preventing conflicts and ensuring proper integration.

### Key Components

- **Agent Role Definitions**: Clear ownership and scope for each agent
- **Task Tracking System**: Track active work and prevent conflicts
- **Conflict Detection**: Automated detection of potential conflicts
- **Integration Validation**: Automated validation of agent changes
- **Coordination Protocols**: Standardized communication between agents

### Benefits

- **Parallel Development**: Multiple agents can work simultaneously
- **Conflict Prevention**: Automated detection prevents conflicts
- **Clear Ownership**: Each agent knows their responsibilities
- **Efficient Coordination**: Standardized protocols reduce overhead
- **Quality Assurance**: Integration validation ensures changes work together

## Getting Started

### Step 1: Identify Your Agent Role

1. Review agent role definitions in `.cursor/agents/`
2. Identify which agent role you represent
3. Read your agent role definition file thoroughly
4. Understand your primary files, secondary permissions, and forbidden files

### Step 2: Review Project Structure

1. Read `.cursorrules` for project-wide context
2. Review `docs/multi-agent/DEPENDENCY_MAP.md` for dependencies
3. Review `docs/multi-agent/FILE_OWNERSHIP.md` for file ownership
4. Review `docs/multi-agent/INTEGRATION_POINTS.md` for integration points

### Step 3: Check Active Tasks

1. Read `.cursor/tasks/ACTIVE_TASKS.md`
2. Check for conflicts with your planned work
3. Identify if files you need are already in use
4. Coordinate with agents working on conflicting tasks

### Step 4: Create Task Entry (if needed)

1. Use `.cursor/tasks/task_template.md` as template
2. Create task entry in `ACTIVE_TASKS.md`
3. Include files affected, dependencies, and coordination needs
4. Set status to `pending` or `in_progress`

## Agent Roles

### Available Agent Roles

1. **UI/UX Agent** (`agent-ui-ux.md`)
   - Primary: `player_gui.py`, `game_launcher.py`, `enhanced_gui_final.py`
   - Focus: UI layout, styling, user experience

2. **Combat Agent** (`agent-combat.md`)
   - Primary: `distribution/combat.py`
   - Focus: Combat mechanics, damage calculations, enemy definitions

3. **Inventory Agent** (`agent-inventory.md`)
   - Primary: `distribution/item.py`
   - Focus: Item management, inventory system, equipment

4. **Testing Agent** (`agent-testing.md`)
   - Primary: `tests/` directory, `utilities/` testing tools
   - Focus: Test creation, quality assurance, validation

5. **Documentation Agent** (`agent-documentation.md`)
   - Primary: `docs/` directory, `README.md`, `MVP_ROADMAP.md`
   - Focus: Documentation maintenance, guides, API references

6. **Assets Agent** (`agent-assets.md`)
   - Primary: `assets/` directory, asset processing utilities
   - Focus: Asset management, processing, validation

### Finding Your Role

- Check `.cursor/agents/agent-*.md` files
- Review `docs/multi-agent/FILE_OWNERSHIP.md` for file ownership
- Read agent role definition file thoroughly
- Understand your responsibilities and boundaries

## Task Management

### Task Lifecycle

1. **Pending**: Task created but not started
2. **In Progress**: Task currently being worked on
3. **Blocked**: Task waiting on dependency (move to BLOCKED_TASKS.md)
4. **Review**: Task completed, awaiting review
5. **Completed**: Task finished (move to COMPLETED_TASKS.md)

### Creating a Task

1. Use `.cursor/tasks/task_template.md` as template
2. Generate unique task ID (TASK-001, TASK-002, etc.)
3. Fill in all required fields
4. Add to `ACTIVE_TASKS.md`
5. Update status as you work

### Task Template Fields

- **Task ID**: Unique identifier (TASK-XXX)
- **Assigned Agent**: Your agent name
- **Status**: Current status
- **Description**: What needs to be done
- **Files Affected**: Which files will change
- **Dependencies**: What other tasks/agents are needed
- **Blocking Reason**: If blocked, explain why
- **Progress Notes**: Track your progress
- **Related Tasks**: Link to related tasks

### Managing Tasks

**Before Starting Work**:
- Check ACTIVE_TASKS.md for conflicts
- Create task entry if modifying shared files
- Update status to `in_progress`

**While Working**:
- Update progress notes regularly
- Update status if blocked
- Document coordination needs

**After Completing**:
- Move task to COMPLETED_TASKS.md
- Update related tasks if dependencies resolved
- Remove from ACTIVE_TASKS.md

## Coordination Protocols

### When Coordination is Required

Coordination is required when:
- Modifying shared state files (`config.py`, `player.py`)
- Modifying integration points (`player_gui.py` shared sections)
- Changing interface contracts
- Modifying files owned by another agent

### Coordination Steps

1. **Check Active Tasks**: Review ACTIVE_TASKS.md for conflicts
2. **Create Task Entry**: Document your planned work
3. **Contact Affected Agents**: Notify agents whose work is affected
4. **Discuss Changes**: Coordinate interface changes and timelines
5. **Get Approval**: Obtain approval before modifying shared files
6. **Implement Changes**: Make changes with coordination
7. **Validate Integration**: Run integration validation
8. **Update Documentation**: Update interface contracts if changed

### Communication Channels

- **ACTIVE_TASKS.md**: Task coordination and status
- **BLOCKED_TASKS.md**: Dependency tracking
- **.cursor/comms/change_log.md**: Document significant changes
- **.cursor/comms/questions.md**: Ask coordination questions

### Coordination Checklist

Before modifying shared files:

- [ ] Check ACTIVE_TASKS.md for conflicts
- [ ] Create task entry
- [ ] Contact affected agents
- [ ] Discuss interface changes
- [ ] Get approval
- [ ] Document coordination agreement
- [ ] Proceed with modification

## Conflict Resolution

### Conflict Detection

**Automated Detection**:
- Run `python utilities/check_agent_conflicts.py`
- Checks modified files against ACTIVE_TASKS.md
- Reports potential conflicts
- Can be run pre-commit

**Manual Detection**:
- Check ACTIVE_TASKS.md before starting work
- Review file ownership matrix
- Check integration points document

### Conflict Types

1. **File Conflicts**: Multiple agents modifying same file
2. **Interface Conflicts**: Changing shared interfaces without coordination
3. **Dependency Conflicts**: Tasks blocking each other
4. **State Conflicts**: Modifying shared state without coordination

### Resolution Steps

1. **Identify Conflict**: Detect conflict through automated or manual check
2. **Contact Conflicting Agent**: Notify agent working on conflicting task
3. **Discuss Resolution**: Determine how to resolve conflict
4. **Update Tasks**: Update task statuses accordingly
5. **Coordinate Changes**: Work together to resolve conflict
6. **Validate Integration**: Run integration validation after resolution

### Conflict Prevention

- Check ACTIVE_TASKS.md before starting work
- Create task entries for shared files
- Coordinate before modifying shared files
- Use conflict detection script regularly
- Communicate changes early

## Integration Workflow

### Integration Validation

**Automated Validation**:
- Run `python utilities/validate_integration.py`
- Checks imports, interfaces, and tests
- Validates configuration consistency
- Can be run pre-commit

**Manual Validation**:
- Review integration points document
- Check interface contracts
- Test affected modules
- Verify configuration consistency

### Integration Steps

1. **Before Changes**: Review integration points and dependencies
2. **During Changes**: Maintain interface contracts
3. **After Changes**: Run integration validation
4. **Test Integration**: Test affected modules together
5. **Update Documentation**: Update interface contracts if changed
6. **Notify Affected Agents**: Inform agents of interface changes

### Integration Checklist

After making changes:

- [ ] Run integration validation script
- [ ] Test affected modules
- [ ] Verify interface contracts still work
- [ ] Update documentation if interfaces changed
- [ ] Notify affected agents
- [ ] Move task to COMPLETED_TASKS.md

## Best Practices

### Code Development

1. **Follow Code Style**: Adhere to `.cursorrules` guidelines
2. **Maintain Interfaces**: Don't break interface contracts
3. **Test Changes**: Test your changes thoroughly
4. **Document Changes**: Document significant changes
5. **Coordinate Early**: Coordinate before modifying shared files

### Task Management

1. **Create Tasks Early**: Create task entries before starting work
2. **Update Regularly**: Update task status and progress regularly
3. **Track Dependencies**: Document task dependencies clearly
4. **Resolve Blockers**: Work to resolve blocking issues quickly
5. **Complete Tasks**: Move completed tasks to COMPLETED_TASKS.md

### Coordination

1. **Communicate Early**: Notify affected agents early
2. **Document Agreements**: Document coordination agreements
3. **Follow Protocols**: Follow coordination protocols consistently
4. **Resolve Conflicts**: Work to resolve conflicts quickly
5. **Update Documentation**: Update docs when interfaces change

### Quality Assurance

1. **Run Validation**: Run integration validation regularly
2. **Check Conflicts**: Check for conflicts before committing
3. **Test Integration**: Test integration after changes
4. **Review Changes**: Review changes before completing tasks
5. **Update Tests**: Update tests when features change

## Troubleshooting

### Common Issues

**Issue: File conflict detected**
- **Solution**: Check ACTIVE_TASKS.md, coordinate with conflicting agent, create task entry

**Issue: Integration validation fails**
- **Solution**: Check interface contracts, fix breaking changes, coordinate with affected agents

**Issue: Task blocked by dependency**
- **Solution**: Move to BLOCKED_TASKS.md, coordinate with blocking agent, update when unblocked

**Issue: Interface contract changed**
- **Solution**: Update INTEGRATION_POINTS.md, notify affected agents, coordinate updates

**Issue: Coordination needed but agent unavailable**
- **Solution**: Document in questions.md, create task entry, wait for coordination

### Getting Help

- **Check Documentation**: Review multi-agent documentation
- **Review Examples**: Look at completed tasks for examples
- **Ask Questions**: Use `.cursor/comms/questions.md`
- **Contact Agents**: Contact relevant agents directly
- **Review Protocols**: Review coordination protocols

## Quick Reference

### Essential Commands

```bash
# Check for conflicts
python utilities/check_agent_conflicts.py

# Validate integration
python utilities/validate_integration.py

# Run tests
python -m pytest tests/ -v
```

### Essential Files

- `.cursorrules` - Project-wide context
- `.cursor/agents/agent-*.md` - Agent role definitions
- `.cursor/tasks/ACTIVE_TASKS.md` - Active tasks
- `docs/multi-agent/DEPENDENCY_MAP.md` - Dependencies
- `docs/multi-agent/FILE_OWNERSHIP.md` - File ownership
- `docs/multi-agent/INTEGRATION_POINTS.md` - Integration points

### Quick Checklist

Before starting work:
- [ ] Identify agent role
- [ ] Review file ownership
- [ ] Check ACTIVE_TASKS.md
- [ ] Create task entry if needed
- [ ] Coordinate if required

After completing work:
- [ ] Run integration validation
- [ ] Test changes
- [ ] Update documentation
- [ ] Move task to COMPLETED_TASKS.md
- [ ] Notify affected agents

## Conclusion

The multi-agent workflow system enables efficient parallel development while preventing conflicts and ensuring proper integration. Follow these guidelines, use the provided tools, and coordinate effectively with other agents for successful multi-agent development.

For more information, see:
- `docs/multi-agent/AGENT_ONBOARDING.md` - Quick start guide
- `docs/multi-agent/BEST_PRACTICES.md` - Detailed best practices
- `.cursor/AGENT_QUICK_REF.md` - Quick reference guide

