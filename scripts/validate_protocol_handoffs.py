#!/usr/bin/env python3
"""
Protocol Handoff Validation Script

Validates protocol transitions and handoff logic:
- Output → Input alignment
- Handoff instruction validation
- State transition validation
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any


class ProtocolHandoffValidator:
    """Validates protocol handoffs and transitions."""
    
    def __init__(self, workspace_root: str = "."):
        self.workspace_root = Path(workspace_root)
        self.ai_driven_workflow_dir = self.workspace_root / ".cursor" / "ai-driven-workflow"
        
        # Protocol files and their expected outputs/inputs
        self.protocols = {
            "00": {
                "file": "00-client-discovery.md",
                "outputs": ["brief.md", "acceptance-criteria.md", "risks.md"],
                "next_protocol": "0"
            },
            "0": {
                "file": "0-bootstrap-your-project.md",
                "outputs": ["context-kit", "project-structure"],
                "next_protocol": "1"
            },
            "1": {
                "file": "1-create-prd.md",
                "outputs": ["PRD", "implementation-ready-prd"],
                "next_protocol": "2"
            },
            "2": {
                "file": "2-generate-tasks.md",
                "outputs": ["tasks", "execution-plan"],
                "next_protocol": "3"
            },
            "3": {
                "file": "3-process-tasks.md",
                "outputs": ["artifacts", "test-results", "coverage"],
                "next_protocol": "4"
            },
            "4": {
                "file": "4-quality-audit.md",
                "outputs": ["audit-report", "quality-gates"],
                "next_protocol": "5"
            },
            "5": {
                "file": "5-implementation-retrospective.md",
                "outputs": ["retrospective-report", "improvements"],
                "next_protocol": None
            }
        }
    
    def validate_protocol_handoffs(self) -> Dict[str, Any]:
        """Run comprehensive handoff validation across all protocols."""
        results = {
            "status": "pass",
            "summary": {
                "total_protocols": len(self.protocols),
                "validated": 0,
                "handoff_issues": 0,
                "critical_issues": 0
            },
            "handoff_map": {},
            "state_transitions": {},
            "issues": [],
            "recommendations": []
        }
        
        # Validate each protocol's handoff
        for protocol_id, protocol_info in self.protocols.items():
            protocol_path = self.dev_workflow_dir / protocol_info["file"]
            
            if not protocol_path.exists():
                results["issues"].append({
                    "severity": "critical",
                    "protocol": f"protocol_{protocol_id}",
                    "message": f"Protocol file not found: {protocol_info['file']}",
                    "fix": f"Create {protocol_path}"
                })
                results["summary"]["critical_issues"] += 1
                continue
            
            try:
                content = protocol_path.read_text(encoding='utf-8')
                handoff_results = self._validate_single_handoff(protocol_id, content, protocol_info)
                results["handoff_map"][f"protocol_{protocol_id}"] = handoff_results
                results["summary"]["validated"] += 1
                
                if handoff_results["issues"]:
                    results["issues"].extend(handoff_results["issues"])
                    results["summary"]["handoff_issues"] += len(handoff_results["issues"])
                    results["summary"]["critical_issues"] += sum(1 for issue in handoff_results["issues"] if issue["severity"] == "critical")
                
            except Exception as e:
                results["issues"].append({
                    "severity": "critical",
                    "protocol": f"protocol_{protocol_id}",
                    "message": f"Cannot read protocol file: {str(e)}",
                    "fix": "Check file permissions and encoding"
                })
                results["summary"]["critical_issues"] += 1
        
        # Validate cross-protocol handoff alignment
        alignment_results = self._validate_handoff_alignment()
        results["handoff_alignment"] = alignment_results
        
        if alignment_results["issues"]:
            results["issues"].extend(alignment_results["issues"])
            results["summary"]["handoff_issues"] += len(alignment_results["issues"])
        
        # Calculate overall status
        if results["summary"]["critical_issues"] > 0:
            results["status"] = "fail"
        elif results["summary"]["handoff_issues"] > 0:
            results["status"] = "warning"
        
        return results
    
    def _validate_single_handoff(self, protocol_id: str, content: str, protocol_info: Dict[str, Any]) -> Dict[str, Any]:
        """Validate handoff for a single protocol."""
        results = {
            "protocol_id": protocol_id,
            "outputs_detected": [],
            "handoff_instructions": [],
            "state_preservation": [],
            "rollback_procedures": [],
            "issues": [],
            "recommendations": []
        }
        
        # Extract outputs mentioned in protocol
        results["outputs_detected"] = self._extract_outputs(content)
        
        # Extract handoff instructions
        results["handoff_instructions"] = self._extract_handoff_instructions(content)
        
        # Extract state preservation instructions
        results["state_preservation"] = self._extract_state_preservation(content)
        
        # Extract rollback procedures
        results["rollback_procedures"] = self._extract_rollback_procedures(content)
        
        # Validate expected outputs are mentioned
        self._validate_expected_outputs(results, protocol_info["outputs"])
        
        # Validate handoff instructions are clear
        self._validate_handoff_clarity(results, content)
        
        # Validate next protocol invocation
        if protocol_info["next_protocol"]:
            self._validate_next_protocol_invocation(results, content, protocol_info["next_protocol"])
        
        return results
    
    def _extract_outputs(self, content: str) -> List[Dict[str, Any]]:
        """Extract output artifacts mentioned in protocol."""
        outputs = []
        
        # Common output patterns
        output_patterns = [
            r'generate\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))',
            r'create\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))',
            r'output\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))',
            r'produce\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))',
            r'write\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))',
            r'save\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))'
        ]
        
        for pattern in output_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                outputs.append({
                    "file": match.group(1),
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                })
        
        return outputs
    
    def _extract_handoff_instructions(self, content: str) -> List[Dict[str, Any]]:
        """Extract handoff instructions from protocol."""
        instructions = []
        
        # Handoff instruction patterns
        handoff_patterns = [
            r'handoff\s+(?:to\s+)?(?:protocol\s+)?(\d+)',
            r'proceed\s+(?:to\s+)?(?:protocol\s+)?(\d+)',
            r'continue\s+(?:to\s+)?(?:protocol\s+)?(\d+)',
            r'next\s+(?:protocol\s+)?(\d+)',
            r'user\s+approval\s+(?:required|needed)',
            r'await\s+(?:user\s+)?(?:confirmation|approval)',
            r'confirm\s+(?:with\s+)?user'
        ]
        
        for pattern in handoff_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                instructions.append({
                    "type": "handoff",
                    "target": match.group(1) if match.groups() else None,
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                })
        
        return instructions
    
    def _extract_state_preservation(self, content: str) -> List[Dict[str, Any]]:
        """Extract state preservation instructions."""
        state_instructions = []
        
        # State preservation patterns
        state_patterns = [
            r'preserve\s+(?:state|context|data)',
            r'maintain\s+(?:state|context|data)',
            r'carry\s+(?:forward|over)\s+(?:state|context|data)',
            r'store\s+(?:state|context|data)',
            r'save\s+(?:state|context|data)',
            r'context\s+(?:kit|preservation)',
            r'state\s+(?:preservation|maintenance)'
        ]
        
        for pattern in state_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                state_instructions.append({
                    "type": "state_preservation",
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                })
        
        return state_instructions
    
    def _extract_rollback_procedures(self, content: str) -> List[Dict[str, Any]]:
        """Extract rollback procedures from protocol."""
        rollback_procedures = []
        
        # Rollback patterns
        rollback_patterns = [
            r'rollback\s+(?:procedure|process)',
            r'revert\s+(?:to|changes)',
            r'undo\s+(?:changes|actions)',
            r'fallback\s+(?:procedure|option)',
            r'error\s+(?:recovery|handling)',
            r'failure\s+(?:recovery|handling)'
        ]
        
        for pattern in rollback_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                rollback_procedures.append({
                    "type": "rollback",
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                })
        
        return rollback_procedures
    
    def _extract_context(self, content: str, start: int, end: int, context_lines: int = 2) -> str:
        """Extract context around a match."""
        lines = content.split('\n')
        match_line = content[:start].count('\n')
        
        start_line = max(0, match_line - context_lines)
        end_line = min(len(lines), match_line + context_lines + 1)
        
        return '\n'.join(lines[start_line:end_line])
    
    def _validate_expected_outputs(self, results: Dict[str, Any], expected_outputs: List[str]) -> None:
        """Validate that expected outputs are mentioned in protocol."""
        detected_files = [output["file"] for output in results["outputs_detected"]]
        
        for expected in expected_outputs:
            if not any(expected in detected for detected in detected_files):
                results["issues"].append({
                    "severity": "warning",
                    "type": "missing_expected_output",
                    "message": f"Expected output '{expected}' not mentioned in protocol",
                    "fix": f"Add instructions to generate {expected}"
                })
    
    def _validate_handoff_clarity(self, results: Dict[str, Any], content: str) -> None:
        """Validate that handoff instructions are clear."""
        if not results["handoff_instructions"]:
            results["issues"].append({
                "severity": "warning",
                "type": "missing_handoff_instructions",
                "message": "No explicit handoff instructions found",
                "fix": "Add clear handoff instructions at protocol end"
            })
        
        # Check for user approval requirements
        approval_patterns = [
            r'user\s+approval',
            r'await\s+confirmation',
            r'confirm\s+with\s+user'
        ]
        
        has_approval = any(
            re.search(pattern, content, re.IGNORECASE)
            for pattern in approval_patterns
        )
        
        if not has_approval:
            results["issues"].append({
                "severity": "warning",
                "type": "missing_user_approval",
                "message": "No user approval requirement found for handoff",
                "fix": "Add user confirmation step before handoff"
            })
    
    def _validate_next_protocol_invocation(self, results: Dict[str, Any], content: str, next_protocol: str) -> None:
        """Validate next protocol invocation instructions."""
        invocation_patterns = [
            rf'protocol\s+{next_protocol}',
            rf'proceed\s+to\s+protocol\s+{next_protocol}',
            rf'continue\s+to\s+protocol\s+{next_protocol}',
            rf'handoff\s+to\s+protocol\s+{next_protocol}'
        ]
        
        has_invocation = any(
            re.search(pattern, content, re.IGNORECASE)
            for pattern in invocation_patterns
        )
        
        if not has_invocation:
            results["issues"].append({
                "severity": "warning",
                "type": "missing_protocol_invocation",
                "message": f"No invocation of next protocol {next_protocol} found",
                "fix": f"Add clear instructions to proceed to protocol {next_protocol}"
            })
    
    def _validate_handoff_alignment(self) -> Dict[str, Any]:
        """Validate handoff alignment between protocols."""
        results = {
            "alignment_issues": [],
            "issues": []
        }
        
        # Check Protocol 00 → 0 handoff
        protocol_00_outputs = ["brief.md", "acceptance-criteria.md", "risks.md"]
        protocol_0_inputs = ["project overview", "requirements", "context"]
        
        alignment_score = self._calculate_alignment_score(protocol_00_outputs, protocol_0_inputs)
        if alignment_score < 0.7:
            results["alignment_issues"].append({
                "from": "protocol_00",
                "to": "protocol_0",
                "score": alignment_score,
                "message": "Output-input alignment is weak"
            })
        
        # Check Protocol 0 → 1 handoff
        protocol_0_outputs = ["context-kit", "project-structure"]
        protocol_1_inputs = ["architecture context", "project setup"]
        
        alignment_score = self._calculate_alignment_score(protocol_0_outputs, protocol_1_inputs)
        if alignment_score < 0.7:
            results["alignment_issues"].append({
                "from": "protocol_0",
                "to": "protocol_1",
                "score": alignment_score,
                "message": "Output-input alignment is weak"
            })
        
        # Add issues for poor alignment
        for issue in results["alignment_issues"]:
            results["issues"].append({
                "severity": "warning",
                "type": "handoff_alignment",
                "message": f"{issue['from']} → {issue['to']}: {issue['message']} (score: {issue['score']:.2f})",
                "fix": "Review and align output-input specifications"
            })
        
        return results
    
    def _calculate_alignment_score(self, outputs: List[str], inputs: List[str]) -> float:
        """Calculate alignment score between outputs and inputs."""
        if not outputs or not inputs:
            return 0.0
        
        # Simple keyword matching for alignment
        output_keywords = set()
        for output in outputs:
            output_keywords.update(output.lower().replace('-', ' ').split())
        
        input_keywords = set()
        for input_item in inputs:
            input_keywords.update(input_item.lower().replace('-', ' ').split())
        
        # Calculate overlap
        overlap = len(output_keywords.intersection(input_keywords))
        total = len(output_keywords.union(input_keywords))
        
        return overlap / total if total > 0 else 0.0


def main():
    """Main entry point for protocol handoff validation."""
    parser = argparse.ArgumentParser(description="Validate protocol handoffs")
    parser.add_argument("--workspace", "-w", default=".", help="Workspace root directory")
    parser.add_argument("--output", "-o", help="Output file for validation results (JSON)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--protocol", "-p", help="Validate specific protocol only")
    
    args = parser.parse_args()
    
    validator = ProtocolHandoffValidator(args.workspace)
    
    if args.protocol:
        # Validate single protocol
        if args.protocol not in validator.protocols:
            print(f"Error: Protocol {args.protocol} not found")
            sys.exit(1)
        
        protocol_file = validator.dev_workflow_dir / validator.protocols[args.protocol]["file"]
        if not protocol_file.exists():
            print(f"Error: Protocol file {protocol_file} not found")
            sys.exit(1)
        
        content = protocol_file.read_text(encoding='utf-8')
        results = validator._validate_single_handoff(args.protocol, content, validator.protocols[args.protocol])
    else:
        # Validate all protocols
        results = validator.validate_protocol_handoffs()
    
    # Output results
    if args.verbose or not args.output:
        print("🔍 Protocol Handoff Validation")
        print("=" * 50)
        print(f"Status: {results['status'].upper()}")
        
        if "summary" in results:
            print(f"Total Protocols: {results['summary']['total_protocols']}")
            print(f"Validated: {results['summary']['validated']}")
            print(f"Handoff Issues: {results['summary']['handoff_issues']}")
            print(f"Critical Issues: {results['summary']['critical_issues']}")
        
        if "handoff_map" in results:
            print("\n📋 Handoff Map:")
            for protocol, data in results["handoff_map"].items():
                print(f"  {protocol}: {len(data.get('outputs_detected', []))} outputs, {len(data.get('issues', []))} issues")
        
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
