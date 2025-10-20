# COMPLETE FORMAT ANALYSIS

## Source Files Inventory

### FORMATS2.md (46,416 bytes)
**Contains 4 STANDALONE formats:**
1. **Protocol 2: Technical Task Generation** (lines 16-906)
   - Type: EXECUTION (Reasoning-based)
   - Has [REASONING] blocks after every step
   - Includes 3 decomposition templates (Frontend, Backend, Global State)
   - Has 4 output variants (Markdown, JSON, YAML, CLI) - these are NOT separate formats

2. **FORMAT 5: GitHub/Jira Issue** (lines 1019-1047)
   - Type: ISSUE-TRACKING
   - Per-task issue structure
   - 9 standard subtasks (Scaffolding → Docs/Runbooks)

3. **FORMAT 6: Prompt Pack** (lines 1051-1063)
   - Type: PROMPT-ENGINEERING
   - System/Developer/User role separation
   - Multi-format output support

4. **INSTRUCTION CREATOR META-SYSTEM** (lines 1067-1548)
   - Type: META-SYSTEM
   - Protocol analysis algorithm (7 phases)
   - Format classification (A/B/C/D)
   - Protocol generator creation

**Plus 1 COMPONENT (not a full format):**
- REASONING BLOCK (lines 1-12) - Drop-in component for other formats

---

### FORMATS.md (14,351 bytes)
**Contains 2 STANDALONE formats:**
1. **Rules & Guidelines Format** (lines 1-228)
   - Type: GUIDELINES
   - YAML frontmatter
   - Step 1-5 structure with Phase sub-sections
   - [STRICT] and [GUIDELINE] markers
   - DO/DON'T examples

2. **Protocol with Numbered Substeps** (lines 232-453)
   - Type: EXECUTION (Numbered substeps)
   - PHASE 1-4 structure  
   - Numbered substeps (1.1, 1.2, 1.3)
   - 3 decomposition templates (A/B/C)

---

### FORMAT3.md (17,507 bytes)
**Contains 1 STANDALONE format:**
1. **Basic Protocol Template** (lines 1-281)
   - Type: EXECUTION (Basic)
   - PHASE 1-4 structure
   - Uses [PLACEHOLDER: ...] notation
   - 3 decomposition templates (A/B/C)

---

## TOTAL FORMATS: 7 UNIQUE TEMPLATES

---

## DUPLICATE/OVERLAP ANALYSIS

### ⚠️ MAJOR OVERLAP DETECTED:

**FORMAT3.md (Basic Protocol) ≈ FORMATS.md Part 2 (Numbered Substeps)**

**Similarities:**
- Both use PHASE 1-4 structure
- Both have numbered substeps in PHASE 4 (4.1, 4.2, 4.3)
- Both have 3 decomposition templates (Template A/B/C)
- Both have FINAL OUTPUT TEMPLATE section
- Both use [CRITICAL], [MUST], [GUIDELINE], [NEW] markers

**Differences:**
- **Placeholder style**: FORMAT3 uses `[PLACEHOLDER: description]`, FORMATS.md uses `{Curly_Brace}`
- **Verbosity**: FORMAT3 has more instructional text
- **YAML frontmatter**: FORMATS.md has it, FORMAT3 doesn't
- **Detail level**: FORMATS.md is more concise

**Verdict:** These are **essentially the same format** with different placeholder conventions. Should be consolidated.

---

## CATEGORIZATION BY TYPE

### 📋 EXECUTION FORMATS (Workflow execution)
Used when protocol needs step-by-step execution guidance.

1. **EXECUTION-BASIC**: Basic Protocol (FORMAT3.md)
   - Simple PHASE 1-4 workflow
   - Best for: straightforward execution plans

2. **EXECUTION-SUBSTEPS**: Numbered Substeps Protocol (FORMATS.md part 2)
   - Detailed substep tracking (1.1, 1.2, etc.)
   - Best for: complex workflows needing precise tracking

3. **EXECUTION-REASONING**: Reasoning-Based Protocol (FORMATS2.md)
   - [REASONING] blocks for decisions
   - Best for: protocols requiring decision documentation

---

### 📜 GUIDELINES FORMATS (Rules & Standards)
Used when setting behavioral rules or coding standards.

1. **GUIDELINES-RULES**: Rules & Guidelines (FORMATS.md part 1)
   - Step-based with [STRICT]/[GUIDELINE] markers
   - Best for: master rules, coding standards, AI behavior guidelines

---

### 🎫 ISSUE-TRACKING FORMATS
Used when breaking down into trackable issues.

1. **ISSUE-GITHUB**: GitHub/Jira Issue Format (FORMATS2.md)
   - 9-subtask standard breakdown
   - Best for: creating issues in project management tools

---

### 🤖 PROMPT-ENGINEERING FORMATS
Used for multi-agent or role-based systems.

1. **PROMPT-MULTIRALE**: Prompt Pack (FORMATS2.md)
   - System/Developer/User role separation
   - Best for: LLM orchestration, multi-agent systems

---

### 🔧 META-SYSTEM FORMATS
Used for protocol generation/analysis.

1. **META-CREATOR**: Instruction Creator (FORMATS2.md)
   - Protocol analysis & generator creation
   - Best for: building protocol generators

---

## RECOMMENDED REORGANIZATION

### Current State (examples/ folder):
```
EXAMPLE-FORMAT1-RULE.md          ← Guidelines
EXAMPLE-FORMAT2-EXECUTION.md     ← Execution-Basic
EXAMPLE-FORMAT3-TEMPLATE.md      ← Execution-Substeps
EXAMPLE-FORMAT4-REASONING.md     ← Execution-Reasoning
README.md
```

### Proposed New Structure:

**Option A: Category-Based Files**
```
examples/
├── EXECUTION-FORMATS.md         ← All 3 execution formats combined
├── GUIDELINES-FORMATS.md        ← Rules format
├── ISSUE-FORMATS.md             ← Issue tracking format
├── PROMPT-FORMATS.md            ← Prompt engineering format
├── META-FORMATS.md              ← Meta-system format
└── README.md                    ← Updated selection guide
```

**Option B: Keep Separate but Rename**
```
examples/
├── EXECUTION-BASIC.md
├── EXECUTION-SUBSTEPS.md
├── EXECUTION-REASONING.md
├── GUIDELINES-RULES.md
├── ISSUE-GITHUB.md
├── PROMPT-MULTIROLE.md
├── META-CREATOR.md
└── README.md
```

**Option C: Type-Based Folders**
```
examples/
├── execution/
│   ├── basic.md
│   ├── substeps.md
│   └── reasoning.md
├── guidelines/
│   └── rules.md
├── issue-tracking/
│   └── github-jira.md
├── prompt-engineering/
│   └── multirole.md
├── meta-system/
│   └── creator.md
└── README.md
```

---

## USAGE GUIDE: Which Format for Which Protocol Section?

### Decision Matrix:

**When section involves:**
- ❓ **Complex decisions** → Use EXECUTION-REASONING
- 📊 **Many sequential substeps** → Use EXECUTION-SUBSTEPS  
- ⚡ **Simple linear workflow** → Use EXECUTION-BASIC
- 📜 **Setting rules/standards** → Use GUIDELINES-RULES
- 🎫 **Breaking into issues** → Use ISSUE-GITHUB
- 🤖 **Multi-agent orchestration** → Use PROMPT-MULTIROLE
- 🔧 **Creating protocol generators** → Use META-CREATOR

### Example Protocol Using Multiple Types:

```markdown
# PROTOCOL 08: GENERATE TASKS

## AI ROLE
[Use EXECUTION-BASIC format - simple role definition]

## PHASE 1: Context Discovery
[Use EXECUTION-BASIC format - straightforward steps]

## PHASE 2: High-Level Task Generation
[Use EXECUTION-REASONING format - decisions on task breakdown]
  - Includes [REASONING] blocks for:
    - Why chose feature-based vs layer-based tasks
    - Evidence from team velocity data

## PHASE 3: Detailed Decomposition
[Use EXECUTION-SUBSTEPS format - precise tracking needed]
  - 3.1. Frontend Decomposition
  - 3.2. Backend Decomposition  
  - 3.3. Testing Strategy

## PHASE 4: Issue Creation (Optional)
[Use ISSUE-GITHUB format - if creating GitHub issues]

## MASTER RULES (Separate file)
[Use GUIDELINES-RULES format - behavioral constraints]
```

---

## NEXT ACTIONS

1. **Consolidate Duplicates**
   - Merge FORMAT3.md and FORMATS.md Part 2
   - Choose single placeholder convention

2. **Extract Missing Formats**
   - Create ISSUE-GITHUB.md from FORMATS2.md lines 1019-1047
   - Create PROMPT-MULTIROLE.md from FORMATS2.md lines 1051-1063
   - Create META-CREATOR.md from FORMATS2.md lines 1067-1548

3. **Reorganize examples/ folder**
   - Choose Option A, B, or C structure
   - Update all file names to match category

4. **Update README.md**
   - Replace "format selection" with "type selection"
   - Add category-based decision tree
   - Show multi-type protocol examples
