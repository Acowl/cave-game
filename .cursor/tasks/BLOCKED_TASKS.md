# Blocked Tasks

This file tracks tasks that are blocked waiting on dependencies or other agents' work.

## Format
Each task entry should follow the task template format with blocking reason clearly stated.

## Blocked Tasks

### Currently Empty
No blocked tasks at this time.

---

## Usage Instructions

### When a Task is Blocked
1. Move task from `ACTIVE_TASKS.md` to this file
2. Clearly state blocking reason
3. Identify what needs to happen to unblock
4. Note which agent/dependency is blocking

### When Unblocking a Task
1. Move task back to `ACTIVE_TASKS.md`
2. Update status to `pending` or `in_progress`
3. Remove blocking reason
4. Notify blocking agent if needed

### Tracking Blockers
- Update blocking status regularly
- Check if blockers have been resolved
- Coordinate with blocking agents
- Document resolution steps

## Blocking Reasons
Common blocking reasons:
- Waiting on another agent's work
- Dependency not implemented
- Shared file conflict
- API change needed
- Testing dependency

## Coordination
- Check this file regularly for unblocked tasks
- Update blocking status when dependencies resolve
- Coordinate with blocking agents to resolve issues

