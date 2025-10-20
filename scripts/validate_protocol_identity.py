#!/usr/bin/env python3
"""
Protocol Identity Validator
Validates protocol identity metadata, prerequisites, integration points, compliance, and documentation quality.
Specification: documentation/validator-01-complete-spec.md
"""

import os
import sys
import json
import yaml
import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Any

class ProtocolIdentityValidator:
    """Validates protocol identity and documentation quality"""
    
    # Required sections for documentation quality check (flexible matching)
    REQUIRED_SECTIONS = [
        ("PREREQUISITES", r"PREREQUISITES"),
        ("AI ROLE AND MISSION", r"AI ROLE AND MISSION"),
        ("WORKFLOW", r"WORKFLOW"),  # Matches any section containing WORKFLOW
        ("INTEGRATION POINTS", r"INTEGRATION POINTS"),
        ("QUALITY GATES", r"QUALITY GATES"),
        ("COMMUNICATION PROTOCOLS", r"COMMUNICATION PROTOCOLS"),
        ("AUTOMATION HOOKS", r"AUTOMATION HOOKS"),
        ("HANDOFF CHECKLIST", r"HANDOFF CHECKLIST"),
        ("EVIDENCE SUMMARY", r"EVIDENCE SUMMARY")
    ]
    
    VALID_PHASES = ["Phase 0", "Phase 1-2", "Phase 3", "Phase 4", "Phase 5", "Phase 6"]
    
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root
        self.protocols_dir = workspace_root / ".cursor" / "ai-driven-workflow"
        self.agents_file = workspace_root / "AGENTS.md"
        self.gates_dir = workspace_root / "config" / "protocol_gates"
        self.output_dir = workspace_root / ".artifacts" / "validation"
        
    def validate_protocol(self, protocol_id: str) -> Dict[str, Any]:
        """Validate a single protocol across all dimensions"""
        
        result = {
            "validator": "protocol_identity",
            "protocol_id": protocol_id,
            "validation_timestamp": datetime.utcnow().isoformat() + "Z",
            "basic_information": {},
            "prerequisites": {},
            "integration_points": {},
            "compliance_standards": {},
            "documentation_quality": {},
            "overall_score": 0.0,
            "validation_status": "fail",
            "issues": [],
            "recommendations": []
        }
        
        # Find protocol file
        protocol_file = self._find_protocol_file(protocol_id)
        if not protocol_file:
            result["issues"].append(f"Protocol file not found for ID {protocol_id}")
            result["validation_status"] = "fail"
            return result
            
        # Read protocol content
        try:
            with open(protocol_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            result["issues"].append(f"Failed to read protocol file: {str(e)}")
            result["validation_status"] = "fail"
            return result
        
        # Run all validation dimensions
        result["basic_information"] = self._validate_basic_information(protocol_id, content)
        result["prerequisites"] = self._validate_prerequisites(content)
        result["integration_points"] = self._validate_integration_points(content)
        result["compliance_standards"] = self._validate_compliance_standards(protocol_id, content)
        result["documentation_quality"] = self._validate_documentation_quality(content)
        
        # Calculate overall score
        scores = [
            result["basic_information"].get("score", 0),
            result["prerequisites"].get("score", 0),
            result["integration_points"].get("score", 0),
            result["compliance_standards"].get("score", 0),
            result["documentation_quality"].get("score", 0)
        ]
        result["overall_score"] = sum(scores) / len(scores)
        
        # Determine overall status
        if result["overall_score"] >= 0.95:
            result["validation_status"] = "pass"
        elif result["overall_score"] >= 0.80:
            result["validation_status"] = "warning"
        else:
            result["validation_status"] = "fail"
            
        # Collect all issues
        for dimension in ["basic_information", "prerequisites", "integration_points", 
                         "compliance_standards", "documentation_quality"]:
            if "issues" in result[dimension]:
                result["issues"].extend(result[dimension]["issues"])
            if "recommendations" in result[dimension]:
                result["recommendations"].extend(result[dimension]["recommendations"])
        
        return result
    
    def _find_protocol_file(self, protocol_id: str) -> Path:
        """Find protocol file by ID"""
        pattern = f"{protocol_id}-*.md"
        matches = list(self.protocols_dir.glob(pattern))
        return matches[0] if matches else None
    
    def _validate_basic_information(self, protocol_id: str, content: str) -> Dict[str, Any]:
        """Validate basic protocol information (Dimension 1)"""
        result = {
            "score": 0.0,
            "status": "fail",
            "issues": [],
            "elements_found": {}
        }
        
        elements_found = 0
        total_elements = 6
        
        # 1. Protocol Number
        if f"PROTOCOL {protocol_id}" in content.upper():
            elements_found += 1
            result["elements_found"]["protocol_number"] = True
        else:
            result["issues"].append("Protocol number not found in header")
            result["elements_found"]["protocol_number"] = False
        
        # 2. Protocol Name
        name_match = re.search(r'PROTOCOL \d+:\s*([^\n(]+)', content, re.IGNORECASE)
        if name_match and name_match.group(1).strip():
            elements_found += 1
            result["elements_found"]["protocol_name"] = name_match.group(1).strip()
        else:
            result["issues"].append("Protocol name not found or empty")
            result["elements_found"]["protocol_name"] = False
        
        # 3. Protocol Version (check for version markers)
        version_patterns = [r'v\d+\.\d+\.\d+', r'version\s*:\s*\d+\.\d+\.\d+']
        version_found = any(re.search(pattern, content, re.IGNORECASE) for pattern in version_patterns)
        if version_found:
            elements_found += 1
            result["elements_found"]["protocol_version"] = True
        else:
            result["issues"].append("Protocol version not found (semantic versioning expected)")
            result["elements_found"]["protocol_version"] = False
        
        # 4. Phase Assignment (check AGENTS.md)
        phase = self._get_phase_from_agents(protocol_id)
        if phase in self.VALID_PHASES:
            elements_found += 1
            result["elements_found"]["phase_assignment"] = phase
        else:
            result["issues"].append(f"Phase assignment not found or invalid in AGENTS.md")
            result["elements_found"]["phase_assignment"] = False
        
        # 5. Purpose Statement
        purpose_match = re.search(r'(?:Purpose|Mission):\s*([^\n]+)', content, re.IGNORECASE)
        if purpose_match and len(purpose_match.group(1).strip()) > 20:
            elements_found += 1
            result["elements_found"]["purpose_statement"] = True
        else:
            result["issues"].append("Purpose statement not found or too short")
            result["elements_found"]["purpose_statement"] = False
        
        # 6. Scope Definition
        if "SCOPE" in content.upper() or "BOUNDARIES" in content.upper():
            elements_found += 1
            result["elements_found"]["scope_definition"] = True
        else:
            result["issues"].append("Scope definition not found")
            result["elements_found"]["scope_definition"] = False
        
        # Calculate score
        result["score"] = elements_found / total_elements
        
        # Determine status
        if elements_found == total_elements:
            result["status"] = "pass"
        elif elements_found >= total_elements - 2:
            result["status"] = "warning"
        else:
            result["status"] = "fail"
        
        return result
    
    def _validate_prerequisites(self, content: str) -> Dict[str, Any]:
        """Validate prerequisites documentation (Dimension 2)"""
        result = {
            "score": 0.0,
            "status": "fail",
            "issues": [],
            "categories_found": {}
        }
        
        # Extract prerequisites section
        prereq_section = self._extract_section(content, "PREREQUISITES")
        if not prereq_section:
            result["issues"].append("PREREQUISITES section not found")
            result["status"] = "fail"
            return result
        
        categories_found = 0
        total_categories = 3
        
        # 1. Required Artifacts
        if "Required Artifacts" in prereq_section or "ARTIFACTS" in prereq_section.upper():
            categories_found += 1
            result["categories_found"]["required_artifacts"] = True
        else:
            result["issues"].append("Required Artifacts category missing")
            result["categories_found"]["required_artifacts"] = False
        
        # 2. Required Approvals
        if re.search(r'Required Approvals|Approvals', prereq_section, re.IGNORECASE):
            categories_found += 1
            result["categories_found"]["required_approvals"] = True
        else:
            result["issues"].append("Required Approvals category missing")
            result["categories_found"]["required_approvals"] = False
        
        # 3. System State
        if re.search(r'System State|Environment|Dependencies', prereq_section, re.IGNORECASE):
            categories_found += 1
            result["categories_found"]["system_state"] = True
        else:
            result["issues"].append("System State category missing")
            result["categories_found"]["system_state"] = False
        
        # Calculate score
        result["score"] = categories_found / total_categories
        
        # Determine status
        if categories_found == total_categories:
            result["status"] = "pass"
        elif categories_found >= total_categories - 1:
            result["status"] = "warning"
        else:
            result["status"] = "fail"
        
        return result
    
    def _validate_integration_points(self, content: str) -> Dict[str, Any]:
        """Validate integration points mapping (Dimension 3)"""
        result = {
            "score": 0.0,
            "status": "fail",
            "issues": [],
            "elements_found": {}
        }
        
        # Extract integration points section
        integration_section = self._extract_section(content, "INTEGRATION POINTS")
        if not integration_section:
            result["issues"].append("INTEGRATION POINTS section not found")
            result["status"] = "fail"
            return result
        
        elements_found = 0
        total_elements = 4
        
        # 1. Input Sources
        if "Inputs From" in integration_section or "INPUT" in integration_section.upper():
            elements_found += 1
            result["elements_found"]["input_sources"] = True
        else:
            result["issues"].append("Input sources not documented")
            result["elements_found"]["input_sources"] = False
        
        # 2. Output Destinations
        if "Outputs To" in integration_section or "OUTPUT" in integration_section.upper():
            elements_found += 1
            result["elements_found"]["output_destinations"] = True
        else:
            result["issues"].append("Output destinations not documented")
            result["elements_found"]["output_destinations"] = False
        
        # 3. Data Formats
        format_patterns = [r'\.md', r'\.json', r'\.yaml', r'\.yml']
        if any(re.search(pattern, integration_section) for pattern in format_patterns):
            elements_found += 1
            result["elements_found"]["data_formats"] = True
        else:
            result["issues"].append("Data formats not specified")
            result["elements_found"]["data_formats"] = False
        
        # 4. Storage Locations
        if ".artifacts" in integration_section or "Storage" in integration_section:
            elements_found += 1
            result["elements_found"]["storage_locations"] = True
        else:
            result["issues"].append("Storage locations not documented")
            result["elements_found"]["storage_locations"] = False
        
        # Calculate score
        result["score"] = elements_found / total_elements
        
        # Determine status
        if elements_found == total_elements:
            result["status"] = "pass"
        elif elements_found >= total_elements - 1:
            result["status"] = "warning"
        else:
            result["status"] = "fail"
        
        return result
    
    def _validate_compliance_standards(self, protocol_id: str, content: str) -> Dict[str, Any]:
        """Validate compliance standards (Dimension 4)"""
        result = {
            "score": 0.0,
            "status": "fail",
            "issues": [],
            "categories_found": {}
        }
        
        # Extract quality gates section
        gates_section = self._extract_section(content, "QUALITY GATES")
        if not gates_section:
            result["issues"].append("QUALITY GATES section not found")
            result["status"] = "fail"
            return result
        
        categories_found = 0
        total_categories = 4
        
        # 1. Industry Standards
        standards = ["CommonMark", "JSON Schema", "YAML", "Markdown"]
        if any(std in content for std in standards):
            categories_found += 1
            result["categories_found"]["industry_standards"] = True
        else:
            result["issues"].append("Industry standards not documented")
            result["categories_found"]["industry_standards"] = False
        
        # 2. Security Requirements
        security_terms = ["HIPAA", "SOC2", "GDPR", "security", "compliance"]
        if any(term in content.upper() for term in [s.upper() for s in security_terms]):
            categories_found += 1
            result["categories_found"]["security_requirements"] = True
        else:
            result["issues"].append("Security requirements not documented")
            result["categories_found"]["security_requirements"] = False
        
        # 3. Regulatory Compliance
        regulatory_terms = ["FDA", "FTC", "regulatory", "compliance"]
        if any(term in content.upper() for term in [r.upper() for r in regulatory_terms]):
            categories_found += 1
            result["categories_found"]["regulatory_compliance"] = True
        else:
            result["issues"].append("Regulatory compliance not documented")
            result["categories_found"]["regulatory_compliance"] = False
        
        # 4. Quality Gates with Automation
        gate_file = self.gates_dir / f"{protocol_id}.yaml"
        if gate_file.exists():
            categories_found += 1
            result["categories_found"]["quality_gates"] = True
        else:
            result["issues"].append(f"Automated quality gates config not found: {gate_file}")
            result["categories_found"]["quality_gates"] = False
        
        # Calculate score
        result["score"] = categories_found / total_categories
        
        # Determine status
        if categories_found == total_categories:
            result["status"] = "pass"
        elif categories_found >= total_categories - 1:
            result["status"] = "warning"
        else:
            result["status"] = "fail"
        
        return result
    
    def _validate_documentation_quality(self, content: str) -> Dict[str, Any]:
        """Validate documentation quality (Dimension 5)"""
        result = {
            "score": 0.0,
            "status": "fail",
            "issues": [],
            "sections_found": {},
            "metrics": {}
        }
        
        sections_found = 0
        total_sections = len(self.REQUIRED_SECTIONS)
        
        for section_name, section_pattern in self.REQUIRED_SECTIONS:
            if self._extract_section(content, section_pattern):
                sections_found += 1
                result["sections_found"][section_name] = True
            else:
                result["issues"].append(f"Required section missing: {section_name}")
                result["sections_found"][section_name] = False
        
        # Calculate completeness
        completeness = sections_found / total_sections
        result["metrics"]["completeness"] = completeness
        
        # Calculate clarity (based on examples and structure)
        clarity_score = self._calculate_clarity(content)
        result["metrics"]["clarity"] = clarity_score
        
        # Calculate accessibility (format consistency)
        accessibility_score = self._calculate_accessibility(content)
        result["metrics"]["accessibility"] = accessibility_score
        
        # Calculate technical accuracy (terminology check)
        accuracy_score = self._calculate_technical_accuracy(content)
        result["metrics"]["technical_accuracy"] = accuracy_score
        
        # Overall quality score
        result["score"] = (completeness * 0.4 + clarity_score * 0.3 + 
                          accessibility_score * 0.15 + accuracy_score * 0.15)
        
        # Determine status
        if completeness >= 0.95 and clarity_score >= 0.90:
            result["status"] = "pass"
        elif completeness >= 0.80:
            result["status"] = "warning"
        else:
            result["status"] = "fail"
        
        return result
    
    def _extract_section(self, content: str, section_name: str) -> str:
        """Extract a section from markdown content"""
        # Match section header with optional numbering (e.g., "## 01. PREREQUISITES" or "## PREREQUISITES")
        pattern = rf'^##\s+(?:\d+\.\s+)?{re.escape(section_name)}.*?\n(.*?)(?=^##\s+|\Z)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE | re.MULTILINE)
        return match.group(1) if match else ""
    
    def _get_phase_from_agents(self, protocol_id: str) -> str:
        """Get phase assignment from AGENTS.md"""
        if not self.agents_file.exists():
            return ""
        
        try:
            with open(self.agents_file, 'r', encoding='utf-8') as f:
                agents_content = f.read()
            
            # Look for protocol in phase tables
            for phase in self.VALID_PHASES:
                phase_section = self._extract_section(agents_content, phase)
                if protocol_id in phase_section or f"**{protocol_id}**" in phase_section:
                    return phase
        except Exception:
            pass
        
        return ""
    
    def _calculate_clarity(self, content: str) -> float:
        """Calculate clarity score based on examples and structure"""
        score = 0.0
        
        # Check for code examples
        if "```" in content:
            score += 0.3
        
        # Check for action markers
        markers = ["[MUST]", "[GUIDELINE]", "[CRITICAL]"]
        if any(marker in content for marker in markers):
            score += 0.3
        
        # Check for structured lists
        if re.search(r'^\s*[-*]\s+', content, re.MULTILINE):
            score += 0.2
        
        # Check for step numbering
        if re.search(r'^\s*\d+\.\s+', content, re.MULTILINE):
            score += 0.2
        
        return min(score, 1.0)
    
    def _calculate_accessibility(self, content: str) -> float:
        """Calculate accessibility score based on format consistency"""
        score = 1.0
        
        # Check for consistent heading levels
        headings = re.findall(r'^(#{1,6})\s+', content, re.MULTILINE)
        if len(headings) < 5:
            score -= 0.2
        
        # Check for proper markdown formatting
        if not re.search(r'^\s*---\s*$', content, re.MULTILINE):
            score -= 0.1
        
        return max(score, 0.0)
    
    def _calculate_technical_accuracy(self, content: str) -> float:
        """Calculate technical accuracy based on terminology"""
        score = 1.0
        
        # Check for proper file path references
        if ".artifacts" in content and "scripts/" in content:
            score = 1.0
        else:
            score -= 0.2
        
        # Check for protocol references
        if re.search(r'Protocol \d+', content):
            score = min(score + 0.1, 1.0)
        
        return max(score, 0.0)
    
    def generate_summary_reports(self, all_results: List[Dict[str, Any]]) -> None:
        """Generate summary reports from all validation results"""
        
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. Identity Summary
        identity_summary = {
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
        
        with open(self.output_dir / "identity-validation-summary.json", 'w') as f:
            json.dump(identity_summary, f, indent=2)
        
        # 2. Compliance Matrix
        compliance_matrix = {
            "validation_timestamp": datetime.utcnow().isoformat() + "Z",
            "protocols": [
                {
                    "protocol_id": r["protocol_id"],
                    "compliance_score": r["compliance_standards"].get("score", 0),
                    "categories": r["compliance_standards"].get("categories_found", {})
                }
                for r in all_results
            ]
        }
        
        with open(self.output_dir / "compliance-matrix.json", 'w') as f:
            json.dump(compliance_matrix, f, indent=2)
        
        # 3. Integration Map
        integration_map = {
            "validation_timestamp": datetime.utcnow().isoformat() + "Z",
            "protocols": [
                {
                    "protocol_id": r["protocol_id"],
                    "integration_score": r["integration_points"].get("score", 0),
                    "elements": r["integration_points"].get("elements_found", {})
                }
                for r in all_results
            ]
        }
        
        with open(self.output_dir / "integration-map.json", 'w') as f:
            json.dump(integration_map, f, indent=2)
        
        # 4. Quality Report
        quality_report = {
            "validation_timestamp": datetime.utcnow().isoformat() + "Z",
            "protocols": [
                {
                    "protocol_id": r["protocol_id"],
                    "quality_score": r["documentation_quality"].get("score", 0),
                    "metrics": r["documentation_quality"].get("metrics", {}),
                    "sections_found": r["documentation_quality"].get("sections_found", {})
                }
                for r in all_results
            ]
        }
        
        with open(self.output_dir / "documentation-quality-report.json", 'w') as f:
            json.dump(quality_report, f, indent=2)

def main():
    parser = argparse.ArgumentParser(
        description="Validate protocol identity and documentation quality"
    )
    parser.add_argument(
        "--protocol",
        help="Validate single protocol by ID (e.g., '01')"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all protocols"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate summary reports"
    )
    parser.add_argument(
        "--workspace",
        default=".",
        help="Workspace root directory"
    )
    
    args = parser.parse_args()
    
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolIdentityValidator(workspace_root)
    
    all_results = []
    
    if args.protocol:
        # Validate single protocol
        result = validator.validate_protocol(args.protocol)
        all_results.append(result)
        
        # Save individual result
        output_file = validator.output_dir / f"protocol-{args.protocol}-identity.json"
        validator.output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        
        print(f"✅ Validation complete for Protocol {args.protocol}")
        print(f"   Status: {result['validation_status'].upper()}")
        print(f"   Score: {result['overall_score']:.3f}")
        print(f"   Output: {output_file}")
        
    elif args.all:
        # Validate all protocols (01-27, excluding 00 and 28+)
        protocol_ids = [f"{i:02d}" for i in range(1, 28)]
        
        for protocol_id in protocol_ids:
            result = validator.validate_protocol(protocol_id)
            all_results.append(result)
            
            # Save individual result
            output_file = validator.output_dir / f"protocol-{protocol_id}-identity.json"
            validator.output_dir.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w') as f:
                json.dump(result, f, indent=2)
            
            status_icon = "✅" if result["validation_status"] == "pass" else "⚠️" if result["validation_status"] == "warning" else "❌"
            print(f"{status_icon} Protocol {protocol_id}: {result['validation_status'].upper()} (score: {result['overall_score']:.3f})")
    
    if args.report or args.all:
        # Generate summary reports
        if all_results:
            validator.generate_summary_reports(all_results)
            print(f"\n📊 Summary reports generated in {validator.output_dir}/")
    
    # Exit with appropriate code
    if all_results:
        fail_count = sum(1 for r in all_results if r["validation_status"] == "fail")
        sys.exit(1 if fail_count > 0 else 0)

if __name__ == "__main__":
    main()
