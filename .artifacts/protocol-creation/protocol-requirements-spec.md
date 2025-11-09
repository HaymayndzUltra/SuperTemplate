# PROTOCOL REQUIREMENTS SPECIFICATION

**Generated**: 2025-01-09  
**Workspace**: /home/haymayndz/SuperTemplate  
**Source**: 10 Validator Scripts Analysis  
**Purpose**: Complete requirements for creating valid AI-driven workflow protocols

---

## EXECUTIVE SUMMARY

This specification extracts **ALL** validation requirements from the 10-validator system to guide protocol creation. Every protocol MUST pass these requirements with minimum scores.

### Pass Thresholds by Validator
- **Identity**: ≥ 0.95 (warning: ≥ 0.80)
- **Role**: ≥ 0.90 (warning: ≥ 0.80)
- **Workflow**: ≥ 0.90 (warning: ≥ 0.80)
- **Gates**: ≥ 0.92 (warning: ≥ 0.85)
- **Scripts**: ≥ 0.90 (warning: ≥ 0.80)
- **Communication**: ≥ 0.90 (warning: ≥ 0.80)
- **Evidence**: ≥ 0.90 (warning: ≥ 0.80)
- **Handoff**: ≥ 0.90 (warning: ≥ 0.80)
- **Reasoning**: ≥ 0.85 (warning: ≥ 0.70)
- **Reflection**: ≥ 0.85 (warning: ≥ 0.70)

---

## 1. REQUIRED SECTIONS (9 Total)

Every protocol MUST contain these sections:

1. **PREREQUISITES** - Required artifacts, approvals, system state
2. **AI ROLE AND MISSION** - Persona, mission, constraints, success criteria
3. **WORKFLOW** - Sequential steps with actions, evidence, halt conditions
4. **INTEGRATION POINTS** - Inputs from, outputs to, data formats, storage
5. **QUALITY GATES** - Gate definitions, pass criteria, automation, failure handling
6. **COMMUNICATION PROTOCOLS** - Status announcements, user interaction, error messaging
7. **AUTOMATION HOOKS** - Script inventory, registry alignment, execution context
8. **HANDOFF CHECKLIST** - Checklist items, verification, sign-off, documentation
9. **EVIDENCE SUMMARY** - Artifact generation, storage structure, traceability

---

## 2. VALIDATION CRITERIA SUMMARY

### 2.1 Identity Validator (validate_protocol_identity.py)
**Pass**: 0.95 | **Warning**: 0.80

**Dimensions**:
1. Basic Information (20%) - Protocol number, name, version, phase, purpose, scope
2. Prerequisites (20%) - Required artifacts, approvals, system state
3. Integration Points (20%) - Inputs, outputs, formats, storage
4. Compliance Standards (20%) - Industry, security, regulatory
5. Documentation Quality (20%) - All 9 sections present

### 2.2 Role Validator (validate_protocol_role.py)
**Pass**: 0.90 | **Warning**: 0.80

**Dimensions**:
1. Role Definition (25%) - Title, description, expertise, traits
2. Mission Statement (25%) - Clarity, boundaries, success, value
3. Constraints & Guidelines (20%) - Guardrails, boundaries, workflow alignment
4. Output Expectations (15%) - Format, structure, location, validation
5. Behavioral Guidance (15%) - Communication, decisions, errors, interaction

### 2.3 Workflow Validator (validate_protocol_workflow.py)
**Pass**: 0.90 | **Warning**: 0.80

**Dimensions**:
1. Workflow Structure (20%) - Section present, ≥2 steps, sequential, complete
2. Step Definitions (25%) - Action, communication, evidence per step
3. Action Markers (15%) - Imperative, action clarity, contextual support
4. Halt Conditions (20%) - Halt defined, gates, rollback, confirmation
5. Evidence Tracking (20%) - Evidence tags, artifacts, manifest, downstream

### 2.4 Gates Validator (validate_protocol_gates.py)
**Pass**: 0.92 | **Warning**: 0.85

**Dimensions**:
1. Gate Definitions (25%) - ≥2 gates, descriptions, types, naming
2. Pass Criteria (25%) - Thresholds, boolean, metrics, evidence links
3. Automation (20%) - Scripts, CI, automation labels
4. Failure Handling (15%) - Failure actions, rollback, notification, waivers
5. Compliance Integration (15%) - Compliance terms, automation, evidence, governance

### 2.5 Scripts Validator (validate_protocol_scripts.py)
**Pass**: 0.90 | **Warning**: 0.80

**Dimensions**:
1. Script Inventory (25%) - ≥3 commands, executable, paths exist
2. Registry Alignment (20%) - Registry reference, file exists, cross-links, ownership
3. Execution Context (20%) - CI, environment, scheduling, permissions
4. Command Syntax (20%) - Flags, redirection, parameterization, documentation
5. Error Handling (15%) - Exit codes, fallback, logging, manual paths

### 2.6 Communication Validator (validate_protocol_communication.py)
**Pass**: 0.90 | **Warning**: 0.80

**Dimensions**:
1. Status Announcements (25%) - Phase transitions, MASTER RAY, completion, time
2. User Interaction (25%) - Confirmation, clarification, decisions, feedback
3. Error Messaging (20%) - Templates, severity, context, resolution
4. Progress Tracking (15%) - Progress terms, timeline, current, next
5. Evidence Communication (15%) - Artifact announcements, format, location, validation

### 2.7 Evidence Validator (validate_protocol_evidence.py)
**Pass**: 0.90 | **Warning**: 0.80

**Dimensions**:
1. Artifact Generation (30%) - Table present, artifact column, metrics, ≥2 rows
2. Storage Structure (20%) - Protocol directory, subdirectories, permissions, naming
3. Manifest Completeness (20%) - Manifest reference, metadata, dependencies, coverage
4. Traceability (15%) - Inputs, outputs, transformations, audit
5. Archival (15%) - Compression, retention, retrieval, cleanup

### 2.8 Handoff Validator (validate_protocol_handoff.py)
**Pass**: 0.90 | **Warning**: 0.80

**Dimensions**:
1. Checklist Completeness (30%) - ≥6 items, ≥3 categories, dependencies, status markers
2. Verification Procedures (20%) - ≥4 verification terms, QA, automation, evidence
3. Stakeholder Sign-off (20%) - Approvals, reviewers, evidence, confirmation
4. Documentation Requirements (15%) - ≥3 doc terms, storage, reviewer docs, format
5. Next Protocol Alignment (15%) - Ready statements, next commands, dependencies, continuation

### 2.9 Reasoning Validator (validate_protocol_reasoning.py)
**Pass**: 0.85 | **Warning**: 0.70

**Dimensions**:
1. Reasoning Patterns (25%) - ≥2 pattern terms, explanations, improvement, examples
2. Decision Trees (25%) - ≥3 decisions, ≥4 criteria, ≥2 outcomes, ≥2 logging
3. Problem Solving Logic (20%) - ≥3 problems, root cause, ≥2 solutions, ≥2 validation
4. Learning Mechanisms (15%) - Feedback, improvement tracking, knowledge base, adaptation
5. Meta-Cognition (15%) - Awareness, monitoring, correction, improvement

### 2.10 Reflection Validator (validate_protocol_reflection.py)
**Pass**: 0.85 | **Warning**: 0.70

**Dimensions**:
1. Retrospective Analysis (30%) - Review, performance, issues, success
2. Continuous Improvement (25%) - Opportunities, plans, tracking, evidence
3. System Evolution (20%) - Version history, rationale, impact, rollback
4. Knowledge Capture (15%) - Lessons, knowledge base, storage, sharing
5. Future Planning (10%) - Roadmap, priorities, resources, timeline

---

## 3. CONTENT PATTERNS & KEYWORDS

### Required Keywords by Section

**PREREQUISITES**:
- "Required Artifacts" OR "ARTIFACTS"
- "Required Approvals" OR "Approvals"
- "System State" OR "Environment" OR "Dependencies"

**AI ROLE AND MISSION**:
- "You are a" OR "You are an"
- "mission"
- "within", "only", "do not", "boundar", "scope"
- "success", "complete", "validation", "evidence"
- "must", "require", "ensure", "strict"

**WORKFLOW**:
- "### STEP 1", "### STEP 2", etc. (sequential)
- "**Action:**" per step
- "Communication:" per step
- "Evidence:" per step
- "Halt condition|halt|stop if" (≥2 mentions)
- "gate" (>0 mentions)

**INTEGRATION POINTS**:
- "Inputs From" OR "INPUT"
- "Outputs To" OR "OUTPUT"
- `.md`, `.json`, `.yaml`, `.yml`
- `.artifacts/protocol-{ID}/`

**QUALITY GATES**:
- "### Gate 1", "### Gate 2", etc. (≥2 gates)
- "- **Criteria**:|Criteria:"
- "Pass Threshold|threshold|≥|>="
- "Prerequisite|Execution|Completion"
- "python3 scripts/" (≥2 mentions)
- "Failure Handling|on fail|if fails|fallback"

**COMMUNICATION PROTOCOLS**:
- "PHASE\s+\d|PHASE [A-Z]|PHASE COMPLETE" (≥3 mentions)
- "MASTER RAY" (≥1 mention)
- "Reply|Confirm|Choose|Select"
- "clarify|specify|provide"
- "\[RAY .*ERROR\]|ERROR|FAILED"

**AUTOMATION HOOKS**:
- `python3 scripts/` OR `bash scripts/` (≥3 commands)
- "script-registry" OR "registry"
- "ci/cd|workflow|github|runs-on|pipeline"
- "environment|docker|venv|dependencies"
- "exit", "log", "fallback|retry"

**HANDOFF CHECKLIST**:
- "- [ ]" OR "- [x]" (≥6 items)
- "Prerequisite|Workflow|Quality|Evidence|Integration|Automation" (≥3 categories)
- "validate|ensure|confirm|verify" (≥4 mentions)
- "approval|sign-off|authorization"
- "Ready for Protocol"

**EVIDENCE SUMMARY**:
- Markdown table with "|" delimiters
- "artifact" in header
- "metric|evidence|result" in header
- ≥2 table rows OR ≥3 `.artifacts/` mentions
- "Inputs From" and "Outputs To"

---

## 4. MINIMUM COUNTS REFERENCE

| Element | Minimum Count | Validator |
|---------|---------------|-----------|
| Protocol Sections | 9/9 | Identity |
| Workflow Steps | ≥2 | Workflow |
| Quality Gates | ≥2 | Gates |
| Automation Commands | ≥3 | Scripts |
| Checklist Items | ≥6 | Handoff |
| Evidence Table Rows | ≥2 | Evidence |
| Phase Transition Announcements | ≥3 | Communication |
| Halt Condition Mentions | ≥2 | Workflow |
| Evidence Mentions | ≥3 | Workflow |
| Artifact Path Mentions | ≥2 | Workflow, Evidence |
| Verification Terms | ≥4 | Handoff |
| Progress Terms | ≥3 | Communication |
| Compliance Terms | ≥2 | Gates |
| Pattern Terms | ≥2 | Reasoning |
| Decision Points | ≥3 | Reasoning |
| Criteria Terms | ≥4 | Reasoning |

---

## 5. REGEX PATTERNS REFERENCE

### Protocol Header
```regex
PROTOCOL \d+:\s*([^\n(]+)
```

### Version
```regex
v\d+\.\d+\.\d+|version:\s*\d+\.\d+\.\d+
```

### Step Numbering
```regex
###\s+STEP\s+(\d+)
```

### Gate Numbering
```regex
###\s+Gate\s+(\d+)
```

### Artifact Paths
```regex
\.artifacts/protocol-\d+/
```

### Command Patterns
```regex
(?:python3?|bash)\s+[^`\n]+
```

### Script Paths
```regex
(?:\./)?scripts/[\w\-/\.]+
```

### Checklist Items
```regex
- \[ \]|- \[x\]|- \[[^\]]\]
```

---

## 6. FILE REFERENCES

### Required Files
- `AGENTS.md` - Phase assignments for all protocols
- `scripts/script-registry.json` - Central script inventory
- `.artifacts/protocol-{ID}/` - Protocol-specific artifacts

### Optional Files
- `config/protocol_gates/{ID}.yaml` - Gate configuration (recommended)

---

## 7. PHASE ASSIGNMENTS (from AGENTS.md)

**Valid Phases**:
- Phase 0
- Phase 1-2
- Phase 3
- Phase 4
- Phase 5
- Phase 6

Each protocol ID must be listed under exactly one phase in AGENTS.md.

---

## 8. SCORING FORMULAS

### Overall Score Calculation
```
overall_score = Σ(dimension_score × dimension_weight) / Σ(dimension_weight)
```

### Status Determination
```
if overall_score >= pass_threshold: status = "pass"
elif overall_score >= warning_threshold: status = "warning"
else: status = "fail"
```

### Dimension Score (typical)
```
score = passed_checks / total_checks
```

---

## 9. COMMON VALIDATION FAILURES

### Top Issues to Avoid

1. **Missing Sections** - Ensure all 9 required sections present
2. **Non-Sequential Steps** - Steps must be 1, 2, 3... (no gaps)
3. **Insufficient Gates** - Need ≥2 quality gates
4. **Missing Evidence Tags** - Need ≥3 "evidence" mentions
5. **No Halt Conditions** - Need ≥2 halt condition mentions
6. **Missing MASTER RAY** - Need ≥1 "MASTER RAY" mention
7. **Weak Checklist** - Need ≥6 checklist items
8. **No Automation Commands** - Need ≥3 executable commands
9. **Missing Phase Transitions** - Need ≥3 phase announcements
10. **No Compliance Terms** - Need ≥2 compliance keywords

---

## 10. PROTOCOL CREATION CHECKLIST

Use this checklist when creating a new protocol:

### Identity Requirements
- [ ] Protocol number in header (PROTOCOL XX)
- [ ] Protocol name after number
- [ ] Version number (v1.0.0)
- [ ] Phase assignment in AGENTS.md
- [ ] Purpose statement (>20 chars)
- [ ] Scope definition

### Role Requirements
- [ ] "You are a..." statement
- [ ] Role description (>60 chars, >1 line)
- [ ] Domain expertise keywords
- [ ] Behavioral traits keywords
- [ ] Mission statement with "mission"
- [ ] Scope boundaries
- [ ] Success criteria
- [ ] Value proposition

### Workflow Requirements
- [ ] WORKFLOW section exists
- [ ] ≥2 steps (### STEP 1, ### STEP 2)
- [ ] Sequential numbering
- [ ] **Action:** in each step
- [ ] Communication: in each step
- [ ] Evidence: in each step
- [ ] ≥2 halt conditions
- [ ] ≥3 "evidence" mentions
- [ ] ≥2 `.artifacts/` paths

### Integration Requirements
- [ ] INTEGRATION POINTS section
- [ ] "Inputs From" specified
- [ ] "Outputs To" specified
- [ ] Data formats (.md, .json, .yaml)
- [ ] Storage locations (.artifacts/)

### Gates Requirements
- [ ] QUALITY GATES section
- [ ] ≥2 gates (### Gate 1, ### Gate 2)
- [ ] Criteria for each gate
- [ ] Pass thresholds (≥, >=)
- [ ] ≥2 script mentions
- [ ] Failure handling
- [ ] ≥2 compliance terms

### Communication Requirements
- [ ] COMMUNICATION PROTOCOLS section
- [ ] ≥3 phase transition mentions
- [ ] ≥1 "MASTER RAY" mention
- [ ] Confirmation prompts
- [ ] Clarification prompts
- [ ] Error templates
- [ ] ≥3 progress terms

### Automation Requirements
- [ ] AUTOMATION HOOKS section
- [ ] ≥3 executable commands
- [ ] Script registry reference
- [ ] CI/CD context
- [ ] Environment requirements
- [ ] Exit code handling
- [ ] Logging requirements

### Handoff Requirements
- [ ] HANDOFF CHECKLIST section
- [ ] ≥6 checklist items (- [ ])
- [ ] ≥3 categories
- [ ] ≥4 verification terms
- [ ] Approval/sign-off mention
- [ ] "Ready for Protocol" statement

### Evidence Requirements
- [ ] EVIDENCE SUMMARY section
- [ ] Markdown table with headers
- [ ] "artifact" column
- [ ] "metric/evidence/result" column
- [ ] ≥2 table rows
- [ ] Protocol directory path
- [ ] Traceability (inputs/outputs)

### Reasoning Requirements (Optional but Recommended)
- [ ] ≥2 pattern terms
- [ ] ≥2 explanation mentions (because, therefore)
- [ ] ≥3 decision points
- [ ] ≥4 criteria terms
- [ ] Root cause analysis mention

### Reflection Requirements (Optional but Recommended)
- [ ] Retrospective/review mention
- [ ] Improvement opportunities
- [ ] Version history
- [ ] Knowledge capture
- [ ] Future planning/roadmap

---

## 11. EXAMPLE SNIPPETS

### Protocol Header
```markdown
# PROTOCOL 01: Client Proposal Generation

**Version**: v1.0.0  
**Phase**: Phase 0  
**Purpose**: Generate human-sounding freelance proposals from job posts with evidence artifacts and quality gates.
```

### AI Role and Mission
```markdown
## AI ROLE AND MISSION

You are a **Proposal Generation Specialist** with expertise in freelance client engagement and persuasive writing. Your mission is to transform job post requirements into compelling, human-sounding proposals that demonstrate value while maintaining authenticity. You must operate within the boundaries of the provided job post context and never fabricate capabilities or experience.

**Success Criteria**: Proposal passes readability score ≥ 0.85 and includes all required evidence artifacts.
```

### Workflow Step
```markdown
### STEP 1: Job Post Analysis

**Action**: Parse the job post to extract key requirements, budget constraints, and client pain points.

**Communication**: `[ANALYSIS START] Parsing job post for requirements...`

**Evidence**: Save extracted requirements to `.artifacts/protocol-01/job-requirements.json`

**Halt Condition**: If job post is empty or malformed, HALT and request valid input.
```

### Quality Gate
```markdown
### Gate 1: Proposal Readability

- **Criteria**: Flesch Reading Ease score ≥ 60
- **Pass Threshold**: score ≥ 60
- **Evidence**: `.artifacts/protocol-01/readability-report.json`
- **Automation**: `python3 scripts/validate_readability.py --proposal proposal.md`
- **Failure Handling**: If score < 60, simplify language and re-run validation
```

### Integration Points
```markdown
## INTEGRATION POINTS

### Inputs From
- User: Job post text (`.txt` or `.md`)
- None (first protocol in workflow)

### Outputs To
- Protocol 02: Proposal document (`.artifacts/protocol-01/PROPOSAL.md`)
- Protocol 02: Evidence package (`.artifacts/protocol-01/PROPOSAL-EVIDENCE.zip`)

### Data Formats
- Input: `.txt`, `.md`
- Output: `.md`, `.json`, `.zip`

### Storage Locations
- `.artifacts/protocol-01/` - All protocol artifacts
```

### Communication Protocols
```markdown
## COMMUNICATION PROTOCOLS

### Status Announcements
- `[MASTER RAY | PHASE 0 START] Protocol 01 initiated`
- `[ANALYSIS COMPLETE] Job requirements extracted`
- `[GATE PASSED: Gate 1] Readability score: 0.87`
- `[PROTOCOL 01 | PHASE 0 COMPLETE] Ready for Protocol 02`

### User Interaction
- **Confirmation**: "Proposal generated. Reply 'approve' to proceed or 'revise' to make changes."
- **Clarification**: "Job post unclear. Please specify: [specific requirement]"

### Error Messaging
- `[RAY ERROR | GATE 1 FAILED] Readability score 0.52 < 0.60. Required action: Simplify language.`
```

### Handoff Checklist
```markdown
## HANDOFF CHECKLIST

### Prerequisites
- [ ] Job post validated and parsed
- [ ] Requirements extracted successfully

### Workflow
- [ ] All 3 steps completed
- [ ] Proposal generated

### Quality
- [ ] Gate 1 passed (Readability ≥ 0.60)
- [ ] Gate 2 passed (Completeness = 100%)

### Evidence
- [ ] PROPOSAL.md saved to `.artifacts/protocol-01/`
- [ ] Evidence package created
- [ ] Validation reports generated

### Integration
- [ ] Output ready for Protocol 02
- [ ] Artifacts accessible

### Automation
- [ ] All validation scripts executed successfully

**Ready for Protocol 02**: Discovery Call Initiation
```

### Evidence Summary
```markdown
## EVIDENCE SUMMARY

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
| PROPOSAL.md | `.artifacts/protocol-01/PROPOSAL.md` | Document | Readability: 0.87 |
| job-requirements.json | `.artifacts/protocol-01/job-requirements.json` | Analysis | Completeness: 100% |
| readability-report.json | `.artifacts/protocol-01/readability-report.json` | Validation | Score: 0.87 |
| PROPOSAL-EVIDENCE.zip | `.artifacts/protocol-01/PROPOSAL-EVIDENCE.zip` | Archive | Size: 45KB |
```

---

## 12. READY FOR PROTOCOL 2

This requirements specification is complete and ready to guide protocol structure generation in Protocol 2.

**Next Step**: `2-generate-protocol-structure.md`

The requirements specification provides all necessary patterns, thresholds, and examples to create protocols that pass all 10 validators with scores ≥ 0.95 (identity) and ≥ 0.90 (others).
