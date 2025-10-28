# 🚀 Quick Start Guide: GPT Codex 2025 Plan Mode

## Para sa AI Agent (Tagalog/English Guide)

### 📋 Bago Magsimula (Before You Start)

Kapag binigyan ka ng task, ito ang **MANDATORY** na sundin:

---

## ⚡ Step-by-Step Execution Guide

### Step 1: Basahin ang Iyong Sariling Instructions
```bash
# FIRST ACTION - NO EXCEPTIONS!
READ: .artifacts/agents.md
```

**Bakit?** Para malaman mo:
- ✅ Ano na ang natapos (completed tasks)
- 🎯 Ano ang kasalukuyang task (current task)
- 📅 Ano ang susunod na gagawin (upcoming tasks)
- 🔄 Context mula sa nakaraang session (continuity)

### Step 2: Basahin ang Plan Mode Protocol
```bash
READ: .artifacts/CODEX_PLAN_MODE_PROMPT.md
```

**Bakit?** Para maintindihan mo ang:
- 🧠 Paano gumamit ng plan mode properly
- 📊 Quality standards na dapat sundin
- 🔄 Update cadence para sa agents.md
- 🛡️ Error handling protocols

### Step 3: Update ang Current Task sa agents.md

Bago magsimula, i-update ang **"Current Task"** section:

```markdown
## 🎯 Current Task (Active)

**Task ID**: TASK-2025-001  
**Task Name**: [Descriptive name ng task]  
**Started**: 2025-10-28T14:30:00Z  
**Status**: IN_PROGRESS

### Task Objective
[Clear description kung ano ang goal]

### Subtasks
- [ ] Step 1: [Specific action]
- [ ] Step 2: [Specific action]
- [ ] Step 3: [Specific action]
```

### Step 4: Analyze ang Target Directory

```bash
# Analyze the .artifacts directory
LIST: .artifacts

# Explore subdirectories
LIST: .artifacts/meta-upgrades/
LIST: .artifacts/protocol-*/
LIST: .artifacts/scripts/
LIST: .artifacts/validation/
```

### Step 5: Break Down into Manageable Tasks

**Halimbawa**: Kung ang task ay "Analyze all meta-upgrades"

```markdown
### Subtasks (Broken Down)
- [ ] Step 1: Read and analyze UPG01-UPG03
- [ ] Step 2: Document patterns found in UPG01-UPG03
- [ ] Step 3: Read and analyze UPG04-UPG06
- [ ] Step 4: Document patterns found in UPG04-UPG06
- [ ] Step 5: Read and analyze UPG07-UPG10
- [ ] Step 6: Document patterns found in UPG07-UPG10
- [ ] Step 7: Cross-analyze all patterns
- [ ] Step 8: Generate comprehensive report
```

### Step 6: Execute Each Subtask Systematically

Para sa bawat subtask:

```yaml
1. UPDATE agents.md:
   - Mark current subtask as active
   
2. EXECUTE the subtask:
   - Read required files
   - Perform analysis
   - Generate output
   
3. VALIDATE the outcome:
   - Check quality standards
   - Verify completeness
   
4. DOCUMENT the result:
   - Update agents.md
   - Create evidence artifacts
   
5. CHECK OFF the subtask:
   - [x] Completed subtask
```

### Step 7: Update Progress Continuously

**During Execution**, update these sections in `agents.md`:

```markdown
### Subtasks
- [x] Step 1: Read and analyze UPG01-UPG03 ✅
- [x] Step 2: Document patterns found ✅
- [ ] Step 3: Read and analyze UPG04-UPG06 ⏳ (CURRENT)

### Decisions Made
- 2025-10-28T14:35:00Z: Decided to use JSON schema for pattern extraction
- 2025-10-28T14:50:00Z: Prioritizing alignment.md validation first

### Blockers/Dependencies
- None currently
```

### Step 8: Handle Blockers Properly

Kung may blocker:

```markdown
### Blockers/Dependencies
- **Blocker 1**: Missing UPG05/intent.json file
  - Impact: Cannot complete UPG04-UPG06 analysis
  - Resolution: Check if file exists elsewhere or mark as gap
  - Status: INVESTIGATING
  - Created: 2025-10-28T15:00:00Z
```

### Step 9: Complete Task & Update

Kapag tapos na ang task:

```markdown
## ✅ Completed Tasks

### Meta-Upgrades Analysis
- [x] **Analyze UPG01-UPG03**: Completed 2025-10-28T15:30:00Z
  - Artifacts: .artifacts/meta-upgrades/analysis-upg01-03.json
  - Patterns: 5 common patterns identified
  - Quality: All gates passed ✅
```

### Step 10: Session Handoff

Bago mag-end ng session, i-update ang **"Session Continuity Protocol"**:

```markdown
## 💡 Session Continuity Protocol

### For Next Agent/Session
**Last Session Summary**: 
Completed analysis of UPG01-UPG03, identified 5 common patterns,
documented findings in analysis-upg01-03.json. All quality gates passed.

**Current State**: 
Ready to begin UPG04-UPG06 analysis. All prerequisites met.

**Next Recommended Action**: 
Execute Step 3: Read and analyze UPG04-UPG06 artifacts.

**Important Context**: 
Pattern schema is defined in .artifacts/meta-upgrades/pattern-schema.json
```

---

## 🎯 Concrete Example: Current Task

### Task: Analyze Meta-Upgrades Directory

#### Before Starting
1. ✅ READ: agents.md
2. ✅ READ: CODEX_PLAN_MODE_PROMPT.md
3. ✅ UPDATE: Current Task in agents.md

#### Execution Flow

```markdown
## Current Task Details

**Task ID**: ANALYZE-META-UPG-001
**Task Name**: Comprehensive Meta-Upgrades Analysis
**Started**: 2025-10-28T16:00:00Z
**Status**: IN_PROGRESS

### Task Objective
Analyze all meta-upgrade artifacts (UPG01-UPG10) in 
.artifacts/meta-upgrades/
and create comprehensive documentation of:
- Common patterns across upgrades
- Gaps or missing artifacts
- Quality compliance status
- Actionable tasks for improvement

### Subtasks
- [ ] Phase 1: Inventory all UPG directories
- [ ] Phase 2: Analyze UPG01-UPG03 artifacts
- [ ] Phase 3: Analyze UPG04-UPG06 artifacts
- [ ] Phase 4: Analyze UPG07-UPG10 artifacts
- [ ] Phase 5: Cross-analysis and pattern identification
- [ ] Phase 6: Gap analysis
- [ ] Phase 7: Generate comprehensive report
- [ ] Phase 8: Create actionable tasks from findings
```

#### Commands to Execute

```bash
# Phase 1: Inventory
LIST: .artifacts/meta-upgrades/
LIST: .artifacts/meta-upgrades/UPG01/
LIST: .artifacts/meta-upgrades/UPG02/
# ... repeat for all UPGs

# Phase 2: Read UPG01 artifacts
READ: .artifacts/meta-upgrades/UPG01/intent.json
READ: .artifacts/meta-upgrades/UPG01/analysis.json
READ: .artifacts/meta-upgrades/UPG01/decision.json
READ: .artifacts/meta-upgrades/UPG01/alignment.md

# Extract and document patterns
CREATE: .artifacts/meta-upgrades/analysis/upg01-patterns.json

# Repeat for other UPGs...
```

---

## 📊 Quality Checklist

Bago i-mark as complete ang task:

- [ ] All subtasks are checked off in agents.md
- [ ] All evidence artifacts are created
- [ ] Quality standards are met:
  - [ ] Structural compliance
  - [ ] Content accuracy
  - [ ] Completeness
  - [ ] Consistency
  - [ ] Traceability
- [ ] agents.md is fully updated:
  - [ ] Current Task moved to Completed
  - [ ] Session Continuity filled out
  - [ ] Next recommended action identified
  - [ ] Decisions documented
  - [ ] Blockers resolved or documented
- [ ] Documentation is clear and actionable

---

## 🚨 Common Mistakes to Avoid

### ❌ Anti-Pattern 1: Starting Without Reading agents.md
```
WRONG: Immediately start analyzing files
RIGHT: First read agents.md to understand context
```

### ❌ Anti-Pattern 2: Not Breaking Down Tasks
```
WRONG: "Analyze all meta-upgrades" (too big)
RIGHT: Break into 8-10 specific subtasks
```

### ❌ Anti-Pattern 3: Not Updating agents.md
```
WRONG: Complete work but don't update agents.md
RIGHT: Update agents.md after every subtask
```

### ❌ Anti-Pattern 4: No Evidence Trail
```
WRONG: Do analysis in memory only
RIGHT: Create JSON/MD artifacts for every finding
```

### ❌ Anti-Pattern 5: Poor Session Handoff
```
WRONG: End session without updating continuity
RIGHT: Fill out complete session summary
```

---

## 🎓 Best Practices

### ✅ Do This
- Read agents.md FIRST, always
- Break tasks into small chunks
- Update agents.md frequently
- Create evidence artifacts
- Document decisions as you make them
- Handle blockers immediately
- Write clear session handoffs

### ❌ Don't Do This
- Skip reading agents.md
- Take on huge tasks without breakdown
- Update agents.md only at the end
- Keep analysis in memory only
- Make decisions without documentation
- Ignore blockers and continue
- End session without handoff notes

---

## 🚀 Ready to Start?

### Your First Command Should Be:
```markdown
"Let me first read my instructions in agents.md to understand 
the context and what has been done so far..."

Then proceed to read:
1. .artifacts/agents.md
2. .artifacts/CODEX_PLAN_MODE_PROMPT.md

Then update Current Task and begin execution!
```

---

## 📞 Help & Resources

### Key Files
- **agents.md**: Your task tracker and instructions
- **CODEX_PLAN_MODE_PROMPT.md**: Plan mode best practices
- **governance-index.json**: Governance tracking
- **meta-upgrades/**: Upgrade artifacts to analyze

### Automation Scripts
```bash
python scripts/validate_protocols.py
python scripts/validate_evidence.py
python scripts/run_quality_audit.py
```

### Quality Standards
All tasks must meet:
- Structural compliance ✅
- Content accuracy ✅
- Completeness ✅
- Consistency ✅
- Traceability ✅

---

**Tandaan (Remember)**: 
- 📖 Basahin muna ang agents.md
- 🎯 Break down big tasks
- ✅ Update frequently
- 📊 Create evidence
- 🔄 Document handoffs

**Simulan na! (Start now!)** 🚀

