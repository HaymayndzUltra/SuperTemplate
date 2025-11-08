# Paano Mag-Execute ng Tasks - Protocol 10 Guide

**Date:** 2025-01-27  
**Language:** Tagalog/Filipino

---

## 📍 Saan Makikita ang Tasks?

### Task File Location:
```
.cursor/tasks/tasks-freelancer-command-center-mvp.md
```

**Full Path:**
```
/home/haymayndz/SuperTemplate/.cursor/tasks/tasks-freelancer-command-center-mvp.md
```

### Paano i-View ang Tasks:

**Option 1: Via Terminal**
```bash
cd /home/haymayndz/SuperTemplate
cat .cursor/tasks/tasks-freelancer-command-center-mvp.md
```

**Option 2: Via Code Editor**
- Open file: `.cursor/tasks/tasks-freelancer-command-center-mvp.md`
- View all tasks with their subtasks

**Option 3: Search Specific Task**
```bash
cd /home/haymayndz/SuperTemplate
grep -A 50 "Task 1.3" .cursor/tasks/tasks-freelancer-command-center-mvp.md
```

---

## 🎯 Paano Mag-Execute ng Task?

### Method 1: Direct Command (Recommended)

**Para mag-execute ng specific task:**
```
proceed Task 1.3 - Authentication Infrastructure
```

**Para mag-execute ng next task:**
```
proceed Task 1.3
```

**Para mag-execute ng task by ID:**
```
proceed Task 1.3
```

### Method 2: Via Protocol 10 Reference

**Sa chat, sabihin mo:**
```
Apply instructions from @10-process-tasks.md
proceed Task 1.3
```

**O kaya:**
```
@10-process-tasks.md proceed Task 1.3
```

### Method 3: Complete Command Format

**Para sa specific task:**
```
proceed Task {task_id} - {task_name}
```

**Example:**
```
proceed Task 1.3 - Authentication Infrastructure
```

---

## 📋 Task Structure

### Task Format:
```markdown
### Task {ID}: {Task Name}
**Priority:** Critical | High | Medium | Low
**Complexity:** High | Medium | Low
**Effort:** X days
**Dependencies:** Task X.Y
**Persona:** Role Name

**Sub-tasks:**
1. Subtask 1
2. Subtask 2
...
```

### Current Tasks Available:

**Epic 1: Foundation & Infrastructure**
- ✅ Task 1.1: Project Setup & Configuration (Complete)
- ✅ Task 1.2: Database Schema & Migrations (Complete - 83%)
- ⏳ Task 1.3: Authentication Infrastructure (Next)
- ⏳ Task 1.4: API Foundation (Pending)

**Epic 2: Core Features**
- ⏳ Task 2.1: Client Management API (Pending)
- ⏳ Task 2.2: Project Management API (Pending)
- ...

---

## ✅ Current Status

### Completed Tasks:
- ✅ **Task 1.1** - Project Setup & Configuration
- ✅ **Task 1.2** - Database Schema & Migrations (83% - migration SQL ready)

### Next Task:
- ⏳ **Task 1.3** - Authentication Infrastructure

---

## 🚀 Quick Commands

### Para mag-view ng task:
```bash
# View specific task
grep -A 50 "Task 1.3" .cursor/tasks/tasks-freelancer-command-center-mvp.md

# View all tasks
cat .cursor/tasks/tasks-freelancer-command-center-mvp.md | grep -E "^### Task"
```

### Para mag-execute:
**Sa chat:**
```
proceed Task 1.3
```

**O kaya:**
```
proceed Task 1.3 - Authentication Infrastructure
```

### Para mag-check ng status:
```bash
# Check task state
cat .artifacts/protocol-10/task-state-task-1.2.json

# Check execution log
cat .artifacts/protocol-10/execution-session-log-task-1.2.md
```

---

## 📝 Evidence Files Location

**All evidence stored in:**
```
.artifacts/protocol-10/
├── subtask-evidence/
│   ├── 1.1/
│   └── 1.2/
├── quality-reports/
├── execution-session-log-task-1.2.md
├── task-state-task-1.2.json
└── preflight-checklist-task-1.2.json
```

---

## 💡 Tips

1. **Always check task file first:**
   ```bash
   cat .cursor/tasks/tasks-freelancer-command-center-mvp.md
   ```

2. **Use simple command format:**
   ```
   proceed Task {ID}
   ```

3. **Check dependencies:**
   - Always check if previous tasks are complete
   - Task 1.3 depends on Task 1.1 (✅ Complete)

4. **View task details:**
   - Open `.cursor/tasks/tasks-freelancer-command-center-mvp.md`
   - Search for specific task ID

---

**Ready to execute Task 1.3? Sabihin mo lang:**
```
proceed Task 1.3
```




