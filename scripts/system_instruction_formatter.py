#!/usr/bin/env python3
"""
System Instruction Formatter Tool (Advanced)
End-to-end protocol to author, validate, conflict-resolve, version, test, and operationalize system instructions
"""

import re
import json
import yaml
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InstructionType(Enum):
    """Instruction type classification"""
    GOVERNANCE = "governance"
    OPERATIONAL = "operational"
    TECHNICAL_POLICY = "technical_policy"
    FORMATTER_PARSER = "formatter_parser"
    FILE_TOOL_SPECIFIC = "file_tool_specific"

class DirectiveTag(Enum):
    """Canonical directive tags"""
    STRICT = "[STRICT]"
    GUIDELINE = "[GUIDELINE]"
    CRITICAL = "[CRITICAL]"
    REQUIRED = "[REQUIRED]"
    OPTIONAL = "[OPTIONAL]"

@dataclass
class InstructionMetadata:
    """Instruction metadata structure"""
    description: str
    always_apply: bool = False
    tags: List[str] = None
    triggers: List[str] = None
    scope: str = ""
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.triggers is None:
            self.triggers = []

@dataclass
class ValidationResult:
    """Validation result structure"""
    is_valid: bool
    errors: List[str] = None
    warnings: List[str] = None
    suggestions: List[str] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []
        if self.warnings is None:
            self.warnings = []
        if self.suggestions is None:
            self.suggestions = []

class SystemInstructionFormatter:
    """System Instruction Formatter Specialist"""
    
    def __init__(self):
        self.canonical_tags = {
            "[MUST]": DirectiveTag.STRICT,
            "[ESSENTIAL]": DirectiveTag.STRICT,
            "[IMPORTANT]": DirectiveTag.GUIDELINE,
            "[SHOULD]": DirectiveTag.GUIDELINE,
            "[MAY]": DirectiveTag.OPTIONAL,
            "[CAN]": DirectiveTag.OPTIONAL
        }
        
        self.precedence_matrix = {
            DirectiveTag.STRICT: 1,
            DirectiveTag.CRITICAL: 2,
            DirectiveTag.REQUIRED: 3,
            DirectiveTag.GUIDELINE: 4,
            DirectiveTag.OPTIONAL: 5
        }
        
        self.minimal_profiles = {
            InstructionType.OPERATIONAL: {
                "include": ["core_principle", "protocol", "minimal_validation"],
                "optional": ["examples"],
                "omit": ["conflict_matrix", "telemetry"]
            },
            InstructionType.TECHNICAL_POLICY: {
                "include": ["persona", "core_principle", "protocol", "lint_quality_gates", "examples"],
                "optional": ["tests"]
            },
            InstructionType.FORMATTER_PARSER: {
                "include": ["grammar", "canonicalization", "failure_modes", "test_harness"],
                "omit": ["persona", "branding"]
            },
            InstructionType.GOVERNANCE: {
                "include": ["persona", "core_principle", "precedence_conflicts", "protocol", "success_criteria"],
                "optional": ["versioning_changelog"]
            }
        }

    def classify_instruction_type(self, content: str) -> InstructionType:
        """Classify instruction type based on content analysis"""
        content_lower = content.lower()
        
        # Governance indicators
        if any(keyword in content_lower for keyword in ["governance", "policy", "compliance", "rules", "standards"]):
            return InstructionType.GOVERNANCE
        
        # Operational indicators
        if any(keyword in content_lower for keyword in ["process", "workflow", "procedure", "steps", "execution"]):
            return InstructionType.OPERATIONAL
        
        # Technical Policy indicators
        if any(keyword in content_lower for keyword in ["technical", "code", "implementation", "architecture", "security"]):
            return InstructionType.TECHNICAL_POLICY
        
        # Formatter/Parser indicators
        if any(keyword in content_lower for keyword in ["format", "parse", "validate", "structure", "grammar"]):
            return InstructionType.FORMATTER_PARSER
        
        # Default to file/tool specific
        return InstructionType.FILE_TOOL_SPECIFIC

    def extract_yaml_frontmatter(self, content: str) -> Tuple[Optional[Dict], str]:
        """Extract YAML frontmatter from content"""
        if not content.startswith('---'):
            return None, content
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None, content
        
        try:
            frontmatter = yaml.safe_load(parts[1])
            remaining_content = parts[2].strip()
            return frontmatter, remaining_content
        except yaml.YAMLError as e:
            logger.warning(f"YAML frontmatter parsing error: {e}")
            return None, content

    def normalize_directives(self, content: str) -> str:
        """Normalize directive tags to canonical set"""
        normalized_content = content
        
        for alias, canonical in self.canonical_tags.items():
            # Replace alias with canonical tag
            normalized_content = re.sub(
                rf'\b{re.escape(alias)}\b',
                canonical.value,
                normalized_content,
                flags=re.IGNORECASE
            )
        
        return normalized_content

    def detect_conflicts(self, content: str) -> List[str]:
        """Detect directive conflicts in content"""
        conflicts = []
        
        # Find all directive tags
        directive_pattern = r'\[(STRICT|GUIDELINE|CRITICAL|REQUIRED|OPTIONAL)\]'
        directives = re.findall(directive_pattern, content, re.IGNORECASE)
        
        # Check for conflicting directives in same section
        sections = content.split('\n###')
        for i, section in enumerate(sections):
            section_directives = re.findall(directive_pattern, section, re.IGNORECASE)
            if len(section_directives) > 1:
                conflicts.append(f"Section {i+1} contains multiple directives: {section_directives}")
        
        return conflicts

    def validate_structure(self, content: str, instruction_type: InstructionType) -> ValidationResult:
        """Validate instruction structure"""
        result = ValidationResult(is_valid=True)
        
        # Check for required sections based on instruction type
        required_sections = self.minimal_profiles.get(instruction_type, {}).get("include", [])
        
        # Map section names to patterns
        section_patterns = {
            "persona": r'## AI Persona|### AI Role',
            "core_principle": r'## Core Principle|### Core Principle',
            "protocol": r'## Protocol|### Protocol',
            "minimal_validation": r'## Validation|### Validation',
            "lint_quality_gates": r'## Quality Gates|### Quality Gates',
            "examples": r'## Examples|### Examples',
            "precedence_conflicts": r'## Precedence|### Precedence',
            "success_criteria": r'## Success Criteria|### Success Criteria'
        }
        
        for section in required_sections:
            pattern = section_patterns.get(section)
            if pattern and not re.search(pattern, content, re.IGNORECASE):
                result.is_valid = False
                result.errors.append(f"Missing required section: {section}")
        
        # Check for YAML frontmatter structure
        frontmatter, _ = self.extract_yaml_frontmatter(content)
        if frontmatter:
            if "description" not in frontmatter:
                result.is_valid = False
                result.errors.append("YAML frontmatter missing 'description' field")
            
            # Check for invalid fields in frontmatter
            invalid_fields = ["branding", "telemetry", "metrics"]
            for field in invalid_fields:
                if field in frontmatter:
                    result.warnings.append(f"Field '{field}' should not be in YAML frontmatter")
        
        # Check for bare URLs
        url_pattern = r'https?://[^\s\)]+(?!\))'
        if re.search(url_pattern, content):
            result.warnings.append("Bare URLs found - use markdown links or backticks")
        
        # Check for mixed code block formats
        if '```' in content and '`' in content:
            result.warnings.append("Mixed code block formats detected")
        
        return result

    def apply_minimal_profile(self, content: str, instruction_type: InstructionType) -> str:
        """Apply minimal profile based on instruction type"""
        profile = self.minimal_profiles.get(instruction_type, {})
        
        # This is a simplified implementation
        # In a full implementation, you would parse the content and restructure it
        # according to the profile requirements
        
        return content

    def format_instruction(self, content: str, purpose: str = "", scope: str = "", constraints: List[str] = None) -> Tuple[str, ValidationResult]:
        """Format instruction using canonical structure"""
        if constraints is None:
            constraints = []
        
        # Step 1: Input Analysis
        instruction_type = self.classify_instruction_type(content)
        logger.info(f"Classified instruction type: {instruction_type.value}")
        
        # Step 2: Extract and validate YAML frontmatter
        frontmatter, content_body = self.extract_yaml_frontmatter(content)
        
        # Step 3: Normalize directives
        normalized_content = self.normalize_directives(content_body)
        
        # Step 4: Detect conflicts
        conflicts = self.detect_conflicts(normalized_content)
        
        # Step 5: Validate structure
        validation_result = self.validate_structure(normalized_content, instruction_type)
        
        # Add conflicts to validation result
        if conflicts:
            validation_result.errors.extend(conflicts)
            validation_result.is_valid = False
        
        # Step 6: Apply minimal profile
        formatted_content = self.apply_minimal_profile(normalized_content, instruction_type)
        
        # Step 7: Reconstruct with frontmatter
        if frontmatter:
            formatted_content = f"---\n{yaml.dump(frontmatter, default_flow_style=False)}---\n\n{formatted_content}"
        
        # Step 8: Add applicability report
        applicability_report = self.generate_applicability_report(instruction_type, formatted_content)
        
        return formatted_content, validation_result

    def generate_applicability_report(self, instruction_type: InstructionType, content: str) -> str:
        """Generate applicability report"""
        profile = self.minimal_profiles.get(instruction_type, {})
        
        report = f"## Applicability Report\n\n"
        report += f"**Instruction Type**: {instruction_type.value}\n\n"
        report += f"**Profile Applied**: {instruction_type.value}\n\n"
        
        # Check which sections are included
        section_patterns = {
            "persona": r'## AI Persona|### AI Role',
            "core_principle": r'## Core Principle|### Core Principle',
            "protocol": r'## Protocol|### Protocol',
            "validation": r'## Validation|### Validation',
            "examples": r'## Examples|### Examples'
        }
        
        report += "| Section | Included? | Reason |\n"
        report += "|---------|-----------|--------|\n"
        
        for section, pattern in section_patterns.items():
            included = bool(re.search(pattern, content, re.IGNORECASE))
            reason = "Required" if section in profile.get("include", []) else "Optional"
            report += f"| {section} | {'✅' if included else '❌'} | {reason} |\n"
        
        return report

    def validate_instruction(self, content: str) -> ValidationResult:
        """Validate instruction without formatting"""
        instruction_type = self.classify_instruction_type(content)
        return self.validate_structure(content, instruction_type)

    def resolve_conflicts(self, content: str, conflict_resolution: str = "user_guidance") -> str:
        """Resolve directive conflicts"""
        conflicts = self.detect_conflicts(content)
        
        if not conflicts:
            return content
        
        if conflict_resolution == "user_guidance":
            # Add conflict markers for user resolution
            for conflict in conflicts:
                content += f"\n\n[RULE CONFLICT] {conflict}. Request guidance."
        
        return content

    def generate_test_harness(self, instruction_type: InstructionType) -> str:
        """Generate test harness for instruction type"""
        if instruction_type != InstructionType.FORMATTER_PARSER:
            return ""
        
        harness = """
## Test Harness

### ✅ Valid Input Example
```markdown
### **[STRICT]** Security Report Generation
- Generate failed login report (userId, timestamp, ip)
- Notify admins on completion
```

### ❌ Invalid Input Example
```markdown
### [maybe] Do security
- Do something fast
```

### Expected Output
- Valid input should pass all validation gates
- Invalid input should fail with specific error messages
"""
        return harness

    def format_phase_protocol(self, phase_content: str, phase_number: int) -> Tuple[str, ValidationResult]:
        """Format phase protocol using System Instruction Formatter"""
        # Determine instruction type based on phase
        phase_types = {
            0: InstructionType.GOVERNANCE,  # Bootstrap
            1: InstructionType.OPERATIONAL,  # PRD Creation
            2: InstructionType.TECHNICAL_POLICY,  # Task Generation
            3: InstructionType.OPERATIONAL,  # Implementation
            4: InstructionType.TECHNICAL_POLICY,  # Quality Audit
            5: InstructionType.GOVERNANCE,  # Retrospective
            6: InstructionType.OPERATIONAL  # Operations
        }
        
        instruction_type = phase_types.get(phase_number, InstructionType.OPERATIONAL)
        
        # Format the instruction
        formatted_content, validation_result = self.format_instruction(
            phase_content,
            purpose=f"Phase {phase_number} protocol",
            scope="unified_developer_workflow"
        )
        
        # Add phase-specific enhancements
        if phase_number == 0:  # Bootstrap
            formatted_content = self.add_bootstrap_enhancements(formatted_content)
        elif phase_number == 4:  # Quality Audit
            formatted_content = self.add_quality_audit_enhancements(formatted_content)
        
        return formatted_content, validation_result

    def add_bootstrap_enhancements(self, content: str) -> str:
        """Add bootstrap-specific enhancements"""
        enhancement = """
## **[STRICT]** Rule Formatting Protocol
- Apply System Instruction Formatter to all discovered rules
- Validate YAML frontmatter structure
- Normalize directive tags to canonical set
- Resolve conflicts using precedence matrix

## **[STRICT]** Directive Grammar Enforcement
- Use canonical tags: `[STRICT]`, `[GUIDELINE]`, `[CRITICAL]`, `[REQUIRED]`, `[OPTIONAL]`
- Map deprecated aliases to canonical set
- Ensure headings carry directive context

## **[STRICT]** Conflict Resolution Protocol
- Detect conflict → halt execution
- Emit: `[RULE CONFLICT] "{X}" conflicts with "{Y}". Quote: "{Y_excerpt}". Request guidance.`
- If auto-resolvable by matrix, apply and log decision
"""
        return content + enhancement

    def add_quality_audit_enhancements(self, content: str) -> str:
        """Add quality audit-specific enhancements"""
        enhancement = """
## **[STRICT]** Quality Gate Formatting
- Format all quality gate instructions using canonical structure
- Apply structural validation to all quality protocols
- Implement enforcement rubric for quality gates
- Use security protocols for security-sensitive gates

## **[STRICT]** Validation Gates
- Gate A (Determinism): All directives must be tagged `[STRICT]` or `[GUIDELINE]`
- Gate B (Measurability): At least one measurable acceptance criterion
- Gate C (Safety): Security controls + audit/logging required
- Gate D (Sanity): No brand/telemetry in YAML frontmatter
- Gate E (Length): Keep under 500 lines or emit `[PERF_WARN]`
"""
        return content + enhancement

def main():
    """Main entry point for CLI usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description="System Instruction Formatter Tool")
    parser.add_argument("input_file", help="Input file to format")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    parser.add_argument("--validate-only", action="store_true", help="Only validate, don't format")
    parser.add_argument("--instruction-type", choices=[t.value for t in InstructionType], help="Force instruction type")
    
    args = parser.parse_args()
    
    # Read input file
    with open(args.input_file, 'r') as f:
        content = f.read()
    
    # Initialize formatter
    formatter = SystemInstructionFormatter()
    
    if args.validate_only:
        # Only validate
        result = formatter.validate_instruction(content)
        print(f"Validation Result: {'PASSED' if result.is_valid else 'FAILED'}")
        if result.errors:
            print("Errors:")
            for error in result.errors:
                print(f"  - {error}")
        if result.warnings:
            print("Warnings:")
            for warning in result.warnings:
                print(f"  - {warning}")
    else:
        # Format instruction
        formatted_content, validation_result = formatter.format_instruction(content)
        
        # Output result
        if args.output:
            with open(args.output, 'w') as f:
                f.write(formatted_content)
            print(f"Formatted instruction written to {args.output}")
        else:
            print(formatted_content)
        
        # Print validation summary
        print(f"\n[FORMATTER_OK] Formatting completed")
        print(f"Validation: {'PASSED' if validation_result.is_valid else 'FAILED'}")
        if validation_result.errors:
            print("Errors:")
            for error in validation_result.errors:
                print(f"  - {error}")

if __name__ == "__main__":
    main()
