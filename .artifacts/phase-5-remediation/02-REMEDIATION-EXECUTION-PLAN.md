# Phase 5 Remediation - Execution Plan

## Objectives
1. Eliminate FAIL status in 8 remaining dimensions (scripts, handoff, gates, evidence, communication, role, workflow, identity)
2. Achieve master validator PASS for all 23 protocols
3. Target average score ≥ 0.90 across all dimensions

---

## Workstream Breakdown

### R1: Handoff & Communication Uplift (Phase 5A)
**Target Dimensions:** protocol_handoff (22 FAIL), protocol_communication (14 FAIL)  
**Total Protocols Affected:** 36

**Tasks:**
1. Add sign-off guidance to all HANDOFF CHECKLIST sections
   - Approvals section (who approves, evidence required)
   - Reviewers section (who reviews, review criteria)
   - Confirmation requirements
2. Add documentation expectations to HANDOFF CHECKLIST
   - Format specifications
   - Storage locations
   - Reviewer documentation requirements
3. Add "Ready-for-next-protocol" statements
   - Next protocol command
   - Dependencies checklist
   - Readiness confirmation
4. Add status markers to checklist items (✅/❌/⚠️)
5. Add communication prompts to all protocols
   - Status announcements (phase mentions, branded messages)
   - User interaction prompts (confirmation, clarification, decision points)
   - Error message templates (severity, context, resolution)
   - Progress tracking terms (timeline, milestones, evidence)

**Acceptance Criteria:**
- [ ] Handoff validator: 0 FAIL protocols
- [ ] Communication validator: 0 FAIL protocols
- [ ] Average scores ≥ 0.90 for both validators
- [ ] All protocols show PASS status for these dimensions

**Evidence:**
- Validation JSON files: `.artifacts/validation/protocol_handoff-summary.json`
- Validation JSON files: `.artifacts/validation/protocol_communication-summary.json`
- Updated protocol files with enhanced sections

---

### R2: Evidence & Quality Gates Uplift (Phase 5B)
**Target Dimensions:** protocol_evidence (20 FAIL), protocol_quality_gates (20 FAIL)  
**Total Protocols Affected:** 40

**Tasks:**
1. Add EVIDENCE SUMMARY sections to all protocols (if missing)
2. Add artifact generation table
   - Artifact name column
   - Metrics column
   - Location column
   - Row coverage for all workflow steps
3. Document storage structure
   - Protocol directories (`.artifacts/protocol-XX/`)
   - Subdirectories per artifact type
   - Permissions and naming conventions
4. Add manifest completeness
   - Manifest file references
   - Metadata requirements
   - Dependency tracking
5. Add traceability documentation
   - Input/output mentions
   - Transformation steps
   - Audit trail requirements
6. Add archival strategy
   - Compression guidelines
   - Retention policies
   - Retrieval procedures
7. Enhance QUALITY GATES sections
   - Pass criteria definitions (thresholds, boolean checks, metrics)
   - Evidence links (link gates to evidence artifacts)
   - Automation hooks (script mentions, CI integration)
   - Failure handling (rollback, notification, waiver)

**Acceptance Criteria:**
- [ ] Evidence validator: 0 FAIL protocols
- [ ] Quality gates validator: 0 FAIL protocols
- [ ] Average scores ≥ 0.90 for both validators
- [ ] All protocols show PASS status for these dimensions

**Evidence:**
- Validation JSON files: `.artifacts/validation/protocol_evidence-summary.json`
- Validation JSON files: `.artifacts/validation/protocol_gates-summary.json`
- Updated protocol files with structured evidence and gates sections

---

### R3: Scripts & Workflow Uplift (Phase 5C)
**Target Dimensions:** protocol_scripts (22 FAIL), protocol_workflow (12 FAIL)  
**Total Protocols Affected:** 34

**Tasks:**
1. **Script Inventory Audit:**
   - List all script references in protocols
   - Verify script paths exist
   - Create missing scripts OR update protocol references
   - Document execution context (CI, environment, scheduling, permissions)
2. **Script Registry Alignment:**
   - Register all scripts in `scripts/script-registry.json`
   - Cross-link registry entries to protocol references
   - Document ownership and purpose
   - Ensure registration ratio ≥ 0.80
3. **Command Syntax Enhancement:**
   - Fix flag usage (consistent flags, proper ordering)
   - Add output redirection (where needed)
   - Document parameterization
   - Add usage documentation
4. **Error Handling Enhancement:**
   - Document exit codes
   - Add fallback procedures
   - Add logging requirements
   - Document manual paths (if automation fails)
5. **Workflow Structure Enhancement:**
   - Ensure step headings with sequential numbering (Step 1, Step 2, etc.)
   - Add action markers (imperative verbs, clarity, contextual support)
   - Add halt conditions (mentions, gates, rollback, user confirmation)
   - Enhance evidence tracking (tags, artifact locations, manifest, downstream trace)

**Acceptance Criteria:**
- [ ] Scripts validator: 0 FAIL protocols
- [ ] Workflow validator: 0 FAIL protocols
- [ ] Average scores ≥ 0.90 for both validators
- [ ] All scripts referenced exist or references updated
- [ ] All protocols show PASS status for these dimensions

**Evidence:**
- Validation JSON files: `.artifacts/validation/protocol_scripts-summary.json`
- Validation JSON files: `.artifacts/validation/protocol_workflow-summary.json`
- Updated script-registry.json
- Updated protocol files with enhanced automation and workflow sections

---

### R4: Identity & Role Uplift (Phase 5D)
**Target Dimensions:** protocol_identity (5 FAIL), protocol_role (12 FAIL)  
**Total Protocols Affected:** 17

**Tasks:**
1. **Identity Enhancement:**
   - Add prerequisites section (required artifacts, approvals, system state)
   - Document integration points (input/output sources, data formats, storage locations)
   - Add compliance standards (industry standards, security, regulatory requirements)
   - Enhance documentation quality (required sections present, clear structure)
2. **Role Enhancement:**
   - Clarify role definition (title, description, domain expertise, behavioral traits)
   - Strengthen mission statement (clarity, scope, success criteria, value proposition)
   - Add constraints/guidelines (guardrails, boundaries, workflow alignment, optional guidance)
   - Enhance output expectations (format, structure, location, validation)
   - Add behavioral guidance (communication style, decision-making, error handling, user interaction)

**Acceptance Criteria:**
- [ ] Identity validator: 0 FAIL protocols
- [ ] Role validator: 0 FAIL protocols
- [ ] Average scores ≥ 0.90 for both validators
- [ ] All protocols show PASS status for these dimensions

**Evidence:**
- Validation JSON files: `.artifacts/validation/protocol_identity-summary.json`
- Validation JSON files: `.artifacts/validation/protocol_role-summary.json`
- Updated protocol files with enhanced identity and role sections

---

## Execution Sequence

1. **R1 First** (Handoff + Communication) - Quick wins, builds momentum
2. **R2 Second** (Evidence + Gates) - Foundation for automation
3. **R3 Third** (Scripts + Workflow) - Depends on R2 (gates needed for automation)
4. **R4 Last** (Identity + Role) - Final polish, foundational clarity

---

## Dependencies

- R2 (Evidence) → R3 (Scripts): Evidence artifacts needed for script validation
- R2 (Gates) → R3 (Workflow): Gates needed for workflow halt conditions
- R1 (Communication) → R3 (Workflow): Communication prompts needed in workflow steps

---

## Communication Cadence

- **Per Workstream:** Validation run after completion, update tracker
- **Final:** Master validator run, generate uplift summary

---

## Rollback Strategy

- All protocol files backed up before modification
- Batch remediation allows rollback per workstream
- Validation tracker shows pre/post scores for comparison

---

*Generated: 2025-11-06*  
*Phase 5 Execution Plan*

