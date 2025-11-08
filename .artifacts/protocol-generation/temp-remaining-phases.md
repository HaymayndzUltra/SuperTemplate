### PHASE 4: NEW PROTOCOL CREATION (IF GAPS DETECTED)

**Purpose:** Create new protocols dynamically when coverage gaps are detected.

<!-- [Category: EXECUTION - SUBSTEPS variant] -->

**STEP 4.1: Generate Protocol Specifications**

**[MUST]** For each gap, create detailed protocol specification:

```bash
python scripts/orchestration/generate_protocol_spec_from_gap.py \
  --gap-analysis .artifacts/protocol-05b/gap-analysis.json \
  --output-dir .artifacts/protocol-05b/new-protocols/
```

**Specification Contents (per gap):**
- Protocol ID (auto-assigned)
- Protocol name
- Purpose statement
- Workflow steps (inputs, process, outputs)
- Quality gates
- Validation criteria
- Integration points

**Evidence Generated:** `.artifacts/protocol-05b/new-protocols/{ID}-specification.json` (per gap)

---

**STEP 4.2: Call Bootstrap Protocol Context (Protocol 0)**

**[CRITICAL]** For each gap, invoke Protocol 0 to create new protocol:

**Substep 4.2.1: Prepare Protocol 0 Inputs**

```bash
python scripts/orchestration/prepare_protocol_0_inputs.py \
  --spec .artifacts/protocol-05b/new-protocols/{ID}-specification.json \
  --output .artifacts/protocol-05b/new-protocols/{ID}-protocol-0-inputs/
```

**Inputs to Protocol 0:**
- `gap-specification.json` (gap details, requirements)
- `workflow-requirements.md` (workflow steps, inputs, outputs)
- `format-template-suggestions.yaml` (recommended templates)

---

**Substep 4.2.2: Execute Protocol 0**

```bash
# Manual invocation - Protocol 0 is AI-driven
# AI reads inputs from .artifacts/protocol-05b/new-protocols/{ID}-protocol-0-inputs/
# AI generates protocol file
```

**Expected Output:** `.artifacts/protocol-05b/new-protocols/{ID}-{name}.md`

**Retry Logic:**
- **IF** Protocol 0 fails → Retry once with adjusted inputs
- **IF** second failure → Escalate to user with error details

---

**Substep 4.2.3: Track Protocol Creation**

**[MUST]** Log each protocol creation attempt:

**Evidence Generated:** `.artifacts/protocol-05b/new-protocols/creation-log.json`

**Format:**
```json
{
  "protocol_id": "XX",
  "gap_addressed": "Blockchain deployment",
  "attempts": 1,
  "status": "success",
  "timestamp": "2025-11-09T02:00:00Z"
}
```

---

**STEP 4.3: Validate New Protocols**

**[CRITICAL]** Each new protocol MUST score ≥0.95 on validation:

**Substep 4.3.1: Run All 10 Validators**

```bash
python validators-system/scripts/validate_all_protocols.py \
  --protocol {ID} \
  --workspace /path/to/workspace
```

**Success Criteria:** Overall score ≥0.95

---

**Substep 4.3.2: Iterate on Validation Failures**

**[MUST]** If validation score <0.95:

1. **Analyze Validation Report**
   - Identify failing validators
   - Extract specific issues
   - Prioritize by impact

2. **Apply Fixes**
   - Address highest-impact issues first
   - Re-run validators after each fix
   - Track iteration count

3. **Retry Validation**
   - Maximum 5 iterations per protocol
   - **IF** still <0.95 after 5 iterations → Escalate to user

**Evidence Generated:** `.artifacts/protocol-05b/new-protocols/{ID}-validation-report.json`

**Iteration Tracking:**
```json
{
  "protocol_id": "XX",
  "iteration": 3,
  "score": 0.96,
  "status": "pass",
  "issues_fixed": ["Domain expertise missing", "REASONING blocks added"]
}
```

---

**STEP 4.4: Register New Protocols**

**[MUST]** Add new protocols to system registries:

**Substep 4.4.1: Update Script Registry**

```bash
python scripts/orchestration/register_new_protocol.py \
  --protocol-file .artifacts/protocol-05b/new-protocols/{ID}-{name}.md \
  --registry scripts/script-registry.json
```

**Registry Update:**
- Add entry for each automation script in new protocol
- Include: script path, purpose, owner, dependencies

---

**Substep 4.4.2: Add to Protocol Directory**

**[MUST]** Copy validated protocol to appropriate directory:

```bash
cp .artifacts/protocol-05b/new-protocols/{ID}-{name}.md \
   .cursor/ai-driven-workflow/{ID}-{name}.md
```

---

**Substep 4.4.3: Document Integration Points**

**[MUST]** Update integration documentation:

**Evidence Generated:** `.artifacts/protocol-05b/new-protocols/gap-resolution-log.md`

**Contents:**
- List of gaps addressed
- New protocols created
- Integration points documented
- Validation scores achieved

---

**PHASE 4 OUTPUTS:**
- ✅ `new-protocols/{ID}-specification.json` (per gap)
- ✅ `new-protocols/{ID}-{name}.md` (per gap)
- ✅ `new-protocols/{ID}-validation-report.json` (per gap)
- ✅ `new-protocols/creation-log.json`
- ✅ `new-protocols/gap-resolution-log.md`

**PHASE 4 SKIP CONDITION:**
- **IF** gap-analysis.json shows coverage ≥95% → Skip PHASE 4 entirely, proceed to PHASE 5

---

### PHASE 5: SEQUENCE & CUSTOMIZE

**Purpose:** Order protocols logically and identify customization requirements.

<!-- [Category: EXECUTION - REASONING variant] -->

**STEP 5.1: Build Dependency Graph**

**[MUST]** Extract prerequisites and create dependency graph:

```bash
python scripts/orchestration/build_dependency_graph.py \
  --selection .artifacts/protocol-05b/protocol-selection.json \
  --protocol-dir .cursor/ai-driven-workflow/ \
  --ai-protocol-dir AI-project-workflow/ \
  --output .artifacts/protocol-05b/dependency-graph.json
```

**Graph Structure:**
```json
{
  "nodes": [
    {"id": "06", "name": "Create PRD", "prerequisites": ["05b"]},
    {"id": "07", "name": "Technical Design", "prerequisites": ["06"]}
  ],
  "edges": [
    {"from": "05b", "to": "06"},
    {"from": "06", "to": "07"}
  ]
}
```

**Evidence Generated:** `.artifacts/protocol-05b/dependency-graph.json`

---

**STEP 5.2: Determine Execution Order**

**[MUST]** Perform topological sort and identify parallel opportunities:

```bash
python scripts/orchestration/sequence_protocols.py \
  --dependency-graph .artifacts/protocol-05b/dependency-graph.json \
  --output .artifacts/protocol-05b/execution-sequence.json
```

**Sequencing Algorithm:**
1. **Topological Sort** - Order protocols respecting dependencies
2. **Parallel Detection** - Identify protocols with no interdependencies
3. **Critical Path Analysis** - Calculate longest path through graph

**Evidence Generated:** 
- `.artifacts/protocol-05b/execution-sequence.json`
- `.artifacts/protocol-05b/critical-path-analysis.json`

**[REASONING]**

**Premises:**
- Protocols have explicit prerequisites
- Some protocols can run in parallel
- Critical path determines minimum timeline

**Sequencing Logic:**
- **FOR EACH** protocol in selection:
  - Check prerequisites
  - **IF** all prerequisites complete → Add to ready queue
  - **IF** no dependencies on other ready protocols → Mark as parallel candidate
- **SORT** by: dependencies first, then alphabetical
- **GROUP** parallel candidates into execution batches

**Decision:**
Generate ordered sequence with parallel batches identified

**Evidence:**
- Dependency graph
- Topological sort result
- Parallel execution opportunities
- Critical path calculation

**Risks & Mitigations:**
- **Risk:** Circular dependencies → Execution blocked
- **Mitigation:** Validate no cycles in graph, fail fast if detected

**Acceptance Link:**
- Validator 3 (Workflow Algorithm) - Sequencing algorithm documented
- Validator 9 (Cognitive Reasoning) - Decision logic present

---

**STEP 5.3: Analyze Customization Needs**

**[MUST]** Identify protocol modifications required for project:

```bash
python scripts/orchestration/analyze_customization_needs.py \
  --selection .artifacts/protocol-05b/protocol-selection.json \
  --brief .artifacts/protocol-05b/project-brief-parsed.json \
  --characteristics .artifacts/protocol-05b/characteristics-detection.json \
  --output .artifacts/protocol-05b/customization-requirements.json
```

**Customization Analysis:**

**Project-Specific Customizations:**
- **Solo Developer:** Remove team collaboration steps, sign-off processes
- **MVP Project:** Defer optimization protocols (18, 22-25) to v2
- **AI/ML Project:** Add model-specific sections to generic protocols
- **Compliance Required:** Add audit trail steps to all protocols

**Evidence Generated:** `.artifacts/protocol-05b/customization-requirements.json`

**Format:**
```json
{
  "protocol_06": {
    "customizations": [
      {
        "section": "PHASE 3: Stakeholder Review",
        "modification": "Remove (solo developer)",
        "rationale": "No external stakeholders",
        "impact": "Saves 2 hours"
      }
    ]
  }
}
```

**[REASONING]**

**Premises:**
- Standard protocols assume team environment
- Project characteristics require adaptations
- Customizations affect timeline and effort

**Customization Logic:**
- **IF** team_structure = "solo developer" → Remove collaboration steps
- **IF** project_phase = "MVP" → Defer non-critical protocols
- **IF** compliance_required = true → Add audit steps
- **IF** ai_ml_project = true → Add model-specific sections

**Decision:**
Document all required customizations with rationale and impact

**Evidence:**
- Project characteristics
- Protocol standard assumptions
- Customization recommendations
- Timeline impact per customization

**Risks & Mitigations:**
- **Risk:** Over-customization removes critical steps
- **Mitigation:** Flag critical steps, require explicit user approval to remove

**Acceptance Link:**
- Validator 3 (Workflow Algorithm) - Customization logic documented
- Validator 9 (Cognitive Reasoning) - Decision rationale present

---

**STEP 5.4: Estimate Timeline**

**[MUST]** Calculate effort and timeline for execution plan:

```bash
python scripts/orchestration/estimate_timeline.py \
  --sequence .artifacts/protocol-05b/execution-sequence.json \
  --customization .artifacts/protocol-05b/customization-requirements.json \
  --output .artifacts/protocol-05b/timeline-estimate.json
```

**Estimation Formula:**
```
Total Effort = Σ (Base Hours × Complexity Multiplier × Customization Penalty)
Actual Timeline = Total Effort × (1 - Parallel Discount)

Where:
- Base Hours: Standard protocol execution time
- Complexity Multiplier: 1.0 (simple), 1.5 (medium), 2.0 (complex)
- Customization Penalty: +20% if customizations required
- Parallel Discount: -40% for protocols in parallel batches
```

**Evidence Generated:** `.artifacts/protocol-05b/timeline-estimate.json`

**Format:**
```json
{
  "total_effort_hours": 120,
  "parallel_discount_hours": 48,
  "actual_timeline_hours": 72,
  "estimated_days": 9,
  "milestones": [
    {"phase": "Planning (06-08)", "hours": 24, "days": 3},
    {"phase": "Development (09-13)", "hours": 36, "days": 4.5}
  ]
}
```

---

**PHASE 5 OUTPUTS:**
- ✅ `dependency-graph.json`
- ✅ `execution-sequence.json`
- ✅ `critical-path-analysis.json`
- ✅ `customization-requirements.json`
- ✅ `timeline-estimate.json`

---

### PHASE 6: PLAN GENERATION & APPROVAL

**Purpose:** Generate complete execution plan and obtain user approval.

**STEP 6.1: Generate PROTOCOL-EXECUTION-PLAN.md**

**[MUST]** Compile comprehensive execution plan:

```bash
python scripts/orchestration/generate_execution_plan.py \
  --artifacts-dir .artifacts/protocol-05b/ \
  --output PROTOCOL-EXECUTION-PLAN.md
```

**Document Structure (15-25 pages):**

1. **Executive Summary** (1 page)
   - Project classification
   - Total protocols: REQUIRED/RECOMMENDED/MAYBE
   - Timeline: X days, Y hours
   - Key milestones

2. **Project Analysis** (2-3 pages)
   - Classification details with confidence
   - Detected characteristics (27+ dimensions)
   - Key findings

3. **Protocol Selection** (5-8 pages)
   - REQUIRED protocols with rationale
   - RECOMMENDED protocols with value proposition
   - MAYBE protocols with decision criteria
   - SKIP protocols with justification

4. **Gap Analysis** (1-2 pages)
   - Coverage metrics (X%)
   - Gaps identified
   - New protocols created
   - Resolution approach

5. **Execution Sequence** (3-5 pages)
   - Ordered protocol list
   - Dependency graph visualization
   - Parallel execution batches
   - Critical path

6. **Customization Requirements** (2-3 pages)
   - Per-protocol modifications
   - Rationale and impact
   - Implementation guidance

7. **Timeline & Resources** (2-3 pages)
   - Effort estimates per protocol
   - Total hours and days
   - Milestones and checkpoints
   - Resource requirements

8. **Approval & Sign-off** (1 page)
   - Approval request
   - Sign-off form
   - Conditions and assumptions

**Evidence Generated:** `PROTOCOL-EXECUTION-PLAN.md` (workspace root)

---

**STEP 6.2: Generate PROTOCOL-CHECKLIST.md**

**[MUST]** Create simple execution tracking tool:

```bash
python scripts/orchestration/generate_protocol_checklist.py \
  --sequence .artifacts/protocol-05b/execution-sequence.json \
  --output PROTOCOL-CHECKLIST.md
```

**Format:**
```markdown
# Protocol Execution Checklist

## REQUIRED Protocols
- [ ] Protocol 06: Create PRD (Generic) - 8 hours
- [ ] Protocol 07: Technical Design (Generic) - 12 hours
- [ ] Protocol AI:12: Algorithm Selection (AI) - 6 hours

## RECOMMENDED Protocols
- [ ] Protocol 18: Performance Optimization (Generic) - 10 hours

## MAYBE Protocols (User Decision Required)
- [ ] Protocol 22: Model Monitoring (AI) - 8 hours
```

**Evidence Generated:** `PROTOCOL-CHECKLIST.md` (workspace root)

---

**STEP 6.3: Package Evidence Artifacts**

**[MUST]** Create complete evidence package:

```bash
python scripts/orchestration/package_evidence.py \
  --artifacts-dir .artifacts/protocol-05b/ \
  --output .artifacts/protocol-05b/handoff-package.zip
```

**Package Contents:**
- All JSON artifacts (35+ files)
- `evidence-manifest.json` (artifact inventory)
- `checksums.sha256` (integrity verification)
- New protocols (if created)

**Evidence Generated:** `.artifacts/protocol-05b/handoff-package.zip`

---

**STEP 6.4: Request User Approval**

**[CRITICAL]** Present execution plan for approval:

**User Prompt:**
```
[PROTOCOL 05B | APPROVAL REQUIRED]

Protocol execution plan generated:
📊 Project Classification: [Type] (confidence: X%)
📋 Protocols Selected: X REQUIRED, Y RECOMMENDED, Z MAYBE
⏱️  Estimated Timeline: X days (Y hours total)
🎯 Requirement Coverage: X%

Documents generated:
✅ PROTOCOL-EXECUTION-PLAN.md (workspace root)
✅ PROTOCOL-CHECKLIST.md (workspace root)
✅ Evidence package (.artifacts/protocol-05b/handoff-package.zip)

Please review PROTOCOL-EXECUTION-PLAN.md and approve to proceed.

MAYBE Protocols (Your Decision):
- Protocol XX: [Name] - [Value proposition] - [Hours]
  Include? (yes/no/defer)

Approve execution plan? (yes/no/revise)
```

**Evidence Generated:** `.artifacts/protocol-05b/approval-record.json`

**Approval Options:**
- **yes** → Proceed to handoff (Gate 6 passed)
- **no** → Halt execution, log reason
- **revise** → Return to specified phase for adjustments

**Error Handling:**
- User requests revision → Return to specified phase (2, 3, or 5)
- User declines → Halt gracefully, preserve all artifacts
- No response after 10 minutes → Prompt again, escalate after 3 attempts

---

**PHASE 6 OUTPUTS:**
- ✅ `PROTOCOL-EXECUTION-PLAN.md` (workspace root)
- ✅ `PROTOCOL-CHECKLIST.md` (workspace root)
- ✅ `handoff-package.zip` (.artifacts/protocol-05b/)
- ✅ `approval-record.json` (.artifacts/protocol-05b/)

---

