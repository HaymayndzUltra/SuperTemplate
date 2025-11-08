# GAP FILLING REQUIREMENTS - PROTOCOL CREATION WORKFLOW

This document specifies all missing elements that must be added to make the protocol creation workflow validator-first and zero-ambiguity.

---

## GAP CATEGORY 1: VALIDATOR CODE PARSING

### Gap 1.1: Python Code Analysis Algorithm
**Missing From**: Protocol 1  
**Required For**: Systematic requirement extraction from validator scripts

**Implementation**:

```python
#!/usr/bin/env python3
"""
Validator Requirements Extractor
Parses Python validator scripts to extract structured requirements
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Any

class ValidatorParser:
    """Parse validator Python code to extract requirements"""
    
    def __init__(self, validator_file: Path):
        self.file = validator_file
        self.content = validator_file.read_text()
        self.tree = ast.parse(self.content)
        self.lines = self.content.split('\n')
    
    def extract_all_requirements(self) -> Dict[str, Any]:
        """Extract complete requirements from validator"""
        return {
            "validator_name": self.extract_class_name(),
            "purpose": self.extract_docstring(),
            "dimensions": self.extract_dimensions(),
            "thresholds": self.extract_thresholds(),
            "patterns": self.extract_patterns(),
            "counts": self.extract_count_requirements()
        }
    
    def extract_class_name(self) -> str:
        """Extract validator class name"""
        pattern = r'class\s+(\w+Validator)'
        match = re.search(pattern, self.content)
        return match.group(1) if match else "Unknown"
    
    def extract_docstring(self) -> str:
        """Extract class docstring"""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef) and 'Validator' in node.name:
                return ast.get_docstring(node) or ""
        return ""
    
    def extract_dimensions(self) -> List[Dict[str, Any]]:
        """Extract validation dimensions"""
        dimensions = []
        
        # Find all _validate_* and _evaluate_* methods
        pattern = r'def\s+_(?:validate|evaluate)_(\w+)\(self'
        matches = re.finditer(pattern, self.content)
        
        for match in matches:
            dim_name = match.group(1)
            line_num = self.content[:match.start()].count('\n') + 1
            
            dimension = {
                "name": dim_name,
                "line": line_num,
                "checks": self.extract_checks_from_method(dim_name),
                "weight": self.extract_weight(dim_name)
            }
            dimensions.append(dimension)
        
        return dimensions
    
    def extract_checks_from_method(self, method_name: str) -> List[str]:
        """Extract check names from method's checks dictionary"""
        # Find method in code
        pattern = rf'def\s+_(?:validate|evaluate)_{method_name}\(.*?\):\s*\n(.*?)(?=\n    def\s+|\Z)'
        match = re.search(pattern, self.content, re.DOTALL)
        
        if not match:
            return []
        
        method_body = match.group(1)
        
        # Find checks dictionary
        checks_pattern = r'checks\s*=\s*\{([^}]+)\}'
        checks_match = re.search(checks_pattern, method_body)
        
        if not checks_match:
            return []
        
        checks_dict = checks_match.group(1)
        
        # Extract check names (dictionary keys)
        check_names = re.findall(r'"([^"]+)":', checks_dict)
        return check_names
    
    def extract_weight(self, method_name: str) -> float:
        """Extract dimension weight"""
        pattern = rf'_evaluate_{method_name}.*?weight=([\d.]+)'
        match = re.search(pattern, self.content)
        return float(match.group(1)) if match else 1.0
    
    def extract_thresholds(self) -> Dict[str, float]:
        """Extract pass/warning thresholds"""
        thresholds = {}
        
        # Pass threshold
        pass_pattern = r'pass_threshold=([\d.]+)'
        pass_match = re.search(pass_pattern, self.content)
        if pass_match:
            thresholds["pass"] = float(pass_match.group(1))
        
        # Warning threshold
        warn_pattern = r'warning_threshold=([\d.]+)'
        warn_match = re.search(warn_pattern, self.content)
        if warn_match:
            thresholds["warning"] = float(warn_match.group(1))
        
        # Alternative: direct score comparison
        if not thresholds:
            score_pattern = r'if\s+.*?score.*?>=\s*([\d.]+)'
            score_match = re.search(score_pattern, self.content)
            if score_match:
                thresholds["pass"] = float(score_match.group(1))
        
        return thresholds
    
    def extract_patterns(self) -> List[Dict[str, Any]]:
        """Extract required text patterns (regex)"""
        patterns = []
        
        # Find all regex patterns
        regex_patterns = [
            r're\.search\(r[\'"]([^\'"]+)[\'"]',  # re.search(r'pattern'
            r're\.findall\(r[\'"]([^\'"]+)[\'"]',  # re.findall(r'pattern'
            r're\.match\(r[\'"]([^\'"]+)[\'"]',    # re.match(r'pattern'
        ]
        
        for pattern_type in regex_patterns:
            matches = re.finditer(pattern_type, self.content)
            for match in matches:
                line_num = self.content[:match.start()].count('\n') + 1
                patterns.append({
                    "regex": match.group(1),
                    "line": line_num,
                    "context": self.get_context(line_num)
                })
        
        # Find exact string matches
        string_pattern = r'"([^"]+)"\s+in\s+(content|section)'
        matches = re.finditer(string_pattern, self.content)
        for match in matches:
            line_num = self.content[:match.start()].count('\n') + 1
            patterns.append({
                "exact_string": match.group(1),
                "location": match.group(2),
                "line": line_num,
                "context": self.get_context(line_num)
            })
        
        return patterns
    
    def extract_count_requirements(self) -> List[Dict[str, Any]]:
        """Extract minimum count requirements"""
        counts = []
        
        # Pattern: len(...) >= N
        pattern = r'len\(([^)]+)\)\s*>=?\s*(\d+)'
        matches = re.finditer(pattern, self.content)
        
        for match in matches:
            line_num = self.content[:match.start()].count('\n') + 1
            counts.append({
                "variable": match.group(1),
                "minimum": int(match.group(2)),
                "line": line_num,
                "context": self.get_context(line_num)
            })
        
        return counts
    
    def get_context(self, line_num: int, context_lines: int = 2) -> str:
        """Get context around line number"""
        start = max(0, line_num - context_lines - 1)
        end = min(len(self.lines), line_num + context_lines)
        return '\n'.join(self.lines[start:end])

# Usage
def extract_all_validator_requirements(validator_dir: Path) -> Dict[str, Dict]:
    """Extract requirements from all validators"""
    requirements = {}
    
    for validator_file in validator_dir.glob("validate_protocol_*.py"):
        parser = ValidatorParser(validator_file)
        requirements[parser.extract_class_name()] = parser.extract_all_requirements()
    
    return requirements

# CLI
if __name__ == "__main__":
    import sys
    import json
    
    if len(sys.argv) < 2:
        print("Usage: python extract_validator_requirements.py <validator_file_or_dir>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    
    if path.is_dir():
        requirements = extract_all_validator_requirements(path)
    else:
        parser = ValidatorParser(path)
        requirements = {parser.extract_class_name(): parser.extract_all_requirements()}
    
    # Output as JSON
    print(json.dumps(requirements, indent=2))
```

**Output Format**:
```json
{
  "ProtocolRoleValidator": {
    "validator_name": "ProtocolRoleValidator",
    "purpose": "Validates AI role, mission, and behavioral guidance",
    "dimensions": [
      {
        "name": "role_definition",
        "line": 93,
        "weight": 0.25,
        "checks": ["role_title", "role_description", "domain_expertise", "behavioral_traits"]
      }
    ],
    "thresholds": {
      "pass": 0.90,
      "warning": 0.80
    },
    "patterns": [
      {
        "exact_string": "You are a",
        "location": "section",
        "line": 101
      }
    ],
    "counts": []
  }
}
```

---

## GAP CATEGORY 2: CONTENT PATTERN LIBRARY

### Gap 2.1: Validator-Compliant Content Examples
**Missing From**: Protocol 3  
**Required For**: AI to write content that passes validators

**File**: `content-patterns-library.yaml`

```yaml
# Content Patterns Library - Validator-Compliant Examples
version: "1.0"

patterns:
  
  # Role Validator Patterns
  role_validator:
    
    role_definition:
      pattern_name: "role_title"
      validator_check: "validate_protocol_role.py line 101"
      required: "You are a" or "You are an"
      examples:
        - text: "You are a **Protocol Requirements Analyst**."
          passes: true
          score: 1.0
        - text: "You are an **Integration Specialist**."
          passes: true
          score: 1.0
        - text: "This protocol defines a Requirements Analyst."
          passes: false
          reason: "Missing 'You are a' pattern"
    
    mission_statement:
      pattern_name: "complete_mission"
      validator_check: "validate_protocol_role.py lines 136-139"
      required_elements: 4
      elements:
        - name: "mission_keyword"
          keywords: ["mission"]
          line: 136
        - name: "scope_boundary"
          keywords: ["within", "only", "do not", "boundar", "scope"]
          line: 137
        - name: "success_criteria"
          keywords: ["success", "complete", "validation", "evidence"]
          line: 138
        - name: "value_proposition"
          keywords: ["client", "value", "impact", "benefit", "outcome"]
          line: 139
      
      examples:
        - text: "**Mission**: Extract requirements **within** validator scope, ensuring **complete** specification, delivering **value** to Protocol 2."
          passes: true
          elements_found: ["mission", "within", "complete", "value"]
          score: 1.0
        
        - text: "**Mission**: Analyze validators to generate specifications."
          passes: false
          elements_found: ["mission"]
          reason: "Missing scope, success, and value elements"
  
  # Gates Validator Patterns
  gates_validator:
    
    gate_definition:
      pattern_name: "complete_gate"
      validator_check: "validate_protocol_gates.py lines 100-210"
      required_elements:
        - element: "gate_heading"
          format: "### Gate N: [Name] ([Type])"
          types: ["Prerequisite", "Execution", "Completion"]
        - element: "criteria"
          required: true
        - element: "pass_threshold"
          format: "≥X.XX" or "status = pass"
        - element: "metrics"
          keywords: ["score", "confidence", "rate", "percentage"]
        - element: "evidence_links"
          minimum_mentions: 3 (across all gates)
        - element: "failure_handling"
          required_keywords: ["rollback", "notification", "waiver"]
      
      examples:
        - text: |
            ### Gate 1: Requirements Completeness (Execution)
            - **Criteria**: All 10 validators analyzed
            - **Pass Threshold**: 10/10 = 100%
            - **Metrics**: Completion rate, coverage score
            - **Evidence Links**: `.artifacts/validation/analysis.log` contains evidence
            - **Failure Handling**:
              - Rollback: Not applicable
              - Notification: Alert user
              - Waiver: None
          passes: true
          score: 1.0
          elements_found: ["heading_with_type", "numeric_threshold", "metrics", "evidence", "failure_handling"]

# ... more patterns for all validators
```

**Usage in Protocol 3**:
```python
import yaml

def get_content_pattern(validator, dimension, pattern_name):
    """Get validator-compliant content pattern"""
    with open('content-patterns-library.yaml') as f:
        library = yaml.safe_load(f)
    
    pattern = library['patterns'][validator][dimension]['pattern_name']
    examples = pattern['examples']
    
    # Return passing example
    for ex in examples:
        if ex['passes']:
            return ex['text']
    
    return None

# Use in content generation
role_title_pattern = get_content_pattern('role_validator', 'role_definition', 'role_title')
# Returns: "You are a **[Role]**."
```

---

## GAP CATEGORY 3: PRE-VALIDATION FRAMEWORK

### Gap 3.1: Section-Specific Pre-Validators
**Missing From**: Protocol 3  
**Required For**: Catching validator failures before formal validation

**File**: `prevalidators/prevalidate_ai_role.py`

```python
#!/usr/bin/env python3
"""Pre-validator for AI ROLE AND MISSION section"""

def prevalidate_ai_role(section_content: str) -> List[Dict]:
    """
    Pre-validate AI ROLE section before formal validation.
    Returns list of issues found.
    """
    issues = []
    
    # Load content patterns library
    patterns = load_patterns('role_validator')
    
    # Check 1: Role title pattern
    if not check_pattern(section_content, patterns['role_definition']['role_title']):
        issues.append({
            "check": "role_title",
            "status": "FAIL",
            "validator": "validate_protocol_role.py",
            "line": 101,
            "issue": "Missing 'You are a' pattern",
            "fix_suggestion": "Add: You are a **[Role Title]**.",
            "priority": "CRITICAL"
        })
    
    # Check 2: Character count
    char_count = len(section_content.strip())
    if char_count <= 60:
        issues.append({
            "check": "role_description_length",
            "status": "FAIL",
            "validator": "validate_protocol_role.py",
            "line": 103,
            "issue": f"Role description too short: {char_count} chars (need >60)",
            "fix_suggestion": "Expand description with domain expertise and behavioral traits",
            "priority": "CRITICAL"
        })
    
    # Check 3: Mission elements (all 4 required)
    mission_elements = check_mission_elements(section_content)
    missing_elements = [e for e, present in mission_elements.items() if not present]
    
    if missing_elements:
        issues.append({
            "check": "mission_completeness",
            "status": "FAIL",
            "validator": "validate_protocol_role.py",
            "lines": "136-139",
            "issue": f"Mission missing elements: {missing_elements}",
            "fix_suggestion": f"Add keywords: {get_keywords_for_elements(missing_elements)}",
            "priority": "HIGH"
        })
    
    return issues
```

---

## GAP CATEGORY 4: ISSUE FIX ALGORITHMS

### Gap 4.1: Automated Fix Procedures
**Missing From**: Protocol 4  
**Required For**: Systematic issue resolution

**File**: `fixers/fix_role_issues.py`

```python
def fix_missing_role_title(section_content: str) -> str:
    """Auto-fix missing 'You are a' pattern"""
    
    # Try to extract role name from context
    role_patterns = [
        r'\*\*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\*\*',  # **Role Name**
        r'([A-Z][a-z]+\s+(?:Specialist|Analyst|Engineer|Architect))',  # Common titles
    ]
    
    role_name = None
    for pattern in role_patterns:
        match = re.search(pattern, section_content)
        if match:
            role_name = match.group(1)
            break
    
    if not role_name:
        role_name = "Protocol Specialist"
    
    # Insert at beginning
    role_title = f"You are a **{role_name}**. "
    
    if section_content.strip():
        return role_title + section_content
    else:
        return role_title

def fix_mission_missing_elements(section_content: str, missing_elements: List[str]) -> str:
    """Auto-fix missing mission elements"""
    
    mission_fixes = {
        "scope_boundary": " within the protocol scope",
        "success_criteria": " ensuring complete validation",
        "value_proposition": " delivering value to downstream processes"
    }
    
    # Find mission statement
    mission_pattern = r'(\*\*Mission\*\*:[^\n]+)'
    mission_match = re.search(mission_pattern, section_content)
    
    if mission_match:
        mission_text = mission_match.group(1)
        
        # Append missing elements
        for element in missing_elements:
            if element in mission_fixes:
                mission_text += mission_fixes[element]
        
        # Replace in content
        return section_content.replace(mission_match.group(1), mission_text)
    
    return section_content
```

---

## IMPLEMENTATION PRIORITY

### Phase 1: CRITICAL (Week 1)
1. **Validator Parser** - Enable systematic requirement extraction
2. **Content Pattern Library** - Provide exact examples
3. **Pre-Validation Framework** - Catch issues early

### Phase 2: HIGH (Week 2)
4. **Automated Fix Algorithms** - Systematic issue resolution
5. **Typed Placeholder System** - Clear content expectations
6. **Validator Mapping Comments** - Explicit validator links

### Phase 3: MEDIUM (Week 3-4)
7. **Quantitative Scoring** - Measurable quality
8. **Benchmark System** - Performance tracking
9. **Continuous Improvement Log** - Learn from iterations

**Total Effort**: ~60 hours over 4 weeks  
**Expected Outcome**: First-pass success rate improves from 30% to 85%
