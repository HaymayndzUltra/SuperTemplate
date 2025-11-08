# META-PATTERNS REFERENCE FOR PROTOCOL CREATION

## OVERVIEW
This document extracts reusable patterns from successful protocols. Use these patterns as building blocks for Protocol 09: AI Data Cleaning & Validation.

---

## PATTERN 1: PROTOCOL IDENTITY STRUCTURE
**Source**: Protocol 01, Protocol 08, Protocol 19

### Standard Identity Template
```markdown
## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID**: [number]
- **Protocol Name**: [Descriptive Name]
- **Protocol Owner**: [Role/Team]
- **Owner Contact**: [Email/Slack]
- **Created**: [YYYY-MM-DD]
- **Last Updated**: [YYYY-MM-DD]
- **Version**: [X.X]

### Protocol Classification
- **Category**: [Execution/Planning/Validation/etc.]
- **Criticality**: [High/Medium/Low]
- **Complexity**: [Simple/Medium/Complex]
- **Scope**: [Local/Module/System]

### Protocol Lineage
- **Predecessor**: Protocol [XX]
- **Successor**: Protocol [XX]
- **Related Protocols**: [List related protocols]
```

**Usage Guidelines**:
- Always include Protocol ID and Name
- Specify lineage for clear handoffs
- Use consistent versioning (semantic)
- Define scope and criticality clearly

---

## PATTERN 2: PREREQUISITES FRAMEWORK
**Source**: Protocol 01, Protocol 08, Protocol 19

### Standard Prerequisites Template
```markdown
## PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS - Standard prerequisite checklist] -->
<!-- Why: Standard prerequisite structure with inputs, approvals, and system state requirements -->

### Required Artifacts
- [ ] [Artifact 1 from previous protocol]
- [ ] [Artifact 2 from previous protocol]
- [ ] [Additional required files]

### Required Approvals
- [ ] [Stakeholder 1] sign-off for [specific purpose]
- [ ] [Stakeholder 2] approval of [specific aspect]
- [ ] [Quality assurance] confirmation of [criteria]

### System State Requirements
- [ ] [Directory] exists and is writable
- [ ] [Software/service] available and configured
- [ ] [Configuration file] up to date

If any prerequisite fails, pause and resolve before continuing.
```

**Usage Guidelines**:
- Group by type: Artifacts, Approvals, System State
- Be specific about what "ready" means
- Include pause instruction for failures
- Reference previous protocols explicitly

---

## PATTERN 3: AI ROLE DEFINITION
**Source**: Protocol 01, Protocol 08, Protocol 19

### Standard AI Role Template
```markdown
## AI ROLE AND MISSION

You are a **[Specific Role Title]**. Your mission is to [clear mission statement].

**[CRITICAL] NEVER [critical prohibition]**
**[GUIDELINE] Always [recommended behavior]**
**[STRICT] Must [mandatory requirement]**
```

**Role Examples**:
- **Proposal Writer/Freelancer**: Transform job posts into proposals
- **Technical Lead**: Generate and organize development tasks
- **Technical Documentation Lead**: Capture and distribute durable knowledge

**Usage Guidelines**:
- Use specific, expert-level role titles
- Include clear mission statement
- Add critical prohibitions with [CRITICAL]
- Include behavioral guidelines with [GUIDELINE] and [STRICT]

---

## PATTERN 4: 4-PHASE EXECUTION WORKFLOW
**Source**: Protocol 01, Protocol 08, Protocol 19

### Standard 4-Phase Template
```markdown
<!-- [Category: EXECUTION-FORMATS - BASIC/SUBSTEPS/REASONING variant] -->
<!-- Why: [Specific reason for format choice] -->

## PHASE 1: [Phase Name]
**[STRICT]** Complete all [phase name] steps before proceeding.

### 1.1 [Sub-step 1]
- [ ] [Action 1]
- [ ] [Action 2]
- [ ] [Action 3]

### 1.2 [Sub-step 2]
- [ ] [Action 1]
- [ ] [Action 2]

**Halt-and-await**: Confirm [phase name] complete before proceeding to Phase 2.

---

## PHASE 2: [Phase Name]
**[STRICT]** Execute steps in sequence. Do not skip steps.

### 2.1 [Sub-step 1]
1. **Step 1**: [Action description]
   - Input: [What's needed]
   - Output: [What's produced]
   - Validation: [How to verify]

### 2.2 [Sub-step 2]
[Detailed steps with validation]

**Halt-and-await**: Confirm [phase name] complete before proceeding to Phase 3.

---

## PHASE 3: [Phase Name]
**[STRICT]** Validate all outputs meet quality criteria.

### 3.1 [Validation type]
- [ ] [Check 1]
- [ ] [Check 2]

### 3.2 [Review type]
- [ ] [Review 1]
- [ ] [Review 2]

**Halt-and-await**: Proceed to Phase 4 only after validation approval.

---

## PHASE 4: [Phase Name]
**[STRICT]** Prepare and execute clean handoff to next protocol.

### 4.1 [Handoff preparation]
- [ ] [Preparation action 1]
- [ ] [Preparation action 2]

### 4.2 [Handoff execution]
- [ ] [Execution action 1]
- [ ] [Execution action 2]

**Success Criteria**: [Clear success definition]
```

**Phase Types**:
- **Phase 1**: Preparation/Assessment/Setup
- **Phase 2**: Execution/Processing/Generation  
- **Phase 3**: Validation/Quality Assurance/Review
- **Phase 4**: Handoff/Documentation/Completion

**Usage Guidelines**:
- Use [STRICT] for mandatory requirements
- Include "Halt-and-await" checkpoints
- Define clear success criteria
- Specify format variant in HTML comment

---

## PATTERN 5: QUALITY GATES & VALIDATION
**Source**: Protocol 01, Protocol 08, Protocol 9

### Standard Quality Gates Template
```markdown
## QUALITY GATES
**[STRICT]** All quality gates must pass before proceeding to next protocol.

### Gate 1: [Gate Name]
**Threshold**: [Specific metric threshold]
**Validation Method**: [How to validate]
**Pass Criteria**: [What constitutes passing]

### Gate 2: [Gate Name]  
**Threshold**: [Specific metric threshold]
**Validation Method**: [How to validate]
**Pass Criteria**: [What constitutes passing]

### Gate 3: [Gate Name]
**Threshold**: [Specific metric threshold]  
**Validation Method**: [How to validate]
**Pass Criteria**: [What constitutes passing]

**Failure Handling**: [What to do if gates fail]
```

**Gate Types**:
- **Input Quality Gates**: Validate inputs from previous protocol
- **Processing Quality Gates**: Validate processing results
- **Output Quality Gates**: Validate final outputs
- **Handoff Gates**: Validate readiness for next protocol

**Usage Guidelines**:
- Define specific, measurable thresholds
- Include validation methods
- Specify failure handling procedures
- Link to automation scripts where available

---

## PATTERN 6: AUTOMATION HOOKS INTEGRATION
**Source**: Protocol 01, Protocol 08, Protocol 9

### Standard Automation Hooks Template
```markdown
## AUTOMATION HOOKS
**[GUIDELINE]** Use registered scripts for all automation tasks.

### Data Processing Scripts
```bash
# [Script purpose]
python3 scripts/[script-name].py --input [input-file] --output [output-file]

# Parameters:
# --input: [Description of input parameter]
# --output: [Description of output parameter]
# --config: [Description of config parameter] (optional)
```

### Validation Scripts
```bash
# [Validation purpose]
python3 scripts/[validation-script].py --data [data-file] --threshold [value]

# Exit codes:
# 0: Pass
# 1: Warning  
# 2: Fail
```

### Monitoring Scripts
```bash
# [Monitoring purpose]
python3 scripts/[monitoring-script].py --log-level [level] --output [log-file]
```

### Script Registry Reference
All scripts referenced above must be registered in `scripts/script-registry.json` with:
- **Purpose**: Clear description of script function
- **Dependencies**: Required packages and system requirements
- **Parameters**: Complete parameter documentation
- **Exit Codes**: Expected exit codes and meanings
```

**Usage Guidelines**:
- Only reference registered scripts
- Provide exact command syntax
- Document all parameters
- Include exit code meanings
- Reference script registry

---

## PATTERN 7: EVIDENCE COLLECTION & DOCUMENTATION
**Source**: Protocol 01, Protocol 08, Protocol 9

### Standard Evidence Template
```markdown
## EVIDENCE SUMMARY
**[STRICT]** Document all evidence for auditability and reproducibility.

### Required Evidence Artifacts
- [ ] **[Artifact 1]**: [Description and format]
  - Location: `.artifacts/protocol-09/[filename]`
  - Validation: [How to validate artifact]
- [ ] **[Artifact 2]**: [Description and format]
  - Location: `.artifacts/protocol-09/[filename]`
  - Validation: [How to validate artifact]

### Evidence Collection Process
1. **Pre-Processing Evidence**: Collect before any data cleaning
   - Data quality assessment
   - Raw data statistics
   - Initial validation results

2. **Processing Evidence**: Collect during cleaning operations
   - Cleaning operation logs
   - Decision records
   - Intermediate quality metrics

3. **Post-Processing Evidence**: Collect after cleaning completion
   - Final data quality report
   - Validation summary
   - Handoff readiness confirmation

### Evidence Validation
- **Completeness Check**: All required evidence present
- **Quality Check**: Evidence meets quality standards
- **Integrity Check**: Evidence hasn't been corrupted
- **Accessibility Check**: Evidence accessible to stakeholders

### Evidence Storage
```
.artifacts/protocol-09/
├── evidence/
│   ├── preprocessing/
│   ├── processing/
│   ├── postprocessing/
│   └── validation/
├── reports/
│   ├── quality-report.json
│   ├── validation-summary.md
│   └── handoff-manifest.json
└── logs/
    ├── processing.log
    ├── validation.log
    └── errors.log
```
```

**Usage Guidelines**:
- Define specific evidence artifacts
- Organize evidence by processing phase
- Include validation procedures
- Provide clear storage structure
- Ensure accessibility for stakeholders

---

## PATTERN 8: HANDOFF CHECKLIST & COMMUNICATION
**Source**: Protocol 01, Protocol 08, Protocol 9

### Standard Handoff Template
```markdown
## HANDOFF CHECKLIST
**[STRICT]** Complete all handoff requirements before declaring protocol complete.

### Deliverable Verification
- [ ] **[Deliverable 1]**: [Verification criteria]
- [ ] **[Deliverable 2]**: [Verification criteria]
- [ ] **[Deliverable 3]**: [Verification criteria]

### Quality Confirmation
- [ ] **Quality Gates**: All quality gates passed
- [ ] **Validation**: All validation checks successful
- [ ] **Stakeholder Review**: Required approvals obtained

### Documentation Completion
- [ ] **Protocol Summary**: Execution summary documented
- [ ] **Known Issues**: Any issues or limitations documented
- [ ] **Next Protocol Guidance**: Clear guidance for Protocol [XX]

### Communication Protocol
#### Status Update Template
```markdown
# Protocol 09 Status Update
**Date**: [YYYY-MM-DD]
**Status**: [In Progress/Complete/Blocked]
**Progress**: [Summary of progress]
**Issues**: [Any issues or blockers]
**Next Steps**: [Planned next steps]
**ETA**: [Estimated completion]
```

#### Handoff Notification Template
```markdown
# Protocol 09 Handoff to Protocol 10
**Date**: [YYYY-MM-DD]
**From**: Protocol 09 (AI Data Cleaning & Validation)
**To**: Protocol 10 (AI Feature Engineering)
**Status**: Ready for handoff

## Deliverables
- [List of deliverables with locations]

## Quality Summary
- [Quality metrics and results]

## Known Considerations
- [Any issues or considerations for next protocol]

## Contact
- [Contact information for questions]
```

**Usage Guidelines**:
- Create comprehensive deliverable checklist
- Include quality confirmation steps
- Provide communication templates
- Define clear handoff success criteria
- Ensure continuity for next protocol

---

## PATTERN 9: DIRECTIVE SYSTEM USAGE
**Source**: All protocols

### Directive Hierarchy Template
```markdown
**[CRITICAL]** NEVER [critical prohibition] - Will cause system failure
**[STRICT]** MUST [mandatory requirement] - Cannot proceed without compliance  
**[GUIDELINE]** SHOULD [recommended practice] - Best practice to follow
**[BLOCKING]** HALT until [blocking condition] - Stop execution until condition met
```

**Directive Usage Examples**:
- **[CRITICAL]** NEVER modify source data without backup
- **[STRICT]** MUST validate all inputs before processing
- **[GUIDELINE]** SHOULD use automated validation where available
- **[BLOCKING]** HALT until quality gates pass

**Usage Guidelines**:
- Use [CRITICAL] for system-breaking prohibitions
- Use [STRICT] for mandatory requirements
- Use [GUIDELINE] for best practices
- Use [BLOCKING] for execution stops

---

## PATTERN 10: FORMAT TEMPLATE SELECTION
**Source**: Meta-analysis examples

### Format Selection Decision Tree
```
1. What is the section purpose?
   ├─ Execution workflow → EXECUTION-FORMATS
   ├─ Rules/standards → GUIDELINES-FORMATS  
   ├─ Issue tracking → ISSUE-FORMATS
   ├─ Agent coordination → PROMPT-FORMATS
   └─ Analysis/design → META-FORMATS

2. What is the complexity level?
   ├─ Simple linear steps → BASIC variant
   ├─ Detailed substeps needed → SUBSTEPS variant
   └─ Decision reasoning required → REASONING variant

3. What is the validation requirement?
   ├─ High validation needed → Include detailed checkpoints
   ├─ Medium validation needed → Include basic checkpoints
   └─ Low validation needed → Minimal checkpoints
```

**Format Usage Examples**:
- **PREREQUISITES**: GUIDELINES-FORMATS (standard checklist)
- **WORKFLOW**: EXECUTION-FORMATS (REASONING variant for data decisions)
- **QUALITY GATES**: GUIDELINES-FORMATS (standards and thresholds)
- **COMMUNICATION**: GUIDELINES-FORMATS (templates and protocols)

**Usage Guidelines**:
- Analyze each section independently
- Choose format based on section purpose
- Mix formats within same protocol
- Always include format rationale in HTML comments

---

## PATTERN APPLICATION FOR PROTOCOL 09

### Recommended Pattern Combination
1. **Identity**: Use Pattern 1 (Protocol Identity Structure)
2. **Prerequisites**: Use Pattern 2 (Prerequisites Framework) - reference Protocol 08
3. **AI Role**: Use Pattern 3 (AI Role Definition) - Data Quality Engineer
4. **Workflow**: Use Pattern 4 (4-Phase Execution) with EXECUTION-FORMATS (REASONING)
5. **Quality Gates**: Use Pattern 5 (Quality Gates) - data quality thresholds
6. **Automation**: Use Pattern 6 (Automation Hooks) - reference registered scripts
7. **Evidence**: Use Pattern 7 (Evidence Collection) - data quality evidence
8. **Handoff**: Use Pattern 8 (Handoff Checklist) - to Protocol 10
9. **Directives**: Use Pattern 9 (Directive System) throughout
10. **Formats**: Use Pattern 10 (Format Selection) per section

### Protocol 09 Specific Adaptations
- **Data Quality Focus**: Emphasize validation and quality metrics
- **Script Integration**: Reference actual data processing scripts
- **Evidence Emphasis**: Comprehensive data quality documentation
- **Handoff Clarity**: Specific requirements for ML pipeline readiness

These patterns provide a solid foundation for creating Protocol 09 that follows established conventions while meeting the specific requirements of AI data cleaning and validation.
