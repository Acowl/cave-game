# Active Tasks

This file tracks all currently active tasks being worked on by agents. Agents must check this file before starting work and update it when starting/completing tasks.

## Format
Each task entry should follow the task template format defined in `task_template.md`.

## Active Tasks

### Currently Empty
No active tasks at this time. All cleanup and restructuring tasks have been completed.

---

## Usage Instructions

### Before Starting Work
1. Check this file for conflicts with your planned work
2. Check if files you need to modify are listed in active tasks
3. Create a new task entry if modifying shared files
4. Update task status when starting work

### While Working
- Keep task status updated
- Update progress as you work
- Note any blocking issues

### After Completing
- Move task to `COMPLETED_TASKS.md`
- Remove from this file
- Update related tasks if dependencies resolved

## Task Status Values
- `pending` - Task created but not started
- `in_progress` - Task currently being worked on
- `blocked` - Task waiting on dependency (move to BLOCKED_TASKS.md)
- `review` - Task completed, awaiting review

## Coordination
- If you find a conflict, contact the agent working on the conflicting task
- Coordinate through `.cursor/comms/questions.md` if needed
- Update task status when blocking/unblocking others
