# 🎯 VALIDATOR QUICK REFERENCE CARD

## GAMITIN ITO PARA GUMAWA NG VALIDATOR

### 1️⃣ STEP 1: Piliin ang Validator

```bash
# Tingnan ang list ng validators sa MASTER-VALIDATOR-COMPLETE-SPEC.md
# Piliin ang susunod na gagawin (2-10)

Validator 2: AI Role ⏭️ NEXT
Validator 3: Workflow Algorithm ⏭️
Validator 4: Quality Gates ⏭️
Validator 5: Script Integration ⏭️
Validator 6: Communication Protocol ⏭️
Validator 7: Evidence Package ⏭️
Validator 8: Handoff Checklist ⏭️
Validator 9: Cognitive Reasoning ⏭️
Validator 10: Meta-Reflection ⏭️
```

### 2️⃣ STEP 2: Copy ang Template

```bash
# Copy ang template mula sa VALIDATOR-GENERATOR-PROMPT.md
# I-save bilang: scripts/validate_protocol_[name].py

cp documentation/VALIDATOR-GENERATOR-PROMPT.md scripts/validate_protocol_role.py
# Then edit the file
```

### 3️⃣ STEP 3: Palitan ang Placeholders

```python
# Palitan ito:
[ValidatorName]Validator → ProtocolRoleValidator
[validator_name] → "protocol_role"
[validator purpose] → "AI role definition and mission clarity"

# Example:
class ProtocolRoleValidator:
    """Validates AI role definition and mission clarity"""
```

### 4️⃣ STEP 4: Implement ang 5 Dimensions

```python
def _validate_dimension_1(self, content: str) -> Dict[str, Any]:
    """Validate Role Definition (25%)"""
    
    # 1. Extract section
    role_section = self._extract_section(content, "AI ROLE AND MISSION")
    
    # 2. Check for elements
    has_role_title = bool(re.search(r'You are a \*\*([^*]+)\*\*', role_section))
    has_description = len(role_section) > 100
    
    # 3. Calculate score
    if has_role_title and has_description:
        score = 1.0  # PASS
    elif has_role_title:
        score = 0.85  # WARNING
    else:
        score = 0.0  # FAIL
    
    # 4. Return result
    return {
        "score": score,
        "status": "pass" if score >= 0.95 else "warning" if score >= 0.80 else "fail",
        "issues": [] if score >= 0.95 else ["Missing role description"],
        "elements_found": {
            "role_title": has_role_title,
            "description": has_description
        }
    }
```

### 5️⃣ STEP 5: Set ang Weights

```python
# Based sa spec, set ang weights per dimension
# Example for Validator 2 (AI Role):

weights = [0.25, 0.25, 0.20, 0.15, 0.15]  # Total = 1.0

# Dimension 1: Role Definition (25%)
# Dimension 2: Mission Statement (25%)
# Dimension 3: Constraints (20%)
# Dimension 4: Output Expectations (15%)
# Dimension 5: Behavioral Guidance (15%)
```

### 6️⃣ STEP 6: Test ang Validator

```bash
# Make executable
chmod +x scripts/validate_protocol_role.py

# Test single protocol
python3 scripts/validate_protocol_role.py --protocol 01

# Test all protocols
python3 scripts/validate_protocol_role.py --all
```

### 7️⃣ STEP 7: Create Test Script

```bash
# Create test script
cat > scripts/test_protocol_role_validator.sh << 'EOF'
#!/bin/bash
echo "Testing Protocol Role Validator..."
python3 scripts/validate_protocol_role.py --protocol 01
if [ $? -eq 0 ] || [ $? -eq 1 ]; then
    echo "✅ Test PASSED"
else
    echo "❌ Test FAILED"
    exit 1
fi
EOF

chmod +x scripts/test_protocol_role_validator.sh
./scripts/test_protocol_role_validator.sh
```

### 8️⃣ STEP 8: Update Registry

```bash
# Add to scripts/script-registry.json
{
  "quality": {
    ...
    "validate-protocol-role": "scripts/validate_protocol_role.py",
    "test-protocol-role-validator": "scripts/test_protocol_role_validator.sh"
  }
}
```

---

## 📋 CHEAT SHEET: Common Patterns

### Pattern 1: Extract Section
```python
def _extract_section(self, content: str, section_name: str) -> str:
    pattern = rf'^##\s+(?:\d+\.\s+)?{re.escape(section_name)}.*?\n(.*?)(?=^##\s+|\Z)'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE | re.MULTILINE)
    return match.group(1) if match else ""
```

### Pattern 2: Count Markers
```python
critical_count = content.count('[CRITICAL]')
must_count = content.count('[MUST]')
guideline_count = content.count('[GUIDELINE]')
```

### Pattern 3: Find Files
```python
protocol_file = self._find_protocol_file(protocol_id)
if not protocol_file or not protocol_file.exists():
    result["issues"].append(f"Protocol file not found")
    return result
```

### Pattern 4: Calculate Score
```python
# Binary (yes/no)
score = 1.0 if condition else 0.0

# Percentage
score = items_found / total_items

# Weighted
score = (score1 * 0.25) + (score2 * 0.25) + (score3 * 0.20) + ...
```

### Pattern 5: Determine Status
```python
if score >= 0.95:
    status = "pass"
elif score >= 0.80:
    status = "warning"
else:
    status = "fail"
```

---

## 🎯 VALIDATOR-SPECIFIC QUICK GUIDES

### Validator 2: AI Role
**File**: `validate_protocol_role.py`  
**Section**: `## AI ROLE AND MISSION`  
**Key Checks**: Role title, mission statement, constraints  
**Weights**: 25%, 25%, 20%, 15%, 15%

### Validator 3: Workflow
**File**: `validate_protocol_workflow.py`  
**Section**: `## WORKFLOW`  
**Key Checks**: Steps, markers, halt conditions  
**Weights**: 20%, 25%, 15%, 20%, 20%

### Validator 4: Quality Gates
**File**: `validate_protocol_gates.py`  
**Section**: `## QUALITY GATES`  
**Key Checks**: Gate definitions, automation, compliance  
**Weights**: 25%, 25%, 20%, 15%, 15%

### Validator 5: Scripts
**File**: `validate_protocol_scripts.py`  
**Section**: `## AUTOMATION HOOKS`  
**Key Checks**: Script existence, registration, syntax  
**Weights**: 20%, 25%, 20%, 20%, 15%

### Validator 6: Communication
**File**: `validate_protocol_communication.py`  
**Section**: `## COMMUNICATION PROTOCOLS`  
**Key Checks**: Announcements, prompts, errors  
**Weights**: 25%, 25%, 20%, 15%, 15%

### Validator 7: Evidence
**File**: `validate_protocol_evidence.py`  
**Section**: `## EVIDENCE SUMMARY`  
**Key Checks**: Artifacts, storage, manifest  
**Weights**: 30%, 20%, 20%, 15%, 15%

### Validator 8: Handoff
**File**: `validate_protocol_handoff.py`  
**Section**: `## HANDOFF CHECKLIST`  
**Key Checks**: Checklist items, verification, sign-off  
**Weights**: 30%, 25%, 20%, 15%, 10%

### Validator 9: Reasoning
**File**: `validate_protocol_reasoning.py`  
**Section**: Throughout protocol  
**Key Checks**: Patterns, decisions, problem-solving  
**Weights**: 25%, 25%, 20%, 15%, 15%

### Validator 10: Reflection
**File**: `validate_protocol_reflection.py`  
**Section**: Throughout protocol  
**Key Checks**: Retrospective, improvement, evolution  
**Weights**: 30%, 25%, 20%, 15%, 10%

---

## ⚡ SPEED RUN: 30-Minute Validator

Kung gusto mo mabilis lang:

```bash
# 1. Copy template (2 min)
cp scripts/validate_protocol_identity.py scripts/validate_protocol_role.py

# 2. Find & replace (3 min)
# ProtocolIdentityValidator → ProtocolRoleValidator
# protocol_identity → protocol_role

# 3. Update dimensions (15 min)
# Implement 5 _validate_dimension_X functions

# 4. Update weights (2 min)
weights = [0.25, 0.25, 0.20, 0.15, 0.15]

# 5. Test (5 min)
python3 scripts/validate_protocol_role.py --protocol 01

# 6. Document (3 min)
# Update script-registry.json
# Add to README
```

---

## 🐛 Common Issues & Fixes

### Issue: "Protocol file not found"
```python
# Fix: Check file pattern
pattern = f"{protocol_id}-*.md"  # Correct
pattern = f"{protocol_id}.md"    # Wrong
```

### Issue: "Section not found"
```python
# Fix: Make regex more flexible
pattern = rf'^##\s+(?:\d+\.\s+)?{re.escape(section_name)}'  # Flexible
pattern = rf'^##\s+{re.escape(section_name)}'               # Strict
```

### Issue: "Score calculation wrong"
```python
# Fix: Check weights sum to 1.0
weights = [0.25, 0.25, 0.20, 0.15, 0.15]  # Sum = 1.0 ✅
weights = [0.25, 0.25, 0.25, 0.25, 0.25]  # Sum = 1.25 ❌
```

### Issue: "JSON invalid"
```python
# Fix: Use proper datetime format
datetime.utcnow().isoformat() + "Z"  # Correct
str(datetime.now())                   # Wrong
```

---

## 📊 Expected Output Format

```json
{
  "validator": "protocol_role",
  "protocol_id": "01",
  "validation_timestamp": "2025-10-20T12:00:00Z",
  "role_definition": {
    "score": 1.0,
    "status": "pass",
    "issues": [],
    "elements_found": {
      "role_title": true,
      "description": true
    }
  },
  "mission_statement": {"score": 0.85, "status": "warning"},
  "constraints": {"score": 1.0, "status": "pass"},
  "output_expectations": {"score": 0.90, "status": "pass"},
  "behavioral_guidance": {"score": 0.80, "status": "warning"},
  "overall_score": 0.91,
  "validation_status": "pass",
  "issues": ["Mission boundaries not clearly defined"],
  "recommendations": ["Add explicit scope boundaries to mission statement"]
}
```

---

## ✅ Pre-Submit Checklist

Before submitting your validator:

- [ ] Script runs without errors
- [ ] Single protocol validation works
- [ ] Batch validation works
- [ ] JSON output is valid
- [ ] All 5 dimensions implemented
- [ ] Weights sum to 1.0
- [ ] Pass criteria correct
- [ ] Test script created
- [ ] Test script passing
- [ ] Added to script-registry.json
- [ ] Documentation updated
- [ ] No hardcoded values
- [ ] Error handling present
- [ ] Exit codes correct

---

**GOOD LUCK!** 🚀 **KAYA MO YAN!** 💪
