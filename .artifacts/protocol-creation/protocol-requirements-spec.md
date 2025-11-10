# PROTOCOL REQUIREMENTS SPECIFICATION

**Generated:** 2025-01-09  
**Status:** Complete - All 10 validators analyzed  
**Coverage:** 100/100+ validation checks extracted

---

## 1. REQUIRED SECTIONS (9 Total)

Every protocol MUST contain these 9 sections in this order:

1. **PREREQUISITES** - Required artifacts, approvals, system state
2. **AI ROLE AND MISSION** - Role definition, mission, constraints, success criteria
3. **WORKFLOW** - Sequential steps with actions, evidence tracking, halt conditions
4. **INTEGRATION POINTS** - Inputs from, outputs to, data formats, storage locations
5. **QUALITY GATES** - Gate definitions, pass criteria, automation, failure handling
6. **COMMUNICATION PROTOCOLS** - Status announcements, user interaction, error messaging
7. **AUTOMATION HOOKS** - Script inventory, registry alignment, execution context
8. **HANDOFF CHECKLIST** - Verification procedures, stakeholder sign-off, next protocol alignment
9. **EVIDENCE SUMMARY** - Artifact generation table, storage structure, traceability

---

## 2. SECTION REQUIREMENTS BY VALIDATOR

### 2.1 PREREQUISITES (Identity Validator)

**Required Categories:**
- **Required Artifacts** - List of input files/data needed
- **Required Approvals** - Who must sign off before starting
- **System State** - Environment, dependencies, prerequisites

**Validation Criteria:**
- All 3 categories present (score: 3/3)
- Each category has descriptive content
- Pass threshold: 0.95 | Warning: 0.80

---

### 2.2 AI ROLE AND MISSION (Role Validator)

**Required Elements:**

| Element | Pattern | Required | Weight |
|---------|---------|----------|--------|
| Role Title | "You are a..." or "You are an..." | YES | 0.25 |
| Role Description | >60 characters, >1 line | YES | 0.25 |
| Domain Expertise | Keywords: domain, expertise, industry, capability | YES | 0.20 |
| Behavioral Traits | Keywords: empathy, strategy, rigor, evidence, governance | YES | 0.15 |
| Mission Clarity | "mission" keyword present | YES | 0.15 |
| Scope Boundaries | Keywords: within, only, do not, boundaries, scope | YES | 0.15 |
| Success Criteria | Keywords: success, complete, validation, evidence | YES | 0.15 |
| Value Proposition | Keywords: client, value, impact, benefit, outcome | YES | 0.15 |

**Validation Criteria:**
- All 8 elements present
- Pass threshold: 0.90 | Warning: 0.80

---

### 2.3 WORKFLOW (Workflow Validator)

**Required Structure:**

| Requirement | Pattern | Minimum | Weight |
|-------------|---------|---------|--------|
| Step Headings | "### STEP 1", "### STEP 2", etc. | 2 steps | 0.20 |
| Sequential Numbering | Steps numbered 1, 2, 3... | Sequential | 0.20 |
| Action Definitions | "**Action:**" per step | 50% of steps | 0.25 |
| Evidence Tracking | "Evidence:" mentions | ≥3 mentions | 0.20 |
| Halt Conditions | "Halt condition" or "stop if" | ≥2 mentions | 0.20 |
| Validation Gates | "gate" keyword | ≥1 mention | 0.20 |
| User Confirmation | "confirm" or "approval" | ≥1 mention | 0.20 |

**Action Markers (Required):**
- `[MUST]` or `[CRITICAL]` for mandatory actions
- `[GUIDELINE]` for recommended actions
- `[OPTIONAL]` for optional guidance

**Validation Criteria:**
- All structure elements present
- Pass threshold: 0.90 | Warning: 0.80

---

### 2.4 INTEGRATION POINTS (Identity Validator)

**Required Elements:**

| Element | Pattern | Required |
|---------|---------|----------|
| Input Sources | "Inputs From" or "INPUT" | YES |
| Output Destinations | "Outputs To" or "OUTPUT" | YES |
| Data Formats | .md, .json, .yaml, .yml | YES |
| Storage Locations | ".artifacts" or "Storage" | YES |

**Format Specification:**
- Markdown (.md) for documentation
- JSON (.json) for structured data
- YAML (.yaml/.yml) for configuration

**Storage Pattern:**
- `.artifacts/protocol-XX/` for protocol-specific artifacts
- Subdirectories for organization
- Clear naming conventions

**Validation Criteria:**
- All 4 elements documented
- Pass threshold: 0.95 | Warning: 0.80

---

### 2.5 QUALITY GATES (Gates Validator)

**Gate Definition Requirements:**

| Requirement | Pattern | Minimum | Weight |
|-------------|---------|---------|--------|
| Gate Count | "### Gate 1", "### Gate 2" | 2 gates | 0.25 |
| Gate Descriptions | "- **Criteria**:" or "Criteria:" | ≥2 gates | 0.25 |
| Gate Types | Prerequisite/Execution/Completion | ≥1 type | 0.25 |
| Pass Thresholds | "≥" or ">=" with numeric value | ≥2 thresholds | 0.25 |

**Pass Criteria Requirements:**

| Criterion | Pattern | Minimum | Weight |
|-----------|---------|---------|--------|
| Boolean Checks | "status", "pass", "fail" | ≥2 mentions | 0.25 |
| Metrics | "score", "confidence", "rate", "percentage" | ≥3 mentions | 0.25 |
| Evidence Links | "evidence" keyword | ≥3 mentions | 0.25 |
| Numeric Thresholds | "≥", ">=", numeric values | ≥2 thresholds | 0.25 |

**Failure Handling Requirements:**

| Element | Pattern | Required |
|---------|---------|----------|
| Failure Actions | "Failure Handling" or "on fail" | ≥2 mentions |
| Rollback Steps | "rollback", "remediation", "re-run" | ≥1 mention |
| Notifications | "notify", "alert", "escalate" | ≥1 mention |
| Waiver Policies | "waiver", "override" | ≥1 mention |

**Compliance Integration:**

| Element | Pattern | Minimum |
|---------|---------|---------|
| Compliance Terms | HIPAA, SOC2, GDPR, ISO, PCI, FedRAMP, security, regulatory | ≥2 terms |
| Automation Hooks | "check", "validate", "enforce", "audit" | ≥2 terms |
| Evidence | "report" keyword | ≥1 mention |
| Governance | "governance" or "policy" | ≥1 mention |

**Validation Criteria:**
- All gate definitions present
- Pass threshold: 0.92 | Warning: 0.85

---

### 2.6 COMMUNICATION PROTOCOLS (Communication Validator)

**Status Announcements:**

| Announcement Type | Pattern | Minimum |
|------------------|---------|---------|
| Phase Transitions | "PHASE", "PHASE COMPLETE" | ≥3 mentions |
| Branded Announcements | "MASTER RAY" | ≥1 mention |
| Completion Callouts | "COMPLETE", "READY" | ≥1 mention |
| Time Estimates | "ETA", "duration", "time" | ≥1 mention |

**User Interaction Prompts:**

| Prompt Type | Pattern | Required |
|-------------|---------|----------|
| Confirmation | "Reply", "Confirm", "Choose", "Select" | YES |
| Clarification | "clarify", "specify", "provide" | YES |
| Decision Points | "option", "choose", "decision" | YES |
| Feedback Requests | "feedback", "review", "does this" | YES |

**Error Messaging:**

| Component | Pattern | Required |
|-----------|---------|----------|
| Error Templates | "[RAY ... ERROR]", "ERROR", "FAILED" | YES |
| Severity Levels | "CRITICAL", "HIGH", "WARNING" | YES |
| Context Information | "Details", "Criteria", "Actual" | YES |
| Resolution Steps | "Required action", "Resolve", "Fix", "remediation" | YES |

**Progress Tracking:**

| Element | Pattern | Minimum |
|---------|---------|---------|
| Progress Terms | "progress", "percent", "%", "complete", "remaining", "current activity", "next steps" | ≥3 terms |
| Timeline Mentions | "timeline", "schedule", "next" | ≥1 mention |
| Current Activity | "currently" or "now" | YES |
| Next Steps | "next" keyword | YES |

**Evidence Communication:**

| Element | Pattern | Minimum |
|---------|---------|---------|
| Artifact Announcements | ".artifacts/" mentions | ≥2 mentions |
| Format Specification | "markdown", "json", "yaml", "manifest" | ≥1 mention |
| Location Information | "stored in", "location", "repository" | ≥1 mention |
| Validation Status | "validation", "status", "pass" | ≥1 mention |

**Validation Criteria:**
- All 5 communication dimensions present
- Pass threshold: 0.90 | Warning: 0.80

---

### 2.7 AUTOMATION HOOKS (Scripts Validator)

**Script Inventory:**

| Requirement | Pattern | Minimum | Weight |
|-------------|---------|---------|--------|
| Command Count | `python3 scripts/...` or `bash ...` | ≥3 commands | 0.25 |
| Script Paths | `scripts/[category]/[script].py` | Documented | 0.25 |
| Missing Scripts | All referenced scripts exist | 0% missing | 0.25 |
| Command Documentation | Code blocks with ``` | YES | 0.25 |

**Registry Alignment:**

| Requirement | Pattern | Required | Weight |
|-------------|---------|----------|--------|
| Registry Reference | "script-registry", "registry", "register" | YES | 0.20 |
| Registry File | `scripts/script-registry.json` exists | YES | 0.20 |
| Cross-Links | `scripts/` mentions in workflow | ≥50% of commands | 0.20 |
| Ownership | "owner", "responsible", "team" | YES | 0.20 |
| Registration Ratio | Commands registered in registry | ≥80% | 0.20 |

**Execution Context:**

| Context | Pattern | Required |
|---------|---------|----------|
| CI/CD Context | "CI/CD", "workflow", "github", "runs-on", "pipeline" | YES |
| Environment | "environment", "docker", "venv", "dependencies", "requirements" | YES |
| Scheduling | "cron", "schedule", "trigger", "event" | OPTIONAL |
| Permissions | "permission", "token", "secrets", "access" | YES |

**Command Syntax:**

| Requirement | Pattern | Minimum |
|-------------|---------|---------|
| Flag Usage | "--" flags in commands | ≥33% of commands |
| Output Redirection | ">", "|", "&&" operators | ≥1 command |
| Parameterization | "{}", "$(" variables | ≥1 command |
| Documentation | Code blocks with ``` | YES |

**Error Handling:**

| Element | Pattern | Required |
|---------|---------|----------|
| Exit Codes | "exit" keyword | YES |
| Fallback/Retry | "fallback", "retry" | OPTIONAL |
| Logging | "log" keyword | ≥2 mentions |
| Manual Paths | "manual" keyword | YES |

**Validation Criteria:**
- All dimensions present
- Pass threshold: 0.90 | Warning: 0.80

---

### 2.8 HANDOFF CHECKLIST (Handoff Validator)

**Checklist Completeness:**

| Requirement | Pattern | Minimum | Weight |
|-------------|---------|---------|--------|
| Checklist Items | "- [ ]", "- [x]", "- [✓]" | ≥6 items | 0.30 |
| Categories | Prerequisite, Workflow, Quality, Evidence, Integration, Automation | ≥3 categories | 0.30 |
| Dependencies | "before", "after", "next" | ≥1 mention | 0.30 |
| Status Markers | "[x]", "[✓]" in items | ≥1 marker | 0.30 |

**Verification Procedures:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Verification Terms | "validate", "ensure", "confirm", "verify", "gate" | ≥4 mentions | 0.20 |
| QA Involvement | "QA", "quality", "review" | ≥1 mention | 0.20 |
| Automation Reference | "automation", "script", "command" | ≥1 mention | 0.20 |
| Evidence Reference | "evidence" keyword | ≥2 mentions | 0.20 |

**Stakeholder Sign-Off:**

| Element | Pattern | Required | Weight |
|---------|---------|----------|--------|
| Approvals | "approval", "sign-off", "authorization" | YES | 0.20 |
| Reviewers | "reviewer", "lead", "stakeholder" | YES | 0.20 |
| Evidence Reference | "evidence", "package", "manifest" | YES | 0.20 |
| Confirmation | "confirm", "acknowledge" | YES | 0.20 |

**Documentation Requirements:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Doc Terms | "log", "brief", "notes", "transcript", "manifest", "report" | ≥3 terms | 0.15 |
| Storage | "stored", "save", "archive" | ≥1 mention | 0.15 |
| Reviewer Docs | "reviewer", "handoff", "summary" | ≥1 mention | 0.15 |
| Format | ".md", ".json", ".yaml" | ≥1 format | 0.15 |

**Next Protocol Alignment:**

| Element | Pattern | Required | Weight |
|---------|---------|----------|--------|
| Ready Statements | "Ready for Protocol" | YES | 0.15 |
| Next Commands | "@apply", "run", "trigger" | YES | 0.15 |
| Dependencies | "requires", "after", "before" | YES | 0.15 |
| Continuation Scripts | "generate_session_continuation", "continuation" | OPTIONAL | 0.15 |

**Validation Criteria:**
- All 5 dimensions present
- Pass threshold: 0.90 | Warning: 0.80

---

### 2.9 EVIDENCE SUMMARY (Evidence Validator)

**Artifact Generation:**

| Requirement | Pattern | Minimum | Weight |
|-------------|---------|---------|--------|
| Table Present | Markdown table with \| | YES | 0.30 |
| Artifact Column | "artifact" in header | YES | 0.30 |
| Metrics Column | "metric", "evidence", "result" in header | YES | 0.30 |
| Row Coverage | Table rows or .artifacts/ mentions | ≥2 rows OR ≥3 mentions | 0.30 |

**Storage Structure:**

| Requirement | Pattern | Minimum | Weight |
|-------------|---------|---------|--------|
| Protocol Directory | ".artifacts/protocol-XX/" | ≥1 directory | 0.20 |
| Subdirectories | Nested directory structure | ≥1 subdir | 0.20 |
| Permissions | "read", "write", "access" | ≥1 mention | 0.20 |
| Naming Convention | "naming", "convention", "structure" | ≥1 mention | 0.20 |

**Manifest Completeness:**

| Requirement | Pattern | Minimum |
|-------------|---------|---------|
| Manifest Reference | "manifest", "inventory", "index" | OPTIONAL |
| Metadata | "timestamp", "size", "hash", "checksum" | ≥1 mention |
| Dependencies | "dependency", "input", "output" | ≥1 mention |
| Coverage | "100%", "complete" | ≥1 mention |

**Traceability:**

| Element | Pattern | Required |
|---------|---------|----------|
| Inputs | "Inputs From" | YES |
| Outputs | "Outputs To" | YES |
| Transformations | "transform", "derive", "generate" | YES |
| Audit Trail | "audit", "log", "history" | YES |

**Archival Strategy:**

| Element | Pattern | Required |
|---------|---------|----------|
| Compression | "zip", "archive", "compress" | OPTIONAL |
| Retention | "retention", "retain", "30 days", "90 days" | OPTIONAL |
| Retrieval | "retrieve", "access", "restore" | OPTIONAL |
| Cleanup | "cleanup", "delete", "purge" | OPTIONAL |

**Validation Criteria:**
- All 5 dimensions present
- Pass threshold: 0.90 | Warning: 0.80

---

### 2.10 WORKFLOW REASONING (Reasoning Validator)

**Reasoning Patterns:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Pattern Terms | "pattern", "heuristic", "strategy", "playbook", "framework" | ≥2 terms | 0.25 |
| Explanations | "because", "so that", "therefore", "why" | ≥2 mentions | 0.25 |
| Improvement | "improve", "refine", "adjust" | ≥1 mention | 0.25 |
| Examples | "example" keyword | ≥1 mention | 0.25 |

**Decision Trees:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Decision Points | "decision", "option", "choose", "select", "branch" | ≥3 mentions | 0.25 |
| Criteria | "criteria", "if", "when", "threshold" | ≥4 mentions | 0.25 |
| Outcomes | "outcome", "result", "path" | ≥2 mentions | 0.25 |
| Logging | "log", "record", "document" | ≥2 mentions | 0.25 |

**Problem-Solving Logic:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Problem Identification | "issue", "problem", "risk", "blocker" | ≥3 mentions | 0.20 |
| Root Cause Analysis | "root cause", "analysis", "diagnose" | ≥1 mention | 0.20 |
| Solutions | "mitigate", "resolve", "fix" | ≥2 mentions | 0.20 |
| Validation | "validate", "confirm", "re-run", "test" | ≥2 mentions | 0.20 |

**Learning Mechanisms:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Feedback | "feedback", "lessons", "retro", "retrospective", "continuous" | ≥1 mention | 0.15 |
| Improvement Tracking | "improvement", "enhancement", "refine" | ≥1 mention | 0.15 |
| Knowledge Base | "knowledge", "catalog", "library", "index" | ≥1 mention | 0.15 |
| Adaptation | "adapt", "update", "evolve" | ≥1 mention | 0.15 |

**Meta-Cognition:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Self-Awareness | "aware", "limitations", "capacity" | ≥1 mention | 0.15 |
| Monitoring | "monitor", "track", "inspect" | ≥1 mention | 0.15 |
| Correction | "correct", "adjust", "calibrate" | ≥1 mention | 0.15 |
| Improvement | "improve", "mature", "evolve" | ≥1 mention | 0.15 |

**Validation Criteria:**
- All 5 reasoning dimensions present
- Pass threshold: 0.85 | Warning: 0.70

---

### 2.11 REFLECTION & EVOLUTION (Reflection Validator)

**Retrospective Analysis:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Review Terms | "retrospective", "review", "analysis", "postmortem" | ≥1 mention | 0.30 |
| Performance | "performance", "metric", "score" | ≥1 mention | 0.30 |
| Issues | "issue", "problem", "risk" | ≥1 mention | 0.30 |
| Success | "success", "win", "effective" | ≥1 mention | 0.30 |

**Continuous Improvement:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Opportunities | "improvement", "optimize", "enhance" | ≥1 mention | 0.25 |
| Plans | "plan", "roadmap", "task" | ≥1 mention | 0.25 |
| Tracking | "track", "monitor", "measure" | ≥1 mention | 0.25 |
| Evidence | "evidence", "proof", "report" | ≥1 mention | 0.25 |

**System Evolution:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Version History | "version", "v\d+\.\d+\.\d+" | ≥1 mention | 0.20 |
| Rationale | "rationale", "because", "why" | ≥1 mention | 0.20 |
| Impact | "impact", "effect", "change" | ≥1 mention | 0.20 |
| Rollback | "rollback", "revert", "undo" | OPTIONAL | 0.20 |

**Knowledge Capture:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Lessons | "lessons", "best practice", "anti-pattern" | ≥1 mention | 0.15 |
| Knowledge Base | "knowledge", "wiki", "repository", "catalog" | ≥1 mention | 0.15 |
| Storage | "store", "archive", "record" | ≥1 mention | 0.15 |
| Sharing | "share", "broadcast", "publish" | ≥1 mention | 0.15 |

**Future Planning:**

| Element | Pattern | Minimum | Weight |
|---------|---------|---------|--------|
| Roadmap | "roadmap", "future", "next phase", "upcoming" | ≥1 mention | 0.10 |
| Priorities | "priority", "prioritize" | ≥1 mention | 0.10 |
| Resources | "resource", "budget", "team" | ≥1 mention | 0.10 |
| Timeline | "timeline", "schedule", "when" | ≥1 mention | 0.10 |

**Validation Criteria:**
- All 5 reflection dimensions present
- Pass threshold: 0.85 | Warning: 0.70

---

## 3. VALIDATION CRITERIA SUMMARY

### Pass/Warning/Fail Thresholds by Validator

| Validator | Pass Threshold | Warning Threshold | Fail Below |
|-----------|----------------|-------------------|------------|
| Identity | 0.95 | 0.80 | <0.80 |
| Role | 0.90 | 0.80 | <0.80 |
| Workflow | 0.90 | 0.80 | <0.80 |
| Gates | 0.92 | 0.85 | <0.85 |
| Scripts | 0.90 | 0.80 | <0.80 |
| Communication | 0.90 | 0.80 | <0.80 |
| Evidence | 0.90 | 0.80 | <0.80 |
| Handoff | 0.90 | 0.80 | <0.80 |
| Reasoning | 0.85 | 0.70 | <0.70 |
| Reflection | 0.85 | 0.70 | <0.70 |

**Overall Protocol Pass:** Average score ≥ 0.90 across all 10 validators

---

## 4. CONTENT PATTERNS & KEYWORDS

### Required Keywords by Section

**PREREQUISITES:**
- "Required Artifacts", "Required Approvals", "System State"

**AI ROLE AND MISSION:**
- "You are a", "mission", "success", "scope", "value"

**WORKFLOW:**
- "STEP", "Action", "Evidence", "Halt condition", "gate"

**INTEGRATION POINTS:**
- "Inputs From", "Outputs To", ".artifacts/", "format"

**QUALITY GATES:**
- "Gate", "Criteria", "Pass Threshold", "≥", "evidence"

**COMMUNICATION PROTOCOLS:**
- "Status", "Announce", "Confirm", "Error", "progress"

**AUTOMATION HOOKS:**
- "python3", "bash", "scripts/", "registry", "CI/CD"

**HANDOFF CHECKLIST:**
- "[ ]", "Verify", "Approval", "Ready for Protocol"

**EVIDENCE SUMMARY:**
- "|", "artifact", "metric", ".artifacts/", "manifest"

---

## 5. CONFLICT RESOLUTION MATRIX

### Known Conflicts & Resolutions

| Conflict | Validator A | Validator B | Resolution |
|----------|-------------|-------------|------------|
| Gate Count | Gates: ≥2 | Workflow: ≥3 steps | Use HIGHEST: ≥3 |
| Evidence Mentions | Evidence: ≥3 | Workflow: ≥3 | Use BOTH: ≥3 each |
| Script Count | Scripts: ≥3 | Automation: ≥2 | Use HIGHEST: ≥3 |
| Threshold Format | Gates: "≥" | Scripts: ">" | Use BOTH: Accept either |

---

## 6. QUALITY GATES (Protocol 1 Validation)

### Gate 1: Validator Coverage
- **Criteria:** All 10 validators analyzed
- **Pass Threshold:** 10/10 validators covered
- **Evidence:** Validator list with extraction status

### Gate 2: Requirements Completeness
- **Criteria:** All 9 required sections have requirements
- **Pass Threshold:** 9/9 sections documented
- **Evidence:** Requirements spec completeness check

### Gate 3: Validation Criteria Extraction
- **Criteria:** Pass/warning/fail thresholds extracted for each validator
- **Pass Threshold:** 100% of validators have thresholds documented
- **Evidence:** Thresholds table in spec

---

## 7. NEXT STEPS

This requirements specification is **COMPLETE** and ready for:

1. **Protocol 2: Generate Protocol Structure** - Uses this spec to create template
2. **Protocol 3: Create Protocol Content** - Fills template with domain-specific content
3. **Validator Execution** - Validates protocols against these requirements

**Ready for Protocol 2 execution.**

