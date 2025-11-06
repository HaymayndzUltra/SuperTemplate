# Tamang Pag-Check ng Kada Protocol

## Two Types of Verification

### 1. PROTOCOL STRUCTURE VERIFICATION (Before Execution)
**Purpose:** I-verify na well-defined at ready ang protocol para i-execute

**What to Check:**
- ✅ **Structure Completeness**
  - May role definition ba? (specific, hindi generic)
  - May prerequisites section ba? (artifacts, approvals, system state)
  - May integration points ba? (inputs from, outputs to, storage)
  
- ✅ **Quality Gates Definition**
  - Complete ba ang gates? (criteria, threshold, evidence, automation, failure handling)
  - Realistic ba ang thresholds? (MVP vs Enterprise)
  - May automation scripts ba? (kung sinasabi na meron)
  
- ✅ **Workflow Executability**
  - Specific ba ang steps? (hindi vague)
  - Executable ba ang commands? (may full paths)
  - Resolved ba ang dependencies? (may outputs na required)
  
- ✅ **Required INPUTS Only** (from previous protocols)
  - Dapat meron kung na-execute na ang previous protocols
  - Example: Protocol 03 requires `PROPOSAL.md` from Protocol 01
  - **Check:** ✅ Correct - dapat meron kung Protocol 01 na-execute na
  
- ❌ **Required OUTPUTS** (will be created by this protocol)
  - **DON'T CHECK** - wala pa kasi hindi pa na-execute
  - **DON'T PENALIZE** - expected na walang meron
  - Example: Protocol 01 creates `PROPOSAL.md`
  - **Check:** ❌ Wrong - huwag i-check kung protocol not executed yet

**Scoring:**
- Structure: 2 points (role, prerequisites, integration)
- Quality Gates: 3 points (completeness, automation)
- Workflow: 1 point (executability)
- **Inputs Only:** 2 points (do previous protocols deliver?)
- **Outputs:** 0 points (not applicable - will be created)

**Total:** 8/10 max (outputs excluded)

---

### 2. PROTOCOL EXECUTION VERIFICATION (After Execution)
**Purpose:** I-verify na successful ang execution at tama ang artifacts

**What to Check:**
- ✅ **All Artifacts Exist**
  - Required inputs: Meron ba? (should exist)
  - Required outputs: Meron ba? (should exist - protocol executed)
  - Gate artifacts: Meron ba? (should exist - gates passed)
  
- ✅ **Content Validation**
  - JSON schema valid ba?
  - Approval artifacts: May status, approver, timestamp ba?
  - Diagnostic artifacts: Consistent ba ang status?
  
- ✅ **Contradiction Detection**
  - May contradictions ba between related artifacts?
  - Example: Approval says "approved" pero tests_run: 0
  
- ✅ **Quality Gates Status**
  - Did gates actually pass?
  - Evidence matches gate claims?

**Scoring:**
- All artifacts: 2 points
- Content validation: 2 points
- No contradictions: 2 points
- Gates passed: 2 points
- Execution quality: 2 points

**Total:** 10/10 max

---

## Recommended Approach

### Option A: Two Separate Commands

```bash
# Check protocol structure (before execution)
python scripts/verify_protocol.py protocol-01.md --structure-only

# Check protocol execution (after execution)
python scripts/verify_protocol.py protocol-01.md --executed
```

**Structure-Only Mode:**
- Check: Role, Prerequisites, Integration Points
- Check: Quality Gates Definition
- Check: Workflow Executability
- Check: Required INPUTS only (from previous protocols)
- **Don't Check:** Required OUTPUTS (not created yet)
- **Don't Penalize:** Missing outputs

**Executed Mode:**
- Check: All artifacts exist
- Check: Content validation
- Check: Contradiction detection
- Check: Gates actually passed

---

### Option B: Smart Detection

```bash
# Auto-detect: Check inputs only if protocol not executed
python scripts/verify_protocol.py protocol-01.md

# Logic:
# - If required_outputs exist → Protocol executed → Check all
# - If required_outputs missing → Protocol not executed → Check inputs only
```

**Smart Logic:**
```python
# Detect execution state
outputs_exist = any(artifact exists for required_outputs)
if outputs_exist:
    mode = "executed"
    check_all_artifacts = True
    penalize_missing_outputs = True
else:
    mode = "structure_only"
    check_inputs_only = True
    penalize_missing_outputs = False
```

---

### Option C: Explicit Mode Flag (Recommended)

```bash
# Default: Structure verification (before execution)
python scripts/verify_protocol.py protocol-01.md

# Explicit: Post-execution verification
python scripts/verify_protocol.py protocol-01.md --post-execution
```

**Default Mode (Structure):**
- ✅ Check structure completeness
- ✅ Check required INPUTS (should exist from previous protocols)
- ❌ Don't check required OUTPUTS (not created yet)
- **Message:** "Outputs not checked - protocol not executed yet"

**Post-Execution Mode:**
- ✅ Check all artifacts exist
- ✅ Validate content
- ✅ Detect contradictions
- **Message:** "All artifacts verified - execution successful"

---

## Scoring Logic

### Structure Verification Scoring

```python
score = 0.0

# Scope & Role (2 points)
if role_present and not generic:
    score += 0.5
if prerequisites_complete:
    score += 1.0
if integration_points_defined:
    score += 0.5

# Inputs Only (2 points)
if required_inputs_total > 0:
    input_score = (required_inputs_exist / required_inputs_total) * 2.0
    score += input_score
else:
    # No inputs required = perfect score
    score += 2.0

# Quality Gates (3 points)
if gates_total > 0:
    completeness_score = (gates_complete / gates_total) * 2.0
    automation_score = (automation_coverage / gates_total) * 1.0
    score += completeness_score + automation_score

# Workflow (1 point)
if workflow_executable:
    score += 1.0

# Total: 8/10 max (outputs excluded)
```

### Execution Verification Scoring

```python
score = 0.0

# All Artifacts (2 points)
total_artifacts = inputs_total + outputs_total + gate_artifacts_total
existing_artifacts = inputs_exist + outputs_exist + gate_artifacts_exist
if total_artifacts > 0:
    artifact_score = (existing_artifacts / total_artifacts) * 2.0
    score += artifact_score

# Content Validation (2 points)
# ... validation logic

# Contradictions (2 points)
if contradictions_count == 0:
    score += 2.0
else:
    score += max(0, 2.0 - (contradictions_count * 0.5))

# Gates Passed (2 points)
# ... gate verification logic

# Execution Quality (2 points)
# ... execution metrics

# Total: 10/10 max
```

---

## Summary: Tamang Pag-Check

### ✅ DO CHECK (Structure Verification):
1. Protocol structure (role, prerequisites, integration points)
2. Quality gates definition completeness
3. Workflow executability
4. **Required INPUTS only** (from previous protocols)

### ❌ DON'T CHECK (Structure Verification):
1. Required OUTPUTS (not created yet - protocol not executed)
2. Gate artifacts (not created yet - gates not passed)
3. Content validation (no content to validate yet)

### ✅ DO CHECK (Execution Verification):
1. All artifacts exist (inputs + outputs + gate artifacts)
2. Content validation (schema, approval status, diagnostics)
3. Contradiction detection
4. Gate passing status

### Key Insight:
**Separate "protocol design verification" from "protocol execution verification"**

- **Before execution:** Check structure + inputs only
- **After execution:** Check all artifacts + content + contradictions

**This prevents false negatives** (low score kasi walang outputs pero hindi pa naman na-execute!)


