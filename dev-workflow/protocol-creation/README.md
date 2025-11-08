# Protocol Creation Workflow

This workflow creates complete, validator-compliant AI workflow protocols based on the validator system requirements.

## Overview

The protocol creation workflow consists of 5 sequential protocols that transform validator requirements into a production-ready protocol document:

1. **1-analyze-validator-requirements.md** - Analyzes all validators to extract requirements
2. **2-generate-protocol-structure.md** - Generates protocol structure template
3. **3-create-protocol-content.md** - Populates structure with complete content
4. **4-validate-protocol.md** - Validates protocol against all validators
5. **5-protocol-retrospective.md** - Reviews and improves the protocol

## Workflow Flow

```
Protocol 1: Requirements Analysis
    ↓
    Creates: protocol-requirements-spec.md
    ↓
Protocol 2: Structure Generation
    ↓
    Creates: protocol-structure-template.md
    ↓
Protocol 3: Content Creation
    ↓
    Creates: XX-protocol-name.md
    ↓
Protocol 4: Validation
    ↓
    Creates: validation-report-XX.md
    ↓
Protocol 5: Retrospective
    ↓
    Creates: retrospective-XX.md
    ↓
PRODUCTION-READY PROTOCOL
```

## Quick Start

### Step 1: Analyze Validator Requirements
```bash
# Run Protocol 1
@apply dev-workflow/protocol-creation/1-analyze-validator-requirements.md
```

### Step 2: Generate Protocol Structure
```bash
# Run Protocol 2
@apply dev-workflow/protocol-creation/2-generate-protocol-structure.md
```

### Step 3: Create Protocol Content
```bash
# Run Protocol 3
# Provide protocol context when prompted:
# - Protocol number (01-28)
# - Protocol name
# - Protocol purpose
# - Protocol phase
# - Integration points
@apply dev-workflow/protocol-creation/3-create-protocol-content.md
```

### Step 4: Validate Protocol
```bash
# Run Protocol 4
# Validators will run automatically
@apply dev-workflow/protocol-creation/4-validate-protocol.md
```

### Step 5: Retrospective Review
```bash
# Run Protocol 5
@apply dev-workflow/protocol-creation/5-protocol-retrospective.md
```

## Artifacts

All artifacts are stored in `.artifacts/protocol-creation/`:

- `protocol-requirements-spec.md` - Complete requirements from validators
- `protocol-structure-template.md` - Protocol structure template
- `XX-protocol-name.md` - Final protocol file (in `.cursor/ai-driven-workflow/`)
- `validation-report-XX.md` - Validation results and fixes
- `retrospective-XX.md` - Retrospective review and improvements

## Validator Requirements

The workflow ensures protocols meet all requirements from 10 validators:

1. **Identity Validator** - Basic info, prerequisites, integration, compliance, documentation
2. **Role Validator** - AI role, mission, constraints, outputs, behavior
3. **Workflow Validator** - Structure, steps, markers, halt conditions, evidence
4. **Quality Gates Validator** - Gate definitions, criteria, automation, failure handling
5. **Scripts Validator** - Automation hooks, registry alignment, execution context
6. **Communication Validator** - Status announcements, user interaction, error messaging
7. **Evidence Validator** - Artifact generation, storage, manifest, traceability
8. **Handoff Validator** - Checklist, verification, signoff, documentation, next protocol
9. **Reasoning Validator** - Reasoning patterns, decision trees, problem solving
10. **Reflection Validator** - Retrospective, improvement, evolution, knowledge capture

## Required Sections

Every protocol must include these 9 sections:

1. **PREREQUISITES** - Required artifacts, approvals, system state
2. **AI ROLE AND MISSION** - Role definition, mission statement, constraints
3. **WORKFLOW** - Step-by-step execution instructions
4. **INTEGRATION POINTS** - Inputs, outputs, data formats, storage
5. **QUALITY GATES** - Validation criteria and thresholds
6. **COMMUNICATION PROTOCOLS** - Status, interaction, error, progress, evidence
7. **AUTOMATION HOOKS** - Scripts, registry, execution context, error handling
8. **HANDOFF CHECKLIST** - Prerequisites, workflow, quality, evidence, integration
9. **EVIDENCE SUMMARY** - Artifacts, storage, manifest, traceability, archival

## Validation Criteria

Protocols must pass all validators with:

- **Master Validator**: Status = PASS, Score ≥0.90
- **Identity Validator**: Score ≥0.95
- **Role Validator**: Score ≥0.90
- **Workflow Validator**: Score ≥0.90
- **Quality Gates Validator**: Score ≥0.92
- **Scripts Validator**: Score ≥0.90
- **Communication Validator**: Score ≥0.90
- **Evidence Validator**: Score ≥0.90
- **Handoff Validator**: Score ≥0.90
- **Reasoning Validator**: Score ≥0.85
- **Reflection Validator**: Score ≥0.85

## Best Practices

1. **Follow the Sequence**: Execute protocols 1-5 in order
2. **Provide Complete Context**: Give detailed protocol information in Protocol 3
3. **Fix All Issues**: Address all validation failures before proceeding
4. **Document Improvements**: Capture lessons learned in Protocol 5
5. **Validate Thoroughly**: Run all validators and fix all issues

## Troubleshooting

### Validator Failures
- Read the validator JSON file for specific issues
- Fix issues in the protocol file
- Re-run the validator to verify fixes

### Missing Requirements
- Review the requirements spec from Protocol 1
- Check example protocols for patterns
- Consult validator documentation

### Structure Issues
- Verify all 9 sections present
- Check section order matches template
- Validate markdown syntax

## Related Documentation

- Validator System: `validators-system/documentation/`
- Example Protocols: `.cursor/ai-driven-workflow/`
- Phase Assignments: `AGENTS.md`

## Support

For issues or questions:
1. Review the validator documentation
2. Check example protocols
3. Review the retrospective reports
4. Consult the requirements specification

