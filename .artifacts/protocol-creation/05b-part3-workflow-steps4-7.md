### STEP 4: Intelligent Protocol Selection & Gap Analysis

**Action**: Map characteristics to protocols, classify each protocol, identify coverage gaps

1. **[STRICT]** Map detected characteristics to protocols from both workflow sets
   - Load protocol inventory from `.cursor/ai-driven-workflow/` (generic protocols 01-28)
   - Load protocol inventory from `AI-project-workflow/` (AI-specific protocols 01-30)
   - For each detected characteristic, identify which protocols address it
   - Create characteristic-to-protocol mapping matrix
   - Save to `characteristic-protocol-mapping.json`
   - **Strategy**: Use comprehensive mapping **framework** to ensure no characteristic is overlooked

2. **[STRICT]** Classify each protocol as REQUIRED | RECOMMENDED | MAYBE | SKIP
   - **REQUIRED**: Protocol addresses critical project requirement
   - **RECOMMENDED**: Protocol addresses important but not critical requirement
   - **MAYBE**: Protocol provides value but depends on project constraints
   - **SKIP**: Protocol not applicable to project type
   - For each classification, document rationale with evidence
   - Save to `protocol-selection.json`
   - **Decision**: REQUIRED protocols are non-negotiable, MAYBE protocols require user approval

3. **[CRITICAL]** Identify coverage gaps by comparing requirements vs selected protocols
   - List all project requirements from PROJECT-BRIEF.md
   - For each requirement, identify which protocols address it
   - Flag requirements with zero protocol coverage as "gaps"
   - Calculate coverage percentage: (covered requirements / total requirements) × 100
   - **Problem**: Gaps indicate missing protocols **so that** we can create new ones to fill them

4. **[STRICT]** Analyze gap severity and determine resolution strategy
   - For each gap, assess severity: CRITICAL | HIGH | MEDIUM | LOW
   - **Decision Tree**:
     - If coverage ≥95%: Proceed to STEP 5 (skip STEP 4.5)
     - If coverage <95% and critical gaps exist: Force STEP 4.5 (create new protocols)
     - If coverage <95% but no critical gaps: Offer user choice

5. **[GUIDELINE]** Present MAYBE protocols to user for decision
   - For each MAYBE protocol, show: name, purpose, estimated effort, benefits, risks
   - Request user decision: Include | Skip | Defer
   - Record decisions with rationale in `maybe-protocol-decisions.json`

**Communication**:
```
[PHASE 3 START] - Intelligent Protocol Selection & Gap Analysis
[MAPPING] Mapping 18 characteristics to protocols...
[SELECTION] Classified 12 REQUIRED, 8 RECOMMENDED, 5 MAYBE, 15 SKIP
[COVERAGE] Requirement coverage: 92% (23/25 requirements covered)
[GAP ANALYSIS] Identified 2 gaps: API rate limiting, data backup strategy
[USER PROMPT] "5 MAYBE protocols need your decision. Review and choose Include/Skip/Defer."
```

**Evidence**:
- `.artifacts/protocol-05b/characteristic-protocol-mapping.json`
- `.artifacts/protocol-05b/protocol-selection.json`
- `.artifacts/protocol-05b/gap-analysis.json`
- `.artifacts/protocol-05b/coverage-report.json`
- `.artifacts/protocol-05b/maybe-protocol-decisions.json`

**Halt Condition**: If user declines to make MAYBE protocol decisions, HALT until decisions obtained

---

### STEP 4.5: Dynamic Protocol Creation (CONDITIONAL - Only if coverage <95%)

**Action**: Create new protocols to fill identified gaps using protocol-creation workflow

**[CONDITIONAL EXECUTION]**: This step only executes if coverage <95% after STEP 4

1. **[STRICT]** For each critical or high-severity gap, generate gap specification
   - Define gap purpose, scope, required inputs, expected outputs
   - Identify which existing protocols it should integrate with
   - Estimate complexity and effort required
   - Save specification to `.artifacts/protocol-05b/new-protocols/gap-{ID}-spec.json`

2. **[CRITICAL]** Use protocol-creation workflow (protocols 1-5) to create new protocol
   - Execute sub-workflow (AI-driven, no user interaction):
     ```
     @apply dev-workflow/protocol-creation/1-analyze-validator-requirements.md
     @apply dev-workflow/protocol-creation/2-generate-protocol-structure.md
     @apply dev-workflow/protocol-creation/3-create-protocol-content.md
     @apply dev-workflow/protocol-creation/4-validate-protocol.md
     @apply dev-workflow/protocol-creation/5-protocol-retrospective.md
     ```
   - **Iteration limit**: Maximum 5 attempts per protocol
   - **Success criteria**: Validation score ≥0.95 on all 10 validators

3. **[STRICT]** Validate new protocol meets quality standards
   - Run all 10 validators
   - Verify overall score ≥0.95
   - Verify each dimension score ≥0.90
   - Check for zero critical validation failures
   - Save validation report to `.artifacts/protocol-05b/new-protocols/{ID}-validation-report.json`

4. **[GUIDELINE]** Register new protocol in system
   - Assign protocol number (use next available in sequence)
   - Add to protocol inventory
   - Update characteristic-protocol mapping
   - Recalculate coverage percentage

5. **[CRITICAL]** Iterate until coverage ≥95% or user intervention required
   - Repeat steps 1-4 for each remaining gap
   - **Halt Condition**: If 5 iterations fail for any protocol, HALT and escalate to user

**Communication**:
```
[PHASE 4 START] - Dynamic Protocol Creation (Coverage: 92%)
[GAP] Creating protocol for: API Rate Limiting
[PROTOCOL CREATION] Running protocol-creation workflow (1-5)...
[VALIDATION] New protocol validation: 0.96 (PASS)
[REGISTRATION] Protocol 29: API Rate Limiting registered
[COVERAGE] Updated coverage: 96%
[MILESTONE ACHIEVED] All gaps filled, proceeding to PHASE 5
```

**Evidence**:
- `.artifacts/protocol-05b/new-protocols/gap-{ID}-spec.json`
- `.artifacts/protocol-05b/new-protocols/{ID}-protocol.md`
- `.artifacts/protocol-05b/new-protocols/{ID}-validation-report.json`
- `.artifacts/protocol-05b/new-protocols/registry-updates.json`

**Halt Condition**: If any new protocol fails validation after 5 iterations, HALT and escalate to user

---

### STEP 5: Dependency Graph Construction & Execution Sequencing

**Action**: Build dependency graph, determine execution order, identify parallelization opportunities

1. **[STRICT]** Build protocol dependency graph from PREREQUISITES sections
   - For each selected protocol, parse PREREQUISITES section
   - Extract "Required Artifacts" with source protocol references
   - Create directed graph: nodes = protocols, edges = dependencies
   - Validate graph is acyclic (no circular dependencies)
   - Save graph to `dependency-graph.json`

2. **[STRICT]** Determine execution order using topological sort
   - Apply topological sort algorithm to dependency graph
   - Generate linear execution sequence respecting all dependencies
   - Identify protocols with no dependencies (can start immediately)
   - Identify protocols with same dependencies (candidates for parallel execution)

3. **[GUIDELINE]** Identify parallel execution opportunities
   - Group protocols with identical dependency sets
   - Flag protocols that can run concurrently
   - Calculate potential time savings from parallelization
   - Document parallel execution groups in `execution-sequence.json`

4. **[STRICT]** Perform critical path analysis
   - Calculate longest path through dependency graph (critical path)
   - Identify bottleneck protocols
   - Calculate minimum project duration
   - Flag protocols that, if delayed, would delay entire project
   - Save analysis to `critical-path-analysis.json`

**Communication**:
```
[PHASE 5 START] - Dependency Graph & Execution Sequencing
[GRAPH] Building dependency graph from 20 selected protocols...
[VALIDATION] Graph is acyclic (no circular dependencies)
[SEQUENCING] Execution order determined: 20 protocols in 8 phases
[PARALLEL] Identified 3 parallel opportunities (15% time savings)
[CRITICAL PATH] Critical path: 120 hours
[MILESTONE ACHIEVED] Execution sequence optimized
```

**Evidence**:
- `.artifacts/protocol-05b/dependency-graph.json`
- `.artifacts/protocol-05b/execution-sequence.json`
- `.artifacts/protocol-05b/critical-path-analysis.json`

**Halt Condition**: If circular dependencies detected, HALT and report conflicting protocols

---

### STEP 6: Customization Analysis & Timeline Estimation

**Action**: Analyze customization needs, estimate effort, calculate timeline

1. **[STRICT]** Analyze customization requirements based on project context
   - **Solo Developer Optimization**: Simplify or automate protocols
   - **MVP Mode**: Flag protocols that can be deferred
   - **Compliance Requirements**: Add compliance protocols
   - **AI/ML Additions**: Ensure AI-specific protocols included
   - Document customization decisions in `customization-requirements.json`

2. **[STRICT]** Estimate effort for each protocol
   - Assign base effort hours per protocol type
   - Apply customization modifiers:
     - Solo developer: +20%
     - MVP mode: -30%
     - High compliance: +40%
     - AI/ML project: +50%
   - Calculate total effort: sum of all protocol efforts

3. **[GUIDELINE]** Calculate timeline with parallel execution discounts
   - Base timeline: sum of all protocol efforts (sequential)
   - Apply parallel discount
   - Apply team size multiplier
   - Add buffer: +20% for unknowns
   - Calculate critical path duration
   - Save estimates to `timeline-estimate.json`

4. **[GUIDELINE]** Identify resource requirements and constraints
   - List required skills per protocol
   - Flag protocols requiring external resources
   - Identify tooling requirements
   - Document resource constraints

**Communication**:
```
[PHASE 6 START] - Customization Analysis & Timeline Estimation
[CUSTOMIZATION] Detected: Solo developer, MVP mode, AI/ML project
[EFFORT] Base effort: 240 hours, Customized: 336 hours
[TIMELINE] Sequential: 42 days, With parallelization: 36 days
[TIMELINE] Critical path: 30 days, Realistic: 43 days (with buffer)
[RESOURCES] Required skills: Python, ML, React, DevOps
[MILESTONE ACHIEVED] Timeline and resource plan complete
```

**Evidence**:
- `.artifacts/protocol-05b/customization-requirements.json`
- `.artifacts/protocol-05b/timeline-estimate.json`

**Halt Condition**: None (advisory step, does not block)

---

### STEP 7: Execution Plan Generation & Approval

**Action**: Generate comprehensive execution plan documents and obtain user approval

1. **[STRICT]** Generate PROTOCOL-EXECUTION-PLAN.md (15-25 pages)
   - **Section 1**: Executive Summary (1-2 pages)
   - **Section 2**: Project Analysis (2-3 pages)
   - **Section 3**: Protocol Selection (3-4 pages)
   - **Section 4**: Gap Analysis (2-3 pages)
   - **Section 5**: Execution Sequence (2-3 pages)
   - **Section 6**: Customization Requirements (2-3 pages)
   - **Section 7**: Timeline & Resources (2-3 pages)
   - **Section 8**: Approval & Sign-off (1 page)
   - Save to workspace root

2. **[STRICT]** Generate PROTOCOL-CHECKLIST.md (simple checkbox list)
   - Format: `- [ ] Protocol XX: [Name] ([Source]) - [Hours]`
   - Group by phase
   - Include effort estimate per protocol
   - Save to workspace root

3. **[STRICT]** Package all evidence artifacts into handoff-package.zip
   - Include all 35+ JSON artifacts from `.artifacts/protocol-05b/`
   - Include evidence-manifest.json
   - Calculate checksums (SHA-256)
   - Save to `.artifacts/protocol-05b/handoff-package.zip`

4. **[CRITICAL]** Request user approval for final execution plan
   - Present PROTOCOL-EXECUTION-PLAN.md for review
   - Request explicit "yes" approval
   - Record approval with timestamp in `approval-record.json`
   - **Decision**: If user declines, offer options: revise plan, optimize timeline, skip optional protocols

**Communication**:
```
[PHASE 7 START] - Execution Plan Generation & Approval
[GENERATION] Creating PROTOCOL-EXECUTION-PLAN.md... 50% complete
[GENERATION] Creating PROTOCOL-CHECKLIST.md... 75% complete
[PACKAGING] Creating handoff-package.zip... 100% complete
[USER PROMPT] "Execution plan complete. Review PROTOCOL-EXECUTION-PLAN.md and approve to proceed."
[PROTOCOL 05b | PHASE 7 COMPLETE] - Ready for handoff
```

**Evidence**:
- `PROTOCOL-EXECUTION-PLAN.md` (workspace root)
- `PROTOCOL-CHECKLIST.md` (workspace root)
- `.artifacts/protocol-05b/handoff-package.zip`
- `.artifacts/protocol-05b/approval-record.json`

**Halt Condition**: If user declines final approval, HALT and await revision instructions

---
