# PROTOCOL-PRD PART 2: DETAILED PHASES & QUALITY GATES

## PHASE 0: PRE-FLIGHT VALIDATION

### Purpose
Verify Protocol 05 completion and user authorization before proceeding.

### Inputs
- Protocol 05 artifacts (bootstrap-manifest.json, architecture-principles.md)
- Protocol 04 artifacts (.cursor/context/)
- Protocol 03 artifacts (PROJECT-BRIEF.md)

### Process Steps
1. **Verify Protocol 05 Completion**
   - Check bootstrap-manifest.json exists and valid
   - Check architecture-principles.md exists and complete
   - Verify Protocol 05 quality gates all passed

2. **Validate Artifact Integrity**
   - PROJECT-BRIEF.md exists at workspace root
   - PROJECT-BRIEF.md not empty and valid markdown
   - All required sections present

3. **Confirm User Authorization**
   - Request explicit approval to proceed
   - Record authorization timestamp

### Outputs
- phase-00-preflight-check.json
- protocol-05-completion-status.json
- quality-gate-verification.json

### Success Criteria
- 100% of checks pass (all REQUIRED)
- User authorization obtained

### Automation
- Script: `validate_protocol_evidence.py`
- Runtime: <30 seconds

---

## PHASE 1: INPUT VALIDATION & CONTEXT LOADING

### Purpose
Load and parse all foundation artifacts from Protocols 03, 04, 05.

### Inputs
- PROJECT-BRIEF.md (from Protocol 03)
- architecture-principles.md (from Protocol 05)
- bootstrap-manifest.json (from Protocol 05)
- .cursor/context/ directory (from Protocol 04)

### Process Steps
1. **Parse PROJECT-BRIEF** (Parallel)
   - Extract: project_name, goals, deliverables, tech_stack, quality_requirements
   - Validate: All required sections present
   - Output: project-brief-parsed.json

2. **Parse Architecture** (Parallel)
   - Extract: system architecture, constraints, integration requirements
   - Validate: Required sections present
   - Output: architecture-parsed.json

3. **Parse Bootstrap Manifest** (Parallel)
   - Extract: project_type, scaffold_structure, tooling_config
   - Validate: Valid JSON, required fields
   - Output: bootstrap-manifest-parsed.json

4. **Inventory Artifacts**
   - List all available context files
   - Output: artifact-inventory.json

5. **Validate All Artifacts**
   - Check completeness
   - Flag missing/invalid data
   - Output: phase-01-validation.json

### Outputs
- phase-01-validation.json
- project-brief-parsed.json
- architecture-parsed.json
- bootstrap-manifest-parsed.json
- artifact-inventory.json

### Success Criteria
- All required artifacts parsed successfully
- No critical validation errors

### Automation
- Scripts: `parse_project_brief.py`, `parse_architecture.py`
- Runtime: <2 minutes
- Parallelization: 3 tasks

---

## PHASE 2: PROJECT CLASSIFICATION & CHARACTERISTIC DETECTION

### Purpose
Classify project type and detect technical characteristics across 27+ dimensions.

### Inputs
- project-brief-parsed.json
- architecture-parsed.json
- bootstrap-manifest-parsed.json

### Process Steps
1. **Project Classification**
   - Analyze keywords, tech stack, deliverables
   - Classify as: AI/ML, Web App, API, Mobile, Hybrid
   - Calculate confidence score (0-100%)
   - Document reasoning
   - Output: project-classification.json, classification-reasoning.md

2. **Characteristic Detection** (27 Parallel Detectors)
   - ML/AI components detector
   - Web UI framework detector
   - API/microservices detector
   - Database technology detector
   - Authentication/authorization detector
   - Real-time/streaming detector
   - Mobile platform detector
   - Cloud provider detector
   - Containerization detector
   - CI/CD pipeline detector
   - Testing framework detector
   - Monitoring/observability detector
   - Security requirements detector
   - Compliance requirements detector
   - Performance requirements detector
   - Scalability requirements detector
   - Data privacy detector
   - Third-party integration detector
   - Payment processing detector
   - Notification system detector
   - Search functionality detector
   - Caching strategy detector
   - CDN requirements detector
   - Internationalization detector
   - Accessibility requirements detector
   - Documentation requirements detector
   - Team structure detector

3. **Generate Project Fingerprint**
   - Combine all detected characteristics
   - Calculate fingerprint hash
   - Output: project-fingerprint.json

4. **Calculate Confidence Scores**
   - Per-characteristic confidence
   - Overall classification confidence
   - Output: confidence-scores.json

### Outputs
- project-classification.json
- classification-reasoning.md
- characteristics-detection.json
- project-fingerprint.json
- confidence-scores.json

### Success Criteria
- Project type identified
- Classification confidence ≥85% (or human review triggered)
- At least 5 characteristics detected
- At least 3 high-confidence characteristics (≥90%)

### Automation
- Scripts: `classify_project.py`, `detect_characteristics.py`, `calculate_classification_confidence.py`
- Runtime: <2 minutes
- Parallelization: 27 detector tasks

---

## PHASE 3: INTELLIGENT PROTOCOL SELECTION

### Purpose
Map detected characteristics to protocols and select optimal execution set.

### Inputs
- project-classification.json
- characteristics-detection.json
- project-fingerprint.json
- Available protocols (scan .cursor/ai-driven-workflow/ and AI-project-workflow/)

### Process Steps
1. **Map Characteristics to Protocols**
   - For each characteristic, identify relevant protocols
   - Apply selection rules (REQUIRED/RECOMMENDED/MAYBE/SKIP)
   - Document mapping rationale
   - Output: characteristic-protocol-mapping.json

2. **Apply Selection Logic**
   - REQUIRED: Explicit in PROJECT-BRIEF or critical for project type
   - RECOMMENDED: Strongly beneficial but not mandatory
   - MAYBE: Could add value, user decides
   - SKIP: Not applicable or explicitly excluded
   - Output: protocol-selection.json

3. **Detect Coverage Gaps**
   - Compare PROJECT-BRIEF requirements vs selected protocols
   - Identify unmapped requirements
   - Calculate coverage percentage
   - Output: gap-analysis.json

4. **Calculate Coverage Metrics**
   - Overall coverage: (mapped_requirements / total_requirements) × 100%
   - Critical coverage: (mapped_critical / total_critical) × 100%
   - Output: coverage-report.json

5. **Generate Priority Matrix**
   - Rank protocols by: REQUIRED > RECOMMENDED > MAYBE > SKIP
   - Output: protocol-priority-matrix.json

### Outputs
- characteristic-protocol-mapping.json
- protocol-selection.json
- gap-analysis.json
- coverage-report.json
- protocol-priority-matrix.json

### Success Criteria
- All PROJECT-BRIEF requirements analyzed
- Coverage ≥95% (Gate 3 threshold)
- All REQUIRED protocols identified
- MAYBE protocols presented for user decision

### Automation
- Scripts: `map_protocols.py`, `analyze_gaps.py`, `validate_protocol_coverage.py`
- Runtime: <2 minutes
- Parallelization: 2 tasks (gap analysis + coverage)

---

## PHASE 4: NEW PROTOCOL CREATION (IF GAPS DETECTED)

### Purpose
Create new protocols dynamically when coverage gaps are detected.

### Inputs
- gap-analysis.json
- coverage-report.json
- Bootstrap Protocol Context (Protocol 0)

### Process Steps
1. **Generate Protocol Specifications**
   - For each gap, create detailed specification
   - Define: workflow steps, inputs, outputs, validation criteria
   - Output: new-protocols/{ID}-specification.json

2. **Call Bootstrap Protocol Context (Protocol 0)**
   - Pass gap specification to Protocol 0
   - Receive generated protocol file
   - Output: new-protocols/{ID}-{name}.md

3. **Validate New Protocols**
   - Run all 10 validators
   - Require overall score ≥0.95
   - Iterate up to 5 times if needed
   - Output: new-protocols/{ID}-validation-report.json

4. **Register New Protocols**
   - Update script-registry.json
   - Add to protocol workflow directory
   - Document integration points
   - Output: gap-resolution-log.md

### Outputs
- new-protocols/{ID}-specification.json (per gap)
- new-protocols/{ID}-{name}.md (per gap)
- new-protocols/{ID}-validation-report.json (per gap)
- gap-resolution-log.md

### Success Criteria
- All gaps addressed (new protocols created or justified skip)
- All new protocols score ≥0.95 on validation
- All new protocols registered in script registry

### Automation
- Scripts: `create_protocol_from_gap.py`, `validators-system/validate_all_protocols.py`
- Runtime: <15 minutes per protocol (max 5 iterations)
- Parallelization: N tasks (N = number of gaps)

---

## PHASE 5: SEQUENCE & CUSTOMIZE

### Purpose
Order protocols logically and identify customization requirements.

### Process Steps
1. **Build Dependency Graph**
   - Extract prerequisites from each selected protocol
   - Create directed graph
   - Output: dependency-graph.json

2. **Determine Execution Order**
   - Perform topological sort
   - Identify parallel execution opportunities
   - Calculate critical path
   - Output: execution-sequence.json, critical-path-analysis.json

3. **Analyze Customization Needs**
   - For each protocol, check project fit
   - Identify required modifications
   - Document rationale and impact
   - Output: customization-requirements.json

4. **Estimate Timeline**
   - Calculate effort per protocol (base hours × complexity multiplier)
   - Apply customization penalty (+20%)
   - Apply parallel execution discount (-40% for parallel tasks)
   - Output: timeline-estimate.json

### Outputs
- dependency-graph.json
- execution-sequence.json
- critical-path-analysis.json
- customization-requirements.json
- timeline-estimate.json

### Success Criteria
- No circular dependencies
- All protocols sequenced
- Timeline calculated
- Customizations documented

### Automation
- Scripts: `sequence_protocols.py`, `analyze_customization_needs.py`, `estimate_timeline.py`
- Runtime: <2 minutes

---

## PHASE 6: PLAN GENERATION & APPROVAL

### Purpose
Generate complete execution plan and obtain user approval.

### Process Steps
1. **Generate PROTOCOL-EXECUTION-PLAN.md**
   - Compile all analysis results
   - Include: classification, selection, gaps, sequence, timeline
   - Format: Human-readable markdown
   - Output: PROTOCOL-EXECUTION-PLAN.md (root)

2. **Generate PROTOCOL-CHECKLIST.md**
   - Simple checkbox list of protocols
   - One line per protocol with estimated hours
   - Output: PROTOCOL-CHECKLIST.md (root)

3. **Create Evidence Manifest**
   - List all generated artifacts
   - Calculate checksums
   - Output: evidence-manifest.json

4. **Package Handoff Artifacts**
   - Compress all .artifacts/protocol-05b/ files
   - Include checksums
   - Output: handoff-package.zip

5. **Present for Approval**
   - Display execution plan to user
   - Request final approval
   - Record approval decision
   - Output: approval-log.md, protocol-05b-completion-report.json

### Outputs
- PROTOCOL-EXECUTION-PLAN.md (root)
- PROTOCOL-CHECKLIST.md (root)
- evidence-manifest.json
- handoff-package.zip
- approval-log.md
- protocol-05b-completion-report.json

### Success Criteria
- All documents generated
- User approval obtained
- Handoff package complete

### Automation
- Scripts: `generate_execution_plan.py`, `generate_checklist.py`, `package_handoff.py`
- Runtime: <3 minutes
- Parallelization: 3 tasks (plan + checklist + manifest)

---

## QUALITY GATES SPECIFICATION

### GATE 0: Pre-Flight Validation [BLOCKING]
**Trigger:** Before PHASE 0 execution  
**Type:** Automated  
**Threshold:** 100% pass rate  

**Validation Criteria:**
- Protocol 05 artifacts exist and valid
- PROJECT-BRIEF.md exists and complete
- User authorization obtained

**Pass:** All checks pass  
**Fail:** BLOCK - Return to Protocol 05 with gap report  
**Automation:** `validate_protocol_evidence.py`  
**SLO:** <30 seconds  

---

### GATE 1: Classification Confidence [WARNING]
**Trigger:** After PHASE 2  
**Type:** Automated with manual override  
**Threshold:** ≥85% confidence  

**Validation Criteria:**
- Project type identified
- Classification confidence ≥85%
- If <85%: MANDATORY human review
- If 70-84%: WARNING, proceed with caution
- If <70%: BLOCK until human review

**Pass:** Confidence ≥85% OR human approval  
**Warn:** 70-84% confidence  
**Fail:** <70% without human approval  
**Automation:** `calculate_classification_confidence.py`  
**SLO:** <2 minutes (automated), <15 minutes (manual review)  

---

### GATE 2: MAYBE Protocol User Decision [MANUAL]
**Trigger:** After PHASE 3 protocol selection  
**Type:** Manual  
**Threshold:** 100% decisions made  

**Validation Criteria:**
- All MAYBE protocols presented
- User decision for each: Include / Skip / Defer
- Decisions recorded with timestamp

**Pass:** All MAYBE protocols have decision  
**Fail:** BLOCK until all decisions made  
**Automation:** Present via `generate_execution_plan.py`  
**SLO:** <2 hours (recommended, not enforced)  

---

### GATE 3: Protocol Coverage [BLOCKING - AUTOMATED]
**Trigger:** After PHASE 3 gap analysis  
**Type:** Automated  
**Threshold:** ≥95% coverage  

**Validation Criteria:**
- Overall coverage ≥95%
- Critical requirements coverage = 100%
- Zero conflicting protocols

**Pass:** Coverage ≥95%, critical = 100%  
**Fail:** BLOCK - Force PHASE 4 execution  
**Automation:** `validate_protocol_coverage.py`  
**SLO:** <1 minute  

---

### GATE 4: New Protocol Validation [BLOCKING]
**Trigger:** After PHASE 4 (if gaps existed)  
**Type:** Automated with manual escalation  
**Threshold:** ≥0.95 validation score  

**Validation Criteria:**
- All new protocols score ≥0.95
- Each validator dimension ≥0.90
- Zero critical failures

**Pass:** Score ≥0.95  
**Fail:** ITERATE (max 5) or ESCALATE  
**Automation:** `validators-system/validate_all_protocols.py`  
**SLO:** <5 minutes per protocol, <2 hours total  

---

### GATE 5: Timeline Approval [MANUAL]
**Trigger:** After PHASE 5  
**Type:** Manual  
**Threshold:** User approval  

**Validation Criteria:**
- Timeline calculated
- Critical path identified
- User approves timeline

**Pass:** User explicit approval  
**Fail:** Return to PHASE 5 for optimization  
**Automation:** `estimate_timeline.py` generates, user approves  
**SLO:** <1 hour (recommended)  

---

### GATE 6: Final Plan Approval [BLOCKING]
**Trigger:** After PHASE 6  
**Type:** Manual  
**Threshold:** User approval  

**Validation Criteria:**
- PROTOCOL-EXECUTION-PLAN.md complete
- PROTOCOL-CHECKLIST.md complete
- Evidence package valid
- User approves plan

**Pass:** User explicit approval  
**Fail:** Smart rollback to specific phase based on feedback  
**Automation:** `generate_execution_plan.py` + `package_handoff.py`  
**SLO:** <4 hours (recommended)  

---

