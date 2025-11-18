#!/usr/bin/env python3
"""
Script: protocol-01-synthesize-requirements.py
Protocol: 01 - Validator Requirements Analysis
Purpose: Synthesize extracted requirements into specification documents
"""

import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Tuple

class RequirementsSynthesizer:
    """Synthesizes extracted requirements into specification documents."""
    
    # The 9 required sections for all protocols
    REQUIRED_SECTIONS = [
        "PREREQUISITES",
        "AI ROLE AND MISSION",
        "WORKFLOW",
        "INTEGRATION POINTS",
        "QUALITY GATES",
        "COMMUNICATION PROTOCOLS",
        "AUTOMATION HOOKS",
        "HANDOFF CHECKLIST",
        "EVIDENCE SUMMARY"
    ]
    
    # Validator weights and thresholds
    VALIDATOR_CONFIG = {
        "identity": {"weight": 0.20, "pass": 0.95, "warning": 0.80},
        "role": {"weight": 0.30, "pass": 0.90, "warning": 0.80},
        "workflow": {"weight": 0.40, "pass": 0.90, "warning": 0.75},
        "gates": {"weight": 0.30, "pass": 0.90, "warning": 0.80},
        "scripts": {"weight": 0.25, "pass": 0.85, "warning": 0.75},
        "communication": {"weight": 0.20, "pass": 0.85, "warning": 0.75},
        "evidence": {"weight": 0.25, "pass": 0.90, "warning": 0.80},
        "handoff": {"weight": 0.30, "pass": 0.90, "warning": 0.80},
        "reasoning": {"weight": 0.20, "pass": 0.85, "warning": 0.75},
        "reflection": {"weight": 0.15, "pass": 0.80, "warning": 0.70}
    }
    
    # Section-to-validator mappings
    SECTION_VALIDATORS = {
        "PREREQUISITES": ["identity", "handoff"],
        "AI ROLE AND MISSION": ["role"],
        "WORKFLOW": ["workflow", "reasoning"],
        "INTEGRATION POINTS": ["identity"],
        "QUALITY GATES": ["gates"],
        "COMMUNICATION PROTOCOLS": ["communication"],
        "AUTOMATION HOOKS": ["scripts"],
        "HANDOFF CHECKLIST": ["handoff"],
        "EVIDENCE SUMMARY": ["evidence", "reflection"]
    }
    
    def __init__(self, raw_data: Dict[str, Any]):
        self.raw_data = raw_data
        self.validators = raw_data.get('validators', {})
        self.timestamp = datetime.now().isoformat()
    
    def generate_markdown_spec(self) -> str:
        """Generate human-readable markdown specification."""
        md = []
        md.append("# PROTOCOL REQUIREMENTS SPECIFICATION")
        md.append("")
        md.append(f"**Generated**: {self.timestamp}")
        md.append(f"**Validators Analyzed**: {len(self.validators)}/10")
        md.append(f"**Workspace**: /home/haymayndz/SuperTemplate")
        md.append("")
        
        # Section 1: Required Sections
        md.append("## 1. REQUIRED SECTIONS (9 Total)")
        md.append("")
        for i, section in enumerate(self.REQUIRED_SECTIONS, 1):
            md.append(f"{i}. {section}")
        md.append("")
        
        # Section 2: Validation Criteria Summary
        md.append("## 2. VALIDATION CRITERIA SUMMARY")
        md.append("")
        md.append("| Validator | Pass Threshold | Warning Threshold | Weight |")
        md.append("|-----------|----------------|-------------------|--------|")
        for name, config in sorted(self.VALIDATOR_CONFIG.items()):
            md.append(f"| {name} | {config['pass']} | {config['warning']} | {config['weight']} |")
        md.append("")
        
        # Section 3: Section Requirements by Validator
        md.append("## 3. SECTION REQUIREMENTS BY VALIDATOR")
        md.append("")
        for section in self.REQUIRED_SECTIONS:
            validators = self.SECTION_VALIDATORS.get(section, [])
            md.append(f"### {section}")
            md.append(f"**Source Validators**: {', '.join(validators)}")
            md.append("")
            
            # Add validator-specific requirements
            for validator_name in validators:
                if validator_name in self.validators:
                    validator = self.validators[validator_name]
                    md.append(f"**{validator_name.upper()} Requirements**:")
                    md.append(f"- Purpose: {validator.get('purpose', 'N/A')}")
                    
                    # Count requirements
                    counts = validator.get('count_requirements', {})
                    if counts:
                        md.append(f"- Count Requirements: {len(counts)} items")
                        for key, value in sorted(counts.items()):
                            md.append(f"  - {key}: ≥{value}")
                    
                    # Patterns
                    patterns = validator.get('patterns', {})
                    if patterns:
                        md.append(f"- Patterns: {len(patterns)} patterns")
                    
                    md.append("")
        
        # Section 4: Content Patterns
        md.append("## 4. CONTENT PATTERNS")
        md.append("")
        md.append("### Required Keywords per Section")
        for section in self.REQUIRED_SECTIONS:
            md.append(f"- **{section}**: [Keywords from validators]")
        md.append("")
        
        # Section 5: Minimum Counts
        md.append("## 5. MINIMUM COUNTS PER ELEMENT")
        md.append("")
        all_counts = {}
        for validator in self.validators.values():
            counts = validator.get('count_requirements', {})
            for key, value in counts.items():
                if key not in all_counts or all_counts[key] < value:
                    all_counts[key] = value
        
        for key, value in sorted(all_counts.items()):
            md.append(f"- {key}: ≥{value}")
        md.append("")
        
        # Section 6: Quality Gates
        md.append("## 6. QUALITY GATES")
        md.append("")
        md.append("### Gate 1: Validator Coverage")
        md.append("- **Criteria**: All 10 validators analyzed and requirements extracted")
        md.append("- **Pass Threshold**: 10/10 validators covered (100%)")
        md.append("- **Evidence**: `.artifacts/protocol-creation/validator-requirements-raw.json`")
        md.append("")
        
        md.append("### Gate 2: Requirements Completeness")
        md.append("- **Criteria**: All 9 required sections have requirements documented")
        md.append("- **Pass Threshold**: 9/9 sections documented (100%)")
        md.append("- **Evidence**: `.artifacts/protocol-creation/protocol-requirements-spec.md`")
        md.append("")
        
        md.append("### Gate 3: Pattern Specificity")
        md.append("- **Criteria**: All patterns include regex or exact string (no placeholders)")
        md.append("- **Pass Threshold**: 100% patterns have specific format")
        md.append("- **Evidence**: Content patterns section in requirements spec")
        md.append("")
        
        md.append("### Gate 4: Artifact Validation")
        md.append("- **Criteria**: Both markdown and YAML artifacts pass validation")
        md.append("- **Pass Threshold**: 0 validation errors for both artifacts")
        md.append("- **Evidence**: `.artifacts/protocol-creation/checksums.sha256`")
        md.append("")
        
        # Section 7: Summary
        md.append("## 7. EXTRACTION SUMMARY")
        md.append("")
        md.append(f"- **Total Validators**: {len(self.validators)}/10")
        md.append(f"- **Total Patterns**: {self.raw_data.get('total_patterns', 0)}")
        md.append(f"- **Total Count Requirements**: {self.raw_data.get('total_counts', 0)}")
        md.append(f"- **Errors**: {len(self.raw_data.get('errors', []))}")
        md.append(f"- **Warnings**: {len(self.raw_data.get('warnings', []))}")
        md.append("")
        
        if self.raw_data.get('errors'):
            md.append("### Errors")
            for error in self.raw_data['errors']:
                md.append(f"- {error}")
            md.append("")
        
        md.append("## 8. NEXT STEPS")
        md.append("")
        md.append("This specification is ready for Protocol 2: Generate Protocol Structure")
        md.append("- **Input**: `.artifacts/protocol-creation/protocol-requirements-spec.yaml`")
        md.append("- **Output**: Protocol structure template")
        md.append("")
        
        return "\n".join(md)
    
    def generate_yaml_spec(self) -> Dict[str, Any]:
        """Generate machine-readable YAML specification."""
        spec = {
            "version": "1.0",
            "generated_date": self.timestamp,
            "workspace": "/home/haymayndz/SuperTemplate",
            "validator_count": len(self.validators),
            "section_count": len(self.REQUIRED_SECTIONS),
            
            "required_sections": self.REQUIRED_SECTIONS,
            
            "validators": {},
            
            "section_validators": self.SECTION_VALIDATORS,
            
            "validation_criteria": self.VALIDATOR_CONFIG,
            
            "extraction_summary": {
                "total_validators": len(self.validators),
                "total_patterns": self.raw_data.get('total_patterns', 0),
                "total_count_requirements": self.raw_data.get('total_counts', 0),
                "errors": len(self.raw_data.get('errors', [])),
                "warnings": len(self.raw_data.get('warnings', []))
            }
        }
        
        # Add validator details
        for name, validator in self.validators.items():
            spec["validators"][name] = {
                "file": validator.get('file'),
                "purpose": validator.get('purpose'),
                "thresholds": validator.get('thresholds'),
                "patterns_count": len(validator.get('patterns', {})),
                "count_requirements": validator.get('count_requirements', {}),
                "total_lines": validator.get('total_lines')
            }
        
        return spec
    
    def run(self) -> Tuple[str, Dict[str, Any]]:
        """Generate both specifications."""
        print("[SYNTHESIS START] Generating requirements specifications...")
        
        md_spec = self.generate_markdown_spec()
        yaml_spec = self.generate_yaml_spec()
        
        print("[SYNTHESIS COMPLETE] Specifications generated")
        
        return md_spec, yaml_spec

def main():
    """Main entry point."""
    input_file = ".artifacts/protocol-creation/validator-requirements-raw.json"
    
    if not Path(input_file).exists():
        print(f"[ERROR] Input file not found: {input_file}")
        return 1
    
    # Load raw data
    with open(input_file, 'r') as f:
        raw_data = json.load(f)
    
    # Synthesize
    synthesizer = RequirementsSynthesizer(raw_data)
    md_spec, yaml_spec = synthesizer.run()
    
    # Save markdown
    md_file = ".artifacts/protocol-creation/protocol-requirements-spec.md"
    Path(md_file).parent.mkdir(parents=True, exist_ok=True)
    with open(md_file, 'w') as f:
        f.write(md_spec)
    print(f"[✓] Markdown spec saved: {md_file} ({len(md_spec)} bytes)")
    
    # Save YAML
    yaml_file = ".artifacts/protocol-creation/protocol-requirements-spec.yaml"
    with open(yaml_file, 'w') as f:
        yaml.dump(yaml_spec, f, default_flow_style=False, sort_keys=False)
    print(f"[✓] YAML spec saved: {yaml_file}")
    
    # Generate checksums
    import hashlib
    checksums = []
    for filepath in [md_file, yaml_file]:
        with open(filepath, 'rb') as f:
            checksum = hashlib.sha256(f.read()).hexdigest()
            checksums.append(f"{checksum}  {filepath}")
    
    checksum_file = ".artifacts/protocol-creation/checksums.sha256"
    with open(checksum_file, 'w') as f:
        f.write("\n".join(checksums) + "\n")
    print(f"[✓] Checksums generated: {checksum_file}")
    
    print("\n[PROTOCOL 1 | SYNTHESIS COMPLETE]")
    print(f"  - Markdown spec: {len(md_spec)} bytes")
    print(f"  - YAML spec: {len(yaml.dump(yaml_spec))} bytes")
    print(f"  - Validators: {yaml_spec['validator_count']}/10")
    print(f"  - Sections: {yaml_spec['section_count']}/9")
    
    return 0

if __name__ == "__main__":
    exit(main())
