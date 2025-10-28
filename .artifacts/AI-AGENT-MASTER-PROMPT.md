# 🤖 AI Agent Master Prompt - Artifacts Analysis & Management System

## 🎯 Mission Statement

You are an AI agent tasked with systematically analyzing and managing the artifacts directory at `/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts`. Your work will be methodical, evidence-based, and fully documented using a task management system.

---

## 📋 MANDATORY FIRST STEPS (Execute in Order)

### Step 1: Self-Initialization
Before doing ANYTHING else, you MUST:

```
1. Read and understand: /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/agents.md
2. Update the "Current Session" section with:
   - Current timestamp (ISO 8601 format)
   - Your AI model name and version
   - Your planned scope for this session
3. Review all "Completed Tasks" to avoid duplication
4. Review "Next Tasks" to understand priorities
5. Commit to this protocol
```

**Output after Step 1:**
```
✅ Initialization Complete
   - agents.md read and understood
   - Current session logged
   - Task queue reviewed
   - Ready to proceed with highest priority task
```

### Step 2: Plan Mode Activation

Follow GPT Codex 2025 Plan Mode Protocol:

1. **Analyze** the complete task before execution
2. **Break down** complex tasks into atomic steps
3. **Document** each step's purpose and expected output
4. **Validate** prerequisites before proceeding
5. **Execute** systematically with evidence collection
6. **Verify** results against quality gates

---

## 🔍 Primary Analysis Objectives

### Objective 1: Complete Artifacts Inventory
**What to analyze:**
```
/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/
├── All subdirectories
├── All files and their purposes
├── Relationships between artifacts
├── Completion status of work items
└── Quality and validation states
```

**Expected outputs:**
- `artifacts-catalog.json` - Complete inventory
- `artifacts-structure-map.md` - Visual hierarchy
- `artifacts-status-report.md` - Completion analysis

### Objective 2: Meta-Upgrades Deep Analysis
**What to analyze:**
```
/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/meta-upgrades/
├── Each UPG folder (UPG01-UPG10+)
│   ├── alignment.md (check existence and content)
│   ├── analysis.json (check existence and content)
│   ├── intent.json (check existence and content)
│   └── decision.json (check existence and content)
├── catalog/ directory
├── cross/ directory
├── final/ directory
├── integration/ directory
└── pop/ directory
```

**Expected outputs:**
- `meta-upgrades-completion-matrix.json` - Per-UPG status
- `meta-upgrades-analysis-report.md` - Findings and patterns
- `meta-upgrades-gaps.json` - Missing or incomplete items

### Objective 3: Protocol Artifacts Mapping
**What to analyze:**
```
All protocol-XX/ directories and files
- Protocol dependencies
- Execution status
- Validation artifacts
- Integration points
```

**Expected outputs:**
- `protocol-inventory.json` - Complete protocol catalog
- `protocol-dependency-graph.md` - Visual dependencies
- `protocol-validation-status.json` - Validation results

### Objective 4: Scripts & Automation Analysis
**What to analyze:**
```
/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/scripts/
- All automation scripts
- Their purposes and capabilities
- Integration with protocols
- Validation mechanisms
```

**Expected outputs:**
- `scripts-catalog.json` - Script inventory
- `scripts-integration-map.md` - How scripts support workflows
- `scripts-validation-report.md` - Script quality assessment

---

## 🎯 Task Execution Protocol

### For EVERY Task You Execute:

#### 1. PRE-EXECUTION (Mandatory)
```markdown
**Task ID:** [Assign unique ID, e.g., TASK-001]
**Task Name:** [Clear, descriptive name]
**Priority:** [High/Medium/Low]
**Prerequisites:** [List what must exist before starting]
**Expected Outputs:** [List all artifacts this task will produce]
**Success Criteria:** [How you'll know it's complete]
```

#### 2. EXECUTION (Documented)
```markdown
**Steps:**
1. [Action 1] → [Expected Result 1]
2. [Action 2] → [Expected Result 2]
...

**Progress Log:**
- [Timestamp] Started Step 1
- [Timestamp] Completed Step 1 - Result: [brief note]
- [Timestamp] Started Step 2
...
```

#### 3. POST-EXECUTION (Validation)
```markdown
**Outputs Produced:**
- [File 1]: /absolute/path/to/file1.ext
- [File 2]: /absolute/path/to/file2.ext

**Quality Validation:**
✅ File exists and is accessible
✅ Content is well-structured
✅ Data is accurate and complete
✅ Follows format standards
✅ Documented in agents.md

**Evidence:**
[Paste relevant validation results, file snippets, or confirmations]
```

#### 4. AGENTS.MD UPDATE (Required)
```markdown
After completing ANY task, you MUST:

1. Move task from "In Progress" to "Completed Tasks" in agents.md
2. Document:
   - Timestamp
   - Task ID and description
   - All artifacts produced (with paths)
   - Validation evidence
   - Any new tasks discovered
3. Update "Next Tasks" queue with follow-up work
4. Set task status indicators
```

---

## 📐 Quality Gates (Must Pass)

### Gate 1: Structural Integrity
- [ ] All expected files/folders analyzed
- [ ] No broken references or missing dependencies
- [ ] Catalog is complete and accurate

### Gate 2: Content Accuracy
- [ ] Data extracted matches source
- [ ] No assumptions made without documentation
- [ ] Uncertainties explicitly flagged

### Gate 3: Documentation Completeness
- [ ] All findings documented in appropriate artifacts
- [ ] agents.md is current and accurate
- [ ] Evidence is verifiable and traceable

### Gate 4: Task Management Hygiene
- [ ] No orphaned "In Progress" tasks
- [ ] Completed tasks have full evidence
- [ ] Next tasks are clearly defined and prioritized

---

## 🚀 Execution Workflow

### Phase 1: Bootstrap (First Session)
```
1. Read agents.md
2. Initialize "Current Session" section
3. Execute TASK-001: Initial Artifacts Directory Scan
4. Update agents.md with completion
5. Proceed to next highest priority task
```

### Phase 2: Systematic Analysis (Ongoing)
```
For each task in queue:
1. Check prerequisites in agents.md
2. Move to "In Progress"
3. Execute task following execution protocol
4. Validate against quality gates
5. Update agents.md
6. Continue to next task
```

### Phase 3: Integration & Synthesis (Final)
```
When all individual analyses complete:
1. Create master synthesis document
2. Identify cross-cutting patterns
3. Generate actionable recommendations
4. Finalize all documentation
5. Mark project as complete in agents.md
```

---

## 📊 Output Format Standards

### JSON Files
```json
{
  "metadata": {
    "generated_by": "AI Agent",
    "timestamp": "2025-10-28T...",
    "source_analysis": "/.../path/to/source",
    "version": "1.0"
  },
  "data": {
    // Your structured data here
  },
  "validation": {
    "status": "PASS|FAIL",
    "checks_performed": [],
    "notes": ""
  }
}
```

### Markdown Reports
```markdown
# Report Title

**Generated:** [Timestamp]
**AI Model:** [Your model name]
**Source:** [What was analyzed]

## Executive Summary
[2-3 paragraph overview]

## Detailed Findings
### Finding 1
...

## Evidence
[References to source files, with line numbers if applicable]

## Recommendations
[Actionable next steps]

## Appendix
[Supporting data]
```

---

## 🔔 Critical Reminders

### ⚠️ ALWAYS:
1. **Read agents.md FIRST** before any work
2. **Update agents.md AFTER** every task
3. **Validate your work** against quality gates
4. **Document uncertainties** - never assume
5. **Produce tangible artifacts** - no work without evidence
6. **Follow the task lifecycle** - Next → In Progress → Completed

### ❌ NEVER:
1. Skip reading agents.md
2. Leave tasks in "In Progress" indefinitely
3. Create outputs without updating agents.md
4. Make assumptions without flagging them
5. Duplicate work already in "Completed Tasks"
6. Proceed without checking prerequisites

---

## 🎓 Example First Task Execution

### Task: Initial Artifacts Directory Scan

#### Pre-Execution
```markdown
**Task ID:** TASK-001
**Task Name:** Initial Artifacts Directory Scan
**Priority:** High
**Prerequisites:** 
  - agents.md exists and is initialized
  - Access to /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/
**Expected Outputs:**
  - artifacts-catalog.json
  - artifacts-structure-map.md
**Success Criteria:**
  - All directories and files cataloged
  - Structure visualized in markdown
  - No access errors encountered
```

#### Execution
```bash
# Scan directory
ls -R /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/ > raw-scan.txt

# Analyze structure
# ... (AI performs analysis)

# Generate catalog
# ... (AI creates artifacts-catalog.json)

# Generate structure map
# ... (AI creates artifacts-structure-map.md)
```

#### Post-Execution
```markdown
**Outputs Produced:**
- artifacts-catalog.json: /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/artifacts-catalog.json
- artifacts-structure-map.md: /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/artifacts-structure-map.md

**Quality Validation:**
✅ Both files created successfully
✅ Catalog contains 247 entries
✅ Structure map has 5 levels of hierarchy
✅ All paths verified as accessible
✅ Documented in agents.md

**Evidence:**
Catalog excerpt:
{
  "total_items": 247,
  "directories": 45,
  "files": 202,
  ...
}
```

#### Agents.md Update
```markdown
## ✅ Completed Tasks

- [2025-10-28 14:30] TASK-001 - Initial Artifacts Directory Scan
  - Artifacts: 
    - artifacts-catalog.json
    - artifacts-structure-map.md
  - Evidence: 247 items cataloged, 5-level hierarchy mapped
  - Next Actions Triggered: TASK-002 (Meta-Upgrades Analysis)
```

---

## 🎯 Success Indicators

You'll know you're executing correctly when:

1. ✅ agents.md is always current
2. ✅ Every task has documented evidence
3. ✅ No tasks stuck in "In Progress"
4. ✅ Quality gates consistently pass
5. ✅ Work is systematic and traceable
6. ✅ Gaps and uncertainties are explicitly documented

---

## 🚦 Getting Started Command

When you're ready to begin, execute:

```
1. Read: /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/agents.md
2. Initialize: Update "Current Session" section
3. Execute: Start with TASK-001 from "Next Tasks"
4. Document: Update agents.md with completion
5. Continue: Proceed to next priority task
```

---

**Remember:** You are building a systematic, evidence-based analysis of a complex artifact system. Quality and traceability matter more than speed. Document everything, validate rigorously, and maintain the agents.md file as your single source of truth.

**Your success is measured by:** Clear documentation, complete analysis, and a well-maintained task tracking system in agents.md.

---

_Good luck, and execute with precision!_ 🚀

