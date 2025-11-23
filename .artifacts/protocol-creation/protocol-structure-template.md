# PROTOCOL [14]: [PROTOCOL NAME]

**Version**: v1.0.0 | **Phase**: [Phase X] | **Status**: Draft

---

## PREREQUISITES

<\!-- VALIDATOR MAPPING:
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

---

## AI ROLE AND MISSION

<\!-- VALIDATOR MAPPING:
  Primary: Role Validator (validate_protocol_role.py)
  Dimensions: role_definition (lines 93-127), mission_statement (lines 129-155)
  Pass Threshold: 0.90
-->

<\!-- ROLE DEFINITION (Role Validator dimension 1/5, weight 0.25) -->
You are a **[ROLE_TITLE:string]**.

<\!-- ROLE DESCRIPTION (Role Validator line 103: >60 chars, >1 line) -->
[ROLE_DESCRIPTION:string min=60 chars, spanning 2+ lines. Must include domain expertise keywords (domain/expertise/industry/capability) OR behavioral traits (empat/strateg/rigor/evidence/governance)]

<\!-- MISSION STATEMENT (Role Validator dimension 2/5, weight 0.25) -->
**Mission**: [MISSION_STATEMENT:string including ALL 4 elements:
  1. "mission" keyword
  2. Scope boundary: within/only/do not/boundary/scope
  3. Success criteria: success/complete/validation/evidence
  4. Value proposition: client/value/impact/benefit/outcome
]

### Constraints and Guidelines
- **[STRICT]** [CONSTRAINT:string with "must/require/ensure/strict" keyword]
- **[GUIDELINE]** [RECOMMENDATION:string]
- **[CRITICAL]** [CRITICAL_REQ:string with "avoid/within/limit/never" boundary]

---

## WORKFLOW

<\!-- VALIDATOR MAPPING:
  Primary: Workflow Validator (validate_protocol_workflow.py)
  Dimensions: workflow_structure (lines 89-116), step_definitions (lines 118-148), action_markers (lines 150-196), halt_conditions (lines 198-226), evidence_tracking (lines 228-250)
  Pass Threshold: 0.90
  Required: ≥3 sequential steps
-->

### STEP 1: [STEP_1_NAME:string]

<\!-- REQUIRED: Sequential numbering starting at 1 -->
1. **[STRICT]** [ACTION_1:string with "must/require/ensure" keyword]
2. **[GUIDELINE]** [ACTION_2:string with decision point]
3. **[CRITICAL]** [ACTION_3:string with problem-solving logic]

**Validation Checkpoint 1.1**: After STEP 1, verify:
- ✓ [VERIFICATION_1:string]
- ✓ [VERIFICATION_2:string]
- ✓ If any check fails: [REMEDIATION_1:string]

### STEP 2: [STEP_2_NAME:string]

<\!-- REQUIRED: Sequential step numbering (≥3 steps total) -->
1. **[STRICT]** [ACTION_4:string]
2. **[GUIDELINE]** [ACTION_5:string]

**Validation Checkpoint 2.1**: After STEP 2, verify:
- ✓ [VERIFICATION_3:string]
- ✓ [VERIFICATION_4:string]

### STEP 3: [STEP_3_NAME:string]

1. **[CRITICAL]** [ACTION_6:string]
2. **[STRICT]** [ACTION_7:string]

**Validation Checkpoint 3.1**: After STEP 3, verify:
- ✓ [VERIFICATION_5:string]

### Halt Conditions

<\!-- REQUIRED: ≥2 halt mentions -->
- **If [CONDITION_1:string]**: [HALT_ACTION_1:string with error messaging]
- **If [CONDITION_2:string]**: [HALT_ACTION_2:string with rollback]

### Evidence Tracking

<\!-- REQUIRED: Evidence mentions in workflow -->
- [EVIDENCE_POINT_1:string]: Track [METRIC_1:string]
- [EVIDENCE_POINT_2:string]: Track [METRIC_2:string]
- [EVIDENCE_POINT_3:string]: Track [METRIC_3:string]

---

## INTEGRATION POINTS

<\!-- VALIDATOR MAPPING:
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

---

## QUALITY GATES

<\!-- VALIDATOR MAPPING:
  Primary: Gates Validator (validate_protocol_gates.py)
  Required Count: ≥2 gates
  Pass Threshold: 0.90
-->

### Gate 1: [GATE_1_NAME:string] ([TYPE_1:enum(Prerequisite|Execution|Completion)])

- **Criteria**: [DESCRIPTION:string with numeric threshold "≥X" or boolean "= pass"]
- **Pass Threshold**: [THRESHOLD:format("≥X.XX" OR "status = pass")]
- **Metrics**: [METRIC:enum(score|confidence|rate|percentage)]
- **Evidence Links**: [REFERENCE:string linking to .artifacts/protocol-XX/]
- **Failure Handling**: 
  - [ROLLBACK:string procedure]
  - [NOTIFICATION:string path]
  - [WAIVER:string policy]

### Gate 2: [GATE_2_NAME:string] ([TYPE_2:enum(Prerequisite|Execution|Completion)])

- **Criteria**: [DESCRIPTION:string with numeric threshold "≥X" or boolean "= pass"]
- **Pass Threshold**: [THRESHOLD:format("≥X.XX" OR "status = pass")]
- **Metrics**: [METRIC:enum(score|confidence|rate|percentage)]
- **Evidence Links**: [REFERENCE:string linking to .artifacts/protocol-XX/]
- **Failure Handling**: 
  - [ROLLBACK:string procedure]
  - [NOTIFICATION:string path]
  - [WAIVER:string policy]

<\!-- VALIDATION CHECKLIST:
  ✓ Gate count ≥2
  ✓ Each gate has type
  ✓ Each gate has numeric or boolean threshold
  ✓ Metrics specified
  ✓ Evidence links present (≥3 total mentions)
  ✓ Failure handling documented
-->

---

## COMMUNICATION PROTOCOLS

<\!-- VALIDATOR MAPPING:
  Primary: Communication Validator (validate_protocol_communication.py)
  Dimensions: status_announcements (lines 89-117), user_interaction (lines 119-145), error_messaging (lines 147-173), progress_tracking (lines 175-200), evidence_communication (lines 202-230)
  Pass Threshold: 0.90
-->

### Status Announcements

<\!-- REQUIRED: ≥3 phase mentions, ≥1 MASTER RAY mention -->
- `[PHASE [PHASE_NUM:number] START]` [ANNOUNCEMENT:string with MASTER RAY branding]
- `[PHASE [PHASE_NUM:number] COMPLETE]` [COMPLETION:string with ETA/duration]
- `[READY]` [READY_STATE:string announcement]

### User Interaction

<\!-- REQUIRED: Confirmation, clarification, decision points, feedback -->
- **Confirmation**: "[QUESTION:string] Reply 'Go' to continue."
- **Clarification**: "Should I interpret {X} as {Y}?"
- **Decision Points**: "Choose option A or B:"
- **Feedback Requests**: "Does this approach meet your requirements?"

### Error Messaging

<\!-- REQUIRED: Template, severity, context, resolution -->
- `[ERROR]` [ERROR_TEMPLATE:string with severity: CRITICAL/HIGH/WARNING]
- **Context**: [DETAILS:string]
- **Resolution**: [REQUIRED_ACTION:string steps]

### Progress Tracking

<\!-- REQUIRED: ≥3 progress terms, timeline mentions -->
- `[PROGRESS]` [CURRENT_ACTIVITY:string] - [PERCENTAGE:percentage]% complete
- `[NEXT]` [NEXT_STEPS:string with timeline]
- `[STATUS]` [STATUS_UPDATE:string]

### Evidence Communication

- `[ARTIFACT]` [ARTIFACT_NAME:string] saved to `.artifacts/protocol-[PROTOCOL_NUM:number]/`
- **Format**: [FORMAT:enum(markdown|json|yaml)]
- **Validation**: [STATUS:enum(pass|fail)]

---

## AUTOMATION HOOKS

<\!-- VALIDATOR MAPPING:
  Primary: Scripts Validator (validate_protocol_scripts.py)
  Dimensions: script_inventory (lines 96-125), registry_alignment (lines 127-187), execution_context (lines 189-230), command_syntax (lines 232-270), error_handling (lines 272-310)
  Pass Threshold: 0.90
  Required: ≥3 automation commands
-->

### Scripts

<\!-- REQUIRED: ≥3 commands -->
```bash
# [SCRIPT_PURPOSE_1:string]
python3 scripts/[SCRIPT_NAME_1:string].py [ARGS_1:string]

# [SCRIPT_PURPOSE_2:string]
bash scripts/[SCRIPT_NAME_2:string].sh [ARGS_2:string]

# [SCRIPT_PURPOSE_3:string]
python3 scripts/[SCRIPT_NAME_3:string].py [ARGS_3:string]
```

### Registry Alignment

<\!-- REQUIRED: Registry reference -->
- **Script Registry**: `scripts/script-registry.json`
- **Registered Scripts**: [REGISTERED_SCRIPTS:list min=1]

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

<\!-- REQUIRED: Exit codes, fallback, logging -->
- **Exit Codes**: [EXIT_CODES:string - 0 = success, 1 = failure]
- **Fallback**: [FALLBACK:string - retry sequence]
- **Logging**: [LOG_PATH:path_artifact - log file location]
- **Manual Paths**: [MANUAL_STEPS:string - manual intervention steps]

---

## HANDOFF CHECKLIST

<\!-- VALIDATOR MAPPING:
  Primary: Handoff Validator (validate_protocol_handoff.py)
  Dimensions: checklist_completeness (lines 89-113), verification_procedures (lines 115-141), stakeholder_signoff (lines 143-169), documentation_requirements (lines 171-200), next_protocol_alignment (lines 202-230)
  Pass Threshold: 0.90
  Required: ≥6 checklist items, ≥3 categories
-->

### Prerequisites

<\!-- REQUIRED: ≥6 total items across all categories -->
- [ ] [PREREQ_ITEM_1:string]
- [ ] [PREREQ_ITEM_2:string]

### Workflow

<\!-- REQUIRED: ≥3 categories -->
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

<\!-- REQUIRED: ≥4 verification terms -->
- [ ] Validate [ITEM_1:string] using [METHOD_1:string]
- [ ] Confirm [ITEM_2:string] with [STAKEHOLDER_1:string]
- [ ] Verify [ITEM_3:string] against [CRITERIA_1:string]
- [ ] Check [ITEM_4:string] for [CONDITION_1:string]

### Stakeholder Sign-off

<\!-- REQUIRED: Approval, reviewers, evidence reference, confirmation -->
- [ ] **Reviewer**: [REVIEWER_NAME:string/Role] - [APPROVAL_STATUS:enum(approved|pending|rejected)]
- [ ] **Evidence Package**: [EVIDENCE_LOCATION:path_artifact] - [STATUS:enum(complete|pending)]
- [ ] **Confirmation**: [ACKNOWLEDGMENT:string received]

### Documentation Requirements

<\!-- REQUIRED: ≥3 doc terms -->
- [ ] [DOC_TYPE:string] saved to [LOCATION:path_artifact]
- [ ] Format: [FORMAT:enum(.md|.json|.yaml)]
- [ ] Reviewer docs: [REVIEWER_DOCS:path_artifact]

### Next Protocol Alignment

- [ ] **Ready for Protocol [NEXT_PROTOCOL:number]**: [STATEMENT:string]
- [ ] **Next Command**: `@apply protocol-[NEXT_PROTOCOL:number]` or `run protocol-[NEXT_PROTOCOL:number]`
- [ ] **Dependencies**: [DEPENDENCIES:list min=1]
- [ ] **Continuation Script**: [SCRIPT_NAME:string if applicable]

---

## EVIDENCE SUMMARY

<\!-- VALIDATOR MAPPING:
  Primary: Evidence Validator (validate_protocol_evidence.py)
  Dimensions: artifact_generation (lines 89-124), storage_structure (lines 126-154), manifest_completeness (lines 156-200), traceability (lines 202-240), archival (lines 242-280)
  Pass Threshold: 0.90
  Required: Table with artifact column, ≥2 rows
-->

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
| [ARTIFACT_1:string] | `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]` | [TYPE_1:string] | [METRIC_1:string: value] |
| [ARTIFACT_2:string] | `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]` | [TYPE_2:string] | [METRIC_2:string: value] |

### Storage Structure

<\!-- REQUIRED: Protocol directory, subdirectories, permissions, naming -->
- **Protocol Directory**: `.artifacts/protocol-[PROTOCOL_NUM:number]/`
- **Subdirectories**: [SUBDIRS:list min=1]
- **Permissions**: [PERMISSIONS:enum(Read|write|access)]
- **Naming Convention**: [PATTERN:string]

### Manifest

<\!-- REQUIRED: Manifest reference OR metadata/dependencies/coverage -->
- **Manifest File**: [MANIFEST_LOCATION:path_artifact] (optional)
- **Metadata**: [METADATA:string - timestamp, size, hash]
- **Dependencies**: [DEPENDENCIES:string - input/output links]
- **Coverage**: [COVERAGE:enum(100%|complete)]

### Traceability

<\!-- REQUIRED: Inputs, outputs, transformations, audit trail -->
- **Inputs From**: [Protocol [INPUT_PROTOCOL:number] → [INPUT_ARTIFACT:string]]
- **Outputs To**: [Protocol [OUTPUT_PROTOCOL:number] → [OUTPUT_ARTIFACT:string]]
- **Transformations**: [TRANSFORM_DESC:string - process description]
- **Audit Trail**: [AUDIT_LOG:path_artifact]

### Archival (Optional)

- **Compression**: [COMPRESSION_FORMAT:enum(zip|tar.gz)]
- **Retention**: [RETENTION_DURATION:string - 30 days/90 days]
- **Retrieval**: [RETRIEVAL_METHOD:string - access method]
- **Cleanup**: [CLEANUP_POLICY:string - deletion policy]

---

## READY FOR PROTOCOL 14

**Next Step**: `14-create-protocol-content.md`

The protocol structure template is complete and ready for content population.

