# Task Template

Use this template when creating new tasks in `ACTIVE_TASKS.md`.

## Task Entry Format

```markdown
### Task ID: [TASK-XXX]
**Assigned Agent**: [agent-name]
**Status**: [pending/in_progress/blocked/review]
**Created**: [YYYY-MM-DD]
**Updated**: [YYYY-MM-DD]

#### Description
[Clear description of what needs to be done]

#### Files Affected
- `path/to/file1.py` - [what will change]
- `path/to/file2.py` - [what will change]

#### Dependencies
- [Task ID] - [dependency description]
- [Agent Name] - [coordination needed]

#### Blocking Reason
[If blocked, explain why]

#### Progress Notes
- [YYYY-MM-DD] Task created
- [YYYY-MM-DD] Started work on [component]
- [YYYY-MM-DD] [Progress update]

#### Related Tasks
- [Task ID] - [relationship]
```

## Example Task Entry

```markdown
### Task ID: TASK-001
**Assigned Agent**: agent-ui-ux
**Status**: in_progress
**Created**: 2025-01-15
**Updated**: 2025-01-15

#### Description
Improve combat UI layout and add visual feedback for combat actions.

#### Files Affected
- `player_gui.py` - Combat UI display methods
- `distribution/gui.py` - Combat widget layout

#### Dependencies
- TASK-002 - Combat agent must finalize combat state structure
- agent-combat - Coordinate combat state interface

#### Blocking Reason
None

#### Progress Notes
- 2025-01-15 Task created
- 2025-01-15 Started work on combat UI layout
- 2025-01-15 Waiting for combat state structure from combat agent

#### Related Tasks
- TASK-002 - Combat state structure (dependency)
```

## Task ID Format
- Format: `TASK-XXX` where XXX is a sequential number
- Start from TASK-001
- Increment for each new task
- Use leading zeros (001, 002, etc.)

## Status Values
- `pending` - Task created but not started
- `in_progress` - Task currently being worked on
- `blocked` - Task waiting on dependency (move to BLOCKED_TASKS.md)
- `review` - Task completed, awaiting review
- `completed` - Task finished (move to COMPLETED_TASKS.md)

## Guidelines
- Be specific about what files will change
- List all dependencies clearly
- Update progress regularly
- Move to appropriate file when status changes
- Document blocking reasons clearly

