# Protocol Identity Validator - Quick Start

## 🚀 Quick Commands

```bash
# Validate single protocol
python3 scripts/validate_protocol_identity.py --protocol 01

# Validate all protocols
python3 scripts/validate_protocol_identity.py --all

# Run test suite
./scripts/test_protocol_identity_validator.sh
```

## 📊 Understanding Results

### Status Indicators
- ✅ **PASS**: Score ≥ 95%
- ⚠️ **WARNING**: Score 80-94%
- ❌ **FAIL**: Score < 80%

### Score Breakdown
Each protocol receives scores across 5 dimensions (each weighted 20%):
1. **Basic Information**: Metadata completeness
2. **Prerequisites**: Required artifacts/approvals
3. **Integration Points**: Input/output mapping
4. **Compliance Standards**: Industry standards + automation
5. **Documentation Quality**: Section completeness

## 📁 Output Files

### Individual Results
`.artifacts/validation/protocol-{ID}-identity.json`

### Summary Reports
- `identity-validation-summary.json` - Overall statistics
- `compliance-matrix.json` - Compliance by protocol
- `integration-map.json` - Integration completeness
- `documentation-quality-report.json` - Quality metrics

## 🔧 Common Fixes

### "Protocol version not found"
Add to protocol header:
```markdown
Version: v1.0.0
```

### "Required section missing: WORKFLOW"
Ensure section exists:
```markdown
## 01. CLIENT PROPOSAL WORKFLOW
```

### "Industry standards not documented"
Add to QUALITY GATES:
```markdown
- Markdown: CommonMark v0.30
- JSON Schema: Draft-07
```

### "Automated quality gates config not found"
Create gate file:
```bash
touch config/protocol_gates/{ID}.yaml
```

## 📈 Success Criteria

- **Overall Score**: ≥95% across all protocols
- **Pass Rate**: 100% protocols in PASS status
- **Critical Issues**: Zero FAIL status protocols
- **Documentation**: All 9 required sections present

## 🔗 Full Documentation

- **Complete Guide**: `documentation/protocol-identity-validator-guide.md`
- **Implementation Details**: `documentation/protocol-identity-validator-implementation.md`
- **Specification**: `documentation/validator-01-complete-spec.md`
