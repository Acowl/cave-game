# Agent Communication Protocol

Standardized way for agents to communicate changes and coordinate work in the multi-agent workflow.

## Communication Channels

### Task Management
- **ACTIVE_TASKS.md** - Current work and coordination
- **BLOCKED_TASKS.md** - Dependency tracking
- **COMPLETED_TASKS.md** - Completed work log

### Change Documentation
- **.cursor/comms/change_log.md** - Significant changes log
- **.cursor/comms/notifications.md** - Important notifications
- **.cursor/comms/questions.md** - Coordination questions

## Communication Protocol

### Before Starting Work

**Required Actions**:
1. Check `ACTIVE_TASKS.md` for conflicts
2. Create task entry if modifying shared files
3. Contact affected agents if coordination needed
4. Document coordination agreement

**Communication Format**:
- Use task entries in ACTIVE_TASKS.md
- Include files affected, dependencies, coordination needs
- Update status as work progresses

### During Work

**When to Communicate**:
- When blocking another agent's work
- When unblocking a blocked task
- When interface contracts change
- When significant changes are made

**Communication Format**:
- Update task status in ACTIVE_TASKS.md
- Document changes in change_log.md
- Move blocked tasks to BLOCKED_TASKS.md
- Notify affected agents directly

### After Completing Work

**Required Actions**:
1. Update task status to `completed`
2. Move task to COMPLETED_TASKS.md
3. Document changes in change_log.md
4. Notify affected agents if interfaces changed
5. Update documentation if needed

**Communication Format**:
- Move task to COMPLETED_TASKS.md
- Add completion date
- Document changes in change_log.md
- Update related tasks if dependencies resolved

## Standard Messages

### Task Creation
```
Task ID: TASK-XXX
Assigned Agent: [agent-name]
Status: pending
Description: [what needs to be done]
Files Affected: [list of files]
Dependencies: [any dependencies]
```

### Coordination Request
```
Need coordination for: [file/purpose]
Affected agents: [list of agents]
Proposed changes: [description]
Timeline: [when changes will be made]
```

### Change Notification
```
File: [file path]
Changes: [description of changes]
Affected agents: [list of agents]
Interface changes: [yes/no, details if yes]
```

### Blocking Notification
```
Task ID: TASK-XXX
Blocking: TASK-YYY
Reason: [why blocked]
Expected resolution: [when/how]
```

## Coordination Checklist

### Before Modifying Shared Files

- [ ] Check ACTIVE_TASKS.md
- [ ] Create task entry
- [ ] Contact affected agents
- [ ] Discuss changes
- [ ] Get approval
- [ ] Document agreement

### When Blocking Others

- [ ] Update task status
- [ ] Move to BLOCKED_TASKS.md if applicable
- [ ] Document blocking reason
- [ ] Notify blocked agents
- [ ] Estimate resolution time

### When Unblocking

- [ ] Move task back to ACTIVE_TASKS.md
- [ ] Update status
- [ ] Remove blocking reason
- [ ] Notify unblocked agents
- [ ] Update dependencies

## Best Practices

1. **Communicate Early**: Notify agents early about planned changes
2. **Document Everything**: Document coordination agreements and changes
3. **Update Regularly**: Update task status and progress regularly
4. **Respond Promptly**: Respond to coordination requests promptly
5. **Follow Protocols**: Follow communication protocols consistently

## Questions or Issues?

- Check `.cursor/comms/questions.md` for coordination questions
- Review `docs/multi-agent/MULTI_AGENT_GUIDE.md` for detailed protocols
- Contact relevant agents directly for urgent coordination needs

