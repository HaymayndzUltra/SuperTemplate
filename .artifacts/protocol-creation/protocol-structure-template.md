---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL [PROTOCOL_NUM:number]: [PROTOCOL_NAME:string]

**Version**: v[VERSION:string pattern="\\d+\\.\\d+\\.\\d+"] | **Phase**: [PHASE:string pattern="Phase [0-9-]+"] | **Status**: Draft

---

## PREREQUISITES

<!-- VALIDATOR MAPPING:
  Primary: Identity Validator (validate_protocol_identity.py)
  Dimensions: prerequisites (line 209, weight 0.2)
  Pass Threshold: 0.95
  Required: All 3 subsections must be present
-->

### Required Artifacts
<!-- REQUIRED: Line 229 - Must list specific input artifacts -->
- **[ARTIFACT_1:string]**: [DESCRIPTION:string] (from Protocol [SOURCE_PROTOCOL:number])
- **[ARTIFACT_2:string]**: [DESCRIPTION:string] (from Protocol [SOURCE_PROTOCOL:number])
- **[ARTIFACT_3:string]**: [DESCRIPTION:string] (optional)

### Required Approvals
<!-- REQUIRED: Line 237 - Must specify approval workflow -->
- **[APPROVAL_1:string]**: [STAKEHOLDER:string] - [APPROVAL_TYPE:string]
- **[APPROVAL_2:string]**: [STAKEHOLDER:string] - [APPROVAL_TYPE:string]

### System State
<!-- REQUIRED: Line 245 - Must document environment and dependencies -->
- **[STATE_REQ_1:string]**: [DESCRIPTION:string]
- **[STATE_REQ_2:string]**: [DESCRIPTION:string]
- **[STATE_REQ_3:string]**: [DESCRIPTION:string]

---

## AI ROLE AND MISSION

<!-- VALIDATOR MAPPING:
  Primary: Role Validator (validate_protocol_role.py)
  Dimensions: 
    - role_definition (line 93, weight 0.25)
    - mission_statement (line 129, weight 0.25)
    - constraints_guidelines (line 157, weight 0.2)
    - output_expectations (line 208, weight 0.15)
    - behavioral_guidance (line 239, weight 0.15)
  Pass Threshold: 0.90
-->

<!-- ROLE DEFINITION (dimension 1/5) -->
You are a **[ROLE_TITLE:string]**. <!-- REQUIRED: "You are a" or "You are an" (line 101) -->

<!-- ROLE DESCRIPTION (line 103: min 60 chars, multi-line) -->
[ROLE_DESCRIPTION:string min=60 chars, spanning 2+ lines. Must include:
 - Domain expertise keywords: domain/expertise/industry/capability (line 105) OR
 - Behavioral traits: empat/strateg/rigor/evidence/governance (line 108)
]

<!-- MISSION STATEMENT (dimension 2/5) -->
**Mission**: [MISSION_STATEMENT:string including ALL 4 elements:
  1. "mission" keyword (line 136)
  2. Scope boundary: within/only/do not/boundary/scope (line 138)
  3. Success criteria: success/complete/validation/evidence (line 139)
  4. Value proposition: client/value/impact/benefit/outcome (line 140)
]

### Constraints and Guidelines
<!-- REQUIRED: Guardrails (line 165), boundaries (line 170), workflow alignment (line 173) -->
- **[STRICT]** [CONSTRAINT_1:string with "must/require/ensure/strict" keyword]
- **[GUIDELINE]** [RECOMMENDATION_1:string with "within/limit/scope" boundary]
- **[CRITICAL]** [CRITICAL_REQ_1:string with "avoid/never/do not" keyword]

### Output Expectations
<!-- REQUIRED: Format (line 218), structure (line 220), location (line 221), validation (line 222) -->
- **Format**: [FORMAT:enum(.md|.json|.yaml|markdown)]
- **Structure**: [STRUCTURE:string - section/table/manifest/template]
- **Location**: `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]`
- **Validation**: [VALIDATION:string - validate/quality/threshold/gate criteria]

### Behavioral Guidance
<!-- REQUIRED: Communication style (line 247), decision making (line 249), error handling (line 250), user interaction (line 251) -->
- **Communication Style**: [TONE:string - announce/status/communication approach]
- **Decision Making**: [DECISION_APPROACH:string - decide/choose/go-no-go/option]
- **Error Handling**: [ERROR_RESPONSE:string - error/halt procedures]
- **User Interaction**: [INTERACTION:string - confirm/reply/ask/request prompts]

---

## WORKFLOW

<!-- VALIDATOR MAPPING:
  Primary: Workflow Validator (validate_protocol_workflow.py)
  Dimensions:
    - workflow_structure (line 88, weight 0.2)
    - step_definitions (line 118, weight 0.25)
    - action_markers (line 150, weight 0.15)
    - halt_conditions (line 198, weight 0.2)
    - evidence_tracking (line 228, weight 0.2)
  Pass Threshold: 0.90
  Required: ≥2 sequential steps (line 100)
-->

<!-- REASONING PATTERNS (from Reasoning Validator) -->
<!-- REQUIRED: Pattern terms (line 104), explanations (line 105), improvement (line 106) -->

### STEP 1: [STEP_1_NAME:string]
<!-- REQUIRED: Sequential numbering starting at 1 (line 100) -->

**Action**: [ACTION_DESCRIPTION:string]
<!-- REQUIRED: "**Action:**" marker (line 126) -->

1. **[STRICT]** [ACTION_1:string with "must/require/ensure" keyword (line 158)]
   - [DETAIL_1:string]
   - [DETAIL_2:string]

2. **[GUIDELINE]** [ACTION_2:string with decision point]
   - [DETAIL_1:string]
   - [DETAIL_2:string]

3. **[CRITICAL]** [ACTION_3:string with problem-solving logic]
   - [DETAIL_1:string]
   - [DETAIL_2:string]

**Communication**: [COMMUNICATION_GUIDANCE:string]
<!-- REQUIRED: Communication coverage (line 127) -->

**Evidence**: [EVIDENCE_EXPECTATION:string]
<!-- REQUIRED: Evidence coverage (line 128) -->

**Halt Condition**: If [CONDITION:string], then [HALT_ACTION:string with rollback/retry (line 211)]
<!-- REQUIRED: ≥2 halt mentions total (line 209) -->

### STEP 2: [STEP_2_NAME:string]
<!-- REQUIRED: Sequential step numbering (line 100: ≥2 steps) -->

**Action**: [ACTION_DESCRIPTION:string]

1. **[STRICT]** [ACTION_1:string]
   - [DETAIL_1:string]
   - [DETAIL_2:string]

2. **[GUIDELINE]** [ACTION_2:string]
   - [DETAIL_1:string]
   - [DETAIL_2:string]

**Communication**: [COMMUNICATION_GUIDANCE:string]

**Evidence**: [EVIDENCE_EXPECTATION:string]

**Halt Condition**: If [CONDITION:string], then [HALT_ACTION:string]

### STEP 3: [STEP_3_NAME:string] (Optional)

**Action**: [ACTION_DESCRIPTION:string]

1. [ACTION_1:string]
   - [DETAIL_1:string]

**Communication**: [COMMUNICATION_GUIDANCE:string]

**Evidence**: [EVIDENCE_EXPECTATION:string]

---

## INTEGRATION POINTS

<!-- VALIDATOR MAPPING:
  Primary: Identity Validator (validate_protocol_identity.py)
  Dimensions: integration_points (line 265, weight 0.2)
  Pass Threshold: 0.95
  Required: Input sources (line 285), output destinations (line 293), data formats (line 301), storage locations (line 310)
-->

### Inputs From
<!-- REQUIRED: "Inputs From" pattern (line 285) -->
- **Protocol [INPUT_PROTOCOL_1:number]**: [ARTIFACT_1:string] ([FORMAT_1:enum(.md|.json|.yaml)]) from `.artifacts/protocol-[INPUT_PROTOCOL_1:number]/[PATH:string]`
- **Protocol [INPUT_PROTOCOL_2:number]**: [ARTIFACT_2:string] ([FORMAT_2:enum(.md|.json|.yaml)]) from `.artifacts/protocol-[INPUT_PROTOCOL_2:number]/[PATH:string]`

### Outputs To
<!-- REQUIRED: "Outputs To" pattern (line 293) -->
- **Protocol [OUTPUT_PROTOCOL_1:number]**: [ARTIFACT_3:string] ([FORMAT_3:enum(.md|.json|.yaml)]) to `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]`
- **Protocol [OUTPUT_PROTOCOL_2:number]**: [ARTIFACT_4:string] ([FORMAT_4:enum(.md|.json|.yaml)]) to `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]`

### Data Formats
<!-- REQUIRED: File extensions (line 301) -->
- **Markdown (.md)**: [PURPOSE_1:string]
- **JSON (.json)**: [PURPOSE_2:string]
- **YAML (.yaml)**: [PURPOSE_3:string]

### Storage Locations
<!-- REQUIRED: .artifacts/ references (line 310) -->
- `.artifacts/protocol-[PROTOCOL_NUM:number]/` for [ARTIFACT_TYPE_1:string]
- `.artifacts/protocol-[PROTOCOL_NUM:number]/[SUBDIR:string]/` for [ARTIFACT_TYPE_2:string]

---

## QUALITY GATES

<!-- VALIDATOR MAPPING:
  Primary: Gates Validator (validate_protocol_gates.py)
  Dimensions:
    - gate_definitions (line 89, weight 0.25)
    - pass_criteria (line 119, weight 0.25)
    - automation (line 147, weight 0.2)
    - failure_handling (line 187, weight 0.15)
    - compliance_integration (line 218, weight 0.15)
  Pass Threshold: 0.92
  Required: ≥2 gates (line 100)
-->

### Gate 1: [GATE_1_NAME:string] ([TYPE_1:enum(Prerequisite|Execution|Completion)])
<!-- REQUIRED: Gate type (line 102) -->

- **Criteria**: [DESCRIPTION:string with numeric threshold "≥X" or boolean "= pass"]
  <!-- REQUIRED: Line 130 - must include threshold -->
  
- **Pass Threshold**: [THRESHOLD:format("≥X.XX" OR "status = pass")]
  <!-- REQUIRED: Numeric (≥, >=) from line 130 OR Boolean (status, pass, fail) from line 131 -->
  
- **Metrics**: [METRIC:enum(score|confidence|rate|percentage)]
  <!-- REQUIRED: Line 132 - at least one metric type -->
  
- **Evidence Links**: [REFERENCE:string linking to .artifacts/protocol-[PROTOCOL_NUM:number]/]
  <!-- REQUIRED: ≥3 "evidence" mentions across all gates (line 133) -->
  
- **Automation**: 
  <!-- REQUIRED: Scripts (line 160), CI/CD (line 161) -->
  ```bash
  python3 scripts/[SCRIPT_NAME:string].py --protocol [PROTOCOL_NUM:number]
  ```
  
- **Failure Handling**: 
  <!-- REQUIRED: Lines 199-202 - rollback, notification, waiver -->
  - **Rollback**: [ROLLBACK_PROCEDURE:string]
  - **Notification**: [NOTIFICATION_PATH:string]
  - **Waiver**: [WAIVER_POLICY:string]

### Gate 2: [GATE_2_NAME:string] ([TYPE_2:enum(Prerequisite|Execution|Completion)])

- **Criteria**: [DESCRIPTION:string]
  
- **Pass Threshold**: [THRESHOLD:format("≥X.XX" OR "status = pass")]
  
- **Metrics**: [METRIC:enum(score|confidence|rate|percentage)]
  
- **Evidence Links**: [REFERENCE:string]
  
- **Automation**: 
  ```bash
  python3 scripts/[SCRIPT_NAME:string].py --protocol [PROTOCOL_NUM:number]
  ```
  
- **Failure Handling**: 
  - **Rollback**: [ROLLBACK_PROCEDURE:string]
  - **Notification**: [NOTIFICATION_PATH:string]
  - **Waiver**: [WAIVER_POLICY:string]

### Gate 3: [GATE_3_NAME:string] ([TYPE_3:enum(Prerequisite|Execution|Completion)]) (Optional)

- **Criteria**: [DESCRIPTION:string]
- **Pass Threshold**: [THRESHOLD:string]
- **Metrics**: [METRIC:string]
- **Evidence Links**: [REFERENCE:string]
- **Automation**: [AUTOMATION:string]
- **Failure Handling**: [HANDLING:string]

---

## COMMUNICATION PROTOCOLS

<!-- VALIDATOR MAPPING:
  Primary: Communication Validator (validate_protocol_communication.py)
  Dimensions:
    - status_announcements (line 89, weight 0.25)
    - user_interaction (line 119, weight 0.25)
    - error_messaging (line 147, weight 0.2)
    - progress_tracking (line 175, weight 0.15)
    - evidence_communication (line 202, weight 0.15)
  Pass Threshold: 0.90
-->

### Status Announcements
<!-- REQUIRED: ≥3 phase mentions (line 102), ≥1 MASTER RAY mention (line 103), completion callouts (line 104), time estimates (line 105) -->

**█▓▒▒░░░⚡𝙼𝙰𝚂𝚃𝙴𝚁 𝚁𝙰𝚈 ᶠᴿᴬᴹᴱᵂᴼᴿᴷ⚡░░░▒▒▓█**

- `[PROTOCOL [PROTOCOL_NUM:number] | PHASE [PHASE_NUM:number] START]` - [ANNOUNCEMENT:string with ETA/duration]
- `[MILESTONE ACHIEVED]` - [MILESTONE_DESCRIPTION:string]
- `[QUALITY GATE PASSED: Gate [GATE_NUM:number]]` - [GATE_DETAILS:string]
- `[PROTOCOL [PROTOCOL_NUM:number] | PHASE [PHASE_NUM:number] COMPLETE]` - [COMPLETION:string with READY status]

### User Interaction
<!-- REQUIRED: Confirmation (line 131), clarification (line 132), decision points (line 133), feedback (line 134) -->

- **Confirmation**: "[QUESTION:string] Reply 'Go' to continue."
- **Clarification**: "Should I interpret [X:string] as [Y:string]?"
- **Decision Points**: "Choose option [A:string] or [B:string]:"
- **Feedback Requests**: "Does this [ITEM:string] meet your requirements?"

### Error Messaging
<!-- REQUIRED: Templates (line 160), severity (line 161), context (line 162), resolution (line 163) -->

- `[PROTOCOL [PROTOCOL_NUM:number] | GATE [GATE_NUM:number] FAILED: [REASON:string]]`
- `[ERROR]` **[SEVERITY:enum(CRITICAL|HIGH|WARNING)]**: [ERROR_TEMPLATE:string]
  - **Context**: [DETAILS:string - Details/Criteria/Actual]
  - **Resolution**: [REQUIRED_ACTION:string - steps to resolve/fix/remediate]

### Progress Tracking
<!-- REQUIRED: ≥3 progress terms (line 187), timeline (line 188), current activity (line 189), next steps (line 190) -->

- `[PROGRESS]` Currently [CURRENT_ACTIVITY:string] - [PERCENTAGE:percentage]% complete
- `[TIMELINE]` Next: [NEXT_STEPS:string] - ETA: [TIME_ESTIMATE:string]
- `[REMAINING]` [REMAINING_ITEMS:string] remaining

### Evidence Communication
<!-- REQUIRED: ≥2 artifact announcements (line 215), format (line 216), location (line 217), validation (line 218) -->

- `[ARTIFACT GENERATED]` [ARTIFACT_NAME:string] saved to `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]`
- **Format**: [FORMAT:enum(markdown|json|yaml)]
- **Location**: [STORAGE_PATH:path_artifact]
- **Validation**: [STATUS:enum(pass|fail|warning)]

---

## AUTOMATION HOOKS

<!-- VALIDATOR MAPPING:
  Primary: Scripts Validator (validate_protocol_scripts.py)
  Dimensions:
    - script_inventory (line 96, weight 0.25)
    - registry_alignment (line 127, weight 0.2)
    - execution_context (line 189, weight 0.2)
    - command_syntax (line 220, weight 0.2)
    - error_handling (line 251, weight 0.15)
  Pass Threshold: 0.90
  Required: ≥3 automation commands (line 117)
-->

### Scripts
<!-- REQUIRED: ≥3 commands (line 117), script paths (line 120) -->

```bash
# [SCRIPT_PURPOSE_1:string]
python3 scripts/[SCRIPT_NAME_1:string].py \
  --protocol [PROTOCOL_NUM:number] \
  --input .artifacts/protocol-[INPUT_PROTOCOL:number]/[INPUT_FILE:string] \
  --output .artifacts/protocol-[PROTOCOL_NUM:number]/[OUTPUT_FILE:string]

# [SCRIPT_PURPOSE_2:string]
python3 scripts/[SCRIPT_NAME_2:string].py \
  --protocol [PROTOCOL_NUM:number] \
  --validate

# [SCRIPT_PURPOSE_3:string]
bash scripts/[SCRIPT_NAME_3:string].sh \
  --protocol [PROTOCOL_NUM:number]
```

### Registry Alignment
<!-- REQUIRED: Registry reference (line 139), script-registry.json mention (line 140) -->

- **Script Registry**: `scripts/script-registry.json`
- **Registered Scripts**: 
  - [SCRIPT_NAME_1:string] - [PURPOSE:string] (owner: [OWNER:string])
  - [SCRIPT_NAME_2:string] - [PURPOSE:string] (owner: [OWNER:string])
  - [SCRIPT_NAME_3:string] - [PURPOSE:string] (owner: [OWNER:string])

### Execution Context
<!-- REQUIRED: CI context (line 195), environment (line 196), scheduling (line 197), permissions (line 198) -->

- **CI/CD**: [WORKFLOW_NAME:string] on [RUNNER:string] triggered by [TRIGGER:string]
- **Environment**: [ENV_TYPE:enum(Docker|venv|dependencies)] - [REQUIREMENTS:string]
- **Scheduling**: [SCHEDULE_TYPE:enum(Cron|event trigger|manual)] - [SCHEDULE_DETAILS:string]
- **Permissions**: [PERMISSIONS:string - access requirements, tokens, secrets]

### Command Syntax
<!-- REQUIRED: Flags (line 229), output redirection (line 230), parameterization (line 231), documentation (line 237) -->

- **Flags**: Use `--flag value` format
- **Output Redirection**: Use `> output.json` or `| tee log.txt`
- **Parameterization**: Use `{variable}` or `$(command)` for dynamic values

### Error Handling
<!-- REQUIRED: Exit codes (line 264), fallback (line 265), logging (line 266), manual paths (line 267) -->

- **Exit Codes**: 
  - `0` = Success
  - `1` = Failure
  - `2` = Warning
- **Fallback**: [FALLBACK_PROCEDURE:string - retry sequence]
- **Logging**: Logs saved to `.artifacts/protocol-[PROTOCOL_NUM:number]/logs/[LOG_FILE:string]`
- **Manual Paths**: If automation fails: [MANUAL_STEPS:string]

---

## HANDOFF CHECKLIST

<!-- VALIDATOR MAPPING:
  Primary: Handoff Validator (validate_protocol_handoff.py)
  Dimensions:
    - checklist_completeness (line 89, weight 0.3)
    - verification_procedures (line 115, weight 0.2)
    - stakeholder_signoff (line 143, weight 0.2)
    - documentation_requirements (line 171, weight 0.15)
    - next_protocol_alignment (line 199, weight 0.15)
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
- [ ] [QUALITY_ITEM_1:string - validate/ensure/confirm (line 128)]
- [ ] [QUALITY_ITEM_2:string]

### Evidence
- [ ] [EVIDENCE_ITEM_1:string - evidence reference (line 131)]
- [ ] [EVIDENCE_ITEM_2:string]

### Integration
- [ ] [INTEGRATION_ITEM_1:string]
- [ ] [INTEGRATION_ITEM_2:string]

### Automation
- [ ] [AUTOMATION_ITEM_1:string - automation/script/command (line 130)]
- [ ] [AUTOMATION_ITEM_2:string]

### Verification Procedures
<!-- REQUIRED: ≥4 verification terms (line 128: validate/ensure/confirm/verify/gate) -->
- [ ] Validate [ITEM_1:string] using [METHOD_1:string]
- [ ] Confirm [ITEM_2:string] with [STAKEHOLDER_1:string]
- [ ] Verify [ITEM_3:string] against [CRITERIA_1:string]
- [ ] QA review: [CHECKLIST_1:string]

### Stakeholder Sign-off
<!-- REQUIRED: Approval (line 155), reviewers (line 156), evidence reference (line 157), confirmation (line 158) -->
- [ ] **Reviewer**: [REVIEWER_NAME:string/Role] - [APPROVAL_STATUS:enum(approved|pending|rejected)]
- [ ] **Evidence Package**: `.artifacts/protocol-[PROTOCOL_NUM:number]/evidence-package.zip` - [STATUS:enum(complete|pending)]
- [ ] **Confirmation**: [ACKNOWLEDGMENT:string received]

### Documentation Requirements
<!-- REQUIRED: ≥3 doc terms (line 184: log/brief/notes/transcript/manifest/report) -->
- [ ] [DOC_TYPE_1:string] saved to `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]`
- [ ] Format: [FORMAT:enum(.md|.json|.yaml)]
- [ ] Reviewer docs: `.artifacts/protocol-[PROTOCOL_NUM:number]/reviewer-summary.md`

### Next Protocol Alignment
<!-- REQUIRED: Ready statements (line 211), next commands (line 212), dependencies (line 213), continuation (line 214) -->
- [ ] **Ready for Protocol [NEXT_PROTOCOL:number]**: All prerequisites met, evidence complete
- [ ] **Next Command**: `@apply protocol-[NEXT_PROTOCOL:number]` or `run scripts/generate_session_continuation.py`
- [ ] **Dependencies**: [DEPENDENCY_1:string], [DEPENDENCY_2:string]
- [ ] **Continuation Script**: `scripts/generate_session_continuation.py --from [PROTOCOL_NUM:number] --to [NEXT_PROTOCOL:number]`

---

## EVIDENCE SUMMARY

<!-- VALIDATOR MAPPING:
  Primary: Evidence Validator (validate_protocol_evidence.py)
  Dimensions:
    - artifact_generation (line 89, weight 0.3)
    - storage_structure (line 126, weight 0.2)
    - manifest_completeness (line 156, weight 0.2)
    - traceability (line 201, weight 0.15)
    - archival (line 230, weight 0.15)
  Pass Threshold: 0.90
  Required: Table with artifact column (line 103), ≥2 rows or ≥3 artifact mentions (line 105)
-->

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
<!-- REQUIRED: Table present (line 102), artifact column (line 103), metrics column (line 104) -->
| [ARTIFACT_1:string] | `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH_1:string]` | [TYPE_1:string] | [METRIC_1:string]: [VALUE_1:string] |
| [ARTIFACT_2:string] | `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH_2:string]` | [TYPE_2:string] | [METRIC_2:string]: [VALUE_2:string] |
| [ARTIFACT_3:string] | `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH_3:string]` | [TYPE_3:string] | [METRIC_3:string]: [VALUE_3:string] |

### Storage Structure
<!-- REQUIRED: Protocol directory (line 139), subdirectories (line 140), permissions (line 141), naming (line 142) -->

- **Protocol Directory**: `.artifacts/protocol-[PROTOCOL_NUM:number]/`
- **Subdirectories**: 
  - `[SUBDIR_1:string]/` for [PURPOSE_1:string]
  - `[SUBDIR_2:string]/` for [PURPOSE_2:string]
- **Permissions**: [PERMISSIONS:enum(Read|Write|Access)] - [ACCESS_REQUIREMENTS:string]
- **Naming Convention**: [PATTERN:string - e.g., {artifact-name}-{timestamp}.{ext}]

### Manifest (Optional but Recommended)
<!-- OPTIONAL: Manifest reference (line 167), metadata (line 163), dependencies (line 164), coverage (line 165) -->

- **Manifest File**: `.artifacts/protocol-[PROTOCOL_NUM:number]/evidence-manifest.json`
- **Metadata**: Timestamp, size, hash (SHA-256)
- **Dependencies**: Input/output artifact links
- **Coverage**: [COVERAGE:enum(100%|complete)]

### Traceability
<!-- REQUIRED: Inputs (line 214), outputs (line 215), transformations (line 216), audit trail (line 217) -->

- **Inputs From**: 
  - Protocol [INPUT_PROTOCOL_1:number] → [INPUT_ARTIFACT_1:string]
  - Protocol [INPUT_PROTOCOL_2:number] → [INPUT_ARTIFACT_2:string]
- **Outputs To**: 
  - Protocol [OUTPUT_PROTOCOL_1:number] → [OUTPUT_ARTIFACT_1:string]
  - Protocol [OUTPUT_PROTOCOL_2:number] → [OUTPUT_ARTIFACT_2:string]
- **Transformations**: [TRANSFORM_DESC:string - describe data transformations/derivations]
- **Audit Trail**: `.artifacts/protocol-[PROTOCOL_NUM:number]/audit-log.json`

### Archival (Optional)
<!-- OPTIONAL: Compression (line 249), retention (line 250), retrieval (line 251), cleanup (line 252) -->

- **Compression**: [COMPRESSION_FORMAT:enum(zip|tar.gz)] - `.artifacts/protocol-[PROTOCOL_NUM:number]/archive.zip`
- **Retention**: [RETENTION_DURATION:string - e.g., 30 days, 90 days, 1 year]
- **Retrieval**: [RETRIEVAL_METHOD:string - access method and permissions]
- **Cleanup**: [CLEANUP_POLICY:string - deletion policy after retention period]

---

## PLACEHOLDER TYPE SYSTEM REFERENCE

### Type Categories

**STRING Types**:
- `[NAME:string]` - Free-form text
- `[NAME:string min=N]` - Minimum N characters
- `[NAME:string pattern="regex"]` - Must match regex

**ENUM Types**:
- `[NAME:enum(option1|option2|option3)]` - Must be one of listed options

**NUMBER Types**:
- `[NAME:number]` - Any number
- `[NAME:number min=N]` - Minimum value
- `[NAME:percentage]` - Number with % (0-100)
- `[NAME:score]` - Float 0.0-1.0

**PATH Types**:
- `[NAME:path_artifact]` - Path in .artifacts/protocol-XX/

**LIST Types**:
- `[NAME:list min=N]` - List with minimum N items

---

**STRUCTURE TEMPLATE COMPLETE** ✅

This template contains all 9 required sections with proper validator mappings, placeholders, and requirements. Ready for Protocol 3 content population.
