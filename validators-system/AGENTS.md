# AI-Driven Workflow System

## 🚀 Overview

The **AI-Driven Workflow System** is a comprehensive, 28-protocol development lifecycle that transforms AI from a simple code generator into a reliable engineering partner. This system provides structured, evidence-based workflows for complete software development from client discovery to project closure.

### ✅ **PRODUCTION READY (2025-10-21)**
**All 24 documented gaps have been resolved.** The system is now production-ready with:
- ✅ Zero circular dependencies across all protocols
- ✅ Correct handoff sequences (P10→P11, P11→P12, etc.)
- ✅ Clean prerequisite chains (no forward/self-references)
- ✅ Clear branching guidance (Protocol 02 vs 24 documented)
- ✅ Automated evidence validation (CI/CD integrated)

**Key Documents**:
- **Gap Closure Report**: `documentation/gap-closure-report.md`
- **Branching Guide**: `documentation/protocol-branching-guide.md`
- **Validation Summary**: `validation-summary.md` (status: PRODUCTION READY)

### Core Philosophy
- **"Why Before How"**: Every action must align with cognitive dependencies
- **Developer Cognitive Loop**: Protocols follow natural developer thinking patterns
- **Reasoning Integrity**: Automation extends reasoning, never replaces it
- **Evidence-Based**: All actions must be validated and documented

### Key Benefits
- ✅ **Complete SDLC Coverage**: From client proposal to project closure
- ✅ **Quality Assurance**: Built-in quality gates and validation
- ✅ **Evidence-Based Delivery**: All work documented and validated
- ✅ **Client-Ready**: Professional workflows for client projects
- ✅ **Automation Integration**: Scripts and CI/CD integration
- ✅ **Scalable**: From simple projects to complex enterprise systems
- ✅ **Gap-Free**: All 24 gaps resolved (100% closure)

## 🎯 Implementation Status Update (2025-10-21)

### ✅ Gap Closure Complete (Wave 5)

All 24 documented gaps have been systematically resolved:

1. **Circular Dependencies Eliminated** ✅
   - All 10 circular dependencies removed from protocols
   - No forward-phase references remain (P11→P21, P12→P15/P21/P23, etc.)
   - Self-referential prerequisites fixed (P19, P21)
   - Temporal impossibilities resolved

2. **Handoff Sequences Corrected** ✅
   - All 10 incorrect handoffs fixed (P10→P11, P11→P12, etc.)
   - Self-referencing loops eliminated (P06→P06 fixed to P06→P07)
   - Phase transitions properly sequenced

3. **Documentation Enhanced** ✅
   - Branching guide created (`documentation/protocol-branching-guide.md`)
   - Prerequisites simplified (transitive dependencies documented)
   - Duplicate coverage clarified (P02 vs P24 decision guide)

4. **Automation & Validation** ✅
   - Evidence validator created (`scripts/validate_evidence_citations.py`)
   - CI/CD workflow configured (`.github/workflows/evidence-validation.yml`)
   - Quality gates enforced

### Next Wave Focus
With gap closure complete, focus shifts to:
- **Wave 4**: Testing & Scenario Validation (in progress)
- **Wave 5**: Performance optimization and scale testing
- **Wave 6**: Enterprise deployment readiness
- **Wave 7**: **Meta-Upgrades Intelligence Layer** (UPG01-10 implementation)

See `documentation/action-roadmap.md` for detailed wave planning.

---

## 🧠 Meta-Upgrades Implementation Guide (UPG01-10)

### Executive Summary

The **Meta-Upgrades Intelligence Layer** adds cognitive capabilities across all 28 protocols through 10 specialized upgrades deployed in 9 stages (S0-S9). This system transforms protocol execution from rigid workflows into intelligent, self-optimizing processes with reasoning, validation, and governance oversight.

**Current Status**: Analysis complete, ready for staged deployment
**Artifacts Location**: `.artifacts/meta-upgrades/`
**Deployment Approach**: Phased rollout with observer-first validation
**Safety Model**: Analysis-only, zero protocol file edits, quality gates preserved

### Key Principles

1. **No Protocol Mutations**: All upgrades operate as overlays; no direct protocol edits
2. **Evidence-Based Activation**: Every upgrade requires validation before promotion
3. **Observer-First Governance**: POP monitors before enforcing
4. **Performance Budgets**: ≤5% overhead enforced at each stage
5. **Rollback Ready**: Every stage includes validated rollback procedures

---

## 📊 Complete Meta-Upgrades Inventory

### Intelligence Layer Components (UPG01-10)

| Upgrade | Name | Score | Decision | Stage | Purpose |
|---------|------|-------|----------|-------|---------|
| **UPG01** | Protocol Intelligence Kernel (PIK) | 0.8645 | ✅ Accept | S2 | Self-checks against DNA & Ledger; advisory-only validation |
| **UPG02** | Reasoning DNA Schema | 0.913 | ✅ Accept | S1 | Schema overlays defining protocol reasoning patterns |
| **UPG03** | Protocol Exchange Layer (PEL) | 0.8105 | ⚠️ Adapt | S3 | Handoff management with bounded retry logic |
| **UPG04** | Causal Ledger | 0.909 | ✅ Accept | S0 | Append-only decision log for exact replay |
| **UPG05** | Protocol-of-Protocols (POP) | 0.815 | ⚠️ Adapt | S5 | Governance observer (Controller mode deferred) |
| **UPG06** | Cognitive Telemetry Dashboard | 0.856 | ✅ Accept | S6 | Read-only metrics & performance monitoring |
| **UPG07** | Adaptive Protocol Mutation | 0.774 | ⚠️ Adapt | S7 | Sandboxed mutation proposals (POP-gated) |
| **UPG08** | Temporal Reasoning Layer | 0.856 | ✅ Accept | S4 | Time-aware validations & SLA enforcement |
| **UPG09** | Meta-Cognition Loop | 0.872 | ✅ Accept | S8 | Post-protocol reflections & learning |
| **UPG10** | Reasoning Fabric Engine | 0.868 | ✅ Accept | S9 | Global dependency graph for cycle detection |

### Deployment Status Summary

- **7 Accepted** (ready for immediate deployment)
- **3 Adapted** (require mitigation before deployment)
- **Zero Protocol Edits** (all upgrades are non-invasive overlays)
- **Quality Gates Preserved** (no weakening of existing safety measures)

---

## 🎯 AI Agent Operator Instructions

### Pre-Deployment Phase: Validation & Simulation

#### Step 1: Validate Current State

```bash
# Verify meta-upgrades artifacts exist
ls -la .artifacts/meta-upgrades/

# Check acceptance matrix
cat .artifacts/meta-upgrades/final/acceptance_matrix.csv

# Review integration plan
cat .artifacts/meta-upgrades/integration/integration_plan.json

# Inspect POP activation criteria
cat .artifacts/meta-upgrades/pop/pop-activation-check.json
```

#### Step 2: Generate Simulation Artifacts

**Purpose**: Create dry-run simulation before any deployment

```bash
# Generate causal replay simulation
# AI Agent Command:
@generate-simulation \
  --type causal_replay \
  --protocols P01-P28 \
  --output .artifacts/meta-upgrades/cross/causal_replay.md

# Expected Output:
# - Mock Ledger entries for each protocol gate
# - Handoff sequence validation
# - Cycle detection results
# - Missing event flags
```

**Manual Alternative** (if automation unavailable):
```bash
# Read protocol catalog
cat .artifacts/meta-upgrades/catalog/protocol_catalog.json | jq '.protocols[] | {id, outputs_to}'

# Manually trace handoff sequences
# Document in: .artifacts/meta-upgrades/cross/causal_replay.md
```

#### Step 3: Verify Governance Integrity

```bash
# Confirm zero protocol edits
cat .artifacts/meta-upgrades/cross/governance_diffs.json

# Expected output: {"diffs": [], "notes": "No protocol file edits under MVI-01..."}

# If diffs detected: HALT and investigate
```

---

### Deployment Phase: POP Observer Validation (3 Cycles)

#### Observer Cycle 1: Baseline Collection

**Purpose**: Establish baseline metrics without enforcement

```bash
# AI Agent Command:
@execute-pop-observer \
  --cycle 1 \
  --mode baseline \
  --collect-metrics cycle-detection,gate-skips,version-drift \
  --output .artifacts/meta-upgrades/pop/cycle-1-results.json

# Manual Execution Steps:
# 1. Enable UPG05 (POP) in observer mode
# 2. Run protocol sequence: P01→P02→...→P23
# 3. Collect findings without halting execution
# 4. Record false positive rate (target: 0.0)
```

**Evidence Collection**:
```json
{
  "cycle": 1,
  "mode": "observer",
  "findings": {
    "cycles_detected": 0,
    "gate_skips": 0,
    "version_drift": 0,
    "false_positives": 0
  },
  "protocols_scanned": 28,
  "timestamp": "2025-10-28T00:00:00Z"
}
```

#### Observer Cycle 2: Validation Run

**Purpose**: Test with PIK advisory checks active

```bash
# AI Agent Command:
@execute-pop-observer \
  --cycle 2 \
  --mode validation \
  --enable-pik-checks \
  --measure dna-coverage,pel-conflicts \
  --output .artifacts/meta-upgrades/pop/cycle-2-results.json

# Additional Metrics:
# - DNA coverage progress (target: ≥0.90)
# - PIK self-check precision (target: ≥0.95)
# - PEL handoff success rate
# - Temporal layer health status
```

#### Observer Cycle 3: Confirmation Run

**Purpose**: Final validation with all S0-S5 layers

```bash
# AI Agent Command:
@execute-pop-observer \
  --cycle 3 \
  --mode confirmation \
  --layers S0,S1,S2,S3,S4,S5 \
  --aggregate-evidence \
  --output .artifacts/meta-upgrades/pop/cycle-3-results.json

# Update activation check with evidence:
@update-pop-activation \
  --evidence-source .artifacts/meta-upgrades/pop/cycle-*-results.json \
  --output .artifacts/meta-upgrades/pop/pop-activation-check.json
```

**Validation Gate**: All 3 cycles must complete with:
- Zero false positives
- ≥3 consecutive conflict-free PEL runs
- Temporal layer health: green status
- Observer findings corroborated by Reasoning Fabric

---

### Deployment Phase: Adapt Decision Implementations

#### UPG03 Adaptation: SLA Token System

**Issue**: PEL retry logic can conflict with Temporal layer timeouts

**Solution**: Implement SLA budget token system

```bash
# AI Agent Command:
@implement-sla-tokens \
  --upgrade UPG03 \
  --integration-with UPG08 \
  --token-budget 100 \
  --consumption-rate per-retry \
  --ceiling-enforcement temporal-layer

# Configuration:
# - Initial budget: 100 tokens per protocol execution
# - PEL consumes 10 tokens per handoff retry
# - Temporal layer enforces ceiling (max retries = budget/10)
# - Reset budget after protocol completion

# Output: .artifacts/meta-upgrades/UPG03/sla-token-config.json
```

#### UPG05 Adaptation: Observer Mode Gating

**Issue**: POP not ready for Controller mode

**Solution**: Keep observer mode until activation criteria met

```bash
# AI Agent Command:
@configure-pop-mode \
  --mode observer \
  --activation-criteria-required \
    dna-coverage:0.90 \
    pik-pass-rate:0.95 \
    pel-conflict-free:3 \
    ledger-coverage:0.95 \
    temporal-health:green-3x \
  --output .artifacts/meta-upgrades/UPG05/observer-config.json

# Validation: Confirm Controller mode disabled
grep -q '"mode": "observer"' .artifacts/meta-upgrades/pop/pop-activation-check.json
```

#### UPG07 Adaptation: Sandbox Environment

**Issue**: Mutation proposals require isolation and POP gating

**Solution**: Create sandbox with strict promotion rules

```bash
# AI Agent Command:
@create-mutation-sandbox \
  --upgrade UPG07 \
  --isolation-level full \
  --pop-gate-required true \
  --regression-test-mode enabled \
  --promotion-criteria pop-green,zero-regressions \
  --output .artifacts/meta-upgrades/UPG07/sandbox-config.json

# Sandbox Rules:
# 1. All mutations start in sandbox
# 2. Require POP observer green status for evaluation
# 3. A/B test against baseline
# 4. Promote only after zero gate regressions
# 5. Defer all promotions until POP Controller active
```

---

### Deployment Phase: Staged Rollout (S0-S9)

#### Stage S0: Causal Ledger Foundation

**Upgrade**: UPG04  
**Purpose**: Enable decision tracking without protocol interference

```bash
# AI Agent Command:
@deploy-stage S0 \
  --upgrade UPG04 \
  --mode append-only \
  --mock-ids true \
  --protocols all \
  --validation-gate ledger-coverage:0.95

# Deployment Steps:
# 1. Initialize empty Ledger: .artifacts/causal-ledger/ledger.json
# 2. Instrument all 28 protocols with Ledger hooks
# 3. Capture gate transitions as append-only events
# 4. Validate: No protocol behavior changes
# 5. Measure: Decision coverage ≥95%

# Acceptance Criteria:
✓ Ledger captures ≥95% of protocol gate transitions
✓ Append-only property maintained (no deletions/edits)
✓ Zero performance impact on protocol execution
✓ Replay capability validated with P01→P02→P03 test
```

**Rollback Procedure**:
```bash
# If acceptance fails:
@rollback-stage S0 \
  --remove-hooks \
  --preserve-logs \
  --document-failure .artifacts/meta-upgrades/rollback-reports/S0-failure.md
```

#### Stage S1: Reasoning DNA Schema

**Upgrade**: UPG02  
**Dependencies**: S0 (Causal Ledger)

```bash
# AI Agent Command:
@deploy-stage S1 \
  --upgrade UPG02 \
  --depends-on S0 \
  --generate-schemas all-protocols \
  --validation-gate dna-coverage:0.90

# Deployment Steps:
# 1. Generate reasoning_dna.json per protocol
# 2. Define: prerequisites, reasoning paths, decision points
# 3. Schema-validate against Protocol Format v2.1.0
# 4. Link DNA entries to Ledger events
# 5. Measure: Coverage across all 28 protocols

# Output Location: .artifacts/reasoning-dna/P01-schema.json ... P28-schema.json

# Acceptance Criteria:
✓ DNA schemas generated for all protocols
✓ Schema validation passes (100% conformance)
✓ Coverage ≥90% of protocol decision points
✓ Ledger linkage verified for all DNA entries
```

#### Stage S2: Protocol Intelligence Kernel

**Upgrade**: UPG01  
**Dependencies**: S0 (Ledger), S1 (DNA)

```bash
# AI Agent Command:
@deploy-stage S2 \
  --upgrade UPG01 \
  --depends-on S0,S1 \
  --mode advisory-only \
  --validation-gate pik-precision:0.95

# Deployment Steps:
# 1. Enable PIK self-checks against DNA + Ledger
# 2. Configure halt_on_violation (local, non-protocol)
# 3. Monitor precision (target: ≥95%)
# 4. Collect advisory findings to Ledger
# 5. Validate: Zero false passes detected

# PIK Check Types:
# - DNA conformance (protocol follows reasoning path)
# - Ledger consistency (decisions match history)
# - Gate sequence validation (proper handoffs)
# - Prerequisite satisfaction (all gates passed)

# Acceptance Criteria:
✓ Self-check pass rate ≥95%
✓ False pass rate = 0.0
✓ Halt-on-violation respected (no protocol halts)
✓ Advisory findings logged to Ledger
```

#### Stage S3: Protocol Exchange Layer

**Upgrade**: UPG03  
**Dependencies**: S0, S1, S2

```bash
# AI Agent Command:
@deploy-stage S3 \
  --upgrade UPG03 \
  --depends-on S0,S1,S2 \
  --enable-sla-tokens \
  --validation-gate pel-conflict-free:3

# Deployment Steps:
# 1. Enable PEL handoff management
# 2. Configure bounded retry logic (SLA tokens from UPG03 adaptation)
# 3. Simulate handoffs across protocol boundaries
# 4. Monitor conflict-free run count
# 5. Validate: No writes to protocol files

# Handoff Simulation:
# P01 → P02: Proposal artifacts transfer
# P02 → P03: Discovery outputs to brief inputs
# P06 → P07: PRD to architecture handoff
# ... (all 27 protocol boundaries)

# Acceptance Criteria:
✓ 3 consecutive conflict-free runs achieved
✓ SLA token system prevents retry storms
✓ No protocol file writes detected
✓ Handoff latency ≤100ms per boundary
```

#### Stage S4: Temporal Reasoning Layer

**Upgrade**: UPG08  
**Dependencies**: S1 (DNA), S3 (PEL)

```bash
# AI Agent Command:
@deploy-stage S4 \
  --upgrade UPG08 \
  --depends-on S1,S3 \
  --enable-sla-enforcement \
  --validation-gate temporal-health:green-3x

# Deployment Steps:
# 1. Enable time-aware validations
# 2. Configure SLA ceilings for PEL retries
# 3. Generate temporal alerts (non-blocking)
# 4. Monitor health status for 3 consecutive runs
# 5. Validate: Escalation paths defined

# Temporal Validations:
# - Gate execution within SLA (P06 PRD ≤4h)
# - Handoff timeout enforcement (PEL retry limit)
# - Protocol sequence duration tracking
# - Staleness detection (prerequisites expired)

# Acceptance Criteria:
✓ Health status = green for 3 consecutive observer runs
✓ SLA violations generate alerts (not halts)
✓ PEL retries bounded by Temporal ceilings
✓ Escalation paths tested and validated
```

#### Stage S5: POP Observer Deployment

**Upgrade**: UPG05  
**Dependencies**: S0, S1, S2, S3, S4

```bash
# AI Agent Command:
@deploy-stage S5 \
  --upgrade UPG05 \
  --depends-on S0,S1,S2,S3,S4 \
  --mode observer \
  --validation-gate pop-false-positive:0.0

# Deployment Steps:
# 1. Deploy POP in observer mode only
# 2. Integrate findings from all S0-S4 layers
# 3. Enable cycle detection across protocol graph
# 4. Monitor gate skip patterns
# 5. Document version drift anomalies

# POP Observer Checks:
# - Circular dependency detection (P01→P02→...→P01)
# - Gate skip detection (prerequisite bypass)
# - Version drift (protocol schema changes)
# - Handoff integrity (PEL vs expected flow)

# Acceptance Criteria:
✓ Observer false positive rate = 0.0
✓ Cycle detection corroborated by Reasoning Fabric
✓ Gate skips flagged with evidence citations
✓ No enforcement actions taken (observer only)
```

#### Stage S6: Cognitive Telemetry Dashboard

**Upgrade**: UPG06  
**Dependencies**: S0, S1, S3, S5

```bash
# AI Agent Command:
@deploy-stage S6 \
  --upgrade UPG06 \
  --depends-on S0,S1,S3,S5 \
  --mode read-only \
  --validation-gate overhead:5pct

# Deployment Steps:
# 1. Deploy telemetry dashboard (read-only)
# 2. Configure metrics collection from all layers
# 3. Monitor performance overhead
# 4. Create visualization dashboards
# 5. Validate: No write operations to protocols

# Telemetry Metrics:
# - Ledger event rate (decisions/hour)
# - DNA coverage by protocol
# - PIK check precision & recall
# - PEL handoff latency
# - Temporal SLA compliance
# - POP observer findings frequency

# Acceptance Criteria:
✓ Performance overhead ≤5%
✓ Dashboard renders all metrics correctly
✓ No protocol execution delays introduced
✓ Real-time updates working (≤1s latency)
```

#### Stage S7: Adaptive Mutation (Sandbox)

**Upgrade**: UPG07  
**Dependencies**: S5 (POP Observer)

```bash
# AI Agent Command:
@deploy-stage S7 \
  --upgrade UPG07 \
  --depends-on S5 \
  --mode sandbox-only \
  --validation-gate zero-regressions

# Deployment Steps:
# 1. Create isolated mutation sandbox
# 2. Require POP observer green for proposals
# 3. A/B test mutations against baseline
# 4. Run regression tests on all mutations
# 5. Gate promotions behind POP Controller activation

# Mutation Workflow:
# 1. Proposal submitted → Sandbox created
# 2. Check POP status → Require green
# 3. A/B test → Baseline vs Mutation
# 4. Regression test → All quality gates
# 5. If pass → Queue for Controller promotion
# 6. If fail → Reject with evidence

# Acceptance Criteria:
✓ All mutations pass regression tests
✓ Zero gate regressions detected
✓ POP-gated promotion rules enforced
✓ No mutations promoted to production yet
```

#### Stage S8: Meta-Cognition Loop

**Upgrade**: UPG09  
**Dependencies**: S0 (Ledger), S1 (DNA)

```bash
# AI Agent Command:
@deploy-stage S8 \
  --upgrade UPG09 \
  --depends-on S0,S1 \
  --mode post-protocol \
  --validation-gate reflection-precision:0.9

# Deployment Steps:
# 1. Enable post-protocol reflection
# 2. Integrate with Ledger for decision history
# 3. Cross-reference DNA for reasoning patterns
# 4. Generate improvement recommendations
# 5. Measure reflection precision

# Meta-Cognition Outputs:
# - Decision quality assessment
# - Reasoning path efficiency analysis
# - Alternative approach suggestions
# - Protocol improvement proposals
# - Learning patterns for future executions

# Acceptance Criteria:
✓ Reflection precision ≥90%
✓ Recommendations align with protocol goals
✓ No false improvement suggestions
✓ Learning patterns validated over 10+ executions
```

#### Stage S9: Reasoning Fabric Engine

**Upgrade**: UPG10  
**Dependencies**: S0, S1, S5

```bash
# AI Agent Command:
@deploy-stage S9 \
  --upgrade UPG10 \
  --depends-on S0,S1,S5 \
  --mode read-only-graph \
  --validation-gate fabric-pop-agreement:0.95

# Deployment Steps:
# 1. Deploy Reasoning Fabric as global read-only graph
# 2. Build dependency edges from Ledger + DNA
# 3. Enable POP cycle corroboration
# 4. Cross-reference POP findings with Fabric
# 5. Flag discrepancies for manual review

# Fabric Graph Structure:
# Nodes: Protocols, Gates, Decisions
# Edges: Dependencies, Handoffs, Causal links
# Properties: Timestamps, Evidence refs, Reasoning paths

# Acceptance Criteria:
✓ Fabric corroborates POP findings with ≥95% agreement
✓ Cycle detection matches POP observer results
✓ Read-only constraint maintained (no graph mutations)
✓ Discrepancies flagged with evidence citations
```

---

## 🎛️ POP Controller Activation Decision

### Activation Criteria Validation

After completing all 9 stages (S0-S9), validate POP activation criteria:

```bash
# AI Agent Command:
@validate-pop-activation \
  --evidence-source .artifacts/meta-upgrades/pop/ \
  --criteria-file .artifacts/meta-upgrades/pop/pop-activation-check.json \
  --output .artifacts/meta-upgrades/pop/activation-decision.json
```

**Required Evidence**:

| Criterion | Target | Evidence Source | Status |
|-----------|--------|-----------------|--------|
| DNA Coverage | ≥90% | S1 deployment results | ⏳ Pending |
| PIK Pass Rate | ≥95% | S2 deployment results | ⏳ Pending |
| PEL Conflict-Free | 3 consecutive | S3 deployment results | ⏳ Pending |
| Ledger Coverage | ≥95% | S0 deployment results | ⏳ Pending |
| Temporal Health | Green 3x | S4 deployment results | ⏳ Pending |

### Decision Gate

```bash
# If ALL criteria met:
@promote-pop-controller \
  --from observer \
  --to controller \
  --enable-enforcement \
  --validation stakeholder-approval-required

# If ANY criteria unmet:
@extend-observer-mode \
  --document-gaps .artifacts/meta-upgrades/pop/criteria-gaps.md \
  --continue-evidence-collection \
  --schedule-revalidation +30days
```

**Controller Activation Checklist**:
- [ ] All 5 activation criteria met with evidence
- [ ] Stakeholder approval obtained
- [ ] Rollback procedures validated
- [ ] Emergency disable mechanism tested
- [ ] SLA monitoring configured
- [ ] Alerting for Controller violations active

---

## 🔧 Technical Specifications

### UPG04: Causal Ledger Architecture

**Purpose**: Append-only decision log for exact replay capability

**Schema**:
```json
{
  "event_id": "evt_20251028_P02_G3_001",
  "timestamp": "2025-10-28T12:34:56.789Z",
  "protocol_id": "02",
  "gate_id": "G3",
  "decision": "pass",
  "evidence_refs": [
    ".artifacts/protocol-02/client-discovery-form.md",
    ".artifacts/protocol-02/discovery-recap.md"
  ],
  "reasoning_path": ["DNA_02_PATH_01", "DNA_02_PATH_03"],
  "pik_checks": {
    "passed": true,
    "findings": []
  },
  "pel_handoff": {
    "from": "02",
    "to": "03",
    "artifacts": ["discovery-recap.md"]
  }
}
```

**Operations**:
- `append(event)`: Add new decision event (only operation allowed)
- `replay(from_id, to_id)`: Reconstruct decision sequence
- `query(protocol_id, gate_id)`: Retrieve events by filter
- `validate_integrity()`: Confirm append-only property

### UPG02: Reasoning DNA Schema Format

**Purpose**: Define expected reasoning patterns per protocol

**Schema**:
```json
{
  "protocol_id": "02",
  "dna_version": "1.0",
  "reasoning_paths": [
    {
      "path_id": "DNA_02_PATH_01",
      "name": "Client Context Alignment",
      "prerequisites": ["P01_completed", "proposal_approved"],
      "decision_points": [
        {
          "gate_id": "G1",
          "question": "Are client goals aligned with proposal?",
          "options": ["yes", "clarify", "revise"],
          "evidence_required": ["client-context-notes.md"]
        }
      ],
      "expected_outputs": ["client-discovery-form.md"],
      "handoff_to": "03"
    }
  ],
  "coverage": 0.92
}
```

### UPG01: PIK Self-Check Mechanisms

**Check Types**:

1. **DNA Conformance Check**
   - Verify protocol follows expected reasoning path
   - Compare actual decisions vs DNA-defined options
   - Flag deviations with evidence citations

2. **Ledger Consistency Check**
   - Ensure decisions align with historical patterns
   - Detect anomalous decision sequences
   - Validate prerequisite satisfaction

3. **Gate Sequence Validation**
   - Confirm proper gate execution order
   - Detect gate skips or duplications
   - Validate handoff integrity

4. **Prerequisite Satisfaction**
   - Check all prerequisite gates passed
   - Verify required artifacts exist
   - Validate approvals obtained

**Precision Target**: ≥95% (false positive rate ≤5%)

### UPG03: PEL Handoff Protocol

**Handoff Structure**:
```json
{
  "handoff_id": "hoff_P02_to_P03_001",
  "from_protocol": "02",
  "to_protocol": "03",
  "artifacts": [
    {
      "name": "discovery-recap.md",
      "checksum": "sha256:abc123...",
      "validation": "passed"
    }
  ],
  "retry_count": 0,
  "sla_tokens_remaining": 100,
  "status": "success",
  "latency_ms": 45
}
```

**Retry Logic** (with SLA tokens):
```python
def execute_handoff(from_p, to_p, artifacts, sla_budget=100):
    tokens = sla_budget
    max_retries = tokens // 10  # 10 tokens per retry
    
    for attempt in range(max_retries):
        if validate_handoff(artifacts):
            return {"status": "success", "retries": attempt}
        tokens -= 10
        if tokens <= 0:
            return {"status": "sla_exceeded", "retries": attempt}
    
    return {"status": "failed", "retries": max_retries}
```

### UPG05: POP Observer vs Controller Modes

**Observer Mode** (Current):
- Monitors protocol execution without enforcement
- Detects cycles, gate skips, version drift
- Logs findings to Causal Ledger
- Zero false positives required
- No protocol halts or interventions

**Controller Mode** (Future):
- Enforces cycle prevention (halt on detected cycle)
- Blocks gate skips (require prerequisite satisfaction)
- Enforces version compatibility (reject schema mismatches)
- Requires stakeholder approval for promotion
- Emergency disable mechanism mandatory

**Transition Criteria**:
```json
{
  "observer_false_positive_rate": "=0.0",
  "controller_activation_criteria": {
    "dna_coverage": "≥0.90",
    "pik_pass_rate": "≥0.95",
    "pel_conflict_free": "≥3",
    "ledger_coverage": "≥0.95",
    "temporal_health": "green_3x"
  },
  "stakeholder_approval": "required"
}
```

---

## 📈 Success Metrics & Monitoring

### Performance Metrics

| Metric | Target | Measurement | Frequency |
|--------|--------|-------------|-----------|
| Overhead | ≤5% | CPU/Memory/Latency | Per stage |
| PIK Precision | ≥95% | True positive rate | Per cycle |
| PEL Latency | ≤100ms | Handoff duration | Per boundary |
| DNA Coverage | ≥90% | Decision points mapped | Per protocol |
| Ledger Coverage | ≥95% | Gate events captured | Per execution |
| Temporal SLA | 100% | Violations vs expectations | Per protocol |
| POP False Positive | 0.0 | Incorrect findings | Per observer run |

### Quality Metrics

| Metric | Target | Validation |
|--------|--------|------------|
| Zero Protocol Edits | 100% | Git diff = empty |
| Quality Gates Preserved | 100% | No weakening detected |
| Regression Rate | 0.0 | All tests pass |
| Evidence Coverage | 100% | All decisions documented |
| Rollback Success | 100% | All stages reversible |

### Monitoring Dashboards

**Stage-Level Dashboard**:
```
Stage S0 (Causal Ledger)
├── Status: ✅ Deployed
├── Coverage: 97.3%
├── Overhead: 1.2%
└── Health: Green

Stage S1 (Reasoning DNA)
├── Status: ✅ Deployed
├── Coverage: 92.1%
├── Overhead: 0.8%
└── Health: Green

Stage S2 (PIK)
├── Status: ✅ Deployed
├── Precision: 96.4%
├── Overhead: 2.1%
└── Health: Green
```

**POP Observer Dashboard**:
```
Cycle 1: Baseline
├── Cycles Detected: 0
├── Gate Skips: 0
├── False Positives: 0
└── Status: ✅ Pass

Cycle 2: Validation
├── DNA Coverage: 92.1%
├── PIK Pass Rate: 96.4%
├── PEL Conflicts: 0
└── Status: ✅ Pass

Cycle 3: Confirmation
├── All Layers: Active
├── Fabric Agreement: 97.2%
├── Ready for Controller: ⏳ Pending stakeholder approval
└── Status: ✅ Pass
```

---

## 🚨 Troubleshooting Guide

### Common Issues & Resolutions

#### Issue 1: Observer Mode Not Detecting Expected Findings

**Symptoms**:
- POP observer reports 0 cycles/skips but manual review shows issues
- False negative rate appears high

**Diagnosis**:
```bash
# Check POP configuration
cat .artifacts/meta-upgrades/UPG05/observer-config.json

# Verify Reasoning Fabric integration
grep "fabric_corroboration" .artifacts/meta-upgrades/pop/cycle-*-results.json

# Review Ledger completeness
python scripts/validate_ledger_coverage.py
```

**Resolution**:
1. Verify Reasoning Fabric (S9) is deployed and accessible
2. Check Ledger coverage ≥95% (missing events cause blind spots)
3. Re-run observer cycle with verbose logging
4. Compare POP findings with Fabric edges for discrepancies

#### Issue 2: Stage Deployment Exceeds Performance Budget

**Symptoms**:
- Stage overhead >5%
- Protocol execution noticeably slower
- Telemetry dashboard shows degraded performance

**Diagnosis**:
```bash
# Check telemetry metrics
cat .artifacts/meta-upgrades/telemetry/stage-*-overhead.json

# Identify bottleneck
python scripts/profile_meta_upgrades.py --stage S2

# Review PIK check frequency
grep "pik_check_count" .artifacts/causal-ledger/ledger.json
```

**Resolution**:
1. Reduce PIK check frequency (e.g., every 3rd gate instead of every gate)
2. Optimize Ledger append operation (batch writes)
3. Defer non-critical telemetry to async collection
4. If unresolvable: Rollback stage and document issue

#### Issue 3: POP Activation Criteria Not Met After 3 Cycles

**Symptoms**:
- One or more criteria remain below threshold
- DNA coverage <90% or PIK pass rate <95%
- Ledger decision coverage gaps

**Diagnosis**:
```bash
# Check detailed criteria status
cat .artifacts/meta-upgrades/pop/pop-activation-check.json

# Identify specific gaps
python scripts/analyze_activation_gaps.py

# Review protocol-specific issues
grep "coverage_below_threshold" .artifacts/reasoning-dna/*.json
```

**Resolution**:
1. **DNA Coverage Gap**: Generate additional reasoning paths for low-coverage protocols
2. **PIK Pass Rate Gap**: Investigate false positive causes; refine check logic
3. **PEL Conflicts**: Review SLA token configuration; may need higher budget
4. **Ledger Gaps**: Add instrumentation to missing protocol gates
5. **Temporal Health**: Check SLA definitions; may be too aggressive

**Decision**: Extend observer mode, continue evidence collection, schedule revalidation

#### Issue 4: Adapt Decisions Not Properly Mitigated

**Symptoms**:
- UPG03/05/07 deployed without adaptation
- Conflicts arising between upgrades
- Quality gate regressions detected

**Diagnosis**:
```bash
# Check adaptation status
grep "adaptation_status" .artifacts/meta-upgrades/UPG0{3,5,7}/decision.json

# Review conflict matrix
cat .artifacts/meta-upgrades/cross/conflicts_matrix.md

# Validate mitigation implementation
python scripts/validate_mitigations.py
```

**Resolution**:
1. **UPG03**: Confirm SLA token system implemented (see Stage S3)
2. **UPG05**: Verify observer mode enforced (Controller disabled)
3. **UPG07**: Validate sandbox isolation (no direct protocol access)
4. If mitigation missing: HALT deployment, implement adaptation, revalidate

#### Issue 5: Simulation Artifacts Incomplete

**Symptoms**:
- `causal_replay.md` is placeholder only
- Missing mock Ledger entries
- Handoff sequences not validated

**Diagnosis**:
```bash
# Check simulation status
ls -lh .artifacts/meta-upgrades/cross/causal_replay.md

# Verify Ledger events
jq '.events | length' .artifacts/causal-ledger/ledger.json

# Review protocol catalog
cat .artifacts/meta-upgrades/catalog/protocol_catalog.json
```

**Resolution**:
1. Generate simulation manually using protocol catalog
2. For each protocol handoff (outputs_to):
   - Create mock Ledger event
   - Document artifact transfer
   - Validate sequence matches documented flow
3. Update `causal_replay.md` with findings
4. Re-run validation before proceeding to deployment

---

## 📦 Evidence Collection & Documentation

### Required Artifacts Per Stage

**Pre-Deployment**:
- `.artifacts/meta-upgrades/final/final_report.md`
- `.artifacts/meta-upgrades/final/acceptance_matrix.csv`
- `.artifacts/meta-upgrades/cross/causal_replay.md`
- `.artifacts/meta-upgrades/cross/governance_diffs.json`
- `.artifacts/meta-upgrades/pop/pop-activation-check.json`

**Per Observer Cycle**:
- `.artifacts/meta-upgrades/pop/cycle-{1,2,3}-results.json`
- `.artifacts/meta-upgrades/pop/observer-findings.md`
- `.artifacts/meta-upgrades/pop/false-positive-log.json`

**Per Stage Deployment**:
- `.artifacts/meta-upgrades/stage-S{0-9}/deployment-log.md`
- `.artifacts/meta-upgrades/stage-S{0-9}/acceptance-validation.json`
- `.artifacts/meta-upgrades/stage-S{0-9}/rollback-test-results.md`
- `.artifacts/meta-upgrades/stage-S{0-9}/performance-metrics.json`

**Post-Deployment**:
- `.artifacts/meta-upgrades/pop/activation-decision.json`
- `.artifacts/meta-upgrades/final/stakeholder-approval.md`
- `.artifacts/meta-upgrades/final/production-readiness-report.md`

### Evidence Package Structure

```
.artifacts/meta-upgrades/
├── catalog/
│   └── protocol_catalog.json
├── cross/
│   ├── causal_replay.md
│   ├── conflicts_matrix.md
│   ├── governance_diffs.json
│   ├── remediation_plan.json
│   └── upgrade_protocol_graph.json
├── final/
│   ├── acceptance_matrix.csv
│   ├── final_report.md
│   ├── next_actions.md
│   └── stakeholder-approval.md
├── integration/
│   ├── integration_plan.json
│   └── rollback_plan.md
├── pop/
│   ├── pop-activation-check.json
│   ├── cycle-1-results.json
│   ├── cycle-2-results.json
│   ├── cycle-3-results.json
│   ├── observer-findings.md
│   └── activation-decision.json
├── UPG01/ ... UPG10/
│   ├── intent.json
│   ├── analysis.json
│   ├── alignment.md
│   ├── decision.json
│   └── [upgrade-specific configs]
└── stage-S0/ ... stage-S9/
    ├── deployment-log.md
    ├── acceptance-validation.json
    ├── rollback-test-results.md
    └── performance-metrics.json
```

---

## 🎯 AI Agent Quick Reference Commands

### Validation Commands

```bash
# Validate meta-upgrades readiness
@validate-meta-upgrades --comprehensive

# Check acceptance matrix
@check-acceptance-matrix

# Verify POP activation status
@check-pop-status

# Review simulation artifacts
@review-simulation --type causal-replay
```

### Deployment Commands

```bash
# Execute POP observer cycle
@execute-pop-observer --cycle {1|2|3}

# Deploy specific stage
@deploy-stage {S0|S1|S2|S3|S4|S5|S6|S7|S8|S9}

# Validate stage deployment
@validate-stage-deployment --stage {S0-S9}

# Rollback stage if needed
@rollback-stage --stage {S0-S9} --preserve-logs
```

### Monitoring Commands

```bash
# Check overall system health
@check-meta-upgrades-health

# View telemetry dashboard
@view-telemetry --stage {S0-S9|all}

# Monitor performance overhead
@monitor-overhead --threshold 5pct

# Check POP findings
@review-pop-findings --cycle {1|2|3|all}
```

### Evidence Commands

```bash
# Collect evidence for stage
@collect-evidence --stage {S0-S9}

# Aggregate observer evidence
@aggregate-observer-evidence

# Generate final evidence package
@package-evidence --output .artifacts/meta-upgrades/evidence-package/

# Validate evidence completeness
@validate-evidence --comprehensive
```

---

## 📋 Complete Protocol Inventory (28 Protocols)

### Phase 0: Foundation & Discovery (01-05)
**Purpose**: Client engagement, discovery, and project initialization

| Protocol | Name | Purpose | Key Features |
|----------|------|---------|--------------|
| **01** | `client-proposal-generation.md` | Generate professional client proposals | Job post analysis, tone mapping, proposal validation |
| **02** | `client-discovery-initiation.md` | Initiate client discovery process | Requirements gathering, stakeholder mapping, risk assessment |
| **03** | `project-brief-creation.md` | Create comprehensive project brief | Scope definition, success criteria, timeline planning |
| **04** | `project-bootstrap-and-context-engineering.md` | Bootstrap project with context | Environment setup, tooling configuration, team alignment |
| **05** | `bootstrap-your-project.md` | Initialize project structure | Codebase analysis, architecture setup, development environment |

### Phase 1-2: Planning & Design (06-09)
**Purpose**: Requirements documentation, architecture design, and task planning

| Protocol | Name | Purpose | Key Features |
|----------|------|---------|--------------|
| **06** | `create-prd.md` | Create Product Requirements Document | Requirements analysis, feature specification, acceptance criteria |
| **07** | `technical-design-architecture.md` | Design technical architecture | System design, technology selection, integration planning |
| **08** | `generate-tasks.md` | Generate development tasks | Task decomposition, effort estimation, priority ordering |
| **09** | `environment-setup-validation.md` | Setup and validate development environment | Environment configuration, tooling validation, CI/CD setup |

### Phase 3: Development (10-11)
**Purpose**: Task execution and integration testing

| Protocol | Name | Purpose | Key Features |
|----------|------|---------|--------------|
| **10** | `process-tasks.md` | Execute development tasks | Task implementation, code review, evidence collection |
| **11** | `integration-testing.md` | Perform integration testing | API testing, system integration, end-to-end validation |

### Phase 4: Quality & Testing (12-14)
**Purpose**: Quality assurance, user acceptance testing, and pre-deployment

| Protocol | Name | Purpose | Key Features |
|----------|------|---------|--------------|
| **12** | `quality-audit.md` | Comprehensive quality audit | Code review, security scan, performance analysis |
| **13** | `uat-coordination.md` | User Acceptance Testing coordination | UAT planning, stakeholder coordination, feedback integration |
| **14** | `pre-deployment-staging.md` | Pre-deployment staging validation | Staging environment, final testing, deployment preparation |

### Phase 5: Deployment & Operations (15-18)
**Purpose**: Production deployment, monitoring, and incident management

| Protocol | Name | Purpose | Key Features |
|----------|------|---------|--------------|
| **15** | `production-deployment.md` | Production deployment execution | Deployment strategy, rollback planning, go-live coordination |
| **16** | `monitoring-observability.md` | Setup monitoring and observability | Metrics collection, alerting, performance monitoring |
| **17** | `incident-response-rollback.md` | Incident response and rollback procedures | Incident management, rollback execution, post-incident analysis |
| **18** | `performance-optimization.md` | Performance optimization | Performance analysis, optimization implementation, monitoring |

### Phase 6: Closure & Maintenance (19-23)
**Purpose**: Project closure, documentation, and ongoing maintenance

| Protocol | Name | Purpose | Key Features |
|----------|------|---------|--------------|
| **19** | `documentation-knowledge-transfer.md` | Documentation and knowledge transfer | Technical documentation, user guides, knowledge transfer |
| **20** | `project-closure.md` | Project closure and handover | Deliverable validation, stakeholder sign-off, project closure |
| **21** | `maintenance-support.md` | Ongoing maintenance and support | Maintenance planning, support procedures, SLA management |
| **22** | `implementation-retrospective.md` | Implementation retrospective | Process analysis, lessons learned, improvement recommendations |
| **23** | `script-governance-protocol.md` | Script governance and management | Script validation, automation governance, maintenance procedures |

### Supporting Protocols (24-27)
**Purpose**: Additional tools and reference materials

| Protocol | Name | Purpose | Key Features |
|----------|------|---------|--------------|
| **24** | `client-discovery.md` | Extended client discovery | Deep discovery, stakeholder analysis, requirement validation |
| **25** | `protocol-integration-map.md` | Protocol integration mapping | Workflow visualization, dependency mapping, integration points |
| **26** | `integration-guide.md` | Integration and automation guide | Script integration, CI/CD setup, automation configuration |
| **27** | `validation-guide.md` | Validation and quality guide | Quality criteria, validation procedures, compliance checking |

---

## 🎯 Master Rules System

The system includes **8 master rules** that govern AI behavior and ensure consistent, high-quality execution:

| Rule | Name | Purpose |
|------|------|---------|
| **1** | `context-discovery-protocol` | Context gathering and rule loading |
| **2** | `ai-collaboration-guidelines` | AI-user collaboration protocols |
| **3** | `code-quality-checklist` | Code quality standards and best practices |
| **4** | `code-modification-safety-protocol` | Safe code modification procedures |
| **5** | `documentation-and-context-guidelines` | Documentation maintenance and context integrity |
| **6** | `how-to-create-effective-rules` | Rule creation and optimization guidelines |
| **9** | `protocol-orchestrator` | Protocol orchestration and workflow management |
| **Advanced** | `advanced-meta-instruction-intelligence-system` | Advanced analysis and intelligence system |

### Additional Cursor Rules
The system also includes specialized rules for specific domains:

| Rule Type | Location | Purpose |
|-----------|----------|---------|
| **Common Rules** | `.cursor/rules/common-rules/` | Domain-specific guidelines (UI, backend, etc.) |
| **Project Rules** | `.cursor/rules/project-rules/` | Project-specific configurations |
| **Elaboration Specialist** | `.cursor/rules/elaboration-specialist.mdc` | Enhanced instruction clarification |
| **Meta Instructions** | `.cursor/rules/meta-instruction-explain.mdc` | Meta-instruction analysis and explanation |

---

## 🔍 Quality Audit System

### Review Protocols
Located in `.cursor/ai-driven-workflow/review-protocols/`:

- **`code-review.md`**: Code quality validation and DDD compliance
- **`security-check.md`**: Security compliance and vulnerability assessment
- **`architecture-review.md`**: Architecture validation and performance analysis
- **`design-system.md`**: UI/UX compliance and component validation
- **`ui-accessibility.md`**: Accessibility validation and compliance
- **`pre-production.md`**: Pre-deployment validation and readiness check

### Quality Gates
Each protocol includes quality gates with:
- **Prerequisite Gates**: Must pass before protocol execution
- **Execution Gates**: Must pass during protocol execution
- **Completion Gates**: Must pass before protocol completion
- **Integration Gates**: Must pass for workflow integration

---

## ⚙️ Automation Integration

### Script Integration
The system integrates with automation scripts for:
- **Project Analysis**: `analyze_codebase.py`, `classify_domain.py`
- **Validation**: `validate_prd.py`, `validate_tasks.py`
- **Execution**: `execute_task.py`, `evidence_report.py`
- **Quality**: `run_quality_audit.py`, `aggregate_coverage.py`

### Available Scripts
Located in `.artifacts/scripts/`:
- **`script-index.json`**: Complete script inventory and capabilities
- **`static-analysis-report.json`**: Code analysis and quality metrics
- **`validation-report.json`**: Protocol validation results
- **`artifact-compliance-report.json`**: Artifact structure compliance
- **`protocol-4-extension-report.json`**: Protocol extension analysis

### Cursor Commands
Available slash commands in `.cursor/commands/`:
- **`/compare-prs`**: Advanced PR comparison and analysis
- **`/elaborate`**: Enhanced instruction clarification
- **`/generate-cursor-rules`**: Automated rule generation
- **`/generate-proposal`**: Client proposal generation
- **`/protocol-orchestrator`**: Workflow orchestration
- **`/meta-analysis-generator`**: Meta-analysis and intelligence

### Template Packs & Generators
Located in `generators/` directory:
- **Protocol Generators**: Automated protocol creation (6-18)
- **Input Forms**: YAML-based configuration templates
- **Generator Instructions**: Step-by-step generation guides
- **Quick Start Guides**: Rapid setup and deployment
- **Meta Analysis**: Advanced analysis and intelligence tools

### Template Packs System
Located in `template-packs/` directory:
- **Backend Templates**: Django, FastAPI, NestJS, Go frameworks
- **Frontend Templates**: Next.js, Nuxt, Angular, Expo frameworks
- **Database Templates**: PostgreSQL, MongoDB, Firebase configurations
- **DevEx Templates**: DevContainer, Docker Compose, VS Code snippets
- **CI/CD Templates**: GitHub workflows, gates configuration
- **Policy DSL**: YAML definitions for gating rules and policies

### CI/CD Integration
- **Linting**: `.github/workflows/ci-lint.yml`
- **Testing**: `.github/workflows/ci-test.yml`
- **Security**: `.github/workflows/security-scan.yml`
- **Deployment**: `.github/workflows/deploy.yml`

---

## 🚀 Quick Start Guide

### Basic Usage
1. **Initialize Project**: Start with Protocol 05 (bootstrap-your-project.md)
2. **Follow Sequence**: Execute protocols in numerical order
3. **Collect Evidence**: Document all actions and decisions
4. **Validate Gates**: Ensure all quality gates pass

### Command Format
```bash
@apply .cursor/ai-driven-workflow/[protocol-number]-[protocol-name].md
```

### Example Commands
```bash
# Start a new project
@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md

# Create requirements document
@apply .cursor/ai-driven-workflow/06-create-prd.md

# Execute development tasks
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# Run quality audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode comprehensive
```

---

## 📖 Complete Lifecycle Command Playbook

### Client Project Lifecycle (Full SDLC)

#### Phase 0: Client Engagement
```bash
# 1. Generate client proposal
@apply .cursor/ai-driven-workflow/01-client-proposal-generation.md

# 2. Initiate client discovery
@apply .cursor/ai-driven-workflow/02-client-discovery-initiation.md

# 3. Create project brief
@apply .cursor/ai-driven-workflow/03-project-brief-creation.md

# 4. Bootstrap project context
@apply .cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md

# 5. Initialize project structure
@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md
```

#### Phase 1-2: Planning & Design
```bash
# 6. Create Product Requirements Document
@apply .cursor/ai-driven-workflow/06-create-prd.md

# 7. Design technical architecture
@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md

# 8. Generate development tasks
@apply .cursor/ai-driven-workflow/08-generate-tasks.md

# 9. Setup development environment
@apply .cursor/ai-driven-workflow/09-environment-setup-validation.md
```

#### Phase 3: Development
```bash
# 10. Execute development tasks
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# 11. Perform integration testing
@apply .cursor/ai-driven-workflow/11-integration-testing.md
```

#### Phase 4: Quality & Testing
```bash
# 12. Run comprehensive quality audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode comprehensive

# 13. Coordinate User Acceptance Testing
@apply .cursor/ai-driven-workflow/13-uat-coordination.md

# 14. Pre-deployment staging validation
@apply .cursor/ai-driven-workflow/14-pre-deployment-staging.md
```

#### Phase 5: Deployment & Operations
```bash
# 15. Execute production deployment
@apply .cursor/ai-driven-workflow/15-production-deployment.md

# 16. Setup monitoring and observability
@apply .cursor/ai-driven-workflow/16-monitoring-observability.md

# 17. Incident response procedures (if needed)
@apply .cursor/ai-driven-workflow/17-incident-response-rollback.md

# 18. Performance optimization
@apply .cursor/ai-driven-workflow/18-performance-optimization.md
```

#### Phase 6: Closure & Maintenance
```bash
# 19. Documentation and knowledge transfer
@apply .cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md

# 20. Project closure and handover
@apply .cursor/ai-driven-workflow/20-project-closure.md

# 21. Ongoing maintenance and support
@apply .cursor/ai-driven-workflow/21-maintenance-support.md

# 22. Implementation retrospective
@apply .cursor/ai-driven-workflow/22-implementation-retrospective.md
```

### Technical Development Workflow (Development-Focused)

#### Quick Development Cycle
```bash
# Bootstrap project
@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md

# Create requirements
@apply .cursor/ai-driven-workflow/06-create-prd.md

# Design architecture
@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md

# Generate tasks
@apply .cursor/ai-driven-workflow/08-generate-tasks.md

# Execute development
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# Integration testing
@apply .cursor/ai-driven-workflow/11-integration-testing.md

# Quality audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode quick
```

### Quality Assurance Workflow

#### Comprehensive Quality Check
```bash
# Full quality audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode comprehensive

# Security-focused audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode security

# Architecture review
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode architecture

# Pre-deployment validation
@apply .cursor/ai-driven-workflow/14-pre-deployment-staging.md
```

### Emergency Response Workflow

#### Incident Management
```bash
# Incident response
@apply .cursor/ai-driven-workflow/17-incident-response-rollback.md

# Performance optimization
@apply .cursor/ai-driven-workflow/18-performance-optimization.md

# Monitoring setup
@apply .cursor/ai-driven-workflow/16-monitoring-observability.md
```

### Maintenance Workflow

#### Ongoing Maintenance
```bash
# Maintenance planning
@apply .cursor/ai-driven-workflow/21-maintenance-support.md

# Documentation updates
@apply .cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md

# Script governance
@apply .cursor/ai-driven-workflow/23-script-governance-protocol.md
```

---

## 🔧 Advanced Usage

### Custom Workflows
Create custom sequences for specific needs:

#### MVP Development
```bash
@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md
@apply .cursor/ai-driven-workflow/06-create-prd.md
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode quick
```

#### Enterprise Project
```bash
# Full enterprise workflow with all protocols
# Use complete client project lifecycle above
```

#### Bug Fix Workflow
```bash
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode security
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase
@apply .cursor/ai-driven-workflow/11-integration-testing.md
```

### Context Integration
Use Cursor's context features:
- **`@codebase`**: Full project context
- **`@recent-changes`**: Git change analysis
- **`@filename`**: File-specific context

### Automation Hooks
Integrate with existing scripts:
```bash
# Run validation scripts
python scripts/validate_protocols.py
python scripts/test_protocol_execution.py
python scripts/validate_evidence.py
```

---

## 🛠️ Troubleshooting

### Common Issues

#### Missing Prerequisites
- Ensure all prerequisites are met before protocol execution
- Check required artifacts and approvals
- Validate system state requirements

#### Incomplete Evidence
- Verify evidence collection is complete
- Check evidence format and structure
- Ensure all validation results are documented

#### Failed Quality Gates
- Address gate failures immediately
- Review failure reasons and implement fixes
- Re-run gate validation after fixes

#### Integration Problems
- Check protocol dependencies
- Verify handoff requirements
- Ensure proper sequence execution

### Debug Commands
```bash
# Validate protocol structure
python scripts/validate_protocols.py

# Test protocol execution
python scripts/test_protocol_execution.py

# Check evidence collection
python scripts/validate_evidence.py

# Run quality audit
python scripts/run_quality_audit.py
```

---

## 📚 Additional Resources

### Documentation
- **Protocol Integration Map**: `.cursor/ai-driven-workflow/25-protocol-integration-map.md`
- **Integration Guide**: `.cursor/ai-driven-workflow/26-integration-guide.md`
- **Validation Guide**: `.cursor/ai-driven-workflow/27-validation-guide.md`
- **Master Rules**: `.cursor/rules/master-rules/`
- **Common Rules**: `.cursor/rules/common-rules/`
- **Project Rules**: `.cursor/rules/project-rules/`

### Automation Scripts
- **Scripts Directory**: `.artifacts/scripts/`
- **CI/CD Workflows**: `.github/workflows/`
- **Quality Gates**: Built into each protocol

### Template Packs & Generators
- **Generators Directory**: `generators/`
- **Protocol Generators**: Automated protocol creation
- **Input Forms**: YAML configuration templates
- **Quick Start Guides**: Rapid deployment guides

### Template Packs System
- **Template Packs Directory**: `template-packs/`
- **Backend Templates**: Django, FastAPI, NestJS, Go frameworks
- **Frontend Templates**: Next.js, Nuxt, Angular, Expo frameworks
- **Database Templates**: PostgreSQL, MongoDB, Firebase configurations
- **DevEx Templates**: DevContainer, Docker Compose, VS Code snippets
- **CI/CD Templates**: GitHub workflows, gates configuration
- **Policy DSL**: YAML definitions for gating rules and policies

### Cursor Commands
- **Commands Directory**: `.cursor/commands/`
- **Slash Commands**: `/compare-prs`, `/elaborate`, `/generate-proposal`
- **Protocol Orchestrator**: Workflow management
- **Meta Analysis**: Advanced intelligence tools

### Support
- **Review Protocols**: `.cursor/ai-driven-workflow/review-protocols/`
- **Validation Reports**: `.artifacts/validation/`
- **Evidence Collection**: `.artifacts/protocol-[number]/`

---

## 🎯 Success Metrics

### Quality Targets
- **Protocol Completion**: 100% of protocols executed successfully
- **Evidence Collection**: Complete documentation for all actions
- **Quality Gates**: All gates passed with validation
- **Integration**: Seamless workflow continuity
- **Client Satisfaction**: Professional delivery and documentation

### Performance Indicators
- **Efficiency**: Reduced development time through structured workflows
- **Quality**: Improved code quality through systematic validation
- **Consistency**: Standardized processes across all projects
- **Scalability**: Ability to handle projects of any complexity
- **Reliability**: Evidence-based delivery with validation gates

---

**Ready to transform your development workflow? Start with Protocol 05 and follow the complete lifecycle for professional, evidence-based software development!** 🚀

**For Meta-Upgrades Intelligence Layer deployment, begin with Pre-Deployment validation and proceed through staged rollout S0-S9.** 🧠

---

## 🧭 Protocol 02 – Client Discovery Initiation Guardrails

These rules govern every execution of `.cursor/ai-driven-workflow/02-client-discovery-initiation.md`.

### 1. Session Scope & Ownership
- Run **exactly one protocol per session**; do not mix Protocol 02 tasks with other protocols or backlog grooming.
- If prerequisite artifacts from Protocol 01 are missing or stale, stop immediately, document the gap in `.artifacts/protocol-02/manual-validation-log.md`, and notify the reviewer instead of fabricating placeholders.

### 2. Pre-Flight Verification
- Confirm the following before announcing `[MASTER RAY™ | PHASE 1 START]`:
  1. `PROPOSAL.md` and `proposal-summary.json` from Protocol 01 are approved and stored in `.artifacts/protocol-01/`.
  2. Client acceptance or follow-up is captured in `.artifacts/protocol-02/client-reply.md` or an equivalent transcript.
  3. Communication channel, discovery templates, and scheduling commitments are verified (email/call/chat confirmed with timestamp).
- If any prerequisite is absent, capture the blocker in `manual-validation-log.md`, request the missing asset, and halt the session.

### 3. Execution Discipline
- Follow the protocol phases sequentially—Context Alignment → Requirement Deep Dive → Delivery Framework Alignment → Discovery Confirmation.
- Each sub-step produces a named artifact inside `.artifacts/protocol-02/`; never reuse filenames from earlier sessions.
- Use the automation hooks when available:
  - `python scripts/validate_prerequisites_02.py`
  - `python scripts/validate_discovery_objectives.py --input .artifacts/protocol-02/client-context-notes.md`
  - `python scripts/validate_discovery_scope.py --form .artifacts/protocol-02/client-discovery-form.md`
  - `python scripts/validate_discovery_expectations.py --recap .artifacts/protocol-02/discovery-recap.md`
  - `python scripts/aggregate_evidence_02.py --output .artifacts/protocol-02/`
- If automation fails, log the command, error, and remediation in `manual-validation-log.md` before retrying. Do not mark gates as passed without evidence.

### 4. Communication & Evidence Integrity
- Announce each phase transition using the protocol's status prompts and capture exact wording in `communication-plan.md` or call transcripts.
- Maintain a live `risk-log.md` capturing unresolved questions, client dependencies, and approval gaps; update it whenever you pause execution.
- Store raw transcripts in `.artifacts/protocol-02/transcripts/` with ISO-8601 timestamps.
- Enforce readability and empathy by paraphrasing client language inside `discovery-recap.md`; avoid copy-pasting proposal text.

### 5. Session Closeout & Continuity
- Run `python scripts/generate_session_continuation.py --protocol 02` after validations complete to produce updated instructions for the next operator.
- Validate the final evidence package manually if any gate was waived, and record reviewer handoff notes in `.artifacts/protocol-02/reviewer-brief.md`.
- Do not trigger Protocol 03 until the client has explicitly approved `discovery-recap.md` and the approval is archived in `transcripts/`.
