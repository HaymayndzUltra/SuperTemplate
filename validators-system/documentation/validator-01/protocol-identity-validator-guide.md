# Protocol Identity Validator Guide

## Overview

The **Protocol Identity Validator** is an automated tool that validates AI workflow protocols for completeness, quality, and compliance with system standards. It implements the specification defined in `validator-01-complete-spec.md`.

## Purpose

Validate that AI workflow protocols contain:
- Complete identity metadata
- Proper documentation structure
- Integration point mappings
- Compliance standards
- Quality documentation

## Validation Dimensions

The validator checks 5 key dimensions:

### 1. Basic Information (Weight: 20%)
- **Protocol Number**: Correct ID format (01-27)
- **Protocol Name**: Descriptive title
- **Protocol Version**: Semantic versioning (v1.0.0)
- **Phase Assignment**: Valid phase from AGENTS.md
- **Purpose Statement**: Clear mission statement
- **Scope Definition**: Boundaries and inclusions

**Pass Criteria**: All 6 elements present = PASS, 1-2 missing = WARNING, 3+ missing = FAIL

### 2. Prerequisites Documentation (Weight: 20%)
- **Required Artifacts**: Input files with source protocols
- **Required Approvals**: Stakeholder sign-offs needed
- **System State**: Environment setup and dependencies

**Pass Criteria**: All categories documented = PASS, 1 missing = WARNING, 2+ missing = FAIL

### 3. Integration Points Mapping (Weight: 20%)
- **Input Sources**: Which protocols provide inputs
- **Output Destinations**: Which protocols receive outputs
- **Data Formats**: File types (.md, .json, .yaml)
- **Storage Locations**: Directory paths for artifacts

**Pass Criteria**: Complete chain documented = PASS, missing links = WARNING, broken chain = FAIL

### 4. Compliance Standards (Weight: 20%)
- **Industry Standards**: CommonMark, JSON Schema versions
- **Security Requirements**: HIPAA, SOC2, GDPR compliance
- **Regulatory Compliance**: FDA, FTC requirements
- **Quality Gates**: Automated validation in `config/protocol_gates/*.yaml`

**Pass Criteria**: Standards documented + automated = PASS, missing automation = WARNING, no compliance = FAIL

### 5. Documentation Quality (Weight: 20%)
Required sections (all 9 must be present):
1. PREREQUISITES
2. AI ROLE AND MISSION
3. WORKFLOW
4. INTEGRATION POINTS
5. QUALITY GATES
6. COMMUNICATION PROTOCOLS
7. AUTOMATION HOOKS
8. HANDOFF CHECKLIST
9. EVIDENCE SUMMARY

**Quality Metrics**:
- **Completeness**: Percentage of required sections present
- **Clarity**: Readability and example quality
- **Accessibility**: Format consistency and navigation
- **Technical Accuracy**: Correct terminology and references

**Pass Criteria**: Completeness ≥95% + Clarity ≥90% = PASS, Completeness 80-94% = WARNING, Completeness <80% = FAIL

## Usage

### Validate Single Protocol

```bash
python3 scripts/validate_protocol_identity.py --protocol 01
```

**Output**:
```
✅ Validation complete for Protocol 01
   Status: WARNING
   Score: 0.841
   Output: /path/to/.artifacts/validation/protocol-01-identity.json
```

### Validate All Protocols

```bash
python3 scripts/validate_protocol_identity.py --all
```

**Output**:
```
⚠️ Protocol 01: WARNING (score: 0.841)
⚠️ Protocol 02: WARNING (score: 0.832)
❌ Protocol 03: FAIL (score: 0.741)
...
📊 Summary reports generated in .artifacts/validation/
```

### Generate Summary Reports Only

```bash
python3 scripts/validate_protocol_identity.py --all --report
```

## Output Files

### Individual Protocol Results

**Location**: `.artifacts/validation/protocol-{ID}-identity.json`

**Structure**:
```json
{
  "validator": "protocol_identity",
  "protocol_id": "01",
  "validation_timestamp": "2025-10-20T08:00:00Z",
  "basic_information": {
    "score": 0.833,
    "status": "warning",
    "issues": ["Protocol version not found"],
    "elements_found": {
      "protocol_number": true,
      "protocol_name": "CLIENT PROPOSAL GENERATION",
      "protocol_version": false,
      "phase_assignment": "Phase 0",
      "purpose_statement": true,
      "scope_definition": true
    }
  },
  "prerequisites": {"score": 1.0, "status": "pass"},
  "integration_points": {"score": 1.0, "status": "pass"},
  "compliance_standards": {"score": 0.75, "status": "warning"},
  "documentation_quality": {"score": 1.0, "status": "pass"},
  "overall_score": 0.841,
  "validation_status": "warning",
  "issues": [
    "Protocol version not found (semantic versioning expected)",
    "Industry standards not documented"
  ],
  "recommendations": []
}
```

### Summary Reports

#### 1. Identity Validation Summary
**File**: `.artifacts/validation/identity-validation-summary.json`

Contains:
- Total protocols validated
- Pass/Warning/Fail counts
- Average score across all protocols
- Individual protocol scores and statuses

#### 2. Compliance Matrix
**File**: `.artifacts/validation/compliance-matrix.json`

Contains:
- Compliance scores per protocol
- Category-level compliance status
- Industry standards coverage
- Security and regulatory compliance

#### 3. Integration Map
**File**: `.artifacts/validation/integration-map.json`

Contains:
- Integration point completeness per protocol
- Input/output chain validation
- Data format documentation
- Storage location mapping

#### 4. Documentation Quality Report
**File**: `.artifacts/validation/documentation-quality-report.json`

Contains:
- Quality scores per protocol
- Section completeness metrics
- Clarity and accessibility scores
- Technical accuracy assessment

## Success Criteria

- **Overall Score**: ≥95% across all protocols = PASS
- **Individual Dimensions**: Each dimension ≥90% pass rate
- **Critical Issues**: Zero protocols with FAIL status
- **Documentation**: All protocols have complete section coverage

## Common Issues and Fixes

### Issue: "Protocol version not found"
**Fix**: Add semantic version to protocol header:
```markdown
---
**MASTER RAY™ AI-Driven Workflow Protocol**
Version: v1.0.0
© 2025 - All Rights Reserved
---
```

### Issue: "Required section missing: WORKFLOW"
**Fix**: Ensure workflow section exists with proper heading:
```markdown
## 01. CLIENT PROPOSAL WORKFLOW
```

### Issue: "Industry standards not documented"
**Fix**: Add standards reference to QUALITY GATES section:
```markdown
## QUALITY GATES
- Markdown format: CommonMark v0.30
- JSON Schema: Draft-07
```

### Issue: "Automated quality gates config not found"
**Fix**: Create gate configuration file:
```bash
touch config/protocol_gates/{protocol_id}.yaml
```

## Integration with CI/CD

Add to `.github/workflows/validate-protocols.yml`:

```yaml
name: Protocol Identity Validation
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Validate Protocol Identity
        run: |
          python3 scripts/validate_protocol_identity.py --all
      
      - name: Upload Validation Reports
        uses: actions/upload-artifact@v3
        with:
          name: validation-reports
          path: .artifacts/validation/
```

## Error Handling

The validator implements graceful degradation:

- **Missing Files**: Reports as FAIL with specific file path
- **Malformed YAML**: Attempts parsing, reports parsing errors
- **Circular Dependencies**: Flags in integration points validation
- **Invalid References**: Reports broken links or missing artifacts

## Exit Codes

- **0**: All protocols pass or have warnings only
- **1**: One or more protocols fail validation

## Recommendations

1. **Run Before Commits**: Validate protocols before committing changes
2. **Track Trends**: Monitor average scores over time
3. **Fix Critical Issues First**: Address FAIL status protocols before warnings
4. **Update Documentation**: Keep protocols synchronized with implementation
5. **Automate in CI**: Integrate into continuous integration pipeline

## Related Documentation

- **Specification**: `documentation/validator-01-complete-spec.md`
- **Protocol Inventory**: `AGENTS.md`
- **Gate Configurations**: `config/protocol_gates/*.yaml`
- **Integration Guide**: `.cursor/ai-driven-workflow/26-integration-guide-DOCUMENTATION.md`

## Support

For issues or questions:
1. Check the specification: `documentation/validator-01-complete-spec.md`
2. Review validation output JSON for detailed error messages
3. Examine individual protocol files for missing elements
4. Verify gate configuration files exist and are valid YAML
