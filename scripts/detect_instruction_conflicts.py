#!/usr/bin/env python3
"""
Instruction Conflict Detection Script

Detects ambiguous, conflicting, or contradictory instructions:
- Contradiction detection
- Ambiguity detection
- Completeness validation
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any


class InstructionConflictDetector:
    """Detects conflicts and ambiguities in protocol instructions."""
    
    def __init__(self, workspace_root: str = "."):
        self.workspace_root = Path(workspace_root)
        self.ai_driven_workflow_dir = self.workspace_root / ".cursor" / "ai-driven-workflow"
        
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
        
        # Contradiction patterns
        self.contradiction_patterns = [
            (r'\[MUST\].*?(?:skip|ignore|avoid)', r'\[MUST\].*?(?:execute|run|perform)', 'must_skip_vs_execute'),
            (r'\[MUST\].*?(?:never|not)', r'\[MUST\].*?(?:always|always)', 'must_never_vs_always'),
            (r'\[STRICT\].*?(?:optional|may)', r'\[STRICT\].*?(?:required|must)', 'strict_optional_vs_required'),
            (r'\[GUIDELINE\].*?(?:must|required)', r'\[GUIDELINE\].*?(?:should|recommended)', 'guideline_must_vs_should')
        ]
        
        # Ambiguity patterns
        self.ambiguity_patterns = [
            (r'\[MUST\].*?(?:might|could|maybe|perhaps)', 'vague_must_directive'),
            (r'\[STRICT\].*?(?:might|could|maybe|perhaps)', 'vague_strict_directive'),
            (r'\[MUST\].*?(?:if\s+possible|when\s+available)', 'conditional_must'),
            (r'\[STRICT\].*?(?:if\s+possible|when\s+available)', 'conditional_strict'),
            (r'\[MUST\].*?(?:try\s+to|attempt\s+to)', 'attempt_must'),
            (r'\[STRICT\].*?(?:try\s+to|attempt\s+to)', 'attempt_strict')
        ]
        
        # Completeness patterns
        self.completeness_patterns = [
            (r'if\s+(?:.*?)\s+then\s+(?:.*?)(?!\s+else)', 'missing_else_branch'),
            (r'when\s+(?:.*?)\s+do\s+(?:.*?)(?!\s+otherwise)', 'missing_otherwise_branch'),
            (r'\[MUST\].*?(?:handle|manage)\s+(?:.*?)(?!\s+if\s+.*?\s+fails)', 'missing_error_handling'),
            (r'\[STRICT\].*?(?:handle|manage)\s+(?:.*?)(?!\s+if\s+.*?\s+fails)', 'missing_error_handling')
        ]
    
    def detect_instruction_conflicts(self) -> Dict[str, Any]:
        """Run comprehensive conflict detection across all protocols."""
        results = {
            "status": "pass",
            "summary": {
                "total_protocols": len(self.protocols),
                "validated": 0,
                "contradictions": 0,
                "ambiguities": 0,
                "completeness_issues": 0,
                "critical_issues": 0
            },
            "contradictions": [],
            "ambiguities": [],
            "completeness_issues": [],
            "issues": [],
            "recommendations": []
        }
        
        for protocol_id, protocol_file in self.protocols.items():
            protocol_path = self.dev_workflow_dir / protocol_file
            
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
                protocol_results = self._detect_single_protocol_conflicts(protocol_id, content)
                results["summary"]["validated"] += 1
                
                # Aggregate results
                results["contradictions"].extend(protocol_results["contradictions"])
                results["ambiguities"].extend(protocol_results["ambiguities"])
                results["completeness_issues"].extend(protocol_results["completeness_issues"])
                
                if protocol_results["issues"]:
                    results["issues"].extend(protocol_results["issues"])
                
                # Update summary counts
                results["summary"]["contradictions"] += len(protocol_results["contradictions"])
                results["summary"]["ambiguities"] += len(protocol_results["ambiguities"])
                results["summary"]["completeness_issues"] += len(protocol_results["completeness_issues"])
                results["summary"]["critical_issues"] += sum(1 for issue in protocol_results["issues"] if issue["severity"] == "critical")
                
            except Exception as e:
                results["issues"].append({
                    "severity": "critical",
                    "protocol": f"protocol_{protocol_id}",
                    "message": f"Cannot read protocol file: {str(e)}",
                    "fix": "Check file permissions and encoding"
                })
                results["summary"]["critical_issues"] += 1
        
        # Calculate overall status
        total_issues = (results["summary"]["contradictions"] + 
                       results["summary"]["ambiguities"] + 
                       results["summary"]["completeness_issues"])
        
        if results["summary"]["critical_issues"] > 0:
            results["status"] = "fail"
        elif total_issues > 0:
            results["status"] = "warning"
        
        return results
    
    def _detect_single_protocol_conflicts(self, protocol_id: str, content: str) -> Dict[str, Any]:
        """Detect conflicts in a single protocol."""
        results = {
            "protocol_id": protocol_id,
            "contradictions": [],
            "ambiguities": [],
            "completeness_issues": [],
            "issues": []
        }
        
        # Detect contradictions
        results["contradictions"] = self._detect_contradictions(content, protocol_id)
        
        # Detect ambiguities
        results["ambiguities"] = self._detect_ambiguities(content, protocol_id)
        
        # Detect completeness issues
        results["completeness_issues"] = self._detect_completeness_issues(content, protocol_id)
        
        # Convert to issues format
        for contradiction in results["contradictions"]:
            results["issues"].append({
                "severity": "critical",
                "type": "contradiction",
                "message": contradiction["message"],
                "fix": contradiction["fix"]
            })
        
        for ambiguity in results["ambiguities"]:
            results["issues"].append({
                "severity": "warning",
                "type": "ambiguity",
                "message": ambiguity["message"],
                "fix": ambiguity["fix"]
            })
        
        for completeness in results["completeness_issues"]:
            results["issues"].append({
                "severity": "warning",
                "type": "completeness",
                "message": completeness["message"],
                "fix": completeness["fix"]
            })
        
        return results
    
    def _detect_contradictions(self, content: str, protocol_id: str) -> List[Dict[str, Any]]:
        """Detect contradictory instructions."""
        contradictions = []
        
        for pattern1, pattern2, conflict_type in self.contradiction_patterns:
            matches1 = list(re.finditer(pattern1, content, re.IGNORECASE | re.DOTALL))
            matches2 = list(re.finditer(pattern2, content, re.IGNORECASE | re.DOTALL))
            
            if matches1 and matches2:
                contradictions.append({
                    "type": conflict_type,
                    "pattern1": pattern1,
                    "pattern2": pattern2,
                    "matches1": len(matches1),
                    "matches2": len(matches2),
                    "message": f"Contradictory instructions detected: {conflict_type}",
                    "fix": "Review and resolve conflicting directives",
                    "protocol": protocol_id
                })
        
        # Check for circular dependencies
        circular_deps = self._detect_circular_dependencies(content)
        contradictions.extend(circular_deps)
        
        return contradictions
    
    def _detect_circular_dependencies(self, content: str) -> List[Dict[str, Any]]:
        """Detect circular dependencies in instructions."""
        circular_deps = []
        
        # Look for step references that create cycles
        step_ref_pattern = r'STEP\s+(\d+(?:\.\d+)*)'
        step_refs = re.findall(step_ref_pattern, content, re.IGNORECASE)
        
        # Simple circular dependency detection
        # This is a basic implementation - could be enhanced
        for i, ref1 in enumerate(step_refs):
            for j, ref2 in enumerate(step_refs[i+1:], i+1):
                if ref1 == ref2:
                    # Check if they reference each other
                    ref1_context = self._extract_context_around_pattern(content, f"STEP {ref1}")
                    ref2_context = self._extract_context_around_pattern(content, f"STEP {ref2}")
                    
                    if ref2 in ref1_context and ref1 in ref2_context:
                        circular_deps.append({
                            "type": "circular_dependency",
                            "step1": ref1,
                            "step2": ref2,
                            "message": f"Circular dependency detected between STEP {ref1} and STEP {ref2}",
                            "fix": "Break circular dependency by restructuring steps",
                            "protocol": "unknown"  # Would need protocol context
                        })
        
        return circular_deps
    
    def _detect_ambiguities(self, content: str, protocol_id: str) -> List[Dict[str, Any]]:
        """Detect ambiguous instructions."""
        ambiguities = []
        
        for pattern, ambiguity_type in self.ambiguity_patterns:
            matches = list(re.finditer(pattern, content, re.IGNORECASE | re.DOTALL))
            
            for match in matches:
                ambiguities.append({
                    "type": ambiguity_type,
                    "pattern": pattern,
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end()),
                    "message": f"Ambiguous instruction detected: {ambiguity_type}",
                    "fix": "Use definitive language in directives",
                    "protocol": protocol_id
                })
        
        # Check for unclear pronouns
        pronoun_ambiguities = self._detect_pronoun_ambiguities(content)
        ambiguities.extend(pronoun_ambiguities)
        
        return ambiguities
    
    def _detect_pronoun_ambiguities(self, content: str) -> List[Dict[str, Any]]:
        """Detect unclear pronoun references."""
        pronoun_ambiguities = []
        
        # Look for ambiguous pronouns in directive context
        pronoun_pattern = r'\[(?:MUST|STRICT|GUIDELINE)\].*?(?:it|this|that|they|them)\s+(?:should|must|will)'
        matches = re.finditer(pronoun_pattern, content, re.IGNORECASE)
        
        for match in matches:
            pronoun_ambiguities.append({
                "type": "pronoun_ambiguity",
                "line_number": content[:match.start()].count('\n') + 1,
                "context": self._extract_context(content, match.start(), match.end()),
                "message": "Unclear pronoun reference in directive",
                "fix": "Replace pronouns with specific nouns",
                "protocol": "unknown"
            })
        
        return pronoun_ambiguities
    
    def _detect_completeness_issues(self, content: str, protocol_id: str) -> List[Dict[str, Any]]:
        """Detect completeness issues in instructions."""
        completeness_issues = []
        
        for pattern, issue_type in self.completeness_patterns:
            matches = list(re.finditer(pattern, content, re.IGNORECASE | re.DOTALL))
            
            for match in matches:
                completeness_issues.append({
                    "type": issue_type,
                    "pattern": pattern,
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end()),
                    "message": f"Incomplete instruction detected: {issue_type}",
                    "fix": "Add missing branches or error handling",
                    "protocol": protocol_id
                })
        
        # Check for missing error handling
        error_handling_issues = self._detect_missing_error_handling(content)
        completeness_issues.extend(error_handling_issues)
        
        return completeness_issues
    
    def _detect_missing_error_handling(self, content: str) -> List[Dict[str, Any]]:
        """Detect missing error handling in instructions."""
        error_handling_issues = []
        
        # Look for operations that should have error handling
        operation_patterns = [
            r'\[MUST\].*?(?:execute|run|perform|create|generate|write|save)',
            r'\[STRICT\].*?(?:execute|run|perform|create|generate|write|save)'
        ]
        
        for pattern in operation_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE | re.DOTALL)
            
            for match in matches:
                # Check if error handling exists in nearby context
                context = self._extract_context(content, match.start(), match.end(), context_lines=5)
                
                error_handling_patterns = [
                    r'if\s+(?:.*?)\s+(?:fails|error|exception)',
                    r'catch\s+(?:.*?)\s+(?:error|exception)',
                    r'handle\s+(?:.*?)\s+(?:error|failure)',
                    r'on\s+(?:.*?)\s+(?:error|failure)'
                ]
                
                has_error_handling = any(
                    re.search(error_pattern, context, re.IGNORECASE)
                    for error_pattern in error_handling_patterns
                )
                
                if not has_error_handling:
                    error_handling_issues.append({
                        "type": "missing_error_handling",
                        "line_number": content[:match.start()].count('\n') + 1,
                        "context": context,
                        "message": "Operation lacks error handling",
                        "fix": "Add error handling for operation",
                        "protocol": "unknown"
                    })
        
        return error_handling_issues
    
    def _extract_context(self, content: str, start: int, end: int, context_lines: int = 2) -> str:
        """Extract context around a match."""
        lines = content.split('\n')
        match_line = content[:start].count('\n')
        
        start_line = max(0, match_line - context_lines)
        end_line = min(len(lines), match_line + context_lines + 1)
        
        return '\n'.join(lines[start_line:end_line])
    
    def _extract_context_around_pattern(self, content: str, pattern: str, context_lines: int = 3) -> str:
        """Extract context around a specific pattern."""
        match = re.search(pattern, content, re.IGNORECASE)
        if not match:
            return ""
        
        return self._extract_context(content, match.start(), match.end(), context_lines)


def main():
    """Main entry point for instruction conflict detection."""
    parser = argparse.ArgumentParser(description="Detect instruction conflicts and ambiguities")
    parser.add_argument("--workspace", "-w", default=".", help="Workspace root directory")
    parser.add_argument("--output", "-o", help="Output file for detection results (JSON)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--protocol", "-p", help="Detect conflicts in specific protocol only")
    
    args = parser.parse_args()
    
    detector = InstructionConflictDetector(args.workspace)
    
    if args.protocol:
        # Detect conflicts in single protocol
        if args.protocol not in detector.protocols:
            print(f"Error: Protocol {args.protocol} not found")
            sys.exit(1)
        
        protocol_file = detector.dev_workflow_dir / detector.protocols[args.protocol]
        if not protocol_file.exists():
            print(f"Error: Protocol file {protocol_file} not found")
            sys.exit(1)
        
        content = protocol_file.read_text(encoding='utf-8')
        results = detector._detect_single_protocol_conflicts(args.protocol, content)
    else:
        # Detect conflicts in all protocols
        results = detector.detect_instruction_conflicts()
    
    # Output results
    if args.verbose or not args.output:
        print("🔍 Instruction Conflict Detection")
        print("=" * 50)
        print(f"Status: {results['status'].upper()}")
        
        if "summary" in results:
            print(f"Total Protocols: {results['summary']['total_protocols']}")
            print(f"Validated: {results['summary']['validated']}")
            print(f"Contradictions: {results['summary']['contradictions']}")
            print(f"Ambiguities: {results['summary']['ambiguities']}")
            print(f"Completeness Issues: {results['summary']['completeness_issues']}")
            print(f"Critical Issues: {results['summary']['critical_issues']}")
        
        if results.get("contradictions"):
            print("\n❌ Contradictions:")
            for contradiction in results["contradictions"]:
                print(f"  {contradiction['type']}: {contradiction['message']}")
        
        if results.get("ambiguities"):
            print("\n⚠️ Ambiguities:")
            for ambiguity in results["ambiguities"]:
                print(f"  {ambiguity['type']}: {ambiguity['message']}")
        
        if results.get("completeness_issues"):
            print("\n📝 Completeness Issues:")
            for issue in results["completeness_issues"]:
                print(f"  {issue['type']}: {issue['message']}")
    
    # Save to output file if specified
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Detection results saved to: {args.output}")
    
    # Exit with appropriate code
    if results["status"] == "fail":
        sys.exit(1)
    elif results["status"] == "warning":
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
