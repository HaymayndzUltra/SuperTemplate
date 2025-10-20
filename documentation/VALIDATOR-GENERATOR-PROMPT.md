# 🎯 VALIDATOR GENERATOR PROMPT

**Layunin**: Gumawa ng automated validator scripts para sa AI-Driven Workflow System based sa MASTER-VALIDATOR-COMPLETE-SPEC.md

---

## 📝 INSTRUCTIONS PARA SA AI

Ikaw ay isang expert Python developer na gagawa ng production-ready validation scripts. Sundin ang template na ito para sa bawat validator:

### VALIDATOR NA GAGAWIN MO

**Validator Number**: [2-10]  
**Validator Name**: [Kunin sa spec]  
**Status**: TO IMPLEMENT

---

## 🔧 TEMPLATE PARA SA BAWAT VALIDATOR

### 1. BASAHIN ANG SPECIFICATION

```
Basahin ang MASTER-VALIDATOR-COMPLETE-SPEC.md
Hanapin ang section ng validator na gagawin mo
I-extract ang:
  - Purpose
  - 5 Validation Dimensions
  - Pass Criteria per dimension
  - Example locations sa protocol files
  - Expected output format
```

### 2. SCRIPT STRUCTURE

Gumawa ng Python script na may ganitong structure:

```python
#!/usr/bin/env python3
"""
[Validator Name] Validator
Validates [purpose statement from spec]
Specification: documentation/MASTER-VALIDATOR-COMPLETE-SPEC.md
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class [ValidatorName]Validator:
    """Validates [validator purpose]"""
    
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root
        self.protocols_dir = workspace_root / ".cursor" / "ai-driven-workflow"
        self.output_dir = workspace_root / ".artifacts" / "validation"
        
    def validate_protocol(self, protocol_id: str) -> Dict[str, Any]:
        """Validate a single protocol across all dimensions"""
        
        result = {
            "validator": "[validator_name]",
            "protocol_id": protocol_id,
            "validation_timestamp": datetime.utcnow().isoformat() + "Z",
            "dimension_1": {},  # Replace with actual dimension name
            "dimension_2": {},
            "dimension_3": {},
            "dimension_4": {},
            "dimension_5": {},
            "overall_score": 0.0,
            "validation_status": "fail",
            "issues": [],
            "recommendations": []
        }
        
        # Find protocol file
        protocol_file = self._find_protocol_file(protocol_id)
        if not protocol_file:
            result["issues"].append(f"Protocol file not found for ID {protocol_id}")
            return result
            
        # Read protocol content
        try:
            with open(protocol_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            result["issues"].append(f"Failed to read protocol: {str(e)}")
            return result
        
        # Run all validation dimensions
        result["dimension_1"] = self._validate_dimension_1(content)
        result["dimension_2"] = self._validate_dimension_2(content)
        result["dimension_3"] = self._validate_dimension_3(content)
        result["dimension_4"] = self._validate_dimension_4(content)
        result["dimension_5"] = self._validate_dimension_5(content)
        
        # Calculate overall score (weighted average)
        weights = [0.25, 0.25, 0.20, 0.15, 0.15]  # Adjust based on spec
        scores = [
            result["dimension_1"].get("score", 0),
            result["dimension_2"].get("score", 0),
            result["dimension_3"].get("score", 0),
            result["dimension_4"].get("score", 0),
            result["dimension_5"].get("score", 0)
        ]
        result["overall_score"] = sum(s * w for s, w in zip(scores, weights))
        
        # Determine status
        if result["overall_score"] >= 0.95:
            result["validation_status"] = "pass"
        elif result["overall_score"] >= 0.80:
            result["validation_status"] = "warning"
        else:
            result["validation_status"] = "fail"
            
        # Collect issues
        for dim in ["dimension_1", "dimension_2", "dimension_3", "dimension_4", "dimension_5"]:
            if "issues" in result[dim]:
                result["issues"].extend(result[dim]["issues"])
            if "recommendations" in result[dim]:
                result["recommendations"].extend(result[dim]["recommendations"])
        
        return result
    
    def _find_protocol_file(self, protocol_id: str) -> Path:
        """Find protocol file by ID"""
        pattern = f"{protocol_id}-*.md"
        matches = list(self.protocols_dir.glob(pattern))
        return matches[0] if matches else None
    
    def _validate_dimension_1(self, content: str) -> Dict[str, Any]:
        """Validate [dimension 1 name] ([weight]%)"""
        result = {
            "score": 0.0,
            "status": "fail",
            "issues": [],
            "recommendations": [],
            "elements_found": {}
        }
        
        # TODO: Implement validation logic based on spec
        # Check for required elements
        # Calculate score
        # Determine status
        
        return result
    
    # Repeat for _validate_dimension_2 through _validate_dimension_5
    
    def _extract_section(self, content: str, section_name: str) -> str:
        """Extract a section from markdown content"""
        pattern = rf'^##\s+(?:\d+\.\s+)?{re.escape(section_name)}.*?\n(.*?)(?=^##\s+|\Z)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE | re.MULTILINE)
        return match.group(1) if match else ""
    
    def generate_summary_reports(self, all_results: List[Dict[str, Any]]) -> None:
        """Generate summary reports from all validation results"""
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        summary = {
            "validation_timestamp": datetime.utcnow().isoformat() + "Z",
            "total_protocols": len(all_results),
            "pass_count": sum(1 for r in all_results if r["validation_status"] == "pass"),
            "warning_count": sum(1 for r in all_results if r["validation_status"] == "warning"),
            "fail_count": sum(1 for r in all_results if r["validation_status"] == "fail"),
            "average_score": sum(r["overall_score"] for r in all_results) / len(all_results) if all_results else 0,
            "protocols": [
                {
                    "protocol_id": r["protocol_id"],
                    "status": r["validation_status"],
                    "score": r["overall_score"]
                }
                for r in all_results
            ]
        }
        
        output_file = self.output_dir / f"[validator-name]-summary.json"
        with open(output_file, 'w') as f:
            json.dump(summary, f, indent=2)

def main():
    parser = argparse.ArgumentParser(
        description="Validate [validator purpose]"
    )
    parser.add_argument("--protocol", help="Validate single protocol by ID")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--report", action="store_true", help="Generate summary reports")
    parser.add_argument("--workspace", default=".", help="Workspace root directory")
    
    args = parser.parse_args()
    
    workspace_root = Path(args.workspace).resolve()
    validator = [ValidatorName]Validator(workspace_root)
    
    all_results = []
    
    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        all_results.append(result)
        
        # Save individual result
        output_file = validator.output_dir / f"protocol-{args.protocol}-[validator-name].json"
        validator.output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        
        status_icon = "✅" if result["validation_status"] == "pass" else "⚠️" if result["validation_status"] == "warning" else "❌"
        print(f"{status_icon} Validation complete for Protocol {args.protocol}")
        print(f"   Status: {result['validation_status'].upper()}")
        print(f"   Score: {result['overall_score']:.3f}")
        print(f"   Output: {output_file}")
        
    elif args.all:
        protocol_ids = [f"{i:02d}" for i in range(1, 28)]
        
        for protocol_id in protocol_ids:
            result = validator.validate_protocol(protocol_id)
            all_results.append(result)
            
            output_file = validator.output_dir / f"protocol-{protocol_id}-[validator-name].json"
            validator.output_dir.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w') as f:
                json.dump(result, f, indent=2)
            
            status_icon = "✅" if result["validation_status"] == "pass" else "⚠️" if result["validation_status"] == "warning" else "❌"
            print(f"{status_icon} Protocol {protocol_id}: {result['validation_status'].upper()} (score: {result['overall_score']:.3f})")
    
    if args.report or args.all:
        if all_results:
            validator.generate_summary_reports(all_results)
            print(f"\n📊 Summary reports generated in {validator.output_dir}/")
    
    # Exit with appropriate code
    if all_results:
        fail_count = sum(1 for r in all_results if r["validation_status"] == "fail")
        sys.exit(1 if fail_count > 0 else 0)

if __name__ == "__main__":
    main()
```

### 3. IMPLEMENTATION CHECKLIST

Para sa bawat validator, siguruhing:

#### ✅ Code Quality
- [ ] Walang hardcoded values
- [ ] May proper error handling
- [ ] May descriptive variable names
- [ ] May docstrings sa lahat ng functions
- [ ] Sumusunod sa PEP 8 style guide

#### ✅ Validation Logic
- [ ] Lahat ng 5 dimensions implemented
- [ ] Tama ang weights per dimension (based sa spec)
- [ ] Tama ang pass criteria (PASS/WARNING/FAIL thresholds)
- [ ] May specific error messages
- [ ] May actionable recommendations

#### ✅ Output Format
- [ ] JSON output na valid
- [ ] Lahat ng required fields present
- [ ] Timestamps in ISO 8601 format
- [ ] Scores in 0.0-1.0 range
- [ ] Status in ["pass", "warning", "fail"]

#### ✅ Testing
- [ ] Gumawa ng test script (test_[validator_name].sh)
- [ ] Test single protocol validation
- [ ] Test batch validation
- [ ] Test error handling
- [ ] Test summary report generation

#### ✅ Documentation
- [ ] Update script-registry.json
- [ ] Gumawa ng usage guide
- [ ] Magdagdag ng examples
- [ ] Document common issues

---

## 📋 PRIORITY ORDER NG MGA VALIDATORS

### Phase 1: Critical Validators (Gawin muna)
1. **Validator 2: AI Role** (4 hours)
   - Pinaka-importante for AI behavior
   - Madaling i-implement
   - High impact sa quality

2. **Validator 3: Workflow Algorithm** (6 hours)
   - Core ng protocol execution
   - Medium complexity
   - Critical for automation

3. **Validator 4: Quality Gates** (5 hours)
   - Ensures quality standards
   - Integrates with existing gates
   - High value

### Phase 2: Integration Validators
4. **Validator 5: Script Integration** (4 hours)
   - Validates automation
   - Links to script registry
   - Medium priority

5. **Validator 6: Communication Protocol** (4 hours)
   - User experience
   - Status updates
   - Medium priority

### Phase 3: Evidence & Handoff
6. **Validator 7: Evidence Package** (5 hours)
   - Artifact validation
   - Traceability
   - Important for compliance

7. **Validator 8: Handoff Checklist** (3 hours)
   - Completion verification
   - Stakeholder sign-off
   - Medium priority

### Phase 4: Advanced Validators
8. **Validator 9: Cognitive Reasoning** (6 hours)
   - Advanced feature
   - Lower priority
   - Nice to have

9. **Validator 10: Meta-Reflection** (5 hours)
   - Continuous improvement
   - Lower priority
   - Future enhancement

10. **Master Orchestrator** (3 hours)
    - Runs all validators
    - Final integration
    - Last to implement

---

## 🎯 SPECIFIC INSTRUCTIONS PER VALIDATOR

### VALIDATOR 2: AI ROLE

**File**: `scripts/validate_protocol_role.py`

**Dimensions to Validate**:
1. **Role Definition (25%)** - Check for role title and description
2. **Mission Statement (25%)** - Validate mission clarity
3. **Constraints & Guidelines (20%)** - Count [CRITICAL], [MUST], [GUIDELINE] markers
4. **Output Expectations (15%)** - Check output format specifications
5. **Behavioral Guidance (15%)** - Validate communication style

**Key Sections to Parse**:
- `## AI ROLE AND MISSION` (lines 26-32 typically)

**Pass Criteria**:
```python
# Role Definition
if has_role_title and has_description:
    score = 1.0  # PASS
elif has_role_title:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL

# Mission Statement
if has_mission and has_boundaries and has_success_criteria:
    score = 1.0  # PASS
elif has_mission:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL

# Constraints
critical_count = content.count('[CRITICAL]')
must_count = content.count('[MUST]')
guideline_count = content.count('[GUIDELINE]')

if critical_count >= 1:
    score = 1.0  # PASS
elif must_count >= 3 or guideline_count >= 5:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL
```

---

### VALIDATOR 3: WORKFLOW ALGORITHM

**File**: `scripts/validate_protocol_workflow.py`

**Dimensions to Validate**:
1. **Workflow Structure (20%)** - Check for WORKFLOW section and phases
2. **Step Definitions (25%)** - Validate step numbering and completeness
3. **Action Markers (15%)** - Count and validate markers
4. **Halt Conditions (20%)** - Check for error handling
5. **Evidence Tracking (20%)** - Validate artifact generation

**Key Sections to Parse**:
- `## WORKFLOW` or `## [PROTOCOL NAME] WORKFLOW`
- Look for `### STEP 1:`, `### STEP 2:`, etc.

**Pass Criteria**:
```python
# Workflow Structure
if has_workflow_section and step_count >= 3:
    score = 1.0  # PASS
elif has_workflow_section:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL

# Step Definitions
complete_steps = sum(1 for step in steps if has_action and has_output)
score = complete_steps / total_steps

# Halt Conditions
halt_keywords = ['halt condition', 'stop if', 'failure handling', 'error']
halt_count = sum(1 for kw in halt_keywords if kw.lower() in content.lower())
if halt_count >= 3:
    score = 1.0  # PASS
elif halt_count >= 1:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL
```

---

### VALIDATOR 4: QUALITY GATES

**File**: `scripts/validate_protocol_gates.py`

**Dimensions to Validate**:
1. **Gate Definitions (25%)** - Check for gate sections
2. **Pass Criteria (25%)** - Validate thresholds
3. **Automation (20%)** - Check for scripts and config files
4. **Failure Handling (15%)** - Validate error procedures
5. **Compliance Integration (15%)** - Check compliance references

**Key Sections to Parse**:
- `## QUALITY GATES`
- `config/protocol_gates/{protocol_id}.yaml`

**Pass Criteria**:
```python
# Gate Definitions
gate_pattern = r'### Gate \d+:'
gates = re.findall(gate_pattern, content)
if len(gates) >= 3:
    score = 1.0  # PASS
elif len(gates) >= 1:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL

# Automation
gate_config_file = f"config/protocol_gates/{protocol_id}.yaml"
if os.path.exists(gate_config_file):
    score = 1.0  # PASS
else:
    score = 0.0  # FAIL
```

---

### VALIDATOR 5: SCRIPT INTEGRATION

**File**: `scripts/validate_protocol_scripts.py`

**Dimensions to Validate**:
1. **Script References (20%)** - Check for script mentions
2. **Script Existence (25%)** - Verify files exist
3. **Script Registration (20%)** - Check script-registry.json
4. **Command Syntax (20%)** - Validate command format
5. **Error Handling (15%)** - Check exit codes

**Key Sections to Parse**:
- `## PREREQUISITES` (System State)
- `## AUTOMATION HOOKS`

**Pass Criteria**:
```python
# Script Existence
referenced_scripts = extract_script_paths(content)
existing_scripts = [s for s in referenced_scripts if os.path.exists(s)]
score = len(existing_scripts) / len(referenced_scripts) if referenced_scripts else 0

# Script Registration
with open('scripts/script-registry.json') as f:
    registry = json.load(f)
registered = sum(1 for script in referenced_scripts if script in str(registry))
score = registered / len(referenced_scripts) if referenced_scripts else 0
```

---

### VALIDATOR 6: COMMUNICATION PROTOCOL

**File**: `scripts/validate_protocol_communication.py`

**Dimensions to Validate**:
1. **Status Announcements (25%)** - Check for phase messages
2. **User Interaction (25%)** - Validate prompts
3. **Error Messaging (20%)** - Check error templates
4. **Progress Tracking (15%)** - Validate progress indicators
5. **Evidence Communication (15%)** - Check artifact announcements

**Key Sections to Parse**:
- `## COMMUNICATION PROTOCOLS`

**Pass Criteria**:
```python
# Status Announcements
announcement_patterns = [
    r'\[MASTER RAY™ \| PHASE \d+ START\]',
    r'\[MASTER RAY™ \| PHASE \d+ COMPLETE\]'
]
announcements = sum(len(re.findall(p, content)) for p in announcement_patterns)
if announcements >= 4:
    score = 1.0  # PASS
elif announcements >= 2:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL
```

---

### VALIDATOR 7: EVIDENCE PACKAGE

**File**: `scripts/validate_protocol_evidence.py`

**Dimensions to Validate**:
1. **Artifact Generation (30%)** - Check artifact list
2. **Storage Structure (20%)** - Validate directory structure
3. **Manifest Completeness (20%)** - Check manifest file
4. **Traceability (15%)** - Validate input/output tracking
5. **Archival (15%)** - Check archival procedures

**Key Sections to Parse**:
- `## EVIDENCE SUMMARY`
- `.artifacts/protocol-{id}/`

**Pass Criteria**:
```python
# Artifact Generation
artifact_pattern = r'`\.artifacts/protocol-\d+/[^`]+`'
artifacts = re.findall(artifact_pattern, content)
if len(artifacts) >= 3:
    score = 1.0  # PASS
elif len(artifacts) >= 1:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL
```

---

### VALIDATOR 8: HANDOFF CHECKLIST

**File**: `scripts/validate_protocol_handoff.py`

**Dimensions to Validate**:
1. **Checklist Completeness (30%)** - Count checklist items
2. **Verification Procedures (25%)** - Check verification steps
3. **Stakeholder Sign-off (20%)** - Validate approval process
4. **Documentation Requirements (15%)** - Check doc requirements
5. **Transition Support (10%)** - Validate support procedures

**Key Sections to Parse**:
- `## HANDOFF CHECKLIST`

**Pass Criteria**:
```python
# Checklist Completeness
checkbox_pattern = r'- \[ \]'
checkboxes = len(re.findall(checkbox_pattern, handoff_section))
if checkboxes >= 5:
    score = 1.0  # PASS
elif checkboxes >= 3:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL
```

---

### VALIDATOR 9: COGNITIVE REASONING

**File**: `scripts/validate_protocol_reasoning.py`

**Dimensions to Validate**:
1. **Reasoning Patterns (25%)** - Check for decision logic
2. **Decision Trees (25%)** - Validate decision points
3. **Problem-Solving Logic (20%)** - Check problem resolution
4. **Learning Mechanisms (15%)** - Validate feedback loops
5. **Meta-Cognition (15%)** - Check self-awareness

**Pass Criteria**:
```python
# This is more subjective - look for keywords
reasoning_keywords = ['analyze', 'evaluate', 'determine', 'assess', 'consider']
decision_keywords = ['if', 'choose', 'select', 'decide', 'option']
problem_keywords = ['issue', 'problem', 'error', 'failure', 'fix']

score = calculate_keyword_density(content, all_keywords)
```

---

### VALIDATOR 10: META-REFLECTION

**File**: `scripts/validate_protocol_reflection.py`

**Dimensions to Validate**:
1. **Retrospective Analysis (30%)** - Check for review processes
2. **Continuous Improvement (25%)** - Validate improvement tracking
3. **System Evolution (20%)** - Check version history
4. **Knowledge Capture (15%)** - Validate lessons learned
5. **Future Planning (10%)** - Check roadmap

**Pass Criteria**:
```python
# Look for retrospective sections or improvement mentions
retrospective_keywords = ['retrospective', 'review', 'lessons learned', 'improvement']
found = sum(1 for kw in retrospective_keywords if kw.lower() in content.lower())

if found >= 3:
    score = 1.0  # PASS
elif found >= 1:
    score = 0.85  # WARNING
else:
    score = 0.0  # FAIL
```

---

## 🚀 MASTER ORCHESTRATOR

**File**: `scripts/validate_all_protocols.py`

Ito ang script na magru-run ng lahat ng validators:

```python
#!/usr/bin/env python3
"""
Master Protocol Validator Orchestrator
Runs all 10 validators and generates comprehensive report
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Import all validators
from validate_protocol_identity import ProtocolIdentityValidator
from validate_protocol_role import ProtocolRoleValidator
from validate_protocol_workflow import ProtocolWorkflowValidator
from validate_protocol_gates import ProtocolGatesValidator
from validate_protocol_scripts import ProtocolScriptsValidator
from validate_protocol_communication import ProtocolCommunicationValidator
from validate_protocol_evidence import ProtocolEvidenceValidator
from validate_protocol_handoff import ProtocolHandoffValidator
from validate_protocol_reasoning import ProtocolReasoningValidator
from validate_protocol_reflection import ProtocolReflectionValidator

def validate_protocol_comprehensive(protocol_id: str, workspace_root: Path) -> dict:
    """Run all validators on a single protocol"""
    
    validators = [
        ("protocol_identity", ProtocolIdentityValidator(workspace_root)),
        ("ai_role", ProtocolRoleValidator(workspace_root)),
        ("workflow_algorithm", ProtocolWorkflowValidator(workspace_root)),
        ("quality_gates", ProtocolGatesValidator(workspace_root)),
        ("script_integration", ProtocolScriptsValidator(workspace_root)),
        ("communication_protocol", ProtocolCommunicationValidator(workspace_root)),
        ("evidence_package", ProtocolEvidenceValidator(workspace_root)),
        ("handoff_checklist", ProtocolHandoffValidator(workspace_root)),
        ("cognitive_reasoning", ProtocolReasoningValidator(workspace_root)),
        ("meta_reflection", ProtocolReflectionValidator(workspace_root))
    ]
    
    result = {
        "protocol_id": protocol_id,
        "validation_timestamp": datetime.utcnow().isoformat() + "Z",
        "validators": {},
        "overall_score": 0.0,
        "validation_status": "fail"
    }
    
    # Run each validator
    for name, validator in validators:
        validation_result = validator.validate_protocol(protocol_id)
        result["validators"][name] = {
            "score": validation_result.get("overall_score", 0),
            "status": validation_result.get("validation_status", "fail")
        }
    
    # Calculate overall score
    scores = [v["score"] for v in result["validators"].values()]
    result["overall_score"] = sum(scores) / len(scores) if scores else 0
    
    # Determine status
    if result["overall_score"] >= 0.95:
        result["validation_status"] = "pass"
    elif result["overall_score"] >= 0.80:
        result["validation_status"] = "warning"
    else:
        result["validation_status"] = "fail"
    
    return result

def main():
    # Implementation similar to other validators
    pass

if __name__ == "__main__":
    main()
```

---

## ✅ FINAL CHECKLIST

Bago i-submit ang validator:

### Code Quality
- [ ] Walang syntax errors
- [ ] Lahat ng imports gumagana
- [ ] Walang unused variables
- [ ] Proper indentation (4 spaces)
- [ ] Type hints sa functions

### Functionality
- [ ] Single protocol validation works
- [ ] Batch validation works
- [ ] Summary reports generated
- [ ] Exit codes correct (0=success, 1=fail)
- [ ] Error handling graceful

### Output
- [ ] JSON format valid
- [ ] All required fields present
- [ ] Scores in correct range (0.0-1.0)
- [ ] Status values correct
- [ ] Timestamps in ISO format

### Testing
- [ ] Test script created
- [ ] All tests passing
- [ ] Edge cases handled
- [ ] Error cases tested

### Documentation
- [ ] Script registered in script-registry.json
- [ ] Usage guide created
- [ ] Examples provided
- [ ] Common issues documented

### Integration
- [ ] Works with existing validators
- [ ] Output format consistent
- [ ] File paths correct
- [ ] Dependencies minimal

---

## 📞 SUPPORT

Kung may tanong o issue:

1. Check ang MASTER-VALIDATOR-COMPLETE-SPEC.md
2. Tingnan ang existing validator (validate_protocol_identity.py) as reference
3. Run ang test suite
4. Check ang output JSON for detailed errors

---

## 🎯 SUCCESS CRITERIA

Ang validator ay considered COMPLETE kung:

✅ Lahat ng 5 dimensions validated  
✅ Pass criteria implemented correctly  
✅ Test suite passing (10/10 tests)  
✅ Documentation complete  
✅ Registered in script registry  
✅ Works with master orchestrator  
✅ Output format consistent  
✅ Error handling robust  

---

**KAYA MO YAN!** 💪 | **WALANG IMPOSIBLE** 🚀 | **GALINGAN MO** ⭐
