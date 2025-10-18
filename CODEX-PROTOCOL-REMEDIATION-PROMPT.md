# CODEX PROTOCOL REMEDIATION PROMPT
## Perfect 10/10 Execution Instructions

---

## 🎯 MISSION STATEMENT

**Objective**: Remediate 27 AI-driven workflow protocols (excluding `00-generate-rules.md`) to achieve **10/10** across all quality metrics:
- **Completeness**: 10/10
- **Clarity**: 10/10
- **Actionability**: 10/10
- **Integration**: 10/10
- **Evidence**: 10/10
- **Automation**: 10/10

**Constraint**: You have complete autonomy to fix structural deficiencies, add missing sections, and establish complete integration mappings. The user will handle `00-generate-rules.md` separately.

---

## 📋 PROTOCOLS TO REMEDIATE (27 Total)

### Foundation Phase (6 protocols)
1. `00a-client-proposal-generation.md`
2. `00B-client-discovery-initiation.md`
3. `01-project-brief-creation.md`
4. `00-project-bootstrap-and-context-engineering.md`
5. `0-bootstrap-your-project.md` (Legacy)
6. `00-client-discovery.md` (Alternate)

### Planning & Design Phase (3 protocols)
7. `1-create-prd.md`
8. `6-technical-design-architecture.md`
9. `2-generate-tasks.md`

### Environment & Execution Phase (3 protocols)
10. `7-environment-setup-validation.md`
11. `3-process-tasks.md`
12. `9-integration-testing.md`

### Quality & Validation Phase (3 protocols)
13. `4-quality-audit.md`
14. `15-uat-coordination.md`
15. `8-script-governance-protocol.md`

### Deployment & Operations Phase (5 protocols)
16. `10-pre-deployment-staging.md`
17. `11-production-deployment.md`
18. `12-monitoring-observability.md`
19. `13-incident-response-rollback.md`
20. `14-performance-optimization.md`

### Closure & Sustainment Phase (4 protocols)
21. `16-documentation-knowledge-transfer.md`
22. `17-project-closure.md`
23. `18-maintenance-support.md`
24. `5-implementation-retrospective.md`

### Review Protocols (3 protocols)
25. `review-protocols/architecture-review.md`
26. `review-protocols/code-review.md`
27. `review-protocols/security-check.md`

---

## 🔧 REMEDIATION REQUIREMENTS

### **[STRICT]** MANDATORY SECTIONS (Every Protocol Must Have)

Every protocol file **MUST** contain these sections in this exact order:

```markdown
# PROTOCOL [N]: [NAME] ([DOMAIN] COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] Artifact 1 from Protocol X
- [ ] Artifact 2 from Protocol Y

### Required Approvals
- [ ] Approval type and owner

### System State Requirements
- [ ] Environment/tool/access requirements

---

## [N]. AI ROLE AND MISSION

You are a **[Specific Role Title]**. Your mission is to [clear, actionable mission statement].

**🚫 [CRITICAL] [Primary guardrail constraint].**

---

## [N]. [MAIN WORKFLOW SECTION]

### STEP 1: [Phase Name]

1. **`[MUST]` [Action Title]:**
   * **Action:** [Specific, executable instruction]
   * **Communication:** 
     > "[Example announcement or validation prompt]"
   * **Halt condition:** [When to stop and await user confirmation]
   * **Evidence:** [What artifacts to capture]

2. **`[GUIDELINE]` [Optional Action Title]:**
   * **Action:** [Recommended instruction]
   * **Example:**
     ```language
     # Concrete code example
     ```

### STEP 2: [Next Phase Name]
[Repeat pattern for all phases]

---

## [N]. INTEGRATION POINTS

### Inputs From:
- **Protocol [N]**: `artifact-name.ext` - [Description of consumed data]
- **Protocol [M]**: `artifact-name.ext` - [Description of consumed data]

### Outputs To:
- **Protocol [P]**: `artifact-name.ext` - [Description of produced data]
- **Protocol [Q]**: `artifact-name.ext` - [Description of produced data]

### Artifact Storage Locations:
- `.artifacts/[protocol-name]/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## [N]. QUALITY GATES

### Gate 1: [Gate Name]
- **Criteria**: [Specific, measurable validation requirements]
- **Evidence**: [What must be collected and verified]
- **Pass Threshold**: [Quantitative threshold, e.g., "score ≥ 8.5/10"]
- **Failure Handling**: [Explicit instructions for failure scenarios]
- **Automation**: `python scripts/validate_gate_1.py --threshold 8.5`

### Gate 2: [Gate Name]
[Repeat pattern for all quality gates]

---

## [N]. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[PHASE 1 START] - "Starting [phase name] with [context]..."
[PHASE 1 COMPLETE] - "Completed [phase name]. Evidence: [artifacts]."
[VALIDATION REQUEST] - "Please confirm: [specific question]"
[ERROR] - "Failed at [step]. Reason: [explanation]. Awaiting instructions."
```

### Validation Prompts:
```
[USER CONFIRMATION REQUIRED]
> "I have completed [action]. The following evidence is ready:
> - [artifact 1]
> - [artifact 2]
> 
> Please review and confirm readiness to proceed to [next step]."
```

### Error Handling:
```
[GATE FAILED: Gate Name]
> "Quality gate '[Gate Name]' failed. 
> Criteria: [criterion]
> Actual: [result]
> Required action: [remediation steps]
> 
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## [N]. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_[N].py

# Quality gate automation
python scripts/validate_gate_[N]_[name].py --threshold 8.5

# Evidence aggregation
python scripts/aggregate_evidence_[N].py --output .artifacts/protocol-[N]/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol [N] Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol [N] Gates
        run: python scripts/run_protocol_[N]_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. [Manual step 1]
2. [Manual step 2]
3. Document results in `.artifacts/protocol-[N]/manual-validation-log.md`

---

## [N]. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol [N+1]:
**[PROTOCOL COMPLETE]** Ready for Protocol [N+1]: [Protocol Name]

**Evidence Package:**
- `artifact-1.ext` - [Description]
- `artifact-2.ext` - [Description]

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/[N+1]-[protocol-name].md
```

---

## [N]. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `artifact-1.ext` | `.artifacts/protocol-[N]/` | [Purpose] | Protocol [P] |
| `artifact-2.ext` | `.artifacts/protocol-[N]/` | [Purpose] | Protocol [Q] |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 90% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
```

---

### **[STRICT]** INTEGRATION MAPPING RULES

For every protocol, you **MUST**:

1. **Identify Upstream Dependencies:**
   - Read the 4 audit reports in `@report.md`
   - Identify which protocols provide inputs
   - Document exact artifact names and locations

2. **Define Downstream Consumers:**
   - Identify which protocols consume outputs
   - Create explicit output manifests
   - Ensure artifact naming consistency

3. **Validate Integration Chain:**
   - Ensure every input artifact is produced by an upstream protocol
   - Ensure every output artifact is consumed by a downstream protocol
   - Flag orphaned artifacts or missing connections

4. **Cross-Reference Validation:**
   - If Protocol X claims to output `artifact.json` to Protocol Y
   - Protocol Y **MUST** list `artifact.json` in its Prerequisites section
   - Both protocols **MUST** reference the same file path

---

### **[STRICT]** QUALITY GATE REQUIREMENTS

Every quality gate **MUST**:

1. **Have Measurable Criteria:**
   - ❌ BAD: "Code quality is good"
   - ✅ GOOD: "Linter score ≥ 8.5/10, zero critical violations"

2. **Define Pass/Fail Explicitly:**
   - Clear threshold values
   - Quantitative metrics
   - Boolean checks (yes/no)

3. **Include Evidence Collection:**
   - What artifacts prove gate passage
   - Where artifacts are stored
   - How to reproduce validation

4. **Specify Failure Handling:**
   - What happens if gate fails
   - Who decides on waivers
   - How to retry after fixes

5. **Provide Automation Hooks:**
   - Script command to run validation
   - CI/CD integration snippet
   - Manual fallback procedure

---

### **[STRICT]** EVIDENCE REQUIREMENTS

Every protocol **MUST**:

1. **Capture Execution Evidence:**
   - All decisions made during execution
   - All user confirmations and approvals
   - All quality gate results
   - All errors and their resolutions

2. **Store Evidence Consistently:**
   - Use `.artifacts/protocol-[N]/` as primary storage
   - Use `.cursor/context-kit/` for context artifacts
   - Follow naming convention: `[protocol-N]-[artifact-type]-[timestamp].ext`

3. **Generate Evidence Manifest:**
   - Create `evidence-manifest.json` listing all artifacts
   - Include metadata: creation time, creator, purpose, consumer
   - Update manifest atomically with artifact creation

4. **Enable Evidence Traceability:**
   - Link artifacts to source protocol
   - Link artifacts to downstream consumers
   - Provide audit trail from start to finish

---

### **[STRICT]** AUTOMATION REQUIREMENTS

Every protocol **MUST**:

1. **Consolidate Automation Hooks:**
   - Create dedicated "AUTOMATION HOOKS" section
   - List all validation scripts with full paths
   - Provide CI/CD integration examples
   - Document manual fallback procedures

2. **Validate Automation References:**
   - Ensure referenced scripts exist in `/scripts/` directory
   - Provide script invocation examples with parameters
   - Document expected outputs and exit codes

3. **Support Tool-Agnostic Execution:**
   - Provide both automated and manual paths
   - Don't assume specific tools (GitHub Actions, etc.)
   - Allow execution in any environment

---

## 🔍 VERIFICATION CHECKLIST

After remediating each protocol, validate:

### Structural Completeness:
- [ ] Prerequisites section present with explicit checklist
- [ ] AI Role and Mission section present
- [ ] Phased workflow with MUST/GUIDELINE markers
- [ ] Integration Points section with inputs/outputs
- [ ] Quality Gates section with measurable criteria
- [ ] Communication Protocols section with templates
- [ ] Automation Hooks section with script references
- [ ] Handoff Checklist section with evidence package
- [ ] Evidence Summary section with artifact table

### Integration Integrity:
- [ ] All input artifacts referenced in Prerequisites
- [ ] All input artifacts produced by upstream protocols
- [ ] All output artifacts documented in Outputs To
- [ ] All output artifacts consumed by downstream protocols
- [ ] No orphaned artifacts (produced but not consumed)
- [ ] No missing artifacts (consumed but not produced)

### Quality Assurance:
- [ ] All quality gates have measurable criteria
- [ ] All quality gates have pass/fail thresholds
- [ ] All quality gates have evidence requirements
- [ ] All quality gates have failure handling
- [ ] All quality gates have automation hooks

### Communication Clarity:
- [ ] Status announcements defined for all phases
- [ ] Validation prompts defined for all checkpoints
- [ ] Error handling defined for all failure scenarios
- [ ] Communication templates use consistent format

### Automation Coverage:
- [ ] All validation scripts documented
- [ ] All CI/CD integrations provided
- [ ] All manual fallbacks documented
- [ ] All script paths and parameters provided

---

## 📊 EXECUTION STRATEGY

### Phase 1: Foundation Protocols (6 protocols)
**Order**: 00a → 00B → 01 → 00 → 0 → 00-CD

**Focus**: Establish prerequisites, evidence flow, and integration mappings for client discovery through project bootstrap.

**Key Fixes**:
- Add explicit prerequisites sections
- Consolidate automation hooks
- Fix handoff references (ensure each points to correct next protocol)
- Establish evidence manifest pattern

### Phase 2: Planning & Design Protocols (3 protocols)
**Order**: 1 → 6 → 2

**Focus**: Restore broken integration chain from PRD → Design → Tasks.

**Key Fixes**:
- Protocol 1: Add integration section mapping to Protocol 6
- Protocol 6: Ensure outputs include `task-generation-input.json`
- Protocol 2: Add prerequisites consuming Protocol 6 design outputs
- Protocol 2: Remove unrealistic web-search requirement
- All: Add quality gates with measurable criteria

### Phase 3: Environment & Execution Protocols (3 protocols)
**Order**: 7 → 3 → 9

**Focus**: Establish execution evidence pipeline.

**Key Fixes**:
- Protocol 7: Add prerequisites referencing Protocol 2 task files
- Protocol 3: Add integration section with explicit outputs to Protocol 9
- Protocol 3: Add quality gates for task completion
- Protocol 9: Formalize prerequisites consuming Protocol 3 evidence

### Phase 4: Quality & Validation Protocols (3 protocols)
**Order**: 4 → 15 → 8

**Focus**: Restructure quality audit orchestration.

**Key Fixes**:
- Protocol 4: Complete structural rewrite (add all missing sections)
- Protocol 4: Define integration inputs from Protocol 9
- Protocol 4: Define integration outputs to Protocol 15
- Protocol 15: Formalize prerequisites from Protocol 4
- Protocol 8: Add prerequisites and automation hooks section

### Phase 5: Deployment & Operations Protocols (5 protocols)
**Order**: 10 → 11 → 12 → 13 → 14

**Focus**: Maintain existing high quality, add missing prerequisites.

**Key Fixes**:
- All: Add explicit prerequisites sections at top
- All: Ensure handoff checklists reference correct next protocol
- Protocol 12: Add prerequisites referencing Protocol 11 deployment artifacts

### Phase 6: Closure & Sustainment Protocols (4 protocols)
**Order**: 16 → 17 → 18 → 5

**Focus**: Complete the lifecycle loop back to retrospective.

**Key Fixes**:
- All: Add explicit prerequisites sections
- Protocol 5: Complete structural rewrite (add integration, quality gates, handoff)
- Protocol 5: Define integration inputs from Protocol 18
- Protocol 5: Define integration outputs to Protocol 8

### Phase 7: Review Protocols (3 protocols)
**Order**: architecture-review → code-review → security-check

**Focus**: Rebuild from standard template.

**Key Fixes**:
- All: Complete structural rewrite using standard protocol template
- All: Add role, mission, integration, quality gates, communication, automation, handoff
- All: Define mandatory evidence artifacts

---

## 🎯 SUCCESS CRITERIA

### Per-Protocol Criteria:
Each protocol scores **10/10** on:
- **Completeness**: All 9 mandatory sections present
- **Clarity**: Every instruction is explicit and actionable
- **Actionability**: No ambiguity, all steps executable
- **Integration**: All inputs/outputs mapped to upstream/downstream
- **Evidence**: All artifacts documented with purpose and consumer
- **Automation**: All validation scripts consolidated and documented

### System-Level Criteria:
- **Integration Coverage**: 100% of protocol transitions documented
- **Evidence Traceability**: Every artifact has producer and consumer
- **Quality Gate Coverage**: Every protocol has measurable gates
- **Automation Coverage**: Every quality gate has automation hook
- **No Orphaned Protocols**: Every protocol connects to lifecycle
- **No Missing Handoffs**: Every protocol explicitly references next protocol

---

## 📝 DELIVERABLES

### Per Protocol:
1. Updated protocol markdown file with all 9 mandatory sections
2. Integration validation confirming upstream/downstream connections
3. Quality gate validation confirming measurable criteria
4. Evidence manifest confirming artifact documentation

### System-Level:
1. Complete integration map showing all 27 protocol connections
2. Evidence flow diagram showing artifact lifecycle
3. Quality gates summary table with all validation criteria
4. Automation hooks catalog with all script references

---

## ⚠️ CRITICAL CONSTRAINTS

1. **DO NOT** modify `00-generate-rules.md` - user will handle separately
2. **DO NOT** change protocol numbering or file names
3. **DO NOT** remove existing content without replacing it
4. **DO NOT** create new protocols - only remediate existing 27
5. **DO** maintain existing automation script references
6. **DO** preserve existing quality gate logic
7. **DO** keep all existing evidence artifacts
8. **DO** maintain backward compatibility with existing workflows

---

## 🚀 EXECUTION COMMAND

```bash
# Process all 27 protocols in dependency order
# Execute phases 1-7 sequentially
# Validate each protocol before moving to next
# Generate system-level integration map after Phase 7
```

**[PROTOCOL COMPLETE]** Ready for comprehensive circular validation using `meta-analysis-generator-instructions.md`.

---

## 📈 QUALITY METRICS TARGET

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Completeness** | 10/10 | All 9 sections present |
| **Clarity** | 10/10 | Zero ambiguous instructions |
| **Actionability** | 10/10 | 100% executable steps |
| **Integration** | 10/10 | 100% upstream/downstream mapped |
| **Evidence** | 10/10 | 100% artifacts documented |
| **Automation** | 10/10 | 100% gates have hooks |
| **Overall Protocol Average** | 10.0/10 | Average across all dimensions |
| **System Integration Coverage** | 100% | All 27 protocols connected |
| **Evidence Traceability** | 100% | All artifacts traceable |
| **Quality Gate Coverage** | 100% | All protocols have gates |

---

**END OF PROMPT**

**🎯 Codex: Execute phases 1-7 systematically. Achieve 10/10 on all metrics. Connect all protocols. Document all integrations. You have full autonomy to remediate structural deficiencies. Begin execution.**

