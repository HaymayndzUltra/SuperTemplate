# PROTOCOL 2: PROTOCOL STRUCTURE GENERATION

## AI ROLE

You are a **Protocol Structure Architect**. Your mission is to generate a complete protocol structure template based on the validator requirements specification. You create the skeleton framework that Protocol 3 will populate with content.

**🚫 CRITICAL: DO NOT WRITE CONTENT YET.** Your role is structure generation only. Protocol 3 handles content creation.

---

## PREREQUISITES

### Required Artifacts
- Requirements spec: `.artifacts/protocol-creation/protocol-requirements-spec.md` (from Protocol 1)
- Example protocols: `.cursor/ai-driven-workflow/*.md` (for structure reference)
- `AGENTS.md` (for phase assignments)

### Required Approvals
- None (structure generation phase)

### System State
- Requirements spec validated and complete
- Access to example protocols for structure patterns

---

## AI ROLE AND MISSION

**Mission**: Generate a complete protocol structure template that:
1. Includes all 9 required sections
2. Follows validator requirements for section structure
3. Includes placeholders for all required content elements
4. Maintains consistency with existing protocol patterns
5. Enables Protocol 3 to populate content efficiently

**Success Criteria**: Complete protocol structure template that passes structural validation and is ready for content population.

---

## WORKFLOW

### STEP 1: Load Requirements Specification

1. **Read Requirements Spec**
   ```bash
   cat .artifacts/protocol-creation/protocol-requirements-spec.md
   ```

2. **Extract Section Requirements**
   - For each of the 9 required sections, extract:
     - Required subsections
     - Required content patterns
     - Required keywords/phrases
     - Minimum counts/occurrences
     - Format requirements

### STEP 2: Analyze Example Protocols

1. **Select Reference Protocols**
   - Choose 2-3 well-structured existing protocols
   - Prefer protocols with high validation scores

2. **Extract Structure Patterns**
   - Section ordering
   - Heading levels (##, ###, ####)
   - List formats
   - Table structures
   - Code block usage
   - Action marker patterns ([STRICT], [GUIDELINE], [CRITICAL])

### STEP 3: Generate Section Templates

For each of the 9 required sections, create a template:

#### 3.1 PREREQUISITES Template
```markdown
## PREREQUISITES

<!-- VALIDATOR MAPPING:
  Primary: Identity Validator (validate_protocol_identity.py)
  Dimensions: prerequisites (part of identity validation)
  Pass Threshold: 0.95
-->

### Required Artifacts
- [ARTIFACT_1:string]: [DESCRIPTION:string] (from Protocol [PROTOCOL_NUM:number])
- [ARTIFACT_2:string]: [DESCRIPTION:string] (optional)

### Required Approvals
- [APPROVAL_1:string]: [STAKEHOLDER:string]
- [APPROVAL_2:string]: [STAKEHOLDER:string]

### System State
- [STATE_REQ_1:string]
- [STATE_REQ_2:string]
```

#### 3.2 AI ROLE AND MISSION Template
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

#### 3.3 WORKFLOW Template
```markdown
## WORKFLOW

<!-- VALIDATOR MAPPING:
  Primary: Workflow Validator (validate_protocol_workflow.py)
  Dimensions: workflow_structure (lines 89-116), step_definitions (lines 118-148), action_markers (lines 150-196), halt_conditions (lines 198-226), evidence_tracking (lines 228-250)
  Pass Threshold: 0.90
  Required: ≥2 sequential steps (line 100)
-->

### STEP 1: [STEP_1_NAME:string]
<!-- REQUIRED: Sequential numbering starting at 1 (line 96) -->
1. **[STRICT]** [ACTION_1:string with "must/require/ensure" keyword (line 158)]
2. **[GUIDELINE]** [ACTION_2:string with decision point]
3. **[CRITICAL]** [ACTION_3:string with problem-solving logic]

### STEP 2: [STEP_2_NAME:string]
<!-- REQUIRED: Sequential step numbering (line 100: ≥2 steps) -->
[Repeat pattern...]

### Halt Conditions
<!-- REQUIRED: ≥2 halt mentions (line 209) -->
- **If [CONDITION_1:string]**: [HALT_ACTION_1:string with error messaging]
- **If [CONDITION_2:string]**: [HALT_ACTION_2:string with rollback (line 206)]

### Evidence Tracking
<!-- REQUIRED: Evidence mentions in workflow (line 235) -->
- [EVIDENCE_POINT_1:string]: Track [METRIC_1:string]
- [EVIDENCE_POINT_2:string]: Track [METRIC_2:string]
```

#### 3.4 INTEGRATION POINTS Template
```markdown
## INTEGRATION POINTS

<!-- VALIDATOR MAPPING:
  Primary: Identity Validator (validate_protocol_identity.py)
  Dimensions: integration_points (part of identity validation)
  Pass Threshold: 0.95
-->

### Inputs From
- **Protocol [PROTOCOL_XX:number]**: [ARTIFACT_1:string] ([FORMAT_1:enum(.md|.json|.yaml)]) from `.artifacts/protocol-[PROTOCOL_XX:number]/`
- **Protocol [PROTOCOL_YY:number]**: [ARTIFACT_2:string] ([FORMAT_2:enum(.md|.json|.yaml)]) from `.artifacts/protocol-[PROTOCOL_YY:number]/`

### Outputs To
- **Protocol [PROTOCOL_ZZ:number]**: [ARTIFACT_3:string] ([FORMAT_3:enum(.md|.json|.yaml)]) to `.artifacts/protocol-[PROTOCOL_ZZ:number]/`
- **Protocol [PROTOCOL_AA:number]**: [ARTIFACT_4:string] ([FORMAT_4:enum(.md|.json|.yaml)]) to `.artifacts/protocol-[PROTOCOL_AA:number]/`

### Data Formats
- Markdown (.md) for [PURPOSE_1:string]
- JSON (.json) for [PURPOSE_2:string]
- YAML (.yaml) for [PURPOSE_3:string]

### Storage Locations
- `.artifacts/protocol-[PROTOCOL_XX:number]/` for [ARTIFACT_TYPE_1:string]
- `.artifacts/protocol-[PROTOCOL_XX:number]/subdir/` for [ARTIFACT_TYPE_2:string]
```

#### 3.5 QUALITY GATES Template
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

#### 3.6 COMMUNICATION PROTOCOLS Template
```markdown
## COMMUNICATION PROTOCOLS

<!-- VALIDATOR MAPPING:
  Primary: Communication Validator (validate_protocol_communication.py)
  Dimensions: status_announcements (lines 89-117), user_interaction (lines 119-145), error_messaging (lines 147-173), progress_tracking (lines 175-200), evidence_communication (lines 202-230)
  Pass Threshold: 0.90
-->

### Status Announcements
<!-- REQUIRED: ≥3 phase mentions (line 102), ≥1 MASTER RAY mention (line 103) -->
- `[PHASE [PHASE_NUM:number] START]` [ANNOUNCEMENT:string with MASTER RAY branding (line 97)]
- `[PHASE [PHASE_NUM:number] COMPLETE]` [COMPLETION:string with ETA/duration (line 99)]
- `[READY]` [READY_STATE:string announcement]

### User Interaction
<!-- REQUIRED: Confirmation, clarification, decision points, feedback (lines 131-134) -->
- **Confirmation**: "[QUESTION:string] Reply 'Go' to continue." (line 125)
- **Clarification**: "Should I interpret {X} as {Y}?" (line 126)
- **Decision Points**: "Choose option A or B:" (line 127)
- **Feedback Requests**: "Does this approach meet your requirements?" (line 128)

### Error Messaging
<!-- REQUIRED: Template, severity, context, resolution (lines 160-163) -->
- `[ERROR]` [ERROR_TEMPLATE:string with severity: CRITICAL/HIGH/WARNING (line 155)]
- **Context**: [DETAILS:string]
- **Resolution**: [REQUIRED_ACTION:string steps (line 157)]

### Progress Tracking
<!-- REQUIRED: ≥3 progress terms, timeline mentions (lines 187-188) -->
- `[PROGRESS]` [CURRENT_ACTIVITY:string] - [PERCENTAGE:percentage]% complete
- `[NEXT]` [NEXT_STEPS:string with timeline]

### Evidence Communication
- `[ARTIFACT]` [ARTIFACT_NAME:string] saved to `.artifacts/protocol-[PROTOCOL_NUM:number]/`
- **Format**: [FORMAT:enum(markdown|json|yaml)]
- **Validation**: [STATUS:enum(pass|fail)]
```

#### 3.7 AUTOMATION HOOKS Template
```markdown
## AUTOMATION HOOKS

<!-- VALIDATOR MAPPING:
  Primary: Scripts Validator (validate_protocol_scripts.py)
  Dimensions: script_inventory (lines 96-125), registry_alignment (lines 127-187), execution_context (lines 189-230), command_syntax (lines 232-270), error_handling (lines 272-310)
  Pass Threshold: 0.90
  Required: ≥3 automation commands (line 117)
-->

### Scripts
<!-- REQUIRED: ≥3 commands (line 117) -->
```bash
# [SCRIPT_PURPOSE_1:string]
python3 scripts/[SCRIPT_NAME_1:string].py [ARGS_1:string]

# [SCRIPT_PURPOSE_2:string]
bash scripts/[SCRIPT_NAME_2:string].sh [ARGS_2:string]
```

### Registry Alignment
<!-- REQUIRED: Registry reference (line 139), registry file mention (line 140) -->
- **Script Registry**: `scripts/script-registry.json` (line 141)
- **Registered Scripts**: [REGISTERED_SCRIPTS:list min=1] (line 147)

### Execution Context
- **CI/CD**: [WORKFLOW_NAME:string, runner, trigger]
- **Environment**: [ENV_TYPE:enum(Docker|venv|dependencies)]
- **Scheduling**: [SCHEDULE_TYPE:enum(Cron|event trigger)]
- **Permissions**: [PERMISSIONS:string - access requirements, tokens, secrets]

### Command Syntax
- **Flags**: `--flag value`
- **Output Redirection**: `> output.json`
- **Parameterization**: `{variable}` or `$(command)`

### Error Handling
<!-- REQUIRED: Exit codes, fallback, logging (lines 272-310) -->
- **Exit Codes**: [EXIT_CODES:string - 0 = success, 1 = failure]
- **Fallback**: [FALLBACK:string - retry sequence]
- **Logging**: [LOG_PATH:path_artifact - log file location]
- **Manual Paths**: [MANUAL_STEPS:string - manual intervention steps]
```

#### 3.8 HANDOFF CHECKLIST Template
```markdown
## HANDOFF CHECKLIST

<!-- VALIDATOR MAPPING:
  Primary: Handoff Validator (validate_protocol_handoff.py)
  Dimensions: checklist_completeness (lines 89-113), verification_procedures (lines 115-141), stakeholder_signoff (lines 143-169), documentation_requirements (lines 171-200), next_protocol_alignment (lines 202-230)
  Pass Threshold: 0.90
  Required: ≥6 checklist items (line 100), ≥3 categories (line 101)
-->

### Prerequisites
<!-- REQUIRED: ≥6 total items across all categories (line 100) -->
- [ ] [PREREQ_ITEM_1:string]
- [ ] [PREREQ_ITEM_2:string]

### Workflow
<!-- REQUIRED: ≥3 categories (line 101: Prerequisite|Workflow|Quality|Evidence|Integration|Automation) -->
- [ ] [WORKFLOW_ITEM_1:string]
- [ ] [WORKFLOW_ITEM_2:string]

### Quality
- [ ] [QUALITY_ITEM_1:string]
- [ ] [QUALITY_ITEM_2:string]

### Evidence
- [ ] [EVIDENCE_ITEM_1:string]
- [ ] [EVIDENCE_ITEM_2:string]

### Integration
- [ ] [INTEGRATION_ITEM_1:string]
- [ ] [INTEGRATION_ITEM_2:string]

### Automation
- [ ] [AUTOMATION_ITEM_1:string]
- [ ] [AUTOMATION_ITEM_2:string]

### Verification Procedures
<!-- REQUIRED: ≥4 verification terms (line 128: validate/ensure/confirm/verify/gate) -->
- [ ] Validate [ITEM_1:string] using [METHOD_1:string]
- [ ] Confirm [ITEM_2:string] with [STAKEHOLDER_1:string]
- [ ] QA review: [CHECKLIST_1:string]

### Stakeholder Sign-off
<!-- REQUIRED: Approval, reviewers, evidence reference, confirmation (lines 155-158) -->
- [ ] **Reviewer**: [REVIEWER_NAME:string/Role] - [APPROVAL_STATUS:enum(approved|pending|rejected)]
- [ ] **Evidence Package**: [EVIDENCE_LOCATION:path_artifact] - [STATUS:enum(complete|pending)]
- [ ] **Confirmation**: [ACKNOWLEDGMENT:string received]

### Documentation Requirements
<!-- REQUIRED: ≥3 doc terms (line 184: log/brief/notes/transcript/manifest/report) -->
- [ ] [DOC_TYPE:string] saved to [LOCATION:path_artifact]
- [ ] Format: [FORMAT:enum(.md|.json|.yaml)]
- [ ] Reviewer docs: [REVIEWER_DOCS:path_artifact]

### Next Protocol Alignment
- [ ] **Ready for Protocol [NEXT_PROTOCOL:number]**: [STATEMENT:string]
- [ ] **Next Command**: `@apply protocol-[NEXT_PROTOCOL:number]` or `run protocol-[NEXT_PROTOCOL:number]`
- [ ] **Dependencies**: [DEPENDENCIES:list min=1]
- [ ] **Continuation Script**: [SCRIPT_NAME:string if applicable]
```

#### 3.9 EVIDENCE SUMMARY Template
```markdown
## EVIDENCE SUMMARY

<!-- VALIDATOR MAPPING:
  Primary: Evidence Validator (validate_protocol_evidence.py)
  Dimensions: artifact_generation (lines 89-124), storage_structure (lines 126-154), manifest_completeness (lines 156-200), traceability (lines 202-240), archival (lines 242-280)
  Pass Threshold: 0.90
  Required: Table with artifact column, ≥2 rows or ≥3 artifact mentions (line 105)
-->

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
<!-- REQUIRED: Table present (line 102), artifact column (line 103), metrics column (line 104) -->
| [ARTIFACT_1:string] | `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]` | [TYPE_1:string] | [METRIC_1:string: value] |
| [ARTIFACT_2:string] | `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]` | [TYPE_2:string] | [METRIC_2:string: value] |

### Storage Structure
<!-- REQUIRED: Protocol directory (line 139), subdirectories (line 140), permissions (line 141), naming (line 142) -->
- **Protocol Directory**: `.artifacts/protocol-[PROTOCOL_NUM:number]/` (line 133)
- **Subdirectories**: [SUBDIRS:list min=1]
- **Permissions**: [PERMISSIONS:enum(Read|write|access)]
- **Naming Convention**: [PATTERN:string]

### Manifest
<!-- REQUIRED: Manifest reference OR metadata/dependencies/coverage (lines 162-184) -->
- **Manifest File**: [MANIFEST_LOCATION:path_artifact] (optional)
- **Metadata**: [METADATA:string - timestamp, size, hash (line 163)]
- **Dependencies**: [DEPENDENCIES:string - input/output links (line 164)]
- **Coverage**: [COVERAGE:enum(100%|complete)] (line 165)

### Traceability
<!-- REQUIRED: Inputs, outputs, transformations, audit trail (lines 202-240) -->
- **Inputs From**: [Protocol [INPUT_PROTOCOL:number] → [INPUT_ARTIFACT:string]]
- **Outputs To**: [Protocol [OUTPUT_PROTOCOL:number] → [OUTPUT_ARTIFACT:string]]
- **Transformations**: [TRANSFORM_DESC:string - process description]
- **Audit Trail**: [AUDIT_LOG:path_artifact]

### Archival (Optional)
- **Compression**: [COMPRESSION_FORMAT:enum(zip|tar.gz)]
- **Retention**: [RETENTION_DURATION:string - 30 days/90 days]
- **Retrieval**: [RETRIEVAL_METHOD:string - access method]
- **Cleanup**: [CLEANUP_POLICY:string - deletion policy]
```

### STEP 4: Assemble Complete Structure

1. **Create Protocol Header**
   ```markdown
   # PROTOCOL XX: [PROTOCOL NAME]
   
   **Version**: v1.0.0 | **Phase**: [Phase X] | **Status**: Draft
   ```

2. **Combine All Section Templates**
   - In the order: PREREQUISITES → AI ROLE → WORKFLOW → INTEGRATION → GATES → COMMUNICATION → AUTOMATION → HANDOFF → EVIDENCE

3. **Add Metadata Placeholders**
   - Protocol number placeholder
   - Protocol name placeholder
   - Version placeholder
   - Phase placeholder

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

### STEP 6: Validate Structure

1. **Check Section Count**: 9/9 sections present
2. **Check Section Order**: Matches validator expectations
3. **Check Placeholders**: All required elements have placeholders
4. **Check Formatting**: Markdown syntax valid

### STEP 7: Generate Structure Artifact

Save the structure template to:
```
.artifacts/protocol-creation/protocol-structure-template.md
```

---

## INTEGRATION POINTS

### Inputs From
- Requirements spec: `.artifacts/protocol-creation/protocol-requirements-spec.md` (Protocol 1)
- Example protocols: `.cursor/ai-driven-workflow/*.md`
- Phase assignments: `AGENTS.md`

### Outputs To
- Structure template: `.artifacts/protocol-creation/protocol-structure-template.md`
- Next protocol: `3-create-protocol-content.md`

### Data Formats
- Markdown (.md) for structure template

### Storage Locations
- `.artifacts/protocol-creation/` for structure template

---

## QUALITY GATES

### Gate 1: Section Completeness
- **Criteria**: All 9 required sections present
- **Pass Threshold**: 9/9 sections = 100%
- **Evidence**: Section count in structure template

### Gate 2: Requirements Alignment
- **Criteria**: All requirements from spec represented in structure
- **Pass Threshold**: ≥95% requirements covered
- **Evidence**: Requirements coverage matrix

### Gate 3: Structure Validation
- **Criteria**: Markdown syntax valid, placeholders complete
- **Pass Threshold**: 100% valid syntax, 100% placeholders
- **Evidence**: Structure validation report

---

## COMMUNICATION PROTOCOLS

### Status Announcements
- `[STRUCTURE GENERATION START]` Creating protocol structure template...
- `[SECTION COMPLETE] Section {name} complete}`
- `[STRUCTURE VALIDATED]` Template ready for content population

### User Interaction
- **Confirmation**: "Structure template generated. Ready to populate content? Reply 'Go' to continue."

---

## AUTOMATION HOOKS

### Scripts
```bash
# Validate structure template
python3 scripts/validate_structure_template.py --template .artifacts/protocol-creation/protocol-structure-template.md
```

---

## HANDOFF CHECKLIST

### Prerequisites
- [ ] Requirements spec loaded and analyzed
- [ ] Example protocols analyzed for patterns
- [ ] All 9 section templates generated

### Workflow
- [ ] Complete structure template assembled
- [ ] All placeholders included
- [ ] Structure validated

### Quality
- [ ] Section completeness: 9/9
- [ ] Requirements alignment: ≥95%
- [ ] Structure syntax: 100% valid

### Evidence
- [ ] Structure template saved
- [ ] Validation report generated

### Integration
- [ ] Structure template ready for Protocol 3
- [ ] Next protocol file referenced

---

## EVIDENCE SUMMARY

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
| Structure Template | `.artifacts/protocol-creation/protocol-structure-template.md` | Template | Sections: 9/9 |
| Structure Validation Report | `.artifacts/protocol-creation/structure-validation.json` | Report | Validity: 100% |

---

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

---

## READY FOR PROTOCOL 3

**Next Step**: `3-create-protocol-content.md`

The protocol structure template is complete and ready for content population.

