# IMPLEMENTATION PROMPT: PROTOCOL 2 IMPROVEMENTS

Copy this entire prompt to implement Protocol 2 improvements.

---

## TASK

Improve `/home/haymayndz/SuperTemplate/dev-workflow/protocol-creation/2-generate-protocol-structure.md`

**Goal**: Add validator mapping comments to all templates + typed placeholder system

---

## KEY IMPROVEMENTS

### 1. Add Validator Mapping to AI ROLE Template (CRITICAL)

**Location**: Lines 92-104

**Replace**:
```markdown
## AI ROLE AND MISSION

You are a **[Role Title]**. [Role description >60 chars with domain expertise and behavioral traits].

**Mission**: [One-sentence mission statement with scope boundaries, success criteria, and value proposition].
```

**With**:
```markdown
## AI ROLE AND MISSION

<!-- VALIDATOR MAPPING:
  Primary: Role Validator (validate_protocol_role.py)
  Dimensions: role_definition (lines 93-127), mission_statement (lines 129-155)
  Pass Threshold: 0.90
-->

<!-- ROLE DEFINITION (Role Validator dimension 1/5, weight 0.25) -->
You are a **[ROLE_TITLE:string]**. <!-- REQUIRED: "You are a" or "You are an" (line 101) -->

<!-- ROLE DESCRIPTION (Role Validator line 103: >60 chars, >1 line) -->
[ROLE_DESCRIPTION:string min=60 chars, spanning 2+ lines. Must include:
 - Domain expertise keywords: domain/expertise/industry/capability (line 105) OR
 - Behavioral traits: empat/strateg/rigor/evidence/governance (line 108)
]

<!-- MISSION STATEMENT (Role Validator dimension 2/5, weight 0.25) -->
**Mission**: [MISSION_STATEMENT:string including ALL 4 elements:
  1. "mission" keyword (line 136)
  2. Scope boundary: within/only/do not/boundary/scope (line 137)
  3. Success criteria: success/complete/validation/evidence (line 138)
  4. Value proposition: client/value/impact/benefit/outcome (line 139)
]

### Constraints and Guidelines
- **[STRICT]** [CONSTRAINT:string with "must/require/ensure/strict" keyword (line 165)]
- **[GUIDELINE]** [RECOMMENDATION:string]
- **[CRITICAL]** [CRITICAL_REQ:string with "avoid/within/limit/never" boundary (line 170)]
```

---

### 2. Add Validator Mapping to QUALITY GATES Template (CRITICAL)

**Location**: Lines 150-165

**Replace with**:
```markdown
## QUALITY GATES

<!-- VALIDATOR MAPPING:
  Primary: Gates Validator (validate_protocol_gates.py)
  Required Count: ≥2 gates (line 100: len(gate_headers) >= 2)
  Pass Threshold: 0.92
-->

<!-- GATE 1 (REQUIRED) -->
### Gate 1: [GATE_1_NAME:string] ([TYPE_1:enum(Prerequisite|Execution|Completion)])
<!-- TYPE REQUIREMENT: Gates Validator line 112 -->

- **Criteria**: [DESCRIPTION:string with numeric threshold "≥X" or boolean "= pass"]
  <!-- REQUIRED: Line 143 - must include threshold -->
  
- **Pass Threshold**: [THRESHOLD:format("≥X.XX" OR "status = pass")]
  <!-- REQUIRED: Numeric (≥, >=) from line 150 OR Boolean (status, pass, fail) from line 157 -->
  
- **Metrics**: [METRIC:enum(score|confidence|rate|percentage)]
  <!-- REQUIRED: Line 184 - at least one metric type -->
  
- **Evidence Links**: [REFERENCE:string linking to .artifacts/protocol-XX/]
  <!-- REQUIRED: ≥3 "evidence" mentions across all gates (line 167) -->
  
- **Failure Handling**: [STEPS:list]
  <!-- REQUIRED: Lines 201-210 - must include rollback/notification/waiver -->
  - [ROLLBACK:string procedure]
  - [NOTIFICATION:string path]
  - [WAIVER:string policy]

<!-- GATE 2 (REQUIRED) -->
### Gate 2: [GATE_2_NAME:string] ([TYPE_2:enum(Prerequisite|Execution|Completion)])
[Same structure as Gate 1]

<!-- VALIDATION CHECKLIST:
  ✓ Gate count ≥2
  ✓ Each gate has type
  ✓ Each gate has numeric or boolean threshold
  ✓ Metrics specified
  ✓ Evidence links present (≥3 total mentions)
  ✓ Failure handling documented
-->
```

---

### 3. Add Typed Placeholder System Appendix (HIGH)

**Location**: New APPENDIX A at end of file

**Add**:
```markdown
## APPENDIX A: Placeholder Type System

### Type Categories

#### STRING Types
```
[NAME:string]                    # Free-form text
[NAME:string min=N]              # Minimum N characters
[NAME:string max=N]              # Maximum N characters
[NAME:string pattern="regex"]    # Must match regex
```

#### ENUM Types
```
[NAME:enum(option1|option2|option3)]
```

#### NUMBER Types
```
[NAME:number]                    # Any number
[NAME:number min=N]              # Minimum value
[NAME:percentage]                # Number with % (0-100)
[NAME:score]                     # Float 0.0-1.0
```

#### PATH Types
```
[NAME:path_artifact]             # .artifacts/protocol-XX/file
```

#### LIST Types
```
[NAME:list min=N]                # List with minimum N items
```

### Validation Rules

Protocol 3 MUST validate each placeholder replacement against type specification.
```

---

### 4. Add Template Validation Step (HIGH)

**Location**: New STEP 5 between current STEP 4 and 5

**Add**:
```markdown
### STEP 5: Validate Generated Templates

**Validation Checklist**:

1. **Completeness Check**
   ```python
   required_sections = [
       "PREREQUISITES", "AI ROLE AND MISSION", "WORKFLOW",
       "INTEGRATION POINTS", "QUALITY GATES", "COMMUNICATION PROTOCOLS",
       "AUTOMATION HOOKS", "HANDOFF CHECKLIST", "EVIDENCE SUMMARY"
   ]
   
   for section in required_sections:
       if section not in generated_template:
           print(f"[ERROR] Missing section: {section}")
           exit(1)
   ```

2. **Validator Mapping Check**
   ```python
   sections = re.findall(r'^##\s+(.+)$', generated_template, re.MULTILINE)
   
   for section in sections:
       section_content = extract_section_content(section, generated_template)
       if '<!-- VALIDATOR MAPPING:' not in section_content:
           print(f"[WARNING] No validator mapping for section: {section}")
   ```

3. **Count Requirement Check**
   ```python
   if 'QUALITY GATES' in generated_template:
       gate_count = len(re.findall(r'^### Gate \d+:', generated_template, re.MULTILINE))
       if gate_count < 2:
           print(f"[ERROR] Quality Gates must have ≥2 gates, found {gate_count}")
           exit(1)
   ```

**If validation fails**: Fix templates before proceeding to STEP 6
```

---

### 5. Apply Same Pattern to All Section Templates

**Sections to Update**:
- PREREQUISITES (Lines 76-90)
- WORKFLOW (Lines 107-126)
- INTEGRATION POINTS (Lines 128-147)
- COMMUNICATION PROTOCOLS (Lines 168-195)
- AUTOMATION HOOKS (Lines 199-230)
- HANDOFF CHECKLIST (Lines 233-280)
- EVIDENCE SUMMARY (Lines 283-314)

**For Each Section**:
1. Add `<!-- VALIDATOR MAPPING:` comment at top
2. Replace generic `[placeholder]` with `[NAME:type]`
3. Add validator line number references
4. Add required count comments where applicable

---

## VALIDATION

```bash
# Test template generation
python3 -c "
from pathlib import Path
template = Path('dev-workflow/protocol-creation/2-generate-protocol-structure.md').read_text()

# Check validator mappings present
if template.count('<!-- VALIDATOR MAPPING:') < 9:
    print('[ERROR] Not all sections have validator mapping')
    exit(1)

# Check typed placeholders
if '[NAME:type]' not in template:
    print('[WARNING] Example typed placeholder not found')

print('[✓] Protocol 2 improvements validated')
"
```

---

## EXPECTED OUTCOME

**Before**: Generic templates, Protocol 3 guesses content  
**After**: Validator-aware templates, Protocol 3 knows exactly what to write
