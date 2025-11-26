# MASTER RAY™ Rule System

**AI Governance Framework for Consistent, Safe, and High-Quality Interactions**

---

## 🎯 Overview

The MASTER RAY™ Rule System is a comprehensive governance framework that controls AI behavior across all interactions. Rules are defined in `.mdc` (Markdown with Cursor) format and are automatically loaded based on context, scope, and triggers.

### Key Features

- **6 Master Rules**: Core governance that always applies
- **Common Rules**: Shared patterns for UI, security, and quality
- **Project Rules**: Context-specific rules for different project types
- **Automatic Discovery**: Context Discovery Protocol loads relevant rules
- **Directive System**: `[STRICT]` vs `[GUIDELINE]` for enforcement levels

---

## 📂 Directory Structure

```
.cursor/rules/
├── README.md                    # This file
├── AGENTS.md                    # External AI agent guide
│
├── master-rules/                # 🔴 Core governance (always apply)
│   ├── 1-master-rule-context-discovery.mdc
│   ├── 2-master-rule-ai-collaboration-guidelines.mdc
│   ├── 3-master-rule-code-quality-checklist.mdc
│   ├── 4-master-rule-code-modification-safety-protocol.mdc
│   ├── 5-master-rule-documentation-and-context-guidelines.mdc
│   ├── 6-master-rule-how-to-create-effective-rules.mdc
│   ├── advanced-meta-instruction-intelligence-system.mdc
│   ├── edge-case-analyst.mdc
│   └── idea-advocate.mdc
│
├── common-rules/                # 🟡 Shared patterns
│   ├── common-rule-ui-foundation-design-system.mdc
│   ├── common-rule-ui-interaction-a11y-perf.mdc
│   ├── common-rule-ui-premium-brand-dataviz-enterprise-gated.mdc
│   ├── edge-case-analyst.mdc
│   └── idea-advocate.mdc
│
├── project-rules/               # 🟢 Context-specific
│   ├── protocol-ai-workflow-creation.mdc
│   ├── protocol-analysis-brainstorming.mdc
│   ├── protocol-edge-case-logical-validation.mdc
│   └── protocol-prd-question-answering.mdc
│
├── ai-comprehension-system.mdc  # AI understanding validation
├── commit-messages.mdc          # Git commit standards
├── debug-commands.mdc           # Debugging protocols
├── elaboration-specialist.mdc   # Instruction clarification
├── modern-react-nextjs.mdc      # React/Next.js patterns
├── prompt-generator.mdc         # Silent prompt enhancement
├── reveal-model.mdc             # AI model identification
└── semgrep-security-scan.mdc    # Security scanning rules
```

---

## 📜 Master Rules

### Rule 1: Context Discovery Protocol (System BIOS)

**File**: `1-master-rule-context-discovery.mdc`

**Purpose**: The "BIOS" of the system - runs first, discovers all relevant rules, and announces what's loaded.

**Key Features**:
- Exhaustive rule inventory (scan all `.mdc` files)
- Relevance evaluation using TAGS, TRIGGERS, SCOPE
- Dynamic re-evaluation on context shifts
- Rule announcement format

**When Activated**: ALWAYS - First action in any interaction

```
[STRICT] Your very first visible action to the user MUST be 
the rule announcement.
```

---

### Rule 2: AI Collaboration Guidelines

**File**: `2-master-rule-ai-collaboration-guidelines.mdc`

**Purpose**: Supreme operational protocol governing AI-user collaboration.

**Key Protocols**:

1. **Think-First Protocol**: Articulate plan before action
2. **Task Planning**: Break down into structured to-do lists
3. **Tool Usage**: Environment-agnostic, discover-then-execute
4. **Conflict Resolution**: Halt on conflicts, clarify ambiguity
5. **Context Preservation**: Compact and reload during long sessions
6. **Complex Feature Safety**: Extra care for sophisticated code

**Communication Formats**:
```
[RAY MINDZ | PROPOSED PLAN]
[RAY MINDZ | TASK COMPLETED] {task_name}
[RAY MINDZ | RULE CONFLICT]
[RAY MINDZ | CLARIFICATION QUESTION]
```

---

### Rule 3: Code Quality Checklist

**File**: `3-master-rule-code-quality-checklist.mdc`

**Purpose**: Strict checklist for code quality focusing on robustness, reliability, security, and clarity.

**Key Areas**:
- Error handling and edge cases
- Security best practices
- Code readability and maintainability
- Performance considerations
- Testing requirements

---

### Rule 4: Code Modification Safety Protocol

**File**: `4-master-rule-code-modification-safety-protocol.mdc`

**Purpose**: Comprehensive protocol for safe code modification to prevent regressions.

**Phases**:
1. **Pre-Analysis**: Understand existing code before changes
2. **Risk Assessment**: Identify potential impacts
3. **Surgical Implementation**: Minimal, targeted changes
4. **Validation**: Verify no regressions introduced

---

### Rule 5: Documentation & Context Guidelines

**File**: `5-master-rule-documentation-and-context-guidelines.mdc`

**Purpose**: Ensures documentation is updated after significant changes.

**Key Points**:
- Check README.md relevance after modifications
- Update context files when behavior changes
- Maintain documentation accuracy

---

### Rule 6: How to Create Effective Rules

**File**: `6-master-rule-how-to-create-effective-rules.mdc`

**Purpose**: Meta-rule for creating new rules that are effective and maintainable.

**4 Core Pillars**:
1. **Discovery**: Rules must be findable via TAGS, TRIGGERS, SCOPE
2. **Clarity**: Clear, unambiguous instructions
3. **Enforcement**: [STRICT] vs [GUIDELINE] distinction
4. **Maintenance**: Version tracking and updates

---

## 📝 Rule Format (MDC)

### YAML Frontmatter

Every rule has a standardized frontmatter:

```yaml
---
description: "TAGS: [tag1,tag2] | TRIGGERS: keyword1,keyword2 | SCOPE: scope | DESCRIPTION: One-sentence summary"
alwaysApply: true/false
globs: "file-patterns" # Optional
---
```

### Components

| Field | Purpose | Example |
|-------|---------|---------|
| **TAGS** | Categories for classification | `[ui,frontend,component]` |
| **TRIGGERS** | Keywords that activate rule | `component,ui,react` |
| **SCOPE** | Where rule applies | `global`, `frontend`, `backend` |
| **DESCRIPTION** | Brief summary | `UI foundation design system` |
| **alwaysApply** | Load in every session | `true` for Master Rules |
| **globs** | File patterns | `*.tsx`, `**/components/**` |

---

## 🏷️ Standard Tags by Domain

### Global Tags (Master Rules)
- `global` - Applies everywhere
- `collaboration` - AI-user interaction
- `quality` - Code quality standards
- `documentation` - Docs management
- `workflow` - Process rules

### Backend Tags
- `backend` - General backend
- `api` - REST/GraphQL APIs
- `database` - Database operations
- `auth` - Authentication
- `deployment` - CI/CD

### Frontend Tags
- `frontend` - User interface
- `component` - UI components
- `form` - Forms and validation
- `styling` - CSS and theming
- `api-calls` - Frontend API integration

### Infrastructure Tags
- `storage` - Object storage
- `cache` - Caching strategies
- `cdn` - CDN and performance
- `monitoring` - Observability

---

## ⚡ Directive Prefixes

### [STRICT]

**Non-negotiable, mandatory directive.**

```markdown
[STRICT] You MUST follow this exactly as written, without deviation.
Failure to comply is a critical error.
```

**When to Use**:
- Security requirements
- Data integrity operations
- Compliance mandates
- Critical workflow steps

### [GUIDELINE]

**Strong recommendation, can deviate with justification.**

```markdown
[GUIDELINE] You SHOULD follow this by default. However, you are 
permitted to deviate if the specific context provides a compelling 
reason. Any deviation MUST be explicitly announced and justified.
```

**When to Use**:
- Best practices
- Optimization suggestions
- Style preferences
- Optional enhancements

---

## 🔄 Rule Loading Process

### Context Discovery Protocol

```
1. SCAN: Find all .mdc files in .cursor/rules/ and subdirectories
2. PARSE: Read YAML frontmatter of each file
3. FILTER: Apply priority system to select relevant rules
4. LOAD: Load selected rules into context
5. ANNOUNCE: Inform user which rules are active
6. APPLY: Execute rule instructions when triggered
```

### Priority System

```
Priority 1: alwaysApply: true (Kernel Rules)
    ↓
Priority 2: SCOPE matches current context
    ↓
Priority 3: TRIGGERS match user request keywords
    ↓
Priority 4: TAGS align with task intent
```

### Conflict Resolution

When rules conflict:
1. **Higher Priority Wins**: Kernel rules override others
2. **More Specific Wins**: Specific rules override general
3. **User Override**: User can explicitly override
4. **Context Override**: Context-specific rules override global

---

## 📋 Rule Announcement Format

After loading rules, AI announces what's active:

```
█▓▒▒░░░⚡𝙼𝙰𝚂𝚃𝙴𝚁 𝚁𝙰𝚈 ᶠᴿᴬᴹᴱᵂᴼᴿᴷ⚡░░░▒▒▓█

I have loaded the 𝙼𝙰𝚂𝚃𝙴𝚁 𝚁𝙰𝚈 ➡️ `rule-1`, `rule-2`, and `rule-3` 
rules covering {domain} for your request. I am ready to begin.
```

---

## 🔧 Creating New Rules

### 1. Choose Location

| Type | Directory | When |
|------|-----------|------|
| Core governance | `master-rules/` | Affects all interactions |
| Shared patterns | `common-rules/` | Multiple projects |
| Project-specific | `project-rules/` | Single project type |
| Standalone | Root | General utilities |

### 2. Create MDC File

```yaml
---
description: "TAGS: [my,tags] | TRIGGERS: keyword1,keyword2 | SCOPE: scope | DESCRIPTION: What this rule does"
alwaysApply: false
---

# Rule Title

## Purpose
What this rule accomplishes.

## When Applied
Conditions that trigger this rule.

## Instructions

### [STRICT] Mandatory Requirements
Things that MUST be done.

### [GUIDELINE] Recommended Practices
Things that SHOULD be done.

## Examples
Concrete examples of rule application.
```

### 3. Test Discovery

Verify the Context Discovery Protocol finds your rule:
1. Start new conversation
2. Check rule announcement
3. Test with trigger keywords

---

## 📚 Related Documentation

- [AGENTS.md](./AGENTS.md) - External AI agent guide
- [Master Rules](./master-rules/) - Core governance rules
- [Common Rules](./common-rules/) - Shared patterns
- [Project Rules](./project-rules/) - Context-specific rules

---

## ✅ Validation Checklist

When creating or modifying rules, ensure:

- [ ] YAML frontmatter is valid
- [ ] TAGS, TRIGGERS, SCOPE are defined
- [ ] DESCRIPTION is a single, clear sentence
- [ ] alwaysApply is set correctly
- [ ] [STRICT] vs [GUIDELINE] is used appropriately
- [ ] Examples are provided
- [ ] Rule is discoverable by Context Discovery Protocol

---

**MASTER RAY™ Rule System** - Governance that enables consistency, safety, and excellence.

