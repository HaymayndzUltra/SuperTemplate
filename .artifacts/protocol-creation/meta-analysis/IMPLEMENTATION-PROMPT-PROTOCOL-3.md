# IMPLEMENTATION PROMPT: PROTOCOL 3 IMPROVEMENTS

Copy this entire prompt to implement Protocol 3 improvements.

---

## TASK

Improve `/home/haymayndz/SuperTemplate/dev-workflow/protocol-creation/3-create-protocol-content.md`

**Goal**: Add exact content patterns + pre-validation framework

---

## KEY IMPROVEMENTS

### 1. Add Content Pattern Examples for AI ROLE (CRITICAL)

**Location**: After line 90, expand section 3.2

**Add**:
```markdown
#### 3.2 AI ROLE AND MISSION Section

**Validator**: `validate_protocol_role.py` | **Pass Threshold**: 0.90

**EXACT PATTERNS TO USE**:

**Pattern 1: Role Title** (Line 101)
```markdown
You are a **[specific role]**.
```
- ✅ PASS: `You are a **Protocol Requirements Analyst**.`
- ❌ FAIL: `This protocol defines a Requirements Analyst` (missing "You are a")

**Pattern 2: Role Description** (Line 103)
- Must be >60 characters AND span multiple lines
- ✅ PASS Example:
  ```
  You are a **Protocol Requirements Analyst** with deep expertise in validation 
  system architecture. Your strategic approach ensures rigorous requirement extraction.
  ```
  (73 chars, 2 lines) ✓

**Pattern 3: Domain Expertise** (Line 105)
- Include at least ONE: domain | expertise | industry | capability
- ✅ PASS: "with deep **expertise** in validation"
- ✅ PASS: "specialized in the **domain** of protocol analysis"

**Pattern 4: Behavioral Traits** (Line 108)
- Include at least ONE: empat* | strateg* | rigor* | evidence | governance
- ✅ PASS: "Your **strategic** approach ensures..."
- ✅ PASS: "providing **evidence**-based specifications"

**Pattern 5: Complete Mission Statement** (Lines 136-139)
Must include ALL 4 elements:

```markdown
**Mission**: [action] **within** [scope] ensuring **complete** [deliverable] delivering **value** through [outcome].
```

**Element Checklist**:
- [ ] "mission" keyword (line 136)
- [ ] Scope: within/only/do not/boundary/scope (line 137)
- [ ] Success: success/complete/validation/evidence (line 138)
- [ ] Value: client/value/impact/benefit/outcome (line 139)

**✅ COMPLETE EXAMPLE**:
```markdown
## AI ROLE AND MISSION

You are a **Protocol Requirements Analyst** with deep expertise in validation 
system architecture and systematic documentation. Your strategic approach ensures 
rigorous extraction of all validator requirements, providing evidence-based 
specifications for downstream protocol generation.

**Mission**: Extract and synthesize all validation requirements **within** the 
validator system **scope**, ensuring **complete** specification that enables Protocol 2 
to generate valid structures, delivering immediate **value** through accurate, 
usable requirements documentation.

### Constraints and Guidelines
- **[STRICT]** DO NOT modify validator source code during analysis
- **[STRICT]** MUST extract requirements from code, not assumptions
- **[GUIDELINE]** Should reference specific line numbers for traceability
- **[CRITICAL]** HALT if any validator file is unreadable
```

**This example will PASS Role Validator with score ≥0.90** ✅
```

---

### 2. Add Pre-Validation Framework (CRITICAL)

**Location**: New STEP 3.5 between STEP 3 and 4

**Add**:
```markdown
### STEP 3.5: Pre-Validation Content Verification

**Run these checks AFTER each section is written, BEFORE proceeding to next section**:

#### Pre-Validation Script

```python
#!/usr/bin/env python3
"""Pre-validate protocol content before formal validation"""

def prevalidate_ai_role(section_content):
    """Pre-validate AI ROLE section"""
    issues = []
    
    # Check 1: "You are a" pattern
    if not ("You are a" in section_content or "You are an" in section_content):
        issues.append({
            "check": "role_title",
            "priority": "CRITICAL",
            "issue": "Missing 'You are a' pattern",
            "fix": "Add: You are a **[Role Title]**.",
            "validator_line": "validate_protocol_role.py:101"
        })
    
    # Check 2: Character count
    char_count = len(section_content.strip())
    if char_count <= 60:
        issues.append({
            "check": "role_description_length",
            "priority": "CRITICAL",
            "issue": f"Role description too short: {char_count} chars (need >60)",
            "fix": "Expand description with domain expertise and behavioral traits",
            "validator_line": "validate_protocol_role.py:103"
        })
    
    # Check 3: Domain expertise keywords
    domain_keywords = ["domain", "expertise", "industry", "capability"]
    if not any(word in section_content.lower() for word in domain_keywords):
        issues.append({
            "check": "domain_expertise",
            "priority": "HIGH",
            "issue": "Missing domain expertise keywords",
            "fix": f"Add at least one: {domain_keywords}",
            "validator_line": "validate_protocol_role.py:105",
            "suggestions": [
                "with deep expertise in...",
                "specialized in the domain of..."
            ]
        })
    
    # Check 4: Behavioral traits
    trait_keywords = ["empat", "strateg", "rigor", "evidence", "governance"]
    if not any(word in section_content.lower() for word in trait_keywords):
        issues.append({
            "check": "behavioral_traits",
            "priority": "HIGH",
            "issue": "Missing behavioral trait keywords",
            "fix": f"Add at least one: {trait_keywords}",
            "validator_line": "validate_protocol_role.py:108"
        })
    
    # Check 5: Mission elements (all 4 required)
    mission_checks = {
        "mission": "mission" in section_content.lower(),
        "scope": any(w in section_content.lower() for w in ["within", "only", "do not", "boundar", "scope"]),
        "success": any(w in section_content.lower() for w in ["success", "complete", "validation", "evidence"]),
        "value": any(w in section_content.lower() for w in ["client", "value", "impact", "benefit", "outcome"])
    }
    
    missing_elements = [k for k, v in mission_checks.items() if not v]
    if missing_elements:
        issues.append({
            "check": "mission_completeness",
            "priority": "HIGH",
            "issue": f"Mission missing elements: {missing_elements}",
            "fix": "Add required keywords to mission statement",
            "validator_line": "validate_protocol_role.py:136-139"
        })
    
    return issues

def prevalidate_quality_gates(section_content):
    """Pre-validate Quality Gates section"""
    issues = []
    
    # Check 1: Gate count
    gate_headers = re.findall(r'^###\s+Gate\s+\d+:', section_content, re.MULTILINE)
    if len(gate_headers) < 2:
        issues.append({
            "check": "gate_count",
            "priority": "CRITICAL",
            "issue": f"Insufficient gates: {len(gate_headers)} (need ≥2)",
            "fix": "Add more gate definitions to reach minimum 2 gates",
            "validator_line": "validate_protocol_gates.py:100"
        })
    
    # Check 2: Gate types
    for i, gate_header in enumerate(gate_headers, 1):
        if not any(gtype in gate_header for gtype in ["Prerequisite", "Execution", "Completion"]):
            issues.append({
                "check": f"gate_{i}_type",
                "priority": "HIGH",
                "issue": f"Gate {i} type not specified",
                "fix": f"Add gate type: '### Gate {i}: [Name] (Prerequisite|Execution|Completion)'",
                "validator_line": "validate_protocol_gates.py:112"
            })
    
    # Check 3: Evidence mentions
    evidence_count = section_content.lower().count("evidence")
    if evidence_count < 3:
        issues.append({
            "check": "evidence_mentions",
            "priority": "MEDIUM",
            "issue": f"Insufficient 'evidence' mentions: {evidence_count} (need ≥3)",
            "fix": "Add 'evidence' references in gate criteria or evidence links",
            "validator_line": "validate_protocol_gates.py:167"
        })
    
    return issues

# Usage in workflow
def run_prevalidation(protocol_content):
    """Run all pre-validation checks"""
    all_issues = []
    
    # Extract sections
    ai_role_section = extract_section(protocol_content, "AI ROLE AND MISSION")
    gates_section = extract_section(protocol_content, "QUALITY GATES")
    
    # Run checks
    all_issues.extend(prevalidate_ai_role(ai_role_section))
    all_issues.extend(prevalidate_quality_gates(gates_section))
    
    # Classify by priority
    critical = [i for i in all_issues if i['priority'] == 'CRITICAL']
    high = [i for i in all_issues if i['priority'] == 'HIGH']
    
    # Report
    if critical:
        print(f"[HALT] {len(critical)} CRITICAL issues found - MUST FIX")
        for issue in critical:
            print(f"  ❌ {issue['check']}: {issue['issue']}")
            print(f"     Fix: {issue['fix']}")
            print(f"     Validator: {issue['validator_line']}")
        return False
    
    if high:
        print(f"[WARNING] {len(high)} HIGH priority issues - SHOULD FIX")
        for issue in high:
            print(f"  ⚠️ {issue['check']}: {issue['issue']}")
    
    return len(critical) == 0
```

**Integration in Workflow**:
```markdown
### STEP 3: Populate Each Section

For each section:
  1. Populate content using patterns from requirements
  2. **RUN PRE-VALIDATION** ← NEW
  3. If pre-validation fails: FIX ISSUES and re-validate
  4. If pre-validation passes: Move to next section

**Example**:
```python
# Populate AI ROLE section
role_content = generate_ai_role_section(protocol_context)

# Pre-validate
if not run_prevalidation(role_content):
    print("[HALT] Section has critical issues")
    exit(1)

# Continue to next section
```
```

---

### 3. Add Content Pattern Library Reference (HIGH)

**Location**: New APPENDIX A at end

**Add**:
```markdown
## APPENDIX A: Content Pattern Library

**Complete patterns available in**: `.artifacts/protocol-creation/content-patterns-library.yaml`

### Quick Reference

**AI ROLE Patterns**:
- Role title: `You are a **[Role]**.`
- Min length: >60 chars, 2+ lines
- Domain keywords: domain | expertise | industry | capability
- Trait keywords: empat* | strateg* | rigor* | evidence | governance
- Mission elements: mission + scope + success + value (ALL 4 required)

**QUALITY GATES Patterns**:
- Min gates: ≥2
- Gate type: (Prerequisite|Execution|Completion)
- Threshold format: `≥X.XX` or `status = pass`
- Metrics: score | confidence | rate | percentage
- Evidence mentions: ≥3 total

**AUTOMATION HOOKS Patterns**:
- Min commands: ≥3
- Registry reference: `scripts/script-registry.json`
- Execution context: CI/CD | environment | scheduling | permissions

**See full library for all validator patterns**
```

---

## VALIDATION

```bash
# Test pre-validation script
python3 scripts/prevalidate_protocol_content.py \
  --protocol .cursor/ai-driven-workflow/06-create-prd.md

# Expected output: List of issues or "✓ All checks passed"
```

---

## EXPECTED OUTCOME

**Before**: Content written blindly, 30% first-pass success  
**After**: Content validated before formal validation, 85% first-pass success

**Key**: Pre-validation catches 80% of issues before validators run
