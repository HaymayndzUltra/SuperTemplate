# AI Governance System Analysis Protocol (2025)

## TASK
Scan project directories → Apply 7-layer analysis → Find 2025 MCP tools → Output structured report with evidence.

**Workspace**: [/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/](cci:7://file:///home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING:0:0-0:0)

---

## PART 1: SCAN TARGETS
.cursor/rules/ [all *.md] .cursor/rules/master-rules/ [all *.md]
.cursor/rules/common-rules/ [all .md] .cursor/ai-driven-workflow/ [~28 protocol files] scripts/ [.py only] validators-system/ [all subdirs] template-packs/ [structure] *.md (root) [no subdirs]


**Output**: File inventory with `[Path] | [Type] | [Lines]`

---

## PART 2: 7-LAYER ANALYSIS (Per File)

### Layer 1: Structure
- **File type**: Rule | Protocol | Script | Template | Documentation
- **Metadata**: Extract tags, triggers, scope (quote or state "N/A")
- **Directives**: Count [STRICT], [GUIDELINE], [BLOCKING]
- **Sections**: List with line ranges
- **Complexity (1-10)**: 
  - 1-3: <50 lines, linear
  - 4-6: 50-200 lines, some branching
  - 7-9: 200-500 lines, complex logic
  - 10: >500 lines, circular deps
  - **Must state**: `Score X/10: [lines], [decision points], [dependencies]`

### Layer 2: Logic
- **Reasoning model**: Chain-of-thought | Tree | ReAct | Linear | Hybrid (quote evidence)
- **Decision points**: List all `IF/THEN` with line numbers
- **Dependencies**: Map what requires what
- **Cognitive load (1-10)**: Count parallel concepts (1-3: simple, 4-6: moderate, 7-10: complex)

### Layer 3: Integration  
- **Workflow phase**: Which phase, position in sequence
- **Dependencies**: List cross-file references with quotes (or "None found")
- **Triggers**: What activates this file
- **Quality gates**: List checkpoints (or "None detected")

### Layer 4: Execution
- **Trigger conditions**: Quote exact trigger statements
- **Activation sequence**: Number steps with inputs/outputs
- **Checkpoints**: Validation points with success criteria
- **Automation hooks**: Tool calls, scripts, integrations (or "None")

### Layer 5: Impact
- **Scope**: Files/dirs/workflows affected, breadth (Local/Module/System/Global)
- **Ripple effects**: What else changes if this changes (quote dependencies)
- **Conflicts**: Compare with other files (quote both sides or "None detected")
- **Flags**: Performance/security concerns with line numbers

### Layer 6: Quality
- **Coverage (1-10)**: Input (2) + Process (3) + Output (2) + Errors (2) + Validation (1)
  - **Show breakdown**: `Input: 2/2 (line X), Process: 1/3 (missing Y)...`
- **Gaps**: `Line X: Missing [what] | Context: "[quote]" | Impact: High/Med/Low`
- **Ambiguities**: Flag vague verbs, undefined terms, subjective phrases with line numbers
- **Maintainability (1-10)**: Headers + Comments + Versioning + Formatting + Modularity (2pts each)

### Layer 7: Evolution
- **Design intent**: Quote stated purpose
- **Extensibility**: Extension points vs hard constraints (quote examples)
- **Migration**: Breaking changes count, version compatibility
- **Tech debt (1-10)**: TODOs (×2) + Deprecated (×3) + Hard-coded (×1) + Circular (×4)

---

## PART 3: MCP TOOLS (2025)

### Search Queries
Use `search_web`:
1. "Model Context Protocol servers 2025"
2. "MCP tools GitHub awesome list 2025"  
3. "awesome-mcp-servers GitHub"

**Per tool, extract**:
- URL, category, last update
- Features list (from docs)
- Scores (1-10 each with evidence):
  - **Governance alignment**: Quote tool feature + matching project need with file/line
  - **Automation capability**: Feature list + Manual/Semi/Full/Zero-config
  - **Production readiness**: Stars, docs quality, last commit date
  - **Community support**: Contributors, issue activity

---

## PART 4: OUTPUT FORMAT

```markdown
# Analysis Report
Generated: [timestamp] | Workspace: [path]

## SCAN RESULTS
| Category | Count |
|----------|-------|
| Total | X |
| Rules | X |
| Protocols | X |
| Scripts | X |

---

## FILE ANALYSIS

### [Filepath]
**Quick**: Type | Complexity X/10 | Quality X/10 | Lines X-Y

**L1: Structure**
Type, Metadata, Directives, Sections, Complexity score with evidence

**L2: Logic**  
Model, Decisions, Dependencies, Cognitive load score

**L3: Integration**
Phase, Cross-refs, Triggers, Gates

**L4: Execution**
Triggers, Sequence, Checkpoints, Automation

**L5: Impact**
Scope, Ripple effects, Conflicts, Flags

**L6: Quality**
Coverage breakdown, Gaps list, Ambiguities, Maintainability

**L7: Evolution**
Intent, Extensibility, Migration, Debt score

---

[Repeat per file]

---

## MCP TOOLS

### [Tool Name]
- **URL**: [link]
- **Category**: [one type]
- **Features**: [list]
- **Scores**: Alignment X/10 (evidence), Automation X/10, Production X/10, Community X/10
- **Recommendation**: Use | Consider | Skip

---

## SUMMARY TABLES

### Quality Scores
| File | Complexity | Quality | Gaps | Debt |
|------|-----------|---------|------|------|

### MCP Tools  
| Tool | Category | Alignment | Production | Rec |
|------|----------|-----------|------------|-----|

### Issues
| File | Line | Issue | Evidence |
|------|------|-------|----------|

### Conflicts
| File A | Line | File B | Line | Type | Evidence |
|--------|------|--------|------|------|----------|
EVIDENCE RULES
Every score needs: Calculation shown Every gap needs: Line number + quote
Every conflict needs: Both quotes Every tool needs: URL + alignment evidence (tool feature → project need with file/line)

Prohibited:

No generic statements without data
No scores without calculation
No tools without alignment proof
No claims without quotes