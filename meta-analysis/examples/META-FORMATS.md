# META-SYSTEM FORMATS

Para sa protocol analysis, generator creation, at system-level automation.

---

## FORMAT: INSTRUCTION CREATOR META-SYSTEM

**Source:** FORMATS2.md (lines 1067-1548)  
**Use When:** Creating protocol generators, analyzing protocol structures

### Purpose:
Meta-system that analyzes any target protocol and generates specialized protocol-generator-instructions files aligned to that protocol's structure.

### Core Components:

#### 1. Protocol Analysis Algorithm (7 Phases):
- **Phase 1**: Target Protocol Structure Analysis
- **Phase 2**: Format Classification  
- **Phase 3**: Reusable Component Extraction
- **Phase 4**: Format-Specific Template Generation
- **Phase 5**: Input Form Adaptation
- **Phase 6**: Specialized Generator Instructions Creation
- **Phase 7**: Circular Validation Integration

#### 2. Format Classifications:
**Format A: 01/02 Structure (6-Section)**
```markdown
# PROTOCOL [N]: [NAME] ([DOMAIN] COMPLIANT)
## 1. AI ROLE AND MISSION
## 2. [MAIN WORKFLOW SECTION]
## 3. INTEGRATION POINTS
## 4. QUALITY GATES
## 5. COMMUNICATION PROTOCOLS
## 6. HANDOFF CHECKLIST
```

**Format B: Bootstrap Structure (Step-Based)**
```markdown
# PROTOCOL [N]: [NAME]
## 1. AI ROLE AND MISSION
## 2. [MAIN PROCESS SECTION]
### STEP 1-7: [Various Steps]
## FINALIZATION
```

**Format C: PRD Structure (Phase-Based)**
```markdown
# PROTOCOL [N]: [NAME]
## AI ROLE
## PHASE 1-4: [Various Phases]
## FINAL PRD TEMPLATE
```

**Format D: Custom Structure**
- Unique patterns not matching A, B, or C
- Requires custom template generation

#### 3. 4-Layer Architecture Mapping:
- **Layer 1**: System-Level Decisions
- **Layer 2**: Behavioral Control
- **Layer 3**: Procedural Logic
- **Layer 4**: Communication Grammar

### Input Requirements:
**Mandatory:**
- Target Protocol Path (e.g., `.cursor/ai-driven-workflow/0-bootstrap-your-project.md`)
- Target Protocol Name (e.g., "bootstrap", "prd", "tasks")

**Optional:**
- Custom Output Directory (default: `generators/`)
- Validation Mode (default: true)

### Output Generated:
1. **`protocol-generator-instructions-{target-name}.md`**
   - Complete specialized generator instructions
   - Format-specific template and validation
   - Circular validation compatibility

2. **`protocol-input-form-{target-name}.yaml`**
   - Format-specific input form
   - Captures all target format requirements
   - Aligned with generated instructions

### Usage Example:
```bash
# User request:
apply instruction from instruction-creator to protocol-0-bootstrap

# AI executes:
1. Load and analyze protocol-0-bootstrap.md
2. Classify format (e.g., Format B - Bootstrap Structure)
3. Extract patterns and unique characteristics
4. Generate specialized instructions
5. Create aligned input form
6. Validate circular compatibility
7. Output files to generators/
```

### Quality Gates:
- [ ] Target protocol structure accurately extracted
- [ ] Format classification correct
- [ ] All patterns identified
- [ ] Specialized instructions complete
- [ ] Input form aligned with target
- [ ] Circular validation compatibility maintained
- [ ] Meta-analysis generator compatibility verified

### When to Use:
- Creating protocol generators for new protocol types
- Analyzing and extracting protocol patterns
- Ensuring format flexibility across protocol variations
- Maintaining circular validation compatibility
- Building protocol creation automation
- Standardizing protocol structures

### Edge Cases Handled:
- **Unrecognized Format**: Create custom format classification
- **Missing Sections**: Mark as optional in generated instructions
- **Deep Nesting (>4 levels)**: Flatten while preserving hierarchy

### Anti-Patterns to Avoid:
❌ Assuming all protocols follow same structure
❌ Skipping format classification step
❌ Generating instructions without analyzing target
❌ Ignoring unique characteristics
❌ Breaking circular validation compatibility
❌ Creating generic instructions that don't match target

### Best Practices:
✅ Analyze target protocol structure completely
✅ Classify format accurately
✅ Extract all unique characteristics
✅ Generate format-specific instructions
✅ Maintain circular validation compatibility
✅ Test generated instructions with target format
