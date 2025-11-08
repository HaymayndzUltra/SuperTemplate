## QUALITY GATES

### Gate 1: Foundation Validation
**Pass Criteria:** All Protocol 05 artifacts present and valid
**Automation:** `python scripts/validate_protocol_evidence.py --protocol 05`
**Blocking:** Yes

### Gate 2: Classification Confidence
**Pass Criteria:** Project classification confidence ≥ 0.90
**Automation:** `python scripts/calculate_classification_confidence.py`
**Blocking:** No (warning if <0.90)

### Gate 3: Protocol Coverage
**Pass Criteria:** Every PROJECT-BRIEF requirement has assigned protocol
**Automation:** `python scripts/validate_protocol_coverage.py`
**Blocking:** Yes

### Gate 4: New Protocol Validation
**Pass Criteria:** All new protocols score ≥ 0.95 on validators
**Automation:** `python validators-system/scripts/validate_all_protocols.py`
**Blocking:** Yes

### Gate 5: User Approval
**Pass Criteria:** Project Owner approves execution plan
**Automation:** Manual sign-off
**Blocking:** Yes

---

## COMMUNICATION PROTOCOLS

**Phase Start:**
```
[PROTOCOL 05B | PHASE 1 START] - Validating foundation artifacts
```

**Milestones:**
```
[PROJECT CLASSIFIED] - Type: {type}, Confidence: {score}
[PROTOCOL SELECTION COMPLETE] - {X} REQUIRED, {Y} MAYBE, {Z} SKIPPED
[GAP ANALYSIS] - {N} gaps identified, {N} new protocols needed
[NEW PROTOCOL VALIDATED] - Protocol {ID} created, score: {score}
```

**Quality Gates:**
```
[QUALITY GATE PASSED: Gate 1] - Foundation validated
[QUALITY GATE PASSED: Gate 5] - User approval obtained
```

**Phase Complete:**
```
[PROTOCOL 05B | PHASE 6 COMPLETE] - Handoff to Protocol {next}
```

**Errors:**
```
[PROTOCOL 05B | GATE 1 FAILED] - Protocol 05 artifacts incomplete
[PROTOCOL 05B | BLOCKED] - {reason}
```

---

## AUTOMATION HOOKS

```yaml
scripts:
  - validate_protocol_evidence.py: Validate Protocol 05 completion
  - parse_project_brief.py: Extract requirements from PROJECT-BRIEF
  - parse_architecture.py: Extract architecture patterns
  - classify_project.py: Determine project type
  - detect_characteristics.py: Identify project characteristics
  - map_protocols.py: Map characteristics to protocols
  - analyze_gaps.py: Detect protocol gaps
  - calculate_timeline.py: Estimate execution timeline
  - generate_execution_plan.py: Create PROTOCOL-EXECUTION-PLAN.md
  - generate_checklist.py: Create PROTOCOL-CHECKLIST.md
  
validators:
  - validate_all_protocols.py: Validate new protocols (score ≥0.95)
  - validate_protocol_coverage.py: Ensure complete requirement coverage
  
integrations:
  - Bootstrap Protocol Context (Protocol 0): Create new protocols
  - Script Registry: Register new protocol scripts
```

---

## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All quality gates passed
- [ ] PROTOCOL-EXECUTION-PLAN.md generated
- [ ] PROTOCOL-CHECKLIST.md generated
- [ ] New protocols (if any) validated and registered
- [ ] Timeline and cost estimates calculated
- [ ] User approval obtained

### Handoff Deliverables
- [ ] PROTOCOL-EXECUTION-PLAN.md (detailed roadmap)
- [ ] PROTOCOL-CHECKLIST.md (tracking tool)
- [ ] .artifacts/protocol-05b/handoff-package.zip (all artifacts)
- [ ] New protocol files (if created)
- [ ] Protocol customization notes

### Downstream Validation
- [ ] Next protocol owner receives handoff package
- [ ] Next protocol owner confirms understanding
- [ ] Next protocol owner validates inputs
- [ ] Next protocol owner ready to execute

---

## EVIDENCE SUMMARY

### Artifacts Required
```
.artifacts/protocol-05b/
├── phase-01-validation.json
├── project-brief-parsed.json
├── architecture-parsed.json
├── project-classification.json
├── characteristics-detection.json
├── characteristic-protocol-mapping.json
├── protocol-selection.json
├── gap-analysis.json
├── execution-sequence.json
├── customization-requirements.json
├── timeline-estimate.json
├── handoff-package.zip
├── new-protocols/ (if gaps detected)
│   ├── {ID}-specification.json
│   ├── {ID}-{name}.md
│   └── {ID}-validation-report.json
└── evidence-manifest.json
```

### Root-Level Artifacts
```
PROTOCOL-EXECUTION-PLAN.md
PROTOCOL-CHECKLIST.md
```

### Artifact Formats
- JSON: Structured data (classifications, mappings, timelines)
- Markdown: Human-readable plans and documentation
- ZIP: Evidence packages for downstream protocols
