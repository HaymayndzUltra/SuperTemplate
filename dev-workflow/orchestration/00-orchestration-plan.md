# Protocol 05b Split - Orchestration Plan

## Overview

Split Protocol 05b (2,532 lines) into 6 sequential protocols connected via artifacts, following the same pattern as Protocols 01-05.

## Structure

```
dev-workflow/orchestration/
├── 00-orchestration-plan.md (this file)
├── 05b-0-input-validation.md (PHASE 0-1)
├── 05b-1-classification.md (PHASE 2)
├── 05b-2-protocol-selection.md (PHASE 3)
├── 05b-3-gap-detection.md (PHASE 4 with loop control)
├── 05b-4-sequencing.md (PHASE 5)
└── 05b-5-execution-plan.md (PHASE 6-7)
```

## Artifact Flow

```
Protocol 05 artifacts
   ↓
05b-0: Input Validation
   OUTPUT: .artifacts/orchestration/validated-inputs.json
   ↓
05b-1: Classification
   OUTPUT: .artifacts/orchestration/classification.json
           .artifacts/orchestration/characteristics.json
   ↓
05b-2: Protocol Selection ←─────────────┐
   OUTPUT: .artifacts/orchestration/protocol-selection.json
   ↓                                     │
05b-3: Gap Detection                    │
   OUTPUT: .artifacts/orchestration/gap-analysis.json
   DECISION: IF gaps → Trigger Protocol Creation
             THEN → Loop back to 05b-2 ─┘
   ↓
05b-4: Sequencing
   OUTPUT: .artifacts/orchestration/protocol-sequence.json
   ↓
05b-5: Execution Plan
   OUTPUT: PROTOCOL-EXECUTION-PLAN.md
           PROTOCOL-CHECKLIST.md
```

## Triggering Logic

### Auto-Suggest Next Protocol

Each protocol includes logic to suggest next protocol based on current state:

**05b-0 → 05b-1**: Always (no conditions)

**05b-1 → 05b-2**: 
- IF classification confidence >= 85% → Auto-suggest 05b-2
- ELSE → Require manual review, then suggest 05b-2

**05b-2 → 05b-3**: Always (no conditions)

**05b-3 → Decision Point**:
- IF coverage >= 95% → Suggest 05b-4
- ELSE IF coverage < 95% AND iteration < 3 → Suggest Protocol Creation, then loop to 05b-2
- ELSE → Suggest manual gap resolution, then 05b-4

**05b-4 → 05b-5**: Always (no conditions)

**05b-5 → Complete**: Generate final artifacts, suggest execution start

## Loop Control (05b-3)

```json
{
  "max_iterations": 3,
  "current_iteration": 1,
  "loop_history": [
    {
      "iteration": 1,
      "coverage": 92.5,
      "gaps_detected": 3,
      "action": "trigger_protocol_creation"
    }
  ],
  "loop_decision": "continue|complete|manual_escalation"
}
```

## Integration with Protocol Creation

When 05b-3 detects gaps:

1. Generate gap specification from PROJECT-BRIEF context
2. Trigger Protocol Creation workflow (1-5)
3. Wait for validation (score >= 0.95)
4. Update protocol library
5. Loop back to 05b-2 with updated library

## Execution Models

### Option A: Manual Trigger (Current Pattern)
```bash
@apply dev-workflow/orchestration/05b-0-input-validation.md
# Review outputs
@apply dev-workflow/orchestration/05b-1-classification.md
# Review outputs
# ... continue
```

### Option B: Orchestrator Script (Recommended)
```bash
python scripts/orchestration/run_orchestration.py \
  --workspace /path/to/workspace \
  --auto-approve-high-confidence \
  --max-gap-iterations 3
```

## Success Criteria

- All 6 protocols independently executable
- Artifact-based handoffs validated
- Loop control prevents infinite iterations
- Protocol Creation integration seamless
- Same quality gates as current 05b
- Total execution time within 10% of current 05b

## Migration Path

1. ✅ Create 6 protocol files (this task)
2. Extract content from current 05b per phase
3. Test each protocol independently
4. Test loop control (05b-3 → 05b-2)
5. Test Protocol Creation integration
6. Create orchestrator script
7. Validate against test projects
8. Deprecate monolithic 05b

## File Size Targets

- 05b-0: ~350 lines (input validation + context loading)
- 05b-1: ~400 lines (classification + characteristics)
- 05b-2: ~450 lines (protocol selection logic)
- 05b-3: ~500 lines (gap detection + loop control + protocol creation trigger)
- 05b-4: ~400 lines (sequencing + dependency graph)
- 05b-5: ~400 lines (execution plan generation + handoff)

**Total: ~2,500 lines** (within 2% of current 2,532)
