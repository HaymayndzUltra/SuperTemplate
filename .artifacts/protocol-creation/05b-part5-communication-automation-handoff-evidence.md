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

- `[PROTOCOL 05b | PHASE 0 START]` - Pre-Flight Validation initiated (ETA: 5 minutes)
- `[PROTOCOL 05b | PHASE 1 START]` - Input Validation & Context Loading (ETA: 10 minutes)
- `[PROTOCOL 05b | PHASE 2 START]` - Project Classification & Characteristic Detection (ETA: 15 minutes)
- `[PROTOCOL 05b | PHASE 3 START]` - Intelligent Protocol Selection & Gap Analysis (ETA: 20 minutes)
- `[PROTOCOL 05b | PHASE 4 START]` - Dynamic Protocol Creation (ETA: variable, depends on gaps)
- `[PROTOCOL 05b | PHASE 5 START]` - Dependency Graph Construction & Execution Sequencing (ETA: 10 minutes)
- `[PROTOCOL 05b | PHASE 6 START]` - Customization Analysis & Timeline Estimation (ETA: 10 minutes)
- `[PROTOCOL 05b | PHASE 7 START]` - Execution Plan Generation & Approval (ETA: 15 minutes)
- `[MILESTONE ACHIEVED]` - All foundation artifacts loaded and validated
- `[MILESTONE ACHIEVED]` - Project classification complete
- `[MILESTONE ACHIEVED]` - Protocol selection complete
- `[MILESTONE ACHIEVED]` - All gaps filled
- `[MILESTONE ACHIEVED]` - Execution sequence optimized
- `[MILESTONE ACHIEVED]` - Timeline and resource plan complete
- `[PROTOCOL 05b | PHASE 7 COMPLETE]` - Ready for handoff
- `[READY]` - Execution plan approved, ready to proceed to selected protocols

### User Interaction
<!-- REQUIRED: Confirmation (line 131), clarification (line 132), decision points (line 133), feedback (line 134) -->

- **Confirmation**: "Ready to analyze your project and create execution plan? Reply 'yes' to proceed."
- **Clarification**: "Should I interpret tech_stack entry 'TensorFlow' as indication of AI/ML project?"
- **Decision Points**: "5 MAYBE protocols identified. For each, choose: Include | Skip | Defer"
- **Feedback Requests**: "Does this protocol selection (12 REQUIRED, 8 RECOMMENDED) meet your project needs?"

### Error Messaging
<!-- REQUIRED: Templates (line 160), severity (line 161), context (line 162), resolution (line 163) -->

- `[PROTOCOL 05b | GATE 0 FAILED: Protocol 05 artifacts missing]`
- `[ERROR]` **CRITICAL**: bootstrap-manifest.json not found in workspace root or .artifacts/protocol-05/
  - **Context**: Pre-flight validation failed. Required artifact: bootstrap-manifest.json. Expected location: workspace root or .artifacts/protocol-05/. Actual: file not found.
  - **Resolution**: Complete Protocol 05 (Bootstrap Your Project) to generate bootstrap-manifest.json, then retry Protocol 05b.

- `[PROTOCOL 05b | GATE 1 FAILED: Classification confidence too low]`
- `[ERROR]` **HIGH**: Classification confidence 0.65 (threshold: 0.70)
  - **Context**: Project classification ambiguous. Detected indicators for both Web App and API/Microservice. Confidence score: 0.65. Threshold: 0.70.
  - **Resolution**: Manual review required. Provide explicit project type in PROJECT-BRIEF.md or approve classification with documented rationale.

- `[WARNING]` **MEDIUM**: Coverage 92% (target: 95%)
  - **Context**: 2 requirements not covered by selected protocols. Gap severity: HIGH (API rate limiting), MEDIUM (data backup strategy).
  - **Resolution**: Proceed to PHASE 4 to create new protocols, or accept gaps and document as limitations.

### Progress Tracking
<!-- REQUIRED: ≥3 progress terms (line 187), timeline (line 188), current activity (line 189), next steps (line 190) -->

- `[PROGRESS]` Currently parsing PROJECT-BRIEF.md - 25% complete
- `[PROGRESS]` Currently analyzing tech stack - 50% complete
- `[PROGRESS]` Currently mapping characteristics to protocols - 75% complete
- `[PROGRESS]` Currently generating execution plan - 100% complete
- `[TIMELINE]` Next: User approval for MAYBE protocols - ETA: awaiting user input
- `[TIMELINE]` Next: Dynamic protocol creation - ETA: 30-60 minutes (depends on gap count)
- `[REMAINING]` 3 phases remaining until plan complete
- `[REMAINING]` 5 MAYBE protocol decisions pending

### Evidence Communication
<!-- REQUIRED: ≥2 artifact announcements (line 215), format (line 216), location (line 217), validation (line 218) -->

- `[ARTIFACT GENERATED]` project-classification.json saved to `.artifacts/protocol-05b/project-classification.json`
- `[ARTIFACT GENERATED]` gap-analysis.json saved to `.artifacts/protocol-05b/gap-analysis.json`
- `[ARTIFACT GENERATED]` timeline-estimate.json saved to `.artifacts/protocol-05b/timeline-estimate.json`
- `[ARTIFACT GENERATED]` PROTOCOL-EXECUTION-PLAN.md saved to workspace root
- `[ARTIFACT GENERATED]` PROTOCOL-CHECKLIST.md saved to workspace root
- `[ARTIFACT GENERATED]` handoff-package.zip saved to `.artifacts/protocol-05b/handoff-package.zip`
- **Format**: JSON for evidence artifacts, Markdown for execution plan and checklist, ZIP for handoff package
- **Location**: `.artifacts/protocol-05b/` for all JSON artifacts, workspace root for plan and checklist
- **Validation**: All quality gates passed (6/6), coverage 96%, classification confidence 0.88

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

**Note**: Protocol 05b is AI-driven with no external scripts. All automation is performed by the AI during protocol execution. Evidence artifacts are generated automatically.

```bash
# Validation of new protocols (if gaps detected in STEP 4.5)
python3 validators-system/scripts/validate_all_protocols.py \
  --workspace /home/haymayndz/SuperTemplate \
  --protocol-dir AI-project-workflow \
  --protocol-id {NEW_PROTOCOL_ID}

# Checksum calculation for handoff package
sha256sum .artifacts/protocol-05b/handoff-package.zip > \
  .artifacts/protocol-05b/checksums.sha256

# Evidence manifest generation (AI-driven, no script)
# AI generates evidence-manifest.json during STEP 7
```

### Registry Alignment
<!-- REQUIRED: Registry reference (line 139), script-registry.json mention (line 140) -->

- **Script Registry**: `scripts/script-registry.json`
- **Registered Scripts**: 
  - validate_all_protocols.py - Validates new protocols against all 10 validators (owner: Validation System)
  - Note: Protocol 05b primarily uses AI-driven automation, minimal script dependencies

### Execution Context
<!-- REQUIRED: CI context (line 195), environment (line 196), scheduling (line 197), permissions (line 198) -->

- **CI/CD**: Not applicable (AI-driven protocol, runs in IDE context)
- **Environment**: Python 3.10+ for validator scripts (if new protocols created), workspace access for file I/O
- **Scheduling**: On-demand execution triggered by user (manual trigger after Protocol 05 completion)
- **Permissions**: Read access to workspace root, .cursor/, .artifacts/, AI-project-workflow/; Write access to .artifacts/protocol-05b/, workspace root (for plan files)

### Command Syntax
<!-- REQUIRED: Flags (line 229), output redirection (line 230), parameterization (line 231), documentation (line 237) -->

- **Flags**: Use `--workspace`, `--protocol-dir`, `--protocol-id` for validator scripts
- **Output Redirection**: Use `>` for checksum file generation
- **Parameterization**: Use `{NEW_PROTOCOL_ID}` for dynamic protocol validation

### Error Handling
<!-- REQUIRED: Exit codes (line 264), fallback (line 265), logging (line 266), manual paths (line 267) -->

- **Exit Codes**: 
  - `0` = Success (all gates passed, plan approved)
  - `1` = Failure (gate failed, user declined approval)
  - `2` = Warning (advisory gate failed, user can proceed with caution)
- **Fallback**: If new protocol validation fails after 5 iterations, escalate to user for manual fix or gap acceptance
- **Logging**: All evidence artifacts serve as logs, saved to `.artifacts/protocol-05b/` with timestamps
- **Manual Paths**: If classification confidence <70%, user must manually review and override classification

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
- [ ] Protocol 05 artifacts validated (bootstrap-manifest.json, architecture-principles.md)
- [ ] PROJECT-BRIEF.md validated with all required sections
- [ ] User authorization obtained and recorded

### Workflow
<!-- REQUIRED: ≥3 categories (line 101: Prerequisite|Workflow|Quality|Evidence|Integration|Automation) -->
- [ ] All 7 workflow steps completed (STEP 1-7, plus conditional STEP 4.5 if applicable)
- [ ] Project classified with confidence ≥85% or human approval
- [ ] All MAYBE protocols decided by user (Include/Skip/Defer)
- [ ] Coverage ≥95% achieved (gaps filled or accepted)
- [ ] Dependency graph constructed and validated (acyclic)
- [ ] Timeline estimated with customization modifiers applied

### Quality
- [ ] Gate 0 (Pre-Flight Validation): PASSED
- [ ] Gate 1 (Classification Confidence): PASSED (≥85% or approved)
- [ ] Gate 2 (MAYBE Protocol Decisions): PASSED (100% decisions made)
- [ ] Gate 3 (Protocol Coverage): PASSED (≥95% coverage)
- [ ] Gate 4 (New Protocol Validation): PASSED (if applicable, all new protocols ≥0.95)
- [ ] Gate 5 (Timeline Approval): PASSED (user approved)
- [ ] Gate 6 (Final Plan Approval): PASSED (user approved)

### Evidence
- [ ] 35+ JSON artifacts generated in `.artifacts/protocol-05b/`
- [ ] PROTOCOL-EXECUTION-PLAN.md generated (15-25 pages)
- [ ] PROTOCOL-CHECKLIST.md generated
- [ ] handoff-package.zip created with checksums
- [ ] evidence-manifest.json included in package

### Integration
- [ ] Next protocol identified based on project classification
- [ ] Execution plan references correct protocol sequence
- [ ] Handoff package ready for downstream protocols

### Automation
- [ ] New protocol validation completed (if gaps detected)
- [ ] Checksum calculation completed for handoff package
- [ ] All evidence artifacts timestamped and versioned

### Verification Procedures
<!-- REQUIRED: ≥4 verification terms (line 128: validate/ensure/confirm/verify/gate) -->
- [ ] Validate all 35+ JSON artifacts are well-formed and complete
- [ ] Confirm PROTOCOL-EXECUTION-PLAN.md contains all 8 required sections
- [ ] Verify handoff-package.zip integrity using checksums
- [ ] Ensure all quality gates passed with documented evidence

### Stakeholder Sign-off
<!-- REQUIRED: Approval (line 155), reviewers (line 156), evidence reference (line 157), confirmation (line 158) -->
- [ ] **Reviewer**: User/Project Owner - Approval status: Approved
- [ ] **Evidence Package**: `.artifacts/protocol-05b/handoff-package.zip` - Status: Complete
- [ ] **Confirmation**: User approval recorded in `.artifacts/protocol-05b/approval-record.json` with timestamp

### Documentation Requirements
<!-- REQUIRED: ≥3 doc terms (line 184: log/brief/notes/transcript/manifest/report) -->
- [ ] Execution plan (PROTOCOL-EXECUTION-PLAN.md) saved to workspace root
- [ ] Checklist (PROTOCOL-CHECKLIST.md) saved to workspace root
- [ ] Evidence manifest (evidence-manifest.json) included in handoff package
- [ ] Classification reasoning (classification-reasoning.md) documented
- [ ] Format: Markdown for plans, JSON for evidence, ZIP for package
- [ ] Reviewer docs: PROTOCOL-EXECUTION-PLAN.md serves as comprehensive review document

### Next Protocol Alignment
<!-- REQUIRED: Ready statements (line 211), next commands (line 212), dependencies (line 213), continuation (line 214) -->
- [ ] **Ready for Variable Protocol**: Next protocol determined by project classification (Generic 06, AI 06, or Hybrid sequence)
- [ ] **Next Command**: `@apply` command for selected protocol (e.g., `@apply .cursor/ai-driven-workflow/06-create-prd.md` or `@apply AI-project-workflow/06-ai-use-case-definition.md`)
- [ ] **Dependencies**: PROTOCOL-EXECUTION-PLAN.md and PROTOCOL-CHECKLIST.md available in workspace root, handoff-package.zip in `.artifacts/protocol-05b/`
- [ ] **Continuation Script**: Not applicable (next protocol determined dynamically, no fixed continuation)

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
| PROTOCOL-EXECUTION-PLAN.md | Workspace root | Execution Plan | Completeness: 100%, Pages: 15-25 |
| PROTOCOL-CHECKLIST.md | Workspace root | Checklist | Protocol count: 20, Total effort: 336 hours |
| project-classification.json | `.artifacts/protocol-05b/` | Classification | Confidence: 0.88, Type: Hybrid |
| characteristics-detection.json | `.artifacts/protocol-05b/` | Analysis | Characteristics: 18/27 detected |
| protocol-selection.json | `.artifacts/protocol-05b/` | Selection | REQUIRED: 12, RECOMMENDED: 8, MAYBE: 5, SKIP: 15 |
| gap-analysis.json | `.artifacts/protocol-05b/` | Gap Analysis | Coverage: 96%, Gaps filled: 2 |
| coverage-report.json | `.artifacts/protocol-05b/` | Coverage | Before: 92%, After: 96% |
| dependency-graph.json | `.artifacts/protocol-05b/` | Dependency | Nodes: 20, Edges: 35, Acyclic: true |
| execution-sequence.json | `.artifacts/protocol-05b/` | Sequence | Phases: 8, Parallel opportunities: 3 |
| timeline-estimate.json | `.artifacts/protocol-05b/` | Timeline | Sequential: 42 days, Realistic: 43 days |
| handoff-package.zip | `.artifacts/protocol-05b/` | Archive | Artifacts: 35+, Size: ~2MB, Checksum: SHA-256 |
| approval-record.json | `.artifacts/protocol-05b/` | Approval | Gates passed: 6/6, User approval: yes, Timestamp: ISO-8601 |

### Storage Structure
<!-- REQUIRED: Protocol directory (line 139), subdirectories (line 140), permissions (line 141), naming (line 142) -->

- **Protocol Directory**: `.artifacts/protocol-05b/`
- **Subdirectories**: 
  - `new-protocols/` for dynamically created protocols (if gaps detected)
  - Root level for all 35+ JSON evidence artifacts
- **Permissions**: Read/Write for AI during execution, Read-only for downstream protocols
- **Naming Convention**: `{artifact-type}-{timestamp}.json` for timestamped artifacts, `{artifact-type}.json` for latest version

### Manifest
<!-- OPTIONAL: Manifest reference (line 167), metadata (line 163), dependencies (line 164), coverage (line 165) -->

- **Manifest File**: `.artifacts/protocol-05b/evidence-manifest.json`
- **Metadata**: Timestamp (ISO-8601), size (bytes), hash (SHA-256) for each artifact
- **Dependencies**: Input artifacts from Protocols 03, 04, 05; Output artifacts to variable downstream protocols
- **Coverage**: 100% (all required artifacts generated)

### Traceability
<!-- REQUIRED: Inputs (line 214), outputs (line 215), transformations (line 216), audit trail (line 217) -->

- **Inputs From**: 
  - Protocol 03 → PROJECT-BRIEF.md
  - Protocol 04 → .cursor/context/ directory
  - Protocol 05 → bootstrap-manifest.json, architecture-principles.md
- **Outputs To**: 
  - Variable (Generic/AI/Hybrid) → PROTOCOL-EXECUTION-PLAN.md, PROTOCOL-CHECKLIST.md
  - All Downstream → handoff-package.zip
- **Transformations**: Parse foundation artifacts → Classify project → Select protocols → Analyze gaps → Create new protocols (if needed) → Sequence execution → Estimate timeline → Generate plan
- **Audit Trail**: `.artifacts/protocol-05b/approval-record.json` with all gate results and user approvals

### Archival
<!-- OPTIONAL: Compression (line 249), retention (line 250), retrieval (line 251), cleanup (line 252) -->

- **Compression**: ZIP format (handoff-package.zip) containing all 35+ JSON artifacts
- **Retention**: 90 days after project completion (or per organizational policy)
- **Retrieval**: Extract handoff-package.zip, verify checksums, access individual JSON artifacts
- **Cleanup**: After 90 days, archive to cold storage or delete per data retention policy

---

**PROTOCOL 05b COMPLETE** ✅

This protocol successfully orchestrates the transition from foundation to execution phases, ensuring optimal protocol selection and complete requirement coverage through intelligent analysis and dynamic protocol creation.
