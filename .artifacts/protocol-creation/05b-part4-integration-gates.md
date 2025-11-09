## INTEGRATION POINTS

<!-- VALIDATOR MAPPING:
  Primary: Identity Validator (validate_protocol_identity.py)
  Dimensions: integration_points (line 265, weight 0.2)
  Pass Threshold: 0.95
  Required: Input sources (line 285), output destinations (line 293), data formats (line 301), storage locations (line 310)
-->

### Inputs From
<!-- REQUIRED: "Inputs From" pattern (line 285) -->
- **Protocol 03 (Project Brief Creation)**: PROJECT-BRIEF.md (.md) from workspace root
- **Protocol 04 (Project Bootstrap & Context Engineering)**: .cursor/context/ directory contents (various formats) from .cursor/context/
- **Protocol 05 (Bootstrap Your Project)**: bootstrap-manifest.json (.json) from workspace root or `.artifacts/protocol-05/`
- **Protocol 05 (Bootstrap Your Project)**: architecture-principles.md (.md) from workspace root or `.artifacts/protocol-05/`

### Outputs To
<!-- REQUIRED: "Outputs To" pattern (line 293) -->
- **Variable (Generic Web App)**: Protocol 06 (Create PRD - Generic) receives PROTOCOL-EXECUTION-PLAN.md and PROTOCOL-CHECKLIST.md
- **Variable (AI/ML Project)**: AI Protocol 06 (AI Use Case Definition) receives PROTOCOL-EXECUTION-PLAN.md and PROTOCOL-CHECKLIST.md
- **Variable (Hybrid Project)**: Mixed sequence receives PROTOCOL-EXECUTION-PLAN.md with both generic and AI protocols
- **All Downstream Protocols**: handoff-package.zip (.zip) to `.artifacts/protocol-05b/` for audit trail

### Data Formats
<!-- REQUIRED: File extensions (line 301) -->
- **Markdown (.md)**: PROTOCOL-EXECUTION-PLAN.md (15-25 pages), PROTOCOL-CHECKLIST.md (simple checklist), classification-reasoning.md
- **JSON (.json)**: 35+ evidence artifacts including project-classification.json, gap-analysis.json, timeline-estimate.json, approval-record.json
- **ZIP (.zip)**: handoff-package.zip containing all evidence artifacts with checksums

### Storage Locations
<!-- REQUIRED: .artifacts/ references (line 310) -->
- `.artifacts/protocol-05b/` for all 35+ JSON evidence artifacts
- `.artifacts/protocol-05b/new-protocols/` for dynamically created protocols (if gaps detected)
- Workspace root for PROTOCOL-EXECUTION-PLAN.md and PROTOCOL-CHECKLIST.md
- `.artifacts/protocol-05b/handoff-package.zip` for complete evidence package

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

### Gate 0: Pre-Flight Validation (Prerequisite)
<!-- REQUIRED: Gate type (line 102) -->

- **Criteria**: Protocol 05 artifacts exist and valid (100% pass rate), PROJECT-BRIEF.md exists with all required sections, user authorization obtained
  
- **Pass Threshold**: 100% (all checks must pass)
  <!-- REQUIRED: Numeric threshold (line 130) -->
  
- **Metrics**: Validation score (binary: pass/fail), completeness percentage, authorization status
  <!-- REQUIRED: Metric type (line 132) -->
  
- **Evidence Links**: `.artifacts/protocol-05b/phase-00-preflight-check.json`, `.artifacts/protocol-05b/authorization-record.json`
  <!-- REQUIRED: Evidence references (line 133) -->
  
- **Automation**: 
  <!-- REQUIRED: Scripts (line 160) -->
  ```bash
  # AI-driven validation (no script needed - protocol performs validation)
  # Evidence automatically generated during STEP 1
  ```
  
- **Failure Handling**: 
  <!-- REQUIRED: Rollback, notification, waiver (lines 199-202) -->
  - **Rollback**: BLOCK execution, return to Protocol 05 with gap report
  - **Notification**: Alert user that Protocol 05 is incomplete
  - **Waiver**: Not applicable (blocking gate, no waiver allowed)

---

### Gate 1: Classification Confidence (Execution)

- **Criteria**: Project classification confidence score ≥85%, classification reasoning document complete, all 27+ characteristics evaluated
  
- **Pass Threshold**: Confidence ≥85% OR human approval obtained
  
- **Metrics**: Confidence score (0.0-1.0), characteristic detection rate (percentage), classification accuracy
  
- **Evidence Links**: `.artifacts/protocol-05b/project-classification.json`, `.artifacts/protocol-05b/classification-reasoning.md`, `.artifacts/protocol-05b/characteristics-detection.json`
  
- **Automation**: 
  ```bash
  # AI-driven classification (no script needed)
  # Confidence score calculated during STEP 3
  ```
  
- **Failure Handling**: 
  - **Rollback**: BLOCK until human review obtained if confidence <70%, WARN if 70-84%
  - **Notification**: Alert user of low confidence classification, request manual review
  - **Waiver**: Human approval can override low confidence (70-84% range only)

---

### Gate 2: MAYBE Protocol Decisions (Execution)

- **Criteria**: All MAYBE protocols presented to user, user decision recorded for each (Include/Skip/Defer), decision timestamp and rationale documented
  
- **Pass Threshold**: 100% decisions made (all MAYBE protocols have user input)
  
- **Metrics**: Decision completion rate (percentage), MAYBE protocol count, user response time
  
- **Evidence Links**: `.artifacts/protocol-05b/maybe-protocol-decisions.json`, `.artifacts/protocol-05b/protocol-selection.json`
  
- **Automation**: 
  ```bash
  # AI-driven presentation, user interaction required
  # Decisions recorded during STEP 4
  ```
  
- **Failure Handling**: 
  - **Rollback**: BLOCK until all decisions obtained
  - **Notification**: Remind user of pending MAYBE protocol decisions
  - **Waiver**: Not applicable (user decision required)

---

### Gate 3: Protocol Coverage (Execution)

- **Criteria**: Overall requirement coverage ≥95%, critical requirements coverage = 100%, zero conflicting protocols selected
  
- **Pass Threshold**: Coverage ≥95% AND critical = 100%
  
- **Metrics**: Coverage percentage, gap count, critical gap count, conflict count
  
- **Evidence Links**: `.artifacts/protocol-05b/gap-analysis.json`, `.artifacts/protocol-05b/coverage-report.json`, `.artifacts/protocol-05b/protocol-selection.json`
  
- **Automation**: 
  ```bash
  # AI-driven gap analysis
  # Coverage calculated during STEP 4
  # Triggers STEP 4.5 if coverage <95%
  ```
  
- **Failure Handling**: 
  - **Rollback**: Force PHASE 4 execution (create new protocols) if coverage <95%
  - **Notification**: Alert user of coverage gaps and resolution strategy
  - **Waiver**: User can accept gaps <95% if no critical gaps exist (document as limitations)

---

### Gate 4: New Protocol Validation (Execution - Conditional)

- **Criteria**: All new protocols score ≥0.95 on validation, each validator dimension ≥0.90, zero critical validation failures, maximum 5 iteration attempts per protocol
  
- **Pass Threshold**: Overall score ≥0.95 for ALL new protocols
  
- **Metrics**: Validation score (0.0-1.0), dimension scores, iteration count, failure count
  
- **Evidence Links**: `.artifacts/protocol-05b/new-protocols/{ID}-validation-report.json` for each new protocol
  
- **Automation**: 
  ```bash
  # Protocol-creation workflow (protocols 1-5) executed automatically
  # Validation performed during STEP 4.5
  python3 validators-system/scripts/validate_all_protocols.py --protocol {ID}
  ```
  
- **Failure Handling**: 
  - **Rollback**: Iterate up to 5 times with content adjustments, then escalate to user
  - **Notification**: Alert user if protocol validation fails after 5 iterations
  - **Waiver**: User can choose: manual fix, skip protocol (accept gap), or use alternative approach

---

### Gate 5: Timeline Approval (Completion)

- **Criteria**: Timeline calculated with effort estimates, critical path identified, parallel opportunities documented, user approves timeline and resource allocation
  
- **Pass Threshold**: User explicit approval ("yes")
  
- **Metrics**: Timeline duration (days), effort (hours), resource count, approval status
  
- **Evidence Links**: `.artifacts/protocol-05b/timeline-estimate.json`, `.artifacts/protocol-05b/approval-record.json`
  
- **Automation**: 
  ```bash
  # AI-driven timeline calculation
  # User approval requested during STEP 6
  ```
  
- **Failure Handling**: 
  - **Rollback**: Return to PHASE 5 for optimization (not blocking)
  - **Notification**: Offer optimization options: reduce scope, increase resources, extend timeline
  - **Waiver**: Advisory gate - user can proceed with concerns documented

---

### Gate 6: Final Plan Approval (Completion)

- **Criteria**: PROTOCOL-EXECUTION-PLAN.md complete (15-25 pages), PROTOCOL-CHECKLIST.md generated, handoff-package.zip valid and complete, user approves entire execution plan
  
- **Pass Threshold**: User explicit approval ("yes")
  
- **Metrics**: Plan completeness (percentage), artifact count, package integrity (checksum validation), approval status
  
- **Evidence Links**: PROTOCOL-EXECUTION-PLAN.md, PROTOCOL-CHECKLIST.md, `.artifacts/protocol-05b/handoff-package.zip`, `.artifacts/protocol-05b/approval-record.json`
  
- **Automation**: 
  ```bash
  # AI-driven plan generation
  # Package creation during STEP 7
  sha256sum .artifacts/protocol-05b/handoff-package.zip > .artifacts/protocol-05b/checksums.sha256
  ```
  
- **Failure Handling**: 
  - **Rollback**: Smart rollback to specified phase based on user feedback (can revise any phase)
  - **Notification**: Request specific feedback on which sections need revision
  - **Waiver**: Not applicable (blocking gate, approval required to proceed)

---
