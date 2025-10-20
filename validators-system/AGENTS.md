# 🎯 VALIDATORS SYSTEM - AI AGENT GUIDE

**Version**: 1.0.0  
**Last Updated**: 2025-10-20  
**Status**: Phase 1 Complete (1/10 validators), Ready for Phase 2-4

---

## 🚀 QUICK START FOR AI AGENTS

Kung ikaw ay AI agent na gagawa ng validators, **START HERE**:

### Step 1: Basahin ang Overview (2 minutes)
```
File: documentation/VALIDATOR-IMPLEMENTATION-SUMMARY.md
Purpose: Maintindihan ang buong system at current status
```

### Step 2: Tingnan ang Specification (5 minutes)
```
File: documentation/MASTER-VALIDATOR-COMPLETE-SPEC.md
Purpose: Makita ang complete requirements ng validator na gagawin mo
```

### Step 3: Basahin ang Implementation Guide (10 minutes)
```
File: documentation/VALIDATOR-GENERATOR-PROMPT.md
Purpose: Sundin ang step-by-step instructions para gumawa ng validator
```

### Step 4: Check ang Example Code (5 minutes)
```
File: scripts/validate_protocol_identity.py
Purpose: Tingnan ang working example ng validator
```

### Step 5: Start Implementation (4-6 hours)
```
Follow: documentation/VALIDATOR-QUICK-REFERENCE.md
Create: scripts/validate_protocol_[name].py
Test: tests/test_protocol_[name]_validator.sh
```

---

## 📁 FOLDER STRUCTURE

```
validators-system/
├── AGENTS.md                          # This file - Start here!
├── README.md                          # System overview
│
├── documentation/                     # All documentation
│   ├── MASTER-VALIDATOR-COMPLETE-SPEC.md           # ⭐ Main specification
│   ├── VALIDATOR-GENERATOR-PROMPT.md               # 🔧 Implementation guide
│   ├── VALIDATOR-QUICK-REFERENCE.md                # ⚡ Quick reference
│   ├── VALIDATOR-IMPLEMENTATION-SUMMARY.md         # 📊 Status & roadmap
│   ├── VALIDATOR-SYSTEM-INDEX.md                   # 📚 Navigation index
│   │
│   └── validator-01/                  # Validator 1 documentation
│       ├── validator-01-complete-spec.md
│       ├── protocol-identity-validator-guide.md
│       ├── protocol-identity-validator-implementation.md
│       └── protocol-identity-validator-quickstart.md
│
├── scripts/                           # Validator scripts
│   └── validate_protocol_identity.py  # ✅ Validator 1 (DONE)
│
├── tests/                             # Test suites
│   └── test_protocol_identity_validator.sh  # ✅ Validator 1 tests
│
└── examples/                          # Example outputs
    └── validation-results/            # Sample validation results
        ├── protocol-01-identity.json
        ├── identity-validation-summary.json
        └── ... (27 protocol results)
```

---

## 🎯 YOUR MISSION

### Objective
Gumawa ng **9 remaining validators** (Validators 2-10) plus **Master Orchestrator**

### Current Status
- ✅ **Validator 1**: Protocol Identity - COMPLETE
- ⏭️ **Validator 2**: AI Role - NEXT TO IMPLEMENT
- ⏭️ **Validators 3-10**: Waiting for implementation
- ⏭️ **Master Orchestrator**: Final integration

### Priority Order
1. **Phase 1 (Critical)**: Validators 2, 3, 4 - 15 hours
2. **Phase 2 (Integration)**: Validators 5, 6 - 8 hours
3. **Phase 3 (Evidence)**: Validators 7, 8 - 8 hours
4. **Phase 4 (Advanced)**: Validators 9, 10, Orchestrator - 14 hours

**Total Effort**: 45 hours development + 25 hours testing/docs = **70 hours**

---

## 📋 VALIDATOR INVENTORY

### ✅ Implemented (1/10)

| # | Name | File | Status | Docs | Tests |
|---|------|------|--------|------|-------|
| 1 | Protocol Identity | `validate_protocol_identity.py` | ✅ DONE | ✅ Complete | ✅ Passing |

### ⏭️ To Implement (9/10)

| # | Name | File | Priority | Time | Spec Ready |
|---|------|------|----------|------|------------|
| 2 | AI Role | `validate_protocol_role.py` | 🔥 NEXT | 4h | ✅ Yes |
| 3 | Workflow Algorithm | `validate_protocol_workflow.py` | 🔥 High | 6h | ✅ Yes |
| 4 | Quality Gates | `validate_protocol_gates.py` | 🔥 High | 5h | ✅ Yes |
| 5 | Script Integration | `validate_protocol_scripts.py` | ⚡ Med | 4h | ✅ Yes |
| 6 | Communication | `validate_protocol_communication.py` | ⚡ Med | 4h | ✅ Yes |
| 7 | Evidence Package | `validate_protocol_evidence.py` | 📦 Med | 5h | ✅ Yes |
| 8 | Handoff Checklist | `validate_protocol_handoff.py` | 📦 Med | 3h | ✅ Yes |
| 9 | Cognitive Reasoning | `validate_protocol_reasoning.py` | 🧠 Low | 6h | ✅ Yes |
| 10 | Meta-Reflection | `validate_protocol_reflection.py` | 🧠 Low | 5h | ✅ Yes |

### Master Orchestrator
| Component | File | Priority | Time | Spec Ready |
|-----------|------|----------|------|------------|
| Orchestrator | `validate_all_protocols.py` | 🎯 Final | 3h | ✅ Yes |

---

## 🔧 IMPLEMENTATION WORKFLOW

### For Each Validator (Repeat 9 times)

#### Phase A: Preparation (15 minutes)
```bash
# 1. Read specification
cat documentation/MASTER-VALIDATOR-COMPLETE-SPEC.md | grep "VALIDATOR [N]"

# 2. Read implementation guide
cat documentation/VALIDATOR-GENERATOR-PROMPT.md | grep "VALIDATOR [N]"

# 3. Check quick reference
cat documentation/VALIDATOR-QUICK-REFERENCE.md
```

#### Phase B: Implementation (3-6 hours)
```bash
# 1. Copy template
cp scripts/validate_protocol_identity.py scripts/validate_protocol_[name].py

# 2. Implement 5 dimensions
# - Follow VALIDATOR-GENERATOR-PROMPT.md
# - Use patterns from VALIDATOR-QUICK-REFERENCE.md
# - Reference validate_protocol_identity.py

# 3. Set correct weights
# - Check MASTER-VALIDATOR-COMPLETE-SPEC.md for weights
# - Ensure weights sum to 1.0

# 4. Implement validation logic
# - Extract sections from protocol files
# - Check for required elements
# - Calculate scores
# - Generate issues and recommendations
```

#### Phase C: Testing (1 hour)
```bash
# 1. Create test script
cat > tests/test_protocol_[name]_validator.sh << 'EOF'
#!/bin/bash
echo "Testing [Validator Name]..."
python3 scripts/validate_protocol_[name].py --protocol 01
# Add 10 tests similar to test_protocol_identity_validator.sh
EOF

# 2. Make executable
chmod +x tests/test_protocol_[name]_validator.sh

# 3. Run tests
./tests/test_protocol_[name]_validator.sh

# 4. Validate all protocols
python3 scripts/validate_protocol_[name].py --all
```

#### Phase D: Documentation (30 minutes)
```bash
# 1. Create usage guide
cat > documentation/validator-[N]-guide.md << 'EOF'
# Validator [N]: [Name] - User Guide
## Quick Start
## Usage Examples
## Output Format
## Common Issues
EOF

# 2. Update registry
# Add to ../scripts/script-registry.json

# 3. Document results
# Save validation findings
```

---

## 📖 KEY DOCUMENTATION FILES

### Must Read (Before Starting)
1. **MASTER-VALIDATOR-COMPLETE-SPEC.md** (1,110 lines)
   - Complete specification for all 10 validators
   - 5 dimensions per validator
   - Pass criteria and examples

2. **VALIDATOR-GENERATOR-PROMPT.md** (580 lines)
   - Complete Python template
   - Step-by-step implementation guide
   - Specific instructions per validator

3. **VALIDATOR-QUICK-REFERENCE.md** (380 lines)
   - Quick patterns and examples
   - 30-minute speed run guide
   - Common issues and fixes

### Reference (While Implementing)
4. **validate_protocol_identity.py** (656 lines)
   - Working example validator
   - All 5 dimensions implemented
   - Proper error handling

5. **test_protocol_identity_validator.sh** (234 lines)
   - Complete test suite example
   - 10 tests covering all scenarios

### Status Tracking
6. **VALIDATOR-IMPLEMENTATION-SUMMARY.md** (450 lines)
   - Current status and progress
   - Roadmap and timeline
   - Success metrics

---

## 🎯 VALIDATION DIMENSIONS OVERVIEW

Each validator must implement **5 dimensions** with specific weights:

### Example: Validator 2 (AI Role)
```python
# Dimension 1: Role Definition (25%)
# - Check for role title and description
# - Validate role clarity

# Dimension 2: Mission Statement (25%)
# - Check mission clarity
# - Validate boundaries and success criteria

# Dimension 3: Constraints & Guidelines (20%)
# - Count [CRITICAL], [MUST], [GUIDELINE] markers
# - Validate constraint completeness

# Dimension 4: Output Expectations (15%)
# - Check output format specifications
# - Validate structure and location

# Dimension 5: Behavioral Guidance (15%)
# - Check communication style
# - Validate decision-making guidance

# Weights must sum to 1.0
weights = [0.25, 0.25, 0.20, 0.15, 0.15]
```

---

## 🔍 WHERE TO FIND THINGS

### Protocol Files to Validate
```
Location: ../.cursor/ai-driven-workflow/*.md
Count: 27 protocol files (01-27)
Format: Markdown with specific sections
```

### Gate Configuration Files
```
Location: ../config/protocol_gates/*.yaml
Purpose: Automated gate definitions
Used by: Validator 4 (Quality Gates)
```

### Script Registry
```
Location: ../scripts/script-registry.json
Purpose: Register all validators
Update: After creating each validator
```

### Output Directory
```
Location: ../.artifacts/validation/
Contents: Individual results + summary reports
Format: JSON files
```

---

## ✅ SUCCESS CRITERIA

### Per-Validator Checklist
- [ ] All 5 dimensions implemented
- [ ] Weights sum to 1.0
- [ ] Pass criteria correct (PASS ≥0.95, WARNING ≥0.80)
- [ ] Single protocol validation works
- [ ] Batch validation works
- [ ] JSON output valid
- [ ] Test suite created (10 tests)
- [ ] All tests passing
- [ ] Documentation created
- [ ] Registered in script-registry.json

### Overall System Goals
- [ ] All 10 validators implemented
- [ ] Master orchestrator working
- [ ] Average protocol score ≥95%
- [ ] 100% pass rate
- [ ] Zero critical issues
- [ ] CI/CD integrated

---

## 🚨 COMMON PITFALLS TO AVOID

### 1. Incorrect Weights
```python
# ❌ WRONG - Sum = 1.25
weights = [0.25, 0.25, 0.25, 0.25, 0.25]

# ✅ CORRECT - Sum = 1.0
weights = [0.25, 0.25, 0.20, 0.15, 0.15]
```

### 2. Section Extraction
```python
# ❌ WRONG - Too strict
pattern = rf'^##\s+{section_name}'

# ✅ CORRECT - Flexible for numbered sections
pattern = rf'^##\s+(?:\d+\.\s+)?{re.escape(section_name)}'
```

### 3. Status Determination
```python
# ❌ WRONG - Hardcoded thresholds
if score > 0.9:
    status = "pass"

# ✅ CORRECT - Use spec thresholds
if score >= 0.95:
    status = "pass"
elif score >= 0.80:
    status = "warning"
else:
    status = "fail"
```

### 4. File Paths
```python
# ❌ WRONG - Relative paths
protocol_file = f"{protocol_id}-*.md"

# ✅ CORRECT - Absolute paths
protocol_file = self.protocols_dir / f"{protocol_id}-*.md"
```

---

## 🎓 LEARNING PATH

### Beginner (First Validator)
1. Read all documentation (1 hour)
2. Study validate_protocol_identity.py (1 hour)
3. Implement Validator 2 following guide exactly (6 hours)
4. Test thoroughly (1 hour)
5. Document learnings (30 min)

**Total**: ~9-10 hours for first validator

### Intermediate (Validators 3-6)
1. Quick spec review (15 min)
2. Copy and modify template (3-4 hours)
3. Test (30 min)
4. Document (15 min)

**Total**: ~4-5 hours per validator

### Advanced (Validators 7-10)
1. Spec review (10 min)
2. Rapid implementation (2-3 hours)
3. Quick test (15 min)
4. Minimal docs (10 min)

**Total**: ~2-3 hours per validator

---

## 📞 SUPPORT & RESOURCES

### If You Get Stuck

**Problem**: Hindi ko maintindihan ang spec
**Solution**: Basahin ang VALIDATOR-IMPLEMENTATION-SUMMARY.md first

**Problem**: Hindi ko alam paano mag-start
**Solution**: Follow VALIDATOR-GENERATOR-PROMPT.md step-by-step

**Problem**: May error sa code
**Solution**: Compare sa validate_protocol_identity.py

**Problem**: Hindi pumapasa ang tests
**Solution**: Check VALIDATOR-QUICK-REFERENCE.md common issues

**Problem**: Hindi ko alam ang expected output
**Solution**: Tingnan ang examples/validation-results/

---

## 🎯 NEXT ACTIONS

### Immediate (Today)
1. ✅ Read this AGENTS.md file
2. ⏭️ Read VALIDATOR-IMPLEMENTATION-SUMMARY.md
3. ⏭️ Read MASTER-VALIDATOR-COMPLETE-SPEC.md (Validator 2 section)
4. ⏭️ Start implementing Validator 2

### This Week
1. Complete Validator 2 (AI Role)
2. Complete Validator 3 (Workflow Algorithm)
3. Complete Validator 4 (Quality Gates)
4. Test all three validators
5. Document findings

### This Month
1. Complete all 10 validators
2. Implement master orchestrator
3. Full system testing
4. CI/CD integration
5. Final documentation

---

## 🎉 MOTIVATION

**You Can Do This!** 💪

- ✅ Complete specification available
- ✅ Step-by-step guide ready
- ✅ Working example provided
- ✅ Test suite template available
- ✅ All patterns documented

**Estimated Time**: 45 hours development (1-2 weeks)

**Impact**: Enable automated validation of 27 protocols across 10 dimensions!

---

## 📊 PROGRESS TRACKING

Update this section as you complete validators:

```yaml
Phase 1 (Critical):
  - Validator 2 (AI Role): ⏭️ TODO
  - Validator 3 (Workflow): ⏭️ TODO
  - Validator 4 (Quality Gates): ⏭️ TODO

Phase 2 (Integration):
  - Validator 5 (Scripts): ⏭️ TODO
  - Validator 6 (Communication): ⏭️ TODO

Phase 3 (Evidence):
  - Validator 7 (Evidence): ⏭️ TODO
  - Validator 8 (Handoff): ⏭️ TODO

Phase 4 (Advanced):
  - Validator 9 (Reasoning): ⏭️ TODO
  - Validator 10 (Reflection): ⏭️ TODO
  - Master Orchestrator: ⏭️ TODO
```

---

**READY TO START?** 🚀  
**BEGIN WITH**: `documentation/VALIDATOR-GENERATOR-PROMPT.md`  
**FIRST TASK**: Implement Validator 2 (AI Role)

**KAYA MO YAN!** 💪 **LET'S GO!** 🎯
