#!/usr/bin/env python3
"""
Protocol Step Sequence Validation Script

Validates the logical flow and sequence of steps within each protocol:
- Step numbering validation
- Step dependency validation  
- Phase consistency validation
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any


class ProtocolStepValidator:
    """Validates step sequences and dependencies within protocols."""
    
    def __init__(self, workspace_root: str = "."):
        self.workspace_root = Path(workspace_root)
        self.ai_driven_workflow_dir = self.workspace_root / ".cursor" / "ai-driven-workflow"
        self.unified_workflow_dir = self.workspace_root / "unified_workflow" / "phases"

        self.cursor_protocols = {
            "00": "00-client-discovery.md",
            "0": "0-bootstrap-your-project.md",
            "1": "1-create-prd.md",
            "2": "2-generate-tasks.md",
            "3": "3-process-tasks.md",
            "4": "4-quality-audit.md",
            "5": "5-implementation-retrospective.md",
        }

        self.unified_protocols = {
            "0": "0-bootstrap.md",
            "1": "1-prd-creation.md",
            "2": "2-task-generation.md",
            "3": "3-implementation.md",
            "4": "4-quality-audit.md",
            "5": "5-retrospective.md",
            "6": "6-operations.md",
        }
    
    def validate_protocol_steps(self) -> Dict[str, Any]:
        """Run comprehensive step validation across all protocols."""
        results = {
            "status": "pass",
            "summary": {
                "total_protocols": len(self.cursor_protocols) + len(self.unified_protocols),
                "validated": 0,
                "issues_found": 0,
                "critical_issues": 0
            },
            "protocols": {},
            "issues": [],
            "recommendations": []
        }
        
        for protocol_id, protocol_file in self.cursor_protocols.items():
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
                protocol_results = self._validate_single_protocol(protocol_id, content, require_scripts=False)
                results["protocols"][f"protocol_{protocol_id}"] = protocol_results
                results["summary"]["validated"] += 1

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

        for protocol_id, protocol_file in self.unified_protocols.items():
            protocol_path = self.unified_workflow_dir / protocol_file

            if not protocol_path.exists():
                results["issues"].append({
                    "severity": "critical",
                    "protocol": f"unified_protocol_{protocol_id}",
                    "message": f"Unified protocol file not found: {protocol_file}",
                    "fix": f"Create {protocol_path}",
                })
                results["summary"]["critical_issues"] += 1
                continue

            try:
                content = protocol_path.read_text(encoding='utf-8')
                protocol_results = self._validate_single_protocol(protocol_id, content, require_scripts=True)
                results["protocols"][f"unified_protocol_{protocol_id}"] = protocol_results
                results["summary"]["validated"] += 1

                if protocol_results["issues"]:
                    results["issues"].extend(protocol_results["issues"])
                    results["summary"]["issues_found"] += len(protocol_results["issues"])
                    results["summary"]["critical_issues"] += sum(1 for issue in protocol_results["issues"] if issue["severity"] == "critical")

            except Exception as e:
                results["issues"].append({
                    "severity": "critical",
                    "protocol": f"unified_protocol_{protocol_id}",
                    "message": f"Cannot read protocol file: {str(e)}",
                    "fix": "Check file permissions and encoding",
                })
                results["summary"]["critical_issues"] += 1

        # Calculate overall status
        if results["summary"]["critical_issues"] > 0:
            results["status"] = "fail"
        elif results["summary"]["issues_found"] > 0:
            results["status"] = "warning"

        return results

    def _validate_single_protocol(self, protocol_id: str, content: str, *, require_scripts: bool) -> Dict[str, Any]:
        """Validate a single protocol's step sequence."""
        results = {
            "protocol_id": protocol_id,
            "step_validation": {},
            "phase_validation": {},
            "issues": [],
            "recommendations": []
        }

        # Extract steps and phases
        steps = self._extract_steps(content)
        phases = self._extract_phases(content)
        
        # Validate step numbering
        step_results = self._validate_step_numbering(steps)
        results["step_validation"] = step_results
        
        # Validate step dependencies
        dependency_results = self._validate_step_dependencies(steps, content)
        results["step_validation"].update(dependency_results)

        # Validate phase consistency
        phase_results = self._validate_phase_consistency(phases)
        results["phase_validation"] = phase_results

        if require_scripts:
            script_results = self._validate_script_injection(steps, content)
            results["step_validation"].update(script_results)
            if script_results.get("issues"):
                results["issues"].extend(script_results["issues"])

        # Collect issues
        if step_results.get("issues"):
            results["issues"].extend(step_results["issues"])
        if dependency_results.get("issues"):
            results["issues"].extend(dependency_results["issues"])
        if phase_results.get("issues"):
            results["issues"].extend(phase_results["issues"])

        return results

    def _validate_script_injection(self, steps: List[Dict[str, Any]], content: str) -> Dict[str, Any]:
        issues = []
        script_pattern = re.compile(r"\{SCRIPT:\s*([^}]+)\}")

        for idx, step in enumerate(steps):
            start_line = step["line_number"]
            end_line = steps[idx + 1]["line_number"] if idx + 1 < len(steps) else None
            step_lines = content.splitlines()
            segment = "\n".join(step_lines[start_line - 1 : end_line - 1 if end_line else None])
            if not script_pattern.search(segment):
                issues.append({
                    "severity": "warning",
                    "protocol": f"step_{step['number']}",
                    "message": f"Step {step['number']} ('{step['title']}') is missing a SCRIPT binding",
                    "fix": "Add `{SCRIPT: <automation>}` to align with orchestrator requirements.",
                })

        return {"issues": issues}
    
    def _extract_steps(self, content: str) -> List[Dict[str, Any]]:
        """Extract all steps from protocol content."""
        steps = []
        
        # Pattern for step headers (e.g., "### STEP 1.0:", "### STEP 1.1:", etc.)
        step_pattern = r'###\s*STEP\s+(\d+(?:\.\d+)*):\s*(.*)'
        
        for match in re.finditer(step_pattern, content, re.IGNORECASE):
            step_number = match.group(1)
            step_title = match.group(2).strip()
            
            # Parse step number into components
            step_parts = step_number.split('.')
            level = len(step_parts)
            parent = '.'.join(step_parts[:-1]) if level > 1 else None
            
            steps.append({
                "number": step_number,
                "title": step_title,
                "level": level,
                "parent": parent,
                "line_number": content[:match.start()].count('\n') + 1
            })
        
        return sorted(steps, key=lambda x: [int(part) for part in x["number"].split('.')])
    
    def _extract_phases(self, content: str) -> List[Dict[str, Any]]:
        """Extract all phases from protocol content."""
        phases = []
        
        # Pattern for phase headers (e.g., "### PHASE 1:", "### PHASE 4.5:", etc.)
        phase_pattern = r'###\s*PHASE\s+(\d+(?:\.\d+)*):\s*(.*)'
        
        for match in re.finditer(phase_pattern, content, re.IGNORECASE):
            phase_number = match.group(1)
            phase_title = match.group(2).strip()
            
            phases.append({
                "number": phase_number,
                "title": phase_title,
                "line_number": content[:match.start()].count('\n') + 1
            })
        
        return sorted(phases, key=lambda x: [int(part) for part in x["number"].split('.')])
    
    def _validate_step_numbering(self, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Validate step numbering sequence."""
        results = {
            "total_steps": len(steps),
            "duplicate_steps": [],
            "missing_steps": [],
            "sequence_issues": [],
            "issues": []
        }
        
        if not steps:
            return results
        
        # Check for duplicates
        step_numbers = [step["number"] for step in steps]
        duplicates = set([num for num in step_numbers if step_numbers.count(num) > 1])
        results["duplicate_steps"] = list(duplicates)
        
        if duplicates:
            results["issues"].append({
                "severity": "critical",
                "type": "duplicate_steps",
                "message": f"Duplicate step numbers found: {duplicates}",
                "fix": "Ensure each step has a unique number"
            })
        
        # Check sequence gaps
        expected_numbers = []
        for i, step in enumerate(steps):
            parts = step["number"].split('.')
            
            # Generate expected next number
            if i == 0:
                expected_numbers.append(step["number"])
            else:
                prev_parts = steps[i-1]["number"].split('.')
                
                # Simple increment for same level
                if len(parts) == len(prev_parts):
                    try:
                        last_part = int(prev_parts[-1])
                        new_parts = prev_parts[:-1] + [str(last_part + 1)]
                        expected_numbers.append('.'.join(new_parts))
                    except ValueError:
                        expected_numbers.append(step["number"])
                else:
                    expected_numbers.append(step["number"])
        
        # Check for missing steps
        for i, (actual, expected) in enumerate(zip([s["number"] for s in steps], expected_numbers)):
            if actual != expected:
                results["sequence_issues"].append({
                    "position": i,
                    "actual": actual,
                    "expected": expected,
                    "step": steps[i]
                })
        
        if results["sequence_issues"]:
            results["issues"].append({
                "severity": "warning",
                "type": "sequence_gaps",
                "message": f"Step sequence has gaps or jumps: {len(results['sequence_issues'])} issues",
                "fix": "Review step numbering for logical sequence"
            })
        
        return results
    
    def _validate_step_dependencies(self, steps: List[Dict[str, Any]], content: str) -> Dict[str, Any]:
        """Validate step dependencies and references."""
        results = {
            "future_references": [],
            "missing_prerequisites": [],
            "circular_dependencies": [],
            "issues": []
        }
        
        # Check for references to future steps
        step_numbers = [step["number"] for step in steps]
        
        for step in steps:
            step_content_start = content.find(f"### STEP {step['number']}:")
            if step_content_start == -1:
                continue
            
            # Find next step or end of content
            next_step_start = content.find("### STEP ", step_content_start + 1)
            step_content = content[step_content_start:next_step_start] if next_step_start != -1 else content[step_content_start:]
            
            # Look for references to other steps
            step_ref_pattern = r'STEP\s+(\d+(?:\.\d+)*)'
            references = re.findall(step_ref_pattern, step_content, re.IGNORECASE)
            
            for ref in references:
                if ref != step["number"]:  # Not self-reference
                    ref_index = step_numbers.index(ref) if ref in step_numbers else -1
                    current_index = step_numbers.index(step["number"])
                    
                    if ref_index > current_index:
                        results["future_references"].append({
                            "step": step["number"],
                            "references": ref,
                            "line": step["line_number"]
                        })
        
        if results["future_references"]:
            results["issues"].append({
                "severity": "warning",
                "type": "future_references",
                "message": f"Steps reference future steps: {len(results['future_references'])} instances",
                "fix": "Reorder steps or remove forward references"
            })
        
        return results
    
    def _validate_phase_consistency(self, phases: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Validate phase consistency and structure."""
        results = {
            "total_phases": len(phases),
            "phase_overlaps": [],
            "automation_phases": [],
            "issues": []
        }
        
        if not phases:
            return results
        
        # Check for automation phases (e.g., Phase 4.5)
        for phase in phases:
            if '.' in phase["number"]:
                results["automation_phases"].append(phase)
        
        # Check phase sequence
        phase_numbers = [phase["number"] for phase in phases]
        
        # Validate automation phases are properly inserted
        for phase in results["automation_phases"]:
            base_number = phase["number"].split('.')[0]
            base_phase_exists = any(p["number"] == base_number for p in phases)
            
            if not base_phase_exists:
                results["issues"].append({
                    "severity": "warning",
                    "type": "orphaned_automation_phase",
                    "message": f"Automation phase {phase['number']} has no base phase {base_number}",
                    "fix": f"Add base phase {base_number} or rename automation phase"
                })
        
        return results


def main():
    """Main entry point for protocol step validation."""
    parser = argparse.ArgumentParser(description="Validate protocol step sequences")
    parser.add_argument("--workspace", "-w", default=".", help="Workspace root directory")
    parser.add_argument("--output", "-o", help="Output file for validation results (JSON)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--protocol", "-p", help="Validate specific protocol only")
    
    args = parser.parse_args()
    
    validator = ProtocolStepValidator(args.workspace)
    
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
        results = validator.validate_protocol_steps()
    
    # Output results
    if args.verbose or not args.output:
        print("🔍 Protocol Step Sequence Validation")
        print("=" * 50)
        print(f"Status: {results['status'].upper()}")
        
        if "summary" in results:
            print(f"Total Protocols: {results['summary']['total_protocols']}")
            print(f"Validated: {results['summary']['validated']}")
            print(f"Issues Found: {results['summary']['issues_found']}")
            print(f"Critical Issues: {results['summary']['critical_issues']}")
        
        if "protocols" in results:
            print("\n📋 Protocol Results:")
            for protocol, data in results["protocols"].items():
                print(f"  {protocol}: {len(data.get('issues', []))} issues")
        
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
