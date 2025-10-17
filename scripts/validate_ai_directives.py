#!/usr/bin/env python3
"""
AI Directive Consistency Validation Script

Ensures AI behavior directives are consistent and non-conflicting:
- Directive tag consistency
- AI persona alignment
- Gate criteria consistency
- Communication pattern validation
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any


class AIDirectiveValidator:
    """Validates AI directive consistency across protocols."""
    
    def __init__(self, workspace_root: str = "."):
        self.workspace_root = Path(workspace_root)
        self.ai_driven_workflow_dir = self.workspace_root / ".cursor" / "ai-driven-workflow"
        self.orchestrator_instruction = self.ai_driven_workflow_dir / "ORCHESTRATOR-SYSTEM-INSTRUCTION.md"

        # Protocol files
        self.protocols = {
            "00": "00-client-discovery.md",
            "0": "0-bootstrap-your-project.md",
            "1": "1-create-prd.md",
            "2": "2-generate-tasks.md",
            "3": "3-process-tasks.md",
            "4": "4-quality-audit.md",
            "5": "5-implementation-retrospective.md"
        }
        
        # Standard directive tags
        self.directive_tags = {
            "MUST": r'\[MUST\]',
            "GUIDELINE": r'\[GUIDELINE\]',
            "STRICT": r'\[STRICT\]',
            "CRITICAL": r'\[CRITICAL\]',
            "REQUIRED": r'\[REQUIRED\]',
            "OPTIONAL": r'\[OPTIONAL\]'
        }
        
        # Standard communication prefixes
        self.communication_prefixes = [
            r'\[AUTOMATION\]',
            r'\[GATE PASSED\]',
            r'\[GATE FAILED\]',
            r'\[CONTEXT LOADED\]',
            r'\[NEXT TASK\]',
            r'\[TASK COMPLETE\]',
            r'\[QUALITY GATE\]',
            r'\[QUALITY REPORT\]',
            r'\[EVIDENCE CAPTURED\]',
            r'\[INTEGRATION CHECK\]',
            r'\[AUTOMATION RUNNING\]',
            r'\[TEMPLATE DISCOVERY\]',
            r'\[GENERATOR INVOKED\]',
            r'\[EVIDENCE COLLECTED\]',
            r'\[CI/CD ALIGNED\]',
            r'\[CHECKPOINT PASSED\]'
        ]
    
    def validate_ai_directives(self) -> Dict[str, Any]:
        """Run comprehensive AI directive validation across all protocols."""
        results = {
            "status": "pass",
            "summary": {
                "total_protocols": len(self.protocols),
                "validated": 0,
                "issues_found": 0,
                "critical_issues": 0
            },
            "directive_usage": {},
            "persona_analysis": {},
            "communication_patterns": {},
            "gate_criteria": {},
            "issues": [],
            "recommendations": []
        }
        
        # Collect directive usage across all protocols
        all_directives = {tag: [] for tag in self.directive_tags.keys()}
        all_communications = []
        all_personas = []
        all_gates = []
        
        for protocol_id, protocol_file in self.protocols.items():
            protocol_path = self.ai_driven_workflow_dir / protocol_file
            
            if not protocol_path.exists():
                results["issues"].append({
                    "severity": "critical",
                    "protocol": f"protocol_{protocol_id}",
                    "message": f"Protocol file not found: {protocol_file}",
                    "fix": f"Create {protocol_path}"
                })
                results["summary"]["critical_issues"] += 1
                continue
            
            try:
                content = protocol_path.read_text(encoding='utf-8')
                protocol_results = self._validate_single_protocol(protocol_id, content)
                results["summary"]["validated"] += 1
                
                # Aggregate directive usage
                for tag, occurrences in protocol_results["directive_usage"].items():
                    all_directives[tag].extend(occurrences)
                
                # Aggregate other data
                all_communications.extend(protocol_results["communication_patterns"])
                all_personas.extend(protocol_results["persona_analysis"])
                all_gates.extend(protocol_results["gate_criteria"])
                
                if protocol_results["issues"]:
                    results["issues"].extend(protocol_results["issues"])
                    results["summary"]["issues_found"] += len(protocol_results["issues"])
                    results["summary"]["critical_issues"] += sum(1 for issue in protocol_results["issues"] if issue["severity"] == "critical")
                
            except Exception as e:
                results["issues"].append({
                    "severity": "critical",
                    "protocol": f"protocol_{protocol_id}",
                    "message": f"Cannot read protocol file: {str(e)}",
                    "fix": "Check file permissions and encoding"
                })
                results["summary"]["critical_issues"] += 1
        
        # Analyze cross-protocol consistency
        results["directive_usage"] = self._analyze_directive_consistency(all_directives)
        results["persona_analysis"] = self._analyze_persona_consistency(all_personas)
        results["communication_patterns"] = self._analyze_communication_consistency(all_communications)
        results["gate_criteria"] = self._analyze_gate_consistency(all_gates)

        orchestrator_issues = self._validate_orchestrator_instruction()
        if orchestrator_issues:
            results["issues"].extend(orchestrator_issues)
            results["summary"]["issues_found"] += len(orchestrator_issues)
            results["summary"]["critical_issues"] += sum(1 for issue in orchestrator_issues if issue["severity"] == "critical")

        # Calculate overall status
        if results["summary"]["critical_issues"] > 0:
            results["status"] = "fail"
        elif results["summary"]["issues_found"] > 0:
            results["status"] = "warning"
        
        return results
    
    def _validate_single_protocol(self, protocol_id: str, content: str) -> Dict[str, Any]:
        """Validate AI directives in a single protocol."""
        results = {
            "protocol_id": protocol_id,
            "directive_usage": {},
            "persona_analysis": [],
            "communication_patterns": [],
            "gate_criteria": [],
            "issues": [],
            "recommendations": []
        }

        # Extract directive usage
        for tag, pattern in self.directive_tags.items():
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            results["directive_usage"][tag] = [
                {
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                }
                for match in matches
            ]
        
        # Extract AI persona information
        results["persona_analysis"] = self._extract_persona_info(content)
        
        # Extract communication patterns
        results["communication_patterns"] = self._extract_communication_patterns(content)
        
        # Extract gate criteria
        results["gate_criteria"] = self._extract_gate_criteria(content)
        
        # Validate directive consistency within protocol
        self._validate_directive_consistency(results, content)
        
        # Validate persona consistency
        self._validate_persona_consistency(results, content)
        
        # Validate communication patterns
        self._validate_communication_consistency(results, content)
        
        return results

    def _validate_orchestrator_instruction(self) -> List[Dict[str, str]]:
        issues: List[Dict[str, str]] = []
        required_sections = [
            "## Brief Analysis Protocol",
            "## Protocol Selection Matrix",
            "## Script Binding Logic",
            "## Validation Gates",
            "## Command Generation",
        ]

        if not self.orchestrator_instruction.exists():
            issues.append({
                "severity": "critical",
                "protocol": "orchestrator_system_instruction",
                "message": "ORCHESTRATOR-SYSTEM-INSTRUCTION.md is missing",
                "fix": "Create the orchestrator system instruction with required sections.",
            })
            return issues

        content = self.orchestrator_instruction.read_text(encoding="utf-8")
        for section in required_sections:
            if section not in content:
                issues.append({
                    "severity": "critical",
                    "protocol": "orchestrator_system_instruction",
                    "message": f"Missing section '{section}' in ORCHESTRATOR-SYSTEM-INSTRUCTION.md",
                    "fix": "Add the required section to the orchestrator system instruction.",
                })

        if "script-registry.json" not in content:
            issues.append({
                "severity": "warning",
                "protocol": "orchestrator_system_instruction",
                "message": "Orchestrator instruction does not mention script registry integration",
                "fix": "Reference scripts/script-registry.json in the orchestrator instructions.",
            })

        return issues
    
    def _extract_context(self, content: str, start: int, end: int, context_lines: int = 2) -> str:
        """Extract context around a match."""
        lines = content.split('\n')
        match_line = content[:start].count('\n')
        
        start_line = max(0, match_line - context_lines)
        end_line = min(len(lines), match_line + context_lines + 1)
        
        return '\n'.join(lines[start_line:end_line])
    
    def _extract_persona_info(self, content: str) -> List[Dict[str, Any]]:
        """Extract AI persona information from protocol."""
        personas = []
        
        # Look for AI Persona section
        persona_pattern = r'##\s*AI\s+Persona\s*\n(.*?)(?=\n##|\n---|\Z)'
        match = re.search(persona_pattern, content, re.IGNORECASE | re.DOTALL)
        
        if match:
            persona_content = match.group(1).strip()
            personas.append({
                "type": "declared",
                "content": persona_content,
                "line_number": content[:match.start()].count('\n') + 1
            })
        
        # Look for role mentions
        role_pattern = r'(?:Role|Act as|You are)\s*:?\s*(.*?)(?:\n|$)'
        role_matches = re.finditer(role_pattern, content, re.IGNORECASE)
        
        for match in role_matches:
            personas.append({
                "type": "role_mention",
                "content": match.group(1).strip(),
                "line_number": content[:match.start()].count('\n') + 1
            })
        
        return personas
    
    def _extract_communication_patterns(self, content: str) -> List[Dict[str, Any]]:
        """Extract communication patterns from protocol."""
        patterns = []
        
        for prefix_pattern in self.communication_prefixes:
            matches = list(re.finditer(prefix_pattern, content, re.IGNORECASE))
            for match in matches:
                patterns.append({
                    "prefix": match.group(0),
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                })
        
        return patterns
    
    def _extract_gate_criteria(self, content: str) -> List[Dict[str, Any]]:
        """Extract gate criteria from protocol."""
        gates = []
        
        # Look for gate patterns
        gate_patterns = [
            r'Gate\s*:?\s*(.*?)(?:\n|$)',
            r'Pass\s+Criteria\s*:?\s*(.*?)(?:\n|$)',
            r'Validation\s+Threshold\s*:?\s*(.*?)(?:\n|$)',
            r'Score\s*≥\s*(\d+)',
            r'≥\s*(\d+)'
        ]
        
        for pattern in gate_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                gates.append({
                    "criteria": match.group(1) if len(match.groups()) > 0 else match.group(0),
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                })
        
        return gates
    
    def _validate_directive_consistency(self, results: Dict[str, Any], content: str) -> None:
        """Validate directive consistency within protocol."""
        # Check for conflicting directives
        must_pattern = r'\[MUST\].*?(?:skip|ignore|avoid)'
        if re.search(must_pattern, content, re.IGNORECASE):
            results["issues"].append({
                "severity": "warning",
                "type": "conflicting_directive",
                "message": "Found [MUST] directive with negative action (skip/ignore/avoid)",
                "fix": "Review directive for logical consistency"
            })
        
        # Check for vague directives
        vague_pattern = r'\[MUST\].*?(?:might|could|maybe|perhaps)'
        if re.search(vague_pattern, content, re.IGNORECASE):
            results["issues"].append({
                "severity": "warning",
                "type": "vague_directive",
                "message": "Found [MUST] directive with vague language",
                "fix": "Use definitive language in [MUST] directives"
            })
    
    def _validate_persona_consistency(self, results: Dict[str, Any], content: str) -> None:
        """Validate persona consistency within protocol."""
        if not results["persona_analysis"]:
            results["issues"].append({
                "severity": "warning",
                "type": "missing_persona",
                "message": "No AI persona declared in protocol",
                "fix": "Add AI Persona section at protocol start"
            })
    
    def _validate_communication_consistency(self, results: Dict[str, Any], content: str) -> None:
        """Validate communication pattern consistency within protocol."""
        # Check for non-standard communication prefixes
        all_prefixes = set()
        for pattern in results["communication_patterns"]:
            all_prefixes.add(pattern["prefix"])
        
        # Look for non-standard prefixes
        bracket_pattern = r'\[[A-Z][A-Z\s/]+\]'
        all_brackets = re.findall(bracket_pattern, content)
        
        for bracket in all_brackets:
            if bracket not in [p.replace('\\', '') for p in self.communication_prefixes]:
                results["issues"].append({
                    "severity": "warning",
                    "type": "non_standard_prefix",
                    "message": f"Non-standard communication prefix: {bracket}",
                    "fix": "Use standard prefixes or add to communication_prefixes list"
                })
    
    def _analyze_directive_consistency(self, all_directives: Dict[str, List]) -> Dict[str, Any]:
        """Analyze directive consistency across all protocols."""
        analysis = {
            "total_usage": {tag: len(occurrences) for tag, occurrences in all_directives.items()},
            "consistency_score": {},
            "recommendations": []
        }
        
        # Calculate consistency scores
        total_directives = sum(analysis["total_usage"].values())
        
        for tag, occurrences in all_directives.items():
            if total_directives > 0:
                consistency_score = len(occurrences) / total_directives
                analysis["consistency_score"][tag] = consistency_score
        
        # Check for inconsistent usage
        must_count = analysis["total_usage"]["MUST"]
        guideline_count = analysis["total_usage"]["GUIDELINE"]
        
        if must_count > 0 and guideline_count > 0:
            ratio = must_count / guideline_count
            if ratio < 0.5 or ratio > 2.0:
                analysis["recommendations"].append({
                    "type": "directive_balance",
                    "message": f"MUST/GUIDELINE ratio is {ratio:.2f}, consider balancing usage",
                    "fix": "Review directive usage for appropriate balance"
                })
        
        return analysis
    
    def _analyze_persona_consistency(self, all_personas: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze persona consistency across all protocols."""
        analysis = {
            "total_personas": len(all_personas),
            "persona_types": {},
            "consistency_issues": []
        }
        
        # Count persona types
        for persona in all_personas:
            persona_type = persona["type"]
            if persona_type not in analysis["persona_types"]:
                analysis["persona_types"][persona_type] = 0
            analysis["persona_types"][persona_type] += 1
        
        # Check for missing declared personas
        declared_count = analysis["persona_types"].get("declared", 0)
        if declared_count < 7:  # Expected number of protocols
            analysis["consistency_issues"].append({
                "type": "missing_declared_personas",
                "message": f"Only {declared_count} protocols have declared personas",
                "fix": "Add AI Persona section to all protocols"
            })
        
        return analysis
    
    def _analyze_communication_consistency(self, all_communications: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze communication pattern consistency across all protocols."""
        analysis = {
            "total_patterns": len(all_communications),
            "prefix_usage": {},
            "consistency_issues": []
        }
        
        # Count prefix usage
        for pattern in all_communications:
            prefix = pattern["prefix"]
            if prefix not in analysis["prefix_usage"]:
                analysis["prefix_usage"][prefix] = 0
            analysis["prefix_usage"][prefix] += 1
        
        return analysis
    
    def _analyze_gate_consistency(self, all_gates: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze gate criteria consistency across all protocols."""
        analysis = {
            "total_gates": len(all_gates),
            "threshold_values": [],
            "consistency_issues": []
        }
        
        # Extract threshold values
        threshold_pattern = r'≥\s*(\d+)'
        for gate in all_gates:
            matches = re.findall(threshold_pattern, gate["criteria"])
            analysis["threshold_values"].extend([int(m) for m in matches])
        
        # Check for inconsistent thresholds
        if analysis["threshold_values"]:
            unique_thresholds = set(analysis["threshold_values"])
            if len(unique_thresholds) > 3:  # Allow some variation
                analysis["consistency_issues"].append({
                    "type": "inconsistent_thresholds",
                    "message": f"Found {len(unique_thresholds)} different threshold values: {sorted(unique_thresholds)}",
                    "fix": "Standardize gate thresholds across protocols"
                })
        
        return analysis


def main():
    """Main entry point for AI directive validation."""
    parser = argparse.ArgumentParser(description="Validate AI directive consistency")
    parser.add_argument("--workspace", "-w", default=".", help="Workspace root directory")
    parser.add_argument("--output", "-o", help="Output file for validation results (JSON)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--protocol", "-p", help="Validate specific protocol only")
    
    args = parser.parse_args()
    
    validator = AIDirectiveValidator(args.workspace)
    
    if args.protocol:
        # Validate single protocol
        if args.protocol not in validator.protocols:
            print(f"Error: Protocol {args.protocol} not found")
            sys.exit(1)
        
        protocol_file = validator.dev_workflow_dir / validator.protocols[args.protocol]
        if not protocol_file.exists():
            print(f"Error: Protocol file {protocol_file} not found")
            sys.exit(1)
        
        content = protocol_file.read_text(encoding='utf-8')
        results = validator._validate_single_protocol(args.protocol, content)
    else:
        # Validate all protocols
        results = validator.validate_ai_directives()
    
    # Output results
    if args.verbose or not args.output:
        print("🔍 AI Directive Consistency Validation")
        print("=" * 50)
        print(f"Status: {results['status'].upper()}")
        
        if "summary" in results:
            print(f"Total Protocols: {results['summary']['total_protocols']}")
            print(f"Validated: {results['summary']['validated']}")
            print(f"Issues Found: {results['summary']['issues_found']}")
            print(f"Critical Issues: {results['summary']['critical_issues']}")
        
        if "directive_usage" in results:
            print("\n📋 Directive Usage Summary:")
            for tag, count in results["directive_usage"]["total_usage"].items():
                print(f"  {tag}: {count} occurrences")
        
        if results.get("issues"):
            print("\n❌ Issues:")
            for issue in results["issues"]:
                print(f"  {issue['severity'].upper()}: {issue['message']}")
                print(f"    Fix: {issue['fix']}")
    
    # Save to output file if specified
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Validation results saved to: {args.output}")
    
    # Exit with appropriate code
    if results["status"] == "fail":
        sys.exit(1)
    elif results["status"] == "warning":
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
