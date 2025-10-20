# Protocol Format Templates - Category-Based Selection

**Last Updated:** 2025-01-21  
**Purpose:** Guide for selecting format templates per protocol section based on category/type

---

## 📁 AVAILABLE CATEGORY FILES

1. **EXECUTION-FORMATS.md** - Workflow execution formats (3 variants)
2. **GUIDELINES-FORMATS.md** - Rules and behavioral standards  
3. **ISSUE-FORMATS.md** - Issue tracking and task breakdown
4. **PROMPT-FORMATS.md** - Multi-agent prompt engineering
5. **META-FORMATS.md** - Protocol analysis and generator creation

---

## 🎯 Core Principle: CATEGORY-BASED SELECTION PER SECTION

**❌ WRONG APPROACH:**
- "This whole protocol uses one format"
- Picking format before analyzing sections
- Rigid format selection

**✅ CORRECT APPROACH:**
- Analyze EACH SECTION of the protocol
- Determine section TYPE (execution? guidelines? reasoning?)
- Open appropriate CATEGORY file
- Choose specific format variant from that category
- Mix categories intelligently within same protocol

---

## 📋 CATEGORY 1: EXECUTION FORMATS

**File:** `EXECUTION-FORMATS.md`  
**Contains:** 3 execution format variants

**Open this file when section needs:**
- Workflow execution steps
- Task breakdown and tracking
- Phase-based progression
- Action items with evidence collection

**Variants inside:**
1. **BASIC** - Simple PHASE 1-4 workflow
2. **SUBSTEPS** - Detailed numbered substeps (1.1, 1.2)
3. **REASONING** - Includes [REASONING] blocks for decisions

---

## 📜 CATEGORY 2: GUIDELINES FORMATS

**File:** `GUIDELINES-FORMATS.md`  
**Contains:** Rules and behavioral standards format

**Open this file when section needs:**
- Strict enforcement rules
- AI behavioral constraints
- Coding standards
- Step-based procedures with [STRICT]/[GUIDELINE] markers
- DO/DON'T examples

---

## 🎫 CATEGORY 3: ISSUE FORMATS

**File:** `ISSUE-FORMATS.md`  
**Contains:** Issue tracking format

**Open this file when section needs:**
- GitHub/Jira issue creation
- Task breakdown into 9 standard subtasks
- Priority-based task organization
- Project management integration

---

## 🤖 CATEGORY 4: PROMPT FORMATS

**File:** `PROMPT-FORMATS.md`  
**Contains:** Multi-agent prompt engineering format

**Open this file when section needs:**
- Multi-agent AI orchestration
- Role-based system design (System/Developer/User)
- Flexible output format requirements
- Interactive halt-and-await patterns

---

## 🔧 CATEGORY 5: META FORMATS

**File:** `META-FORMATS.md`  
**Contains:** Protocol analysis and generator creation

**Open this file when section needs:**
- Protocol analysis automation
- Generator creation for new protocol types
- Format classification systems
- Circular validation integration

---

## 🧠 Category Selection Decision Tree

### For Each Protocol Section, Ask:

**Question 1: What is this section doing?**

- **Executing a workflow** → Open **EXECUTION-FORMATS.md**
  - Then ask: Simple workflow? → Use **BASIC** variant
  - Need detailed tracking? → Use **SUBSTEPS** variant  
  - Need decision documentation? → Use **REASONING** variant

- **Setting rules/standards** → Open **GUIDELINES-FORMATS.md**
  - Use the Rules & Guidelines format

- **Creating issues** → Open **ISSUE-FORMATS.md**
  - Use the GitHub/Jira Issue format

- **Multi-agent system** → Open **PROMPT-FORMATS.md**
  - Use the Multi-Role Prompt Pack format

- **Analyzing/creating protocols** → Open **META-FORMATS.md**
  - Use the Instruction Creator Meta-System format

---

## 📝 Example: Category-Based Protocol

### Protocol 08: Generate Tasks

```markdown
# PROTOCOL 08: GENERATE TASKS

## AI ROLE AND MISSION
[Category: EXECUTION - BASIC variant]
- Simple role definition
- Clear mission statement
- Basic constraints

## WORKFLOW

### PHASE 1: Context Preparation
[Category: EXECUTION - BASIC variant]
1. **`[MUST]` Index Governance Rules:**
   * **Action:** Simple file indexing
   * **Evidence:** `.artifacts/rule-index.json`

2. **`[MUST]` Load PRD:**
   * **Action:** Read and parse PRD
   * **Evidence:** PRD content loaded

### PHASE 2: High-Level Task Structuring
[Category: EXECUTION - REASONING variant]
Why: Involves critical decisions about task breakdown
1. **`[MUST]` Create Task File:**
   * **Action:** Initialize task file
   [STRICT] Provide a "DO" Example:
   [GUIDELINES]:
   [REASONING]
   - Premises: PRD defines 3 major features
   - Constraints: Must fit in 2-week sprint
   - Alternatives Considered:
     A) One large task file (rejected - hard to track)
     B) Separate file per feature (selected - better organization)
   - Decision: Create `tasks-feature-name.md` per feature
   - Evidence: Similar pattern in Protocol 06 output
   - Risks & Mitigations:
     - Risk: File proliferation → Mitigation: Max 5 files per protocol
   - Acceptance Link: PRD Section 3.2 - "Modular task structure"

2. **`[MUST]` Generate High-Level Tasks:**
   [REASONING]
   - Premises: Frontend + Backend changes identified
   - Constraints: Team has 3 frontend devs, 2 backend devs
   - Alternatives Considered:
     A) Feature-based tasks (selected - aligns with team structure)
     B) Layer-based tasks (rejected - creates bottlenecks)
   - Decision: Create 5 parallel tasks (3 FE, 2 BE)
   - Evidence: Team velocity data from previous sprint

### PHASE 3: Detailed Decomposition
[Category: EXECUTION - SUBSTEPS variant]
Why: Needs precise tracking of many sequential steps
1. **`[MUST]` Break Down Tasks by Layer:**
   * **3.1. Frontend Task Decomposition:**
       * **3.1.1. File Scaffolding:** Create component directories
       * **3.1.2. Base HTML:** Implement markup structure
       * **3.1.3. Styling:** Apply CSS following design system
       * **3.1.4. JavaScript Logic:** Implement interactions
       * **3.1.5. Testing:** Write unit and integration tests
   * **3.2. Backend Task Decomposition:**
       * **3.2.1. Route Scaffolding:** Create endpoint structure
       * **3.2.2. Handler Logic:** Implement business logic
       * **3.2.3. Database Migrations:** Update schema
       * **3.2.4. Testing:** Write API tests

### PHASE 4: Validation and Packaging
[Category: EXECUTION - BASIC variant]
Why: Straightforward validation steps
1. **`[MUST]` Validate Task Structure:**
   * **Action:** Run validation script
   ```bash
   python scripts/validate_tasks.py --task-file .cursor/tasks/tasks-feature.md
   ```
   * **Evidence:** `.artifacts/task-validation.json`

2. **`[MUST]` Package Deliverables:**
   * **Action:** Bundle task files
   * **Evidence:** Task package manifest
```

**Summary:** Protocol 08 uses 2 categories across 4 phases:
- EXECUTION-BASIC: Phases 1 & 4 (simple workflows)
- EXECUTION-REASONING: Phase 2 (decision-making)
- EXECUTION-SUBSTEPS: Phase 3 (detailed tracking)

---

## 🔍 Category Selection Example

### Scenario: Creating Protocol 14 (Pre-Deployment Staging)

**Section Analysis:**

1. **PREREQUISITES** section:
   - What it does: Simple checklist
   - Category: EXECUTION-FORMATS.md → BASIC variant
   - Why: Just listing required artifacts

2. **PHASE 1: Staging Alignment** step:
   - What it does: Compare configs, detect drift
   - Category: EXECUTION-FORMATS.md → SUBSTEPS variant
   - Why: Need precise tracking of each comparison step

3. **PHASE 2: Deployment Rehearsal** step:
   - What it does: Critical go/no-go decision after rehearsal
   - Category: EXECUTION-FORMATS.md → REASONING variant
   - Why: Decision requires:
     - Premises: Test results, staging logs
     - Alternatives: Proceed vs. fix-and-retry vs. abort
     - Evidence: Test coverage, error rates
     - Risk assessment documentation

4. **PHASE 3: Rollback Verification** step:
   - What it does: Execute rollback, verify recovery
   - Category: EXECUTION-FORMATS.md → SUBSTEPS variant
   - Why: Precise sequence matters for rollback

5. **PHASE 4: Readiness Review** step:
   - What it does: Stakeholder approval decision
   - Category: EXECUTION-FORMATS.md → REASONING variant
   - Why: Document approval criteria and risks

**Result:** Protocol 14 uses 1 category file (EXECUTION-FORMATS.md) but 3 different variants across 5 sections!

---

## ✅ Category Selection Checklist

For each protocol section, ask:

### Step 1: Identify Section Type
- [ ] Is this executing a workflow?
  - YES → Open EXECUTION-FORMATS.md
- [ ] Is this setting rules/standards?
  - YES → Open GUIDELINES-FORMATS.md
- [ ] Is this creating project issues?
  - YES → Open ISSUE-FORMATS.md
- [ ] Is this multi-agent orchestration?
  - YES → Open PROMPT-FORMATS.md
- [ ] Is this protocol analysis/generation?
  - YES → Open META-FORMATS.md

### Step 2: Choose Variant (for EXECUTION category only)
- [ ] Does this involve complex decision-making?
  - YES → Use REASONING variant
- [ ] Do I need to track precise substep order (>5 substeps)?
  - YES → Use SUBSTEPS variant
- [ ] Is this straightforward execution?
  - YES → Use BASIC variant

### Step 3: Document Choice
- [ ] Add comment in protocol: `[Category: {CATEGORY} - {VARIANT}]`
- [ ] Add "Why" explanation if not obvious

---

## 🎨 Best Practices

### DO:
- ✅ Analyze each section independently
- ✅ Identify section type FIRST (execution/guidelines/issue/etc)
- ✅ Open appropriate CATEGORY file
- ✅ Choose specific variant based on section needs
- ✅ Document category choice with comments
- ✅ Mix categories intelligently within same protocol

### DON'T:
- ❌ Pick one category for entire protocol
- ❌ Use REASONING variant everywhere (overkill)
- ❌ Use BASIC variant for complex decisions
- ❌ Skip the "What is this section doing?" question
- ❌ Mix variants randomly without logic

---

## 📚 Common Category Patterns

### Pattern 1: Discovery → Decision → Execution
```
PHASE 1: Discovery     → EXECUTION-FORMATS.md (BASIC)
PHASE 2: Analysis      → EXECUTION-FORMATS.md (REASONING - decisions)
PHASE 3: Execution     → EXECUTION-FORMATS.md (SUBSTEPS - tracking)
PHASE 4: Validation    → EXECUTION-FORMATS.md (BASIC)
```

### Pattern 2: Setup → Detailed Work → Review
```
PHASE 1: Setup         → EXECUTION-FORMATS.md (BASIC)
PHASE 2: Detailed Work → EXECUTION-FORMATS.md (SUBSTEPS)
PHASE 3: Review        → EXECUTION-FORMATS.md (REASONING - approval)
```

### Pattern 3: Rule Definition → Application
```
Section 1: Rules       → GUIDELINES-FORMATS.md
Section 2: Application → EXECUTION-FORMATS.md (BASIC)
Section 3: Validation  → EXECUTION-FORMATS.md (SUBSTEPS)
```

### Pattern 4: Multi-Output Protocol
```
PHASE 1-3: Core Logic  → EXECUTION-FORMATS.md (any variant)
PHASE 4: Issue Creation → ISSUE-FORMATS.md (GitHub/Jira)
```

---

## 🚀 Quick Start Guide

### Step 1: Read Your Protocol
Understand the full workflow and purpose

### Step 2: Break Into Sections
Identify major phases/steps

### Step 3: Categorize Each Section
For each section, ask: **"What is this section DOING?"**
- Executing workflow? → EXECUTION-FORMATS.md
- Setting rules? → GUIDELINES-FORMATS.md
- Creating issues? → ISSUE-FORMATS.md
- Multi-agent? → PROMPT-FORMATS.md
- Meta-analysis? → META-FORMATS.md

### Step 4: Select Variant (if needed)
If you opened EXECUTION-FORMATS.md, choose variant:
- Simple workflow? → BASIC
- Many substeps? → SUBSTEPS
- Complex decisions? → REASONING

### Step 5: Apply Template
Copy the template structure from the chosen category file

### Step 6: Document Your Choice
Add comment in protocol: `[Category: {NAME} - {VARIANT}]`

---

## 📖 Next Steps

1. **Browse Category Files:** Open each of the 5 category files
2. **Understand Variants:** Focus on EXECUTION-FORMATS.md variants
3. **Study Example:** Review Protocol 08 example above
4. **Practice:** Analyze an existing protocol and categorize each section
5. **Apply:** Create new protocols using category-based selection

---

## 📁 File Organization Summary

```
examples/
├── EXECUTION-FORMATS.md     ← 3 variants (BASIC, SUBSTEPS, REASONING)
├── GUIDELINES-FORMATS.md    ← Rules & standards
├── ISSUE-FORMATS.md         ← GitHub/Jira issue format
├── PROMPT-FORMATS.md        ← Multi-agent prompts
├── META-FORMATS.md          ← Protocol generators
├── FORMAT-ANALYSIS.md       ← Technical analysis document
└── README.md                ← This file
```

---

**Remember:** The goal is NOT category purity, but selecting the RIGHT TOOL for each section's specific needs!
