# PROTOCOL [PROTOCOL_NUM:number]: [PROTOCOL_NAME:string]

**Version**: v1.0.0 | **Phase**: [PHASE:enum(Phase 0|Phase 1-2|Phase 3|Phase 4|Phase 5|Phase 6)] | **Status**: Draft

---

## PREREQUISITES

<!-- VALIDATOR MAPPING:
  Primary: Identity Validator (validate_protocol_identity.py)
  Dimensions: prerequisites (part of identity validation)
  Pass Threshold: 0.95
  Required: 3 categories (Required Artifacts, Required Approvals, System State)
-->

### Required Artifacts
- [ARTIFACT_1:string]: [DESCRIPTION:string] (from Protocol [PROTOCOL_NUM_INPUT:number])
- [ARTIFACT_2:string]: [DESCRIPTION:string] (optional)
- [ARTIFACT_3:string]: [DESCRIPTION:string] (optional)

### Required Approvals
- [APPROVAL_1:string]: [STAKEHOLDER:string]
- [APPROVAL_2:string]: [STAKEHOLDER:string]

### System State
- [STATE_REQ_1:string]
- [STATE_REQ_2:string]
- [STATE_REQ_3:string]

---

## AI ROLE AND MISSION

<!-- VALIDATOR MAPPING:
  Primary: Role Validator (validate_protocol_role.py)
  Dimensions: role_definition (weight 0.25), mission_statement (weight 0.25), constraints_guidelines (weight 0.20), output_expectations (weight 0.15), behavioral_guidance (weight 0.15)
  Pass Threshold: 0.90
  Required: All 5 dimensions present
-->

You are a **[ROLE_TITLE:string]**. <!-- REQUIRED: "You are a" or "You are an" pattern (Role Validator line 101) -->

<!-- ROLE DESCRIPTION (Role Validator line 103: >60 chars, >1 line) -->
[ROLE_DESCRIPTION:string min=60 chars spanning 2+ lines. Must include domain expertise keywords (domain/expertise/industry/capability) OR behavioral traits (empathy/strategy/rigor/evidence/governance)]

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

<!-- VALIDATOR MAPPING:
  Primary: Workflow Validator (validate_protocol_workflow.py)
  Dimensions: workflow_structure (weight 0.20), step_definitions (weight 0.25), action_markers (weight 0.15), halt_conditions (weight 0.20), evidence_tracking (weight 0.20)
  Pass Threshold: 0.90
  Required: ≥2 sequential steps, action markers, halt conditions, evidence tracking
-->

### STEP 1: [STEP_1_NAME:string]

<!-- REQUIRED: Sequential numbering starting at 1 (Workflow Validator line 96) -->

1. **[STRICT]** [ACTION_1:string with "must/require/ensure" keyword]
   - **Input**: [INPUT_1:string]
   - **Process**: [PROCESS_1:string]
   - **Output**: [OUTPUT_1:string]
   - **Validation**: [VALIDATION_1:string]

2. **[GUIDELINE]** [ACTION_2:string with decision point]
   - **Input**: [INPUT_2:string]
   - **Process**: [PROCESS_2:string]
   - **Output**: [OUTPUT_2:string]
   - **Validation**: [VALIDATION_2:string]

3. **[CRITICAL]** [ACTION_3:string with problem-solving logic]
   - **Input**: [INPUT_3:string]
   - **Process**: [PROCESS_3:string]
   - **Output**: [OUTPUT_3:string]
   - **Validation**: [VALIDATION_3:string]

### STEP 2: [STEP_2_NAME:string]

<!-- REQUIRED: Sequential step numbering (Workflow Validator line 100: ≥2 steps) -->

1. **[STRICT]** [ACTION_4:string]
   - **Input**: [INPUT_4:string]
   - **Process**: [PROCESS_4:string]
   - **Output**: [OUTPUT_4:string]
   - **Validation**: [VALIDATION_4:string]

2. **[GUIDELINE]** [ACTION_5:string]
   - **Input**: [INPUT_5:string]
   - **Process**: [PROCESS_5:string]
   - **Output**: [OUTPUT_5:string]
   - **Validation**: [VALIDATION_5:string]

### Halt Conditions

<!-- REQUIRED: ≥2 halt mentions (Workflow Validator line 209) -->

- **If [CONDITION_1:string]**: [HALT_ACTION_1:string with error messaging]
- **If [CONDITION_2:string]**: [HALT_ACTION_2:string with rollback procedure]

### Evidence Tracking

<!-- REQUIRED: Evidence mentions in workflow (Workflow Validator line 235: ≥3 mentions) -->

- [EVIDENCE_POINT_1:string]: Track [METRIC_1:string]
- [EVIDENCE_POINT_2:string]: Track [METRIC_2:string]
- [EVIDENCE_POINT_3:string]: Track [METRIC_3:string]

---

## INTEGRATION POINTS

<!-- VALIDATOR MAPPING:
  Primary: Identity Validator (validate_protocol_identity.py)
  Dimensions: integration_points (part of identity validation)
  Pass Threshold: 0.95
  Required: Inputs From, Outputs To, Data Formats, Storage Locations
-->

### Inputs From

- **Protocol [PROTOCOL_XX:number]**: [ARTIFACT_INPUT_1:string] ([FORMAT_1:enum(.md|.json|.yaml)]) from `.artifacts/protocol-[PROTOCOL_XX:number]/`
- **Protocol [PROTOCOL_YY:number]**: [ARTIFACT_INPUT_2:string] ([FORMAT_2:enum(.md|.json|.yaml)]) from `.artifacts/protocol-[PROTOCOL_YY:number]/`

### Outputs To

- **Protocol [PROTOCOL_ZZ:number]**: [ARTIFACT_OUTPUT_1:string] ([FORMAT_3:enum(.md|.json|.yaml)]) to `.artifacts/protocol-[PROTOCOL_ZZ:number]/`
- **Protocol [PROTOCOL_AA:number]**: [ARTIFACT_OUTPUT_2:string] ([FORMAT_4:enum(.md|.json|.yaml)]) to `.artifacts/protocol-[PROTOCOL_AA:number]/`

### Data Formats

- Markdown (.md) for [PURPOSE_1:string]
- JSON (.json) for [PURPOSE_2:string]
- YAML (.yaml) for [PURPOSE_3:string]

### Storage Locations

- `.artifacts/protocol-[PROTOCOL_NUM:number]/` for [ARTIFACT_TYPE_1:string]
- `.artifacts/protocol-[PROTOCOL_NUM:number]/subdir/` for [ARTIFACT_TYPE_2:string]

---

## QUALITY GATES

<!-- VALIDATOR MAPPING:
  Primary: Gates Validator (validate_protocol_gates.py)
  Dimensions: gate_definitions (weight 0.25), pass_criteria (weight 0.25), automation (weight 0.20), failure_handling (weight 0.15), compliance_integration (weight 0.15)
  Pass Threshold: 0.92
  Required Count: ≥2 gates with types, thresholds, metrics, evidence links, failure handling
-->

### Gate 1: [GATE_1_NAME:string] ([TYPE_1:enum(Prerequisite|Execution|Completion)])

<!-- REQUIRED: Gate type (Gates Validator line 112) -->

- **Criteria**: [DESCRIPTION:string with numeric threshold "≥X" or boolean "= pass"]
- **Pass Threshold**: [THRESHOLD:format("≥X.XX" OR "status = pass")]
- **Metrics**: [METRIC:enum(score|confidence|rate|percentage)]
- **Evidence Links**: [REFERENCE:string linking to .artifacts/protocol-XX/]
- **Failure Handling**:
  - [ROLLBACK:string procedure]
  - [NOTIFICATION:string path]
  - [WAIVER:string policy]

### Gate 2: [GATE_2_NAME:string] ([TYPE_2:enum(Prerequisite|Execution|Completion)])

<!-- REQUIRED: Minimum 2 gates (Gates Validator line 100) -->

- **Criteria**: [DESCRIPTION:string with numeric threshold "≥X" or boolean "= pass"]
- **Pass Threshold**: [THRESHOLD:format("≥X.XX" OR "status = pass")]
- **Metrics**: [METRIC:enum(score|confidence|rate|percentage)]
- **Evidence Links**: [REFERENCE:string linking to .artifacts/protocol-XX/]
- **Failure Handling**:
  - [ROLLBACK:string procedure]
  - [NOTIFICATION:string path]
  - [WAIVER:string policy]

---

## COMMUNICATION PROTOCOLS

<!-- VALIDATOR MAPPING:
  Primary: Communication Validator (validate_protocol_communication.py)
  Dimensions: status_announcements (weight 0.25), user_interaction (weight 0.25), error_messaging (weight 0.20), progress_tracking (weight 0.15), evidence_communication (weight 0.15)
  Pass Threshold: 0.90
  Required: All 5 dimensions present with specific counts
-->

### Status Announcements

<!-- REQUIRED: ≥3 phase mentions (Communication Validator line 102), ≥1 MASTER RAY mention (line 103) -->

- `[PHASE [PHASE_NUM:number] START]` [ANNOUNCEMENT:string with MASTER RAY branding]
- `[PHASE [PHASE_NUM:number] COMPLETE]` [COMPLETION:string with ETA/duration]
- `[READY]` [READY_STATE:string announcement]

### User Interaction

<!-- REQUIRED: Confirmation, clarification, decision points, feedback (Communication Validator lines 131-134) -->

- **Confirmation**: "[QUESTION:string] Reply 'Go' to continue."
- **Clarification**: "Should I interpret {X} as {Y}?"
- **Decision Points**: "Choose option A or B:"
- **Feedback Requests**: "Does this approach meet your requirements?"

### Error Messaging

<!-- REQUIRED: Template, severity, context, resolution (Communication Validator lines 160-163) -->

- `[ERROR]` [ERROR_TEMPLATE:string with severity: CRITICAL/HIGH/WARNING]
- **Context**: [DETAILS:string]
- **Resolution**: [REQUIRED_ACTION:string steps]

### Progress Tracking

<!-- REQUIRED: ≥3 progress terms, timeline mentions (Communication Validator lines 187-188) -->

- `[PROGRESS]` [CURRENT_ACTIVITY:string] - [PERCENTAGE:percentage]% complete
- `[NEXT]` [NEXT_STEPS:string with timeline]

### Evidence Communication

- `[ARTIFACT]` [ARTIFACT_NAME:string] saved to `.artifacts/protocol-[PROTOCOL_NUM:number]/`
- **Format**: [FORMAT:enum(markdown|json|yaml)]
- **Validation**: [STATUS:enum(pass|fail)]

---

## AUTOMATION HOOKS

<!-- VALIDATOR MAPPING:
  Primary: Scripts Validator (validate_protocol_scripts.py)
  Dimensions: script_inventory (weight 0.25), registry_alignment (weight 0.20), execution_context (weight 0.20), command_syntax (weight 0.20), error_handling (weight 0.15)
  Pass Threshold: 0.90
  Required: ≥3 automation commands, registry alignment, execution context, error handling
-->

### Scripts

<!-- REQUIRED: ≥3 commands (Scripts Validator line 117) -->

```bash
# [SCRIPT_PURPOSE_1:string]
python3 scripts/[SCRIPT_NAME_1:string].py [ARGS_1:string]

# [SCRIPT_PURPOSE_2:string]
bash scripts/[SCRIPT_NAME_2:string].sh [ARGS_2:string]

# [SCRIPT_PURPOSE_3:string]
python3 scripts/[SCRIPT_NAME_3:string].py [ARGS_3:string]
```

### Registry Alignment

<!-- REQUIRED: Registry reference (Scripts Validator line 139), registry file mention (line 140) -->

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

<!-- REQUIRED: Exit codes, fallback, logging (Scripts Validator lines 272-310) -->

- **Exit Codes**: [EXIT_CODES:string - 0 = success, 1 = failure]
- **Fallback**: [FALLBACK:string - retry sequence]
- **Logging**: [LOG_PATH:path_artifact - log file location]
- **Manual Paths**: [MANUAL_STEPS:string - manual intervention steps]

---

## HANDOFF CHECKLIST

<!-- VALIDATOR MAPPING:
  Primary: Handoff Validator (validate_protocol_handoff.py)
  Dimensions: checklist_completeness (weight 0.30), verification_procedures (weight 0.20), stakeholder_signoff (weight 0.20), documentation_requirements (weight 0.15), next_protocol_alignment (weight 0.15)
  Pass Threshold: 0.90
  Required: ≥6 checklist items across ≥3 categories
-->

### Prerequisites

<!-- REQUIRED: ≥6 total items across all categories (Handoff Validator line 100) -->

- [ ] [PREREQ_ITEM_1:string]
- [ ] [PREREQ_ITEM_2:string]

### Workflow

<!-- REQUIRED: ≥3 categories (Handoff Validator line 101: Prerequisite|Workflow|Quality|Evidence|Integration|Automation) -->

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

<!-- REQUIRED: ≥4 verification terms (Handoff Validator line 128: validate/ensure/confirm/verify/gate) -->

- [ ] Validate [ITEM_1:string] using [METHOD_1:string]
- [ ] Confirm [ITEM_2:string] with [STAKEHOLDER_1:string]
- [ ] QA review: [CHECKLIST_1:string]
- [ ] Gate check: [GATE_VALIDATION:string]

### Stakeholder Sign-off

<!-- REQUIRED: Approval, reviewers, evidence reference, confirmation (Handoff Validator lines 155-158) -->

- [ ] **Reviewer**: [REVIEWER_NAME:string/Role] - [APPROVAL_STATUS:enum(approved|pending|rejected)]
- [ ] **Evidence Package**: [EVIDENCE_LOCATION:path_artifact] - [STATUS:enum(complete|pending)]
- [ ] **Confirmation**: [ACKNOWLEDGMENT:string received]

### Documentation Requirements

<!-- REQUIRED: ≥3 doc terms (Handoff Validator line 184: log/brief/notes/transcript/manifest/report) -->

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

<!-- VALIDATOR MAPPING:
  Primary: Evidence Validator (validate_protocol_evidence.py)
  Dimensions: artifact_generation (weight 0.30), storage_structure (weight 0.20), manifest_completeness (weight 0.20), traceability (weight 0.15), archival (weight 0.15)
  Pass Threshold: 0.90
  Required: Table with artifact column, ≥2 rows or ≥3 artifact mentions
-->

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
<!-- REQUIRED: Table present (Evidence Validator line 102), artifact column (line 103), metrics column (line 104) -->
| [ARTIFACT_1:string] | `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]` | [TYPE_1:string] | [METRIC_1:string: value] |
| [ARTIFACT_2:string] | `.artifacts/protocol-[PROTOCOL_NUM:number]/[PATH:string]` | [TYPE_2:string] | [METRIC_2:string: value] |

### Storage Structure

<!-- REQUIRED: Protocol directory (line 139), subdirectories (line 140), permissions (line 141), naming (line 142) -->

- **Protocol Directory**: `.artifacts/protocol-[PROTOCOL_NUM:number]/`
- **Subdirectories**: [SUBDIRS:list min=1]
- **Permissions**: [PERMISSIONS:enum(Read|write|access)]
- **Naming Convention**: [PATTERN:string]

### Manifest

<!-- REQUIRED: Manifest reference OR metadata/dependencies/coverage (Evidence Validator lines 162-184) -->

- **Manifest File**: [MANIFEST_LOCATION:path_artifact] (optional)
- **Metadata**: [METADATA:string - timestamp, size, hash]
- **Dependencies**: [DEPENDENCIES:string - input/output links]
- **Coverage**: [COVERAGE:enum(100%|complete)]

### Traceability

<!-- REQUIRED: Inputs, outputs, transformations, audit trail (Evidence Validator lines 202-240) -->

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

## READY FOR PROTOCOL 3

**Next Step**: `3-create-protocol-content.md`

The protocol structure template is complete and ready for content population.

