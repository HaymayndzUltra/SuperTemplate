# Protocol 05b Split Plan - Complete Specification

**Date:** 2025-01-09  
**Status:** Planning Phase (Awaiting Verification)  
**Purpose:** Split Protocol 05b (2,532 lines) into 6 sequential protocols connected via artifacts

---

## 1. CURRENT STATE ANALYSIS

### Protocol 05b Structure (Monolithic)
```
.cursor/ai-driven-workflow/05b-project-protocol-orchestration-v2.md
├── Lines 1-365: Prerequisites, Identity, AI Role
├── Lines 366-611: PHASE 0-1 (Input Validation & Context Loading)
├── Lines 614-854: PHASE 2 (Classification & Characteristic Detection)
├── Lines 857-980: PHASE 3 (Protocol Selection)
├── Lines 982-1250: PHASE 4 (Gap Detection & Resolution)
├── Lines 1253-1850: PHASE 5 (Sequencing & Optimization)
└── Lines 1853-2532: PHASE 6-7 (Execution Plan Generation & Handoff)
```

**Total:** 2,532 lines in 1 file

---

## 2. PROPOSED SPLIT STRUCTURE

### File Organization
```
dev-workflow/orchestration/
├── SPLIT-PROTOCOL-05B-PLAN.md (this file - master plan)
├── 05b-0-input-validation.md (~350 lines)
├── 05b-1-classification.md (~400 lines)
├── 05b-2-protocol-selection.md (~450 lines)
├── 05b-3-gap-detection.md (~500 lines) ← CRITICAL: Protocol Creation integration
├── 05b-4-sequencing.md (~400 lines)
└── 05b-5-execution-plan.md (~400 lines)
```

**Total:** ~2,500 lines across 6 files (within 2% of original)

---

## 3. ARTIFACT FLOW DESIGN

### Sequential Handoff Pattern
```
Protocol 05 (existing)
   ↓ bootstrap-manifest.json, architecture-principles.md, PROJECT-BRIEF.md
   ↓
05b-0: Input Validation & Context Loading
   ↓ OUTPUT: .artifacts/orchestration/validated-inputs.json
   ↓
05b-1: Classification & Characteristic Detection
   ↓ OUTPUT: .artifacts/orchestration/classification.json
   ↓          .artifacts/orchestration/characteristics.json
   ↓
05b-2: Protocol Selection ←──────────────────────┐
   ↓ OUTPUT: .artifacts/orchestration/protocol-selection.json
   ↓                                              │
05b-3: Gap Detection & Resolution                │
   ↓ OUTPUT: .artifacts/orchestration/gap-analysis.json
   ↓          .artifacts/orchestration/loop-control.json
   ↓                                              │
   ↓ DECISION POINT:                             │
   ↓ IF coverage < 95%:                          │
   ↓    → Trigger Protocol Creation              │
   ↓    → Wait for completion                    │
   ↓    → Update protocol library                │
   ↓    → Loop back to 05b-2 ────────────────────┘
   ↓ ELSE:
   ↓    → Continue to 05b-4
   ↓
05b-4: Sequencing & Dependency Graph
   ↓ OUTPUT: .artifacts/orchestration/protocol-sequence.json
   ↓
05b-5: Execution Plan Generation
   ↓ OUTPUT: PROTOCOL-EXECUTION-PLAN.md
   ↓          PROTOCOL-CHECKLIST.md
   ↓
READY FOR EXECUTION
```

---

## 4. PROTOCOL CREATION INTEGRATION STRATEGY

### Integration Point: Protocol 05b-3 (Gap Detection)

#### Current Gap Detection (Lines 982-1029 in 05b)
```python
# Analyze gaps
gaps_detected = compare_requirements_vs_protocols()

if gaps_detected:
    print("[GAP DETECTED] Missing protocols identified")
    user_choice = input("Create missing protocols now? (Yes/No)")
    
    if user_choice == "yes":
        # MANUAL: User triggers Protocol Creation
        pass
```

#### Proposed Enhancement with Auto-Trigger
```python
# Analyze gaps
gap_analysis = {
    "coverage": 92.5,
    "gaps": [
        {
            "requirement": "Blockchain smart contract deployment",
            "context": {
                "tech_stack": ["solidity", "hardhat", "ethers.js"],
                "networks": ["ethereum", "polygon"],
                "security": ["slither", "mythril"],
                "deployment": ["mainnet", "testnet"]
            },
            "protocol_spec": {
                "number": "29",
                "name": "EVM Smart Contract Deployment",
                "phase": "5",
                "complexity": "high",
                "estimated_hours": 40
            }
        }
    ]
}

if gap_analysis["coverage"] < 95:
    for gap in gap_analysis["gaps"]:
        # AUTO-TRIGGER Protocol Creation with detailed spec
        trigger_protocol_creation(
            gap_spec=gap["protocol_spec"],
            context=gap["context"],
            requirements=extract_from_project_brief(gap["requirement"])
        )
        
        # Wait for Protocol Creation completion
        wait_for_protocol_validation(min_score=0.95)
        
        # Update protocol library
        add_to_library(new_protocol)
    
    # Loop back to 05b-2 for re-selection with updated library
    loop_control["iteration"] += 1
    trigger_protocol("05b-2", loop_control)
```

### Protocol Creation Workflow Trigger

**When 05b-3 detects gaps, it triggers:**
```
dev-workflow/protocol-creation/
├── 1-analyze-validator-requirements.md
├── 2-generate-protocol-structure.md
├── 3-create-protocol-content.md ← Receives gap_spec from 05b-3
├── 4-validate-protocol.md
└── 5-protocol-retrospective.md
```

**Gap Specification Format (passed to Protocol Creation):**
```json
{
  "protocol_number": "29",
  "protocol_name": "EVM Smart Contract Deployment",
  "protocol_purpose": "Deploy and verify Solidity smart contracts to Ethereum-compatible networks",
  "protocol_phase": "5 (MLOps & Deployment)",
  "requirements": {
    "extracted_from": "PROJECT-BRIEF.md",
    "keywords": ["blockchain", "smart contract", "solidity", "deployment"],
    "tech_stack": ["hardhat", "ethers.js", "solidity"],
    "deliverables": [
      "Compiled contract artifacts",
      "Deployment transaction receipts",
      "Etherscan verification proof"
    ]
  },
  "context": {
    "similar_protocol": "15 (Production Deployment)",
    "customizations": [
      "Add gas estimation step",
      "Add Slither security scan",
      "Add network selection logic",
      "Add Etherscan API verification"
    ]
  },
  "workflow_outline": [
    "Compile contracts with solc optimizer",
    "Run Slither/Mythril security analysis",
    "Estimate gas costs for deployment",
    "Deploy to selected network with retry logic",
    "Verify contract source code on block explorer",
    "Run integration tests against deployed contract"
  ],
  "quality_gates": [
    "Security scan: zero HIGH severity findings",
    "Gas cost: within budget constraints",
    "Deployment: confirmed on-chain",
    "Verification: source code matched"
  ]
}
```

**This detailed spec enables Protocol Creation to generate ~80% accurate protocol instead of ~60% generic.**

---

## 5. LOOP CONTROL MECHANISM

### Loop State Management

**Location:** `.artifacts/orchestration/loop-control.json`

**Schema:**
```json
{
  "max_iterations": 3,
  "current_iteration": 1,
  "loop_active": true,
  "history": [
    {
      "iteration": 1,
      "timestamp": "2025-01-09T06:00:00Z",
      "coverage_before": 92.5,
      "gaps_detected": 3,
      "protocols_created": ["29", "30", "31"],
      "action": "trigger_protocol_creation",
      "result": "success"
    }
  ],
  "decision": "continue|complete|manual_escalation"
}
```

### Loop Decision Logic (in 05b-3)

```python
def decide_next_action(gap_analysis, loop_control):
    coverage = gap_analysis["coverage"]
    iteration = loop_control["current_iteration"]
    max_iter = loop_control["max_iterations"]
    
    # SUCCESS: Coverage threshold met
    if coverage >= 95:
        return {
            "action": "continue_to_05b-4",
            "reason": "Coverage threshold met"
        }
    
    # CONTINUE: Gaps remain, iterations left
    elif coverage < 95 and iteration < max_iter:
        # Check if making progress
        if iteration > 1:
            prev_coverage = loop_control["history"][-1]["coverage_before"]
            if coverage <= prev_coverage:
                return {
                    "action": "manual_escalation",
                    "reason": "No progress after iteration"
                }
        
        return {
            "action": "trigger_protocol_creation",
            "reason": f"Coverage {coverage}% < 95%, iteration {iteration}/{max_iter}"
        }
    
    # FAIL: Max iterations reached, still gaps
    else:
        return {
            "action": "manual_escalation",
            "reason": f"Max iterations ({max_iter}) reached, coverage {coverage}%"
        }
```

---

## 6. FILE CONTENT MAPPING

### 05b-0: Input Validation & Context Loading
**Source:** Lines 366-611 of current 05b  
**Content:**
- STEP 2.1: Verify Protocol 05 Completion
- STEP 2.2: Validate PROJECT-BRIEF Integrity
- STEP 2.3: Confirm User Authorization
- STEP 3.1-3.5: Parse artifacts (PROJECT-BRIEF, architecture, bootstrap)
- Consolidate into validated-inputs.json

**Output Artifact:** `validated-inputs.json`

---

### 05b-1: Classification & Characteristic Detection
**Source:** Lines 614-854 of current 05b  
**Content:**
- STEP 4.1: Classify Project Type (with 4-step algorithm)
- STEP 4.2: Detect Characteristics (27+ dimensions)
- STEP 4.3: Generate Classification Reasoning
- Gate 1: Classification confidence check (<85% requires human review)

**Output Artifacts:** 
- `classification.json`
- `characteristics.json`
- `classification-reasoning.md`

---

### 05b-2: Protocol Selection
**Source:** Lines 857-980 of current 05b  
**Content:**
- STEP 5.1: Load Protocol Library (generic + AI protocols)
- STEP 5.2: Map Characteristics to Protocols
- STEP 5.3: Classify Protocols (REQUIRED/RECOMMENDED/MAYBE/SKIP)
- Gate 2: MAYBE protocols (user decision required)

**Output Artifact:** `protocol-selection.json`

**Re-entrant:** This protocol can be triggered multiple times by 05b-3 during gap filling loop

---

### 05b-3: Gap Detection & Resolution (CRITICAL)
**Source:** Lines 982-1250 of current 05b  
**Content:**
- STEP 5.3: Identify Coverage Gaps
- STEP 5.4: Generate Detailed Gap Specifications
- STEP 5.5: Decision Point (coverage >= 95%?)
- STEP 5.6: Trigger Protocol Creation (if gaps exist)
- STEP 5.7: Loop Control (max 3 iterations)
- Gate 3: Coverage threshold (>=95%, blocking)

**Output Artifacts:**
- `gap-analysis.json`
- `loop-control.json`
- `gap-specifications/*.json` (one per gap)

**Integration Points:**
- **Triggers:** `dev-workflow/protocol-creation/` (all 5 protocols)
- **Loops back to:** `05b-2` with updated protocol library
- **Escalates to:** Manual review if max iterations reached

---

### 05b-4: Sequencing & Dependency Graph
**Source:** Lines 1253-1850 of current 05b  
**Content:**
- STEP 6.1: Build Dependency Graph
- STEP 6.2: Topological Sort
- STEP 6.3: Identify Parallel Execution Opportunities
- STEP 6.4: Calculate Critical Path
- STEP 6.5: Estimate Timeline
- Gate 4: Sequence validation (no circular dependencies)

**Output Artifact:** `protocol-sequence.json`

---

### 05b-5: Execution Plan Generation
**Source:** Lines 1853-2532 of current 05b  
**Content:**
- STEP 7.1: Generate PROTOCOL-EXECUTION-PLAN.md
- STEP 7.2: Generate PROTOCOL-CHECKLIST.md
- STEP 7.3: Generate Customization Requirements
- STEP 7.4: Package Handoff Artifacts
- Gate 5: Stakeholder approval
- Gate 6: Final execution plan approval

**Output Artifacts:**
- `PROTOCOL-EXECUTION-PLAN.md` (workspace root)
- `PROTOCOL-CHECKLIST.md` (workspace root)
- `handoff-package.zip`

---

## 7. AUTOMATION SCRIPT REQUIREMENTS

### New Scripts Needed

#### 1. `scripts/orchestration/loop_controller.py`
**Purpose:** Manage loop state between 05b-3 and 05b-2  
**Functions:**
- `initialize_loop()` - Create loop-control.json
- `update_iteration()` - Increment iteration counter
- `check_progress()` - Compare current vs previous coverage
- `decide_action()` - Implement decision logic
- `trigger_protocol()` - Re-invoke 05b-2 or escalate

#### 2. `scripts/orchestration/trigger_protocol_creation.py`
**Purpose:** Trigger Protocol Creation workflow from 05b-3  
**Functions:**
- `generate_gap_spec()` - Create detailed gap specification
- `extract_context()` - Pull context from PROJECT-BRIEF
- `invoke_protocol_creation()` - Trigger dev-workflow/protocol-creation/
- `wait_for_completion()` - Monitor Protocol Creation progress
- `validate_output()` - Check new protocol score >= 0.95
- `update_library()` - Add new protocol to library

#### 3. `scripts/orchestration/protocol_library_manager.py`
**Purpose:** Manage protocol library updates  
**Functions:**
- `add_protocol()` - Add new protocol to library
- `reload_library()` - Refresh protocol list for 05b-2
- `validate_protocol()` - Check protocol meets standards
- `get_protocol_metadata()` - Extract protocol info

#### 4. `scripts/orchestration/orchestrator.py` (Optional)
**Purpose:** Run all 6 protocols in sequence  
**Functions:**
- `run_orchestration()` - Execute 05b-0 through 05b-5
- `handle_loop()` - Manage 05b-3 → 05b-2 loop
- `check_gates()` - Validate quality gates
- `generate_report()` - Consolidate all artifacts

---

## 8. QUALITY GATES DISTRIBUTION

### Gate 0: Input Completeness (05b-0)
- All Protocol 05 artifacts present
- PROJECT-BRIEF valid
- User authorization obtained

### Gate 1: Classification Confidence (05b-1)
- Confidence >= 85%
- If <85%, require human review

### Gate 2: MAYBE Protocol Decision (05b-2)
- User decides on MAYBE protocols
- Document rationale for inclusion/exclusion

### Gate 3: Coverage Threshold (05b-3) ← BLOCKING
- Coverage >= 95%
- If <95%, trigger Protocol Creation (max 3 iterations)
- Manual escalation if no progress

### Gate 4: Sequence Validation (05b-4)
- No circular dependencies
- All dependencies resolvable

### Gate 5: Stakeholder Review (05b-5)
- Timeline acceptable
- Resource estimates approved

### Gate 6: Final Approval (05b-5)
- Execution plan approved
- Ready for handoff

---

## 9. TRIGGERING MECHANISM

### Manual Trigger (Simplest)
```bash
# Sequential execution
@apply dev-workflow/orchestration/05b-0-input-validation.md
# Review .artifacts/orchestration/validated-inputs.json

@apply dev-workflow/orchestration/05b-1-classification.md
# Review classification.json, characteristics.json

@apply dev-workflow/orchestration/05b-2-protocol-selection.md
# Review protocol-selection.json

@apply dev-workflow/orchestration/05b-3-gap-detection.md
# May trigger Protocol Creation automatically
# May loop back to 05b-2

@apply dev-workflow/orchestration/05b-4-sequencing.md
# Review protocol-sequence.json

@apply dev-workflow/orchestration/05b-5-execution-plan.md
# Review PROTOCOL-EXECUTION-PLAN.md
```

### Orchestrator Script (Recommended)
```bash
python scripts/orchestration/orchestrator.py \
  --workspace $(pwd) \
  --auto-approve-classification-threshold 85 \
  --max-gap-iterations 3 \
  --auto-trigger-protocol-creation \
  --interactive-mode false
```

### Next Protocol Suggestion (Built into each protocol)
Each protocol ends with:
```
[PROTOCOL 05b-X | HANDOFF]
All quality gates passed.

Next Protocol: 05b-Y
Trigger Command: @apply dev-workflow/orchestration/05b-Y-<name>.md

Estimated Time: X-Y minutes
Required Decisions: [list if any]
```

---

## 10. MIGRATION & TESTING PLAN

### Phase 1: File Creation
- [ ] Create 6 protocol files
- [ ] Extract content from current 05b
- [ ] Map line ranges to new files
- [ ] Preserve all sections (Prerequisites, AI Role, Workflow, Gates, etc.)

### Phase 2: Artifact System
- [ ] Define all JSON schemas
- [ ] Create `.artifacts/orchestration/` directory structure
- [ ] Implement artifact validation scripts

### Phase 3: Loop Control
- [ ] Implement loop_controller.py
- [ ] Test 05b-3 → 05b-2 loop (manual)
- [ ] Test iteration limits (3 max)
- [ ] Test escalation logic

### Phase 4: Protocol Creation Integration
- [ ] Implement trigger_protocol_creation.py
- [ ] Test gap spec generation
- [ ] Test Protocol Creation invocation
- [ ] Test library update
- [ ] Validate end-to-end gap filling

### Phase 5: Orchestrator
- [ ] Create orchestrator.py
- [ ] Test sequential execution
- [ ] Test gate enforcement
- [ ] Test error handling

### Phase 6: Validation
- [ ] Run against 5 test projects (Generic Web, AI/ML, Hybrid, API, Mobile)
- [ ] Compare outputs with current 05b
- [ ] Measure execution time
- [ ] Verify all gates enforced

### Phase 7: Deprecation
- [ ] Mark current 05b as deprecated
- [ ] Update documentation
- [ ] Archive old 05b
- [ ] Update Protocol 05 to point to new orchestration workflow

---

## 11. SUCCESS CRITERIA

### Functional
- [ ] All 6 protocols executable independently
- [ ] Artifact handoffs work correctly
- [ ] Loop control prevents infinite loops (max 3 iterations)
- [ ] Protocol Creation integration works seamlessly
- [ ] Quality gates enforced correctly
- [ ] Output identical to current 05b (or better)

### Performance
- [ ] Total execution time within 10% of current 05b
- [ ] Gap detection under 5 minutes
- [ ] Protocol Creation integration under 15 minutes per gap

### Quality
- [ ] Each protocol passes its own validation
- [ ] No data loss in artifact handoffs
- [ ] All edge cases handled (low confidence, max iterations, no gaps)
- [ ] Error messages clear and actionable

### Maintainability
- [ ] Each file under 500 lines
- [ ] Clear separation of concerns
- [ ] Easy to modify individual phases
- [ ] Well-documented integration points

---

## 12. RISKS & MITIGATIONS

### Risk 1: Loop Logic Complexity
**Issue:** Loop control between 05b-3 and 05b-2 may be error-prone  
**Mitigation:** 
- Comprehensive loop state tracking (loop-control.json)
- Max iteration limit (3)
- Manual escalation fallback

### Risk 2: Protocol Creation Integration Failure
**Issue:** Auto-triggered Protocol Creation may produce low-quality protocols  
**Mitigation:**
- Detailed gap specification (not generic)
- Validation threshold (score >= 0.95)
- Manual review option for complex gaps

### Risk 3: State Serialization Overhead
**Issue:** Saving/loading JSON between protocols may slow execution  
**Mitigation:**
- Efficient JSON serialization
- Minimal artifact size
- Optional orchestrator script (keeps state in memory)

### Risk 4: Breaking Existing Workflows
**Issue:** Projects using current 05b may break  
**Mitigation:**
- Keep current 05b intact during migration
- Gradual rollout (new projects first)
- Comprehensive testing before deprecation

---

## 13. VERIFICATION CHECKLIST (FOR USER)

### Architecture
- [ ] Artifact flow makes sense (05b-0 → 05b-1 → ... → 05b-5)
- [ ] Loop control is clear (05b-3 → 05b-2 when gaps detected)
- [ ] Protocol Creation integration point is correct (05b-3)
- [ ] All phases from current 05b mapped to new files

### Integration Logic
- [ ] Gap specification format is sufficient for Protocol Creation
- [ ] Loop decision logic handles all cases (success, continue, fail)
- [ ] Max iterations (3) is reasonable
- [ ] Manual escalation path is clear

### Triggering Mechanism
- [ ] Next protocol suggestion is helpful
- [ ] Orchestrator script option is viable
- [ ] Manual trigger flow is documented

### Quality & Completeness
- [ ] All quality gates preserved from current 05b
- [ ] No missing functionality
- [ ] Edge cases handled
- [ ] Error handling comprehensive

### Migration Path
- [ ] Testing plan is thorough
- [ ] Validation criteria are measurable
- [ ] Deprecation strategy is safe

---

**VERIFICATION STATUS:** ⏳ AWAITING USER REVIEW

**NEXT STEPS AFTER APPROVAL:**
1. User verifies plan
2. User provides feedback/corrections
3. Begin Phase 1 (File Creation) after approval

---

**END OF PLAN**
