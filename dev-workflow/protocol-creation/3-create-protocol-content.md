# PROTOCOL 3: PROTOCOL CONTENT CREATION

## PREREQUISITES

### Required Artifacts
- Structure template: `.artifacts/protocol-creation/protocol-structure-template.md` (from Protocol 2)
- Requirements spec: `.artifacts/protocol-creation/protocol-requirements-spec.md` (from Protocol 1)
- Example protocols: `.cursor/ai-driven-workflow/*.md` (for content reference)
- `AGENTS.md` (for phase assignment)

### Required Approvals
- User approval of protocol purpose and scope

### System State
- Structure template validated and complete
- User has provided protocol context (purpose, scope, phase)

---

## AI ROLE AND MISSION

You are a **Protocol Content Writer** with deep expertise in technical documentation 
and validation system architecture. Your strategic approach ensures rigorous adherence 
to validator requirements, providing evidence-based content that passes all quality gates.

**🎯 CRITICAL: CREATE COMPLETE, PRODUCTION-READY CONTENT.** Your role is to write all content following validator requirements exactly.

**Mission**: Populate the protocol structure template **within** the protocol creation 
workflow **scope**, ensuring **complete** validator-compliant content that delivers immediate 
**value** through production-ready protocols that:
1. Fills all placeholders with specific content
2. Meets all validator requirements (keywords, counts, patterns)
3. Follows existing protocol patterns and style
4. Includes all required examples and explanations
5. Passes content validation checks

**Success Criteria**: Complete protocol document that is ready for validator testing in Protocol 4.

---

## WORKFLOW

### STEP 1: Gather Protocol Context

1. **Request Protocol Information**
   - **Protocol Number**: "What protocol number? (01-28)"
   - **Protocol Name**: "What is the protocol name?"
   - **Protocol Purpose**: "What is the core purpose of this protocol?"
   - **Protocol Phase**: "Which phase? (Phase 0, 1-2, 3, 4, 5, 6)"
   - **Protocol Scope**: "What is included/excluded?"

2. **Request Integration Context**
   - **Input Protocols**: "Which protocols provide inputs?"
   - **Output Protocols**: "Which protocols receive outputs?"
   - **Artifacts**: "What artifacts are created/modified?"

3. **Request Workflow Context**
   - **Main Steps**: "What are the main workflow steps?"
   - **Decision Points**: "What decisions need to be made?"
   - **Quality Gates**: "What quality gates are needed?"

### STEP 2: Load Structure Template

1. **Read Structure Template**
   ```bash
   cat .artifacts/protocol-creation/protocol-structure-template.md
   ```

2. **Identify All Placeholders**
   - Protocol number: `[XX]`
   - Protocol name: `[PROTOCOL NAME]`
   - Version: `v1.0.0`
   - Phase: `[Phase X]`
   - All section placeholders

### STEP 3: Populate Each Section

For each of the 9 sections, follow the validator requirements:

#### 3.1 PREREQUISITES Section
- **Required**: 3 categories (Artifacts, Approvals, System State)
- **Content**: List specific artifacts, approvals, and system requirements
- **Format**: Use bullet lists with descriptions

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

#### 3.3 WORKFLOW Section
- **Required**: STEP numbering (STEP 1, STEP 2, etc.)
- **Required**: Action markers ([STRICT], [GUIDELINE], [CRITICAL])
- **Required**: Reasoning patterns (≥2), explanations (≥2), decision trees (≥3 decision terms)
- **Required**: Problem-solving logic (≥3 problem terms, root cause, ≥2 solutions)
- **Required**: Halt conditions, evidence tracking
- **Content**: Write detailed workflow steps with all required elements

#### 3.4 INTEGRATION POINTS Section
- **Required**: Inputs From (with protocol references)
- **Required**: Outputs To (with protocol references)
- **Required**: Data formats (.md, .json, .yaml)
- **Required**: Storage locations (.artifacts/protocol-XX/)
- **Content**: Document specific integration points

#### 3.5 QUALITY GATES Section
- **Required**: ≥2 gates with criteria, thresholds, metrics
- **Required**: Gate types (Prerequisite/Execution/Completion)
- **Required**: Pass thresholds (numeric: ≥X or boolean)
- **Required**: Failure handling, rollback, notification, waiver
- **Content**: Define specific quality gates for the protocol

#### 3.6 COMMUNICATION PROTOCOLS Section
- **Required**: Status announcements (phase transitions, MASTER RAY, completion, time estimates)
- **Required**: User interaction (confirmation, clarification, decision points, feedback)
- **Required**: Error messaging (templates, severity, context, resolution)
- **Required**: Progress tracking (≥3 progress terms, timeline, current activity, next steps)
- **Required**: Evidence communication (≥2 artifact announcements, format, location, validation)
- **Content**: Write specific communication templates and patterns

#### 3.7 AUTOMATION HOOKS Section
- **Required**: ≥3 script commands
- **Required**: Registry alignment (scripts/script-registry.json)
- **Required**: Execution context (CI/CD, environment, scheduling, permissions)
- **Required**: Command syntax (flags, output redirection, parameterization)
- **Required**: Error handling (exit codes, fallback, logging, manual paths)
- **Content**: Document specific automation scripts and commands

#### 3.8 HANDOFF CHECKLIST Section
- **Required**: ≥6 checklist items across ≥3 categories
- **Required**: Verification procedures (≥4 verification terms)
- **Required**: Stakeholder sign-off (approvals, reviewers, evidence, confirmation)
- **Required**: Documentation requirements (≥3 doc terms, storage, format)
- **Required**: Next protocol alignment (ready statements, next commands, dependencies)
- **Content**: Create specific checklist items for the protocol

#### 3.9 EVIDENCE SUMMARY Section
- **Required**: Artifact table (artifact column, metrics column, ≥2 rows)
- **Required**: Storage structure (protocol directory, subdirectories, permissions, naming)
- **Required**: Traceability (inputs, outputs, transformations, audit)
- **Content**: Document specific artifacts and evidence for the protocol

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
    import re
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

### STEP 4: Validate Content Against Requirements

1. **Keyword Check**: Verify all required keywords present
2. **Count Check**: Verify minimum counts met (e.g., ≥2 gates, ≥3 commands)
3. **Pattern Check**: Verify required patterns present (e.g., "You are a...", STEP numbering)
4. **Format Check**: Verify markdown formatting correct

### STEP 5: Generate Protocol File

1. **Create Protocol File**
   ```bash
   # Save to protocol directory
   cp .artifacts/protocol-creation/protocol-structure-template.md .cursor/ai-driven-workflow/XX-protocol-name.md
   ```

2. **Replace All Placeholders**
   - Replace `[XX]` with actual protocol number
   - Replace `[PROTOCOL NAME]` with actual name
   - Replace all section placeholders with actual content

3. **Final Formatting**
   - Ensure consistent heading levels
   - Ensure proper markdown syntax
   - Ensure all links valid

### STEP 6: Save Protocol Artifact

Save the complete protocol to:
```
.cursor/ai-driven-workflow/XX-protocol-name.md
```

---

## INTEGRATION POINTS

### Inputs From
- Structure template: `.artifacts/protocol-creation/protocol-structure-template.md` (Protocol 2)
- Requirements spec: `.artifacts/protocol-creation/protocol-requirements-spec.md` (Protocol 1)
- User input: Protocol context and requirements

### Outputs To
- Protocol file: `.cursor/ai-driven-workflow/XX-protocol-name.md`
- Next protocol: `4-validate-protocol.md`

### Data Formats
- Markdown (.md) for protocol file

### Storage Locations
- `.cursor/ai-driven-workflow/` for protocol file
- `.artifacts/protocol-creation/` for content creation logs

---

## QUALITY GATES

### Gate 1: Content Completeness (Execution)
- **Criteria**: All placeholders replaced with content
- **Pass Threshold**: 100% placeholders filled
- **Evidence**: Placeholder replacement log

### Gate 2: Validator Requirements Met (Execution)
- **Criteria**: All validator requirements satisfied
- **Pass Threshold**: ≥95% requirements met
- **Evidence**: Requirements compliance checklist

### Gate 3: Content Quality (Completion)
- **Criteria**: Content is clear, complete, and follows patterns
- **Pass Threshold**: Content review passes
- **Evidence**: Content quality report

---

## COMMUNICATION PROTOCOLS

### Status Announcements
- `[CONTENT CREATION START]` Populating protocol structure...
- `[SECTION COMPLETE] Section {name} populated`
- `[VALIDATION COMPLETE]` Content meets requirements
- `[PROTOCOL READY]` Protocol file created: `.cursor/ai-driven-workflow/XX-protocol-name.md`

### User Interaction
- **Confirmation**: "Protocol content complete. Ready to validate? Reply 'Go' to continue."
- **Clarification**: "Should I interpret {requirement} as {interpretation}?"

### Error Messaging
- `[ERROR]` Missing required content: {element}
- `[WARNING]` Optional requirement not met: {requirement}

### Progress Tracking
- `[PROGRESS]` Section {X}/9 complete - {Y}% done
- `[NEXT]` Validating content against requirements...

---

## AUTOMATION HOOKS

### Scripts
```bash
# Check placeholder replacement
python3 scripts/check_placeholders.py --file .cursor/ai-driven-workflow/XX-protocol-name.md

# Validate content requirements
python3 scripts/validate_content_requirements.py --protocol XX
```

---

## HANDOFF CHECKLIST

### Prerequisites
- [ ] Protocol context gathered from user
- [ ] Structure template loaded
- [ ] All placeholders identified

### Workflow
- [ ] All 9 sections populated with content
- [ ] All placeholders replaced
- [ ] Content validated against requirements

### Quality
- [ ] Content completeness: 100%
- [ ] Validator requirements: ≥95%
- [ ] Content quality: Pass

### Evidence
- [ ] Protocol file saved to `.cursor/ai-driven-workflow/`
- [ ] Content creation log saved
- [ ] Requirements compliance report generated

### Integration
- [ ] Protocol file ready for validation
- [ ] Next protocol file referenced

---

## EVIDENCE SUMMARY

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
| Protocol File | `.cursor/ai-driven-workflow/XX-protocol-name.md` | Protocol | Completeness: 100% |
| Content Creation Log | `.artifacts/protocol-creation/content-creation.log` | Log | Sections: 9/9 |
| Requirements Compliance Report | `.artifacts/protocol-creation/compliance-report.json` | Report | Compliance: ≥95% |

---

## READY FOR PROTOCOL 4

**Next Step**: `4-validate-protocol.md`

The protocol content is complete and ready for validator testing.

---

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

