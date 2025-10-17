#!/usr/bin/env python3
"""
Comprehensive Consistency Report Generator

Generates comprehensive consistency report across all protocols:
- Protocol flow map
- Directive consistency matrix
- AI persona transitions
- Instruction conflict report
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from datetime import datetime


class ConsistencyReportGenerator:
    """Generates comprehensive consistency reports."""
    
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
        
        # Protocol metadata
        self.protocol_metadata = {
            "00": {
                "name": "Client Discovery",
                "ai_persona": "Client Discovery Specialist",
                "purpose": "Convert job posts into structured project briefs",
                "outputs": ["brief.md", "acceptance-criteria.md", "risks.md"],
                "next_protocol": "0"
            },
            "0": {
                "name": "Bootstrap",
                "ai_persona": "Project Analyst",
                "purpose": "Analyze codebase and configure framework",
                "outputs": ["context-kit", "project-structure"],
                "next_protocol": "1"
            },
            "1": {
                "name": "PRD Creation",
                "ai_persona": "Product Manager",
                "purpose": "Create implementation-ready PRD",
                "outputs": ["PRD", "implementation-ready-prd"],
                "next_protocol": "2"
            },
            "2": {
                "name": "Task Generation",
                "ai_persona": "Tech Lead",
                "purpose": "Transform PRD into execution plan",
                "outputs": ["tasks", "execution-plan"],
                "next_protocol": "3"
            },
            "3": {
                "name": "Task Processing",
                "ai_persona": "Paired Developer",
                "purpose": "Execute tasks and generate artifacts",
                "outputs": ["artifacts", "test-results", "coverage"],
                "next_protocol": "4"
            },
            "4": {
                "name": "Quality Audit",
                "ai_persona": "Senior Quality Engineer",
                "purpose": "Orchestrate quality audits",
                "outputs": ["audit-report", "quality-gates"],
                "next_protocol": "5"
            },
            "5": {
                "name": "Implementation Retrospective",
                "ai_persona": "Process Improvement Lead",
                "purpose": "Conduct retrospectives and improvements",
                "outputs": ["retrospective-report", "improvements"],
                "next_protocol": None
            }
        }
    
    def generate_consistency_report(self) -> Dict[str, Any]:
        """Generate comprehensive consistency report."""
        report = {
            "generated_at": datetime.now().isoformat(),
            "workspace": str(self.workspace_root),
            "summary": {
                "total_protocols": len(self.protocols),
                "analyzed": 0,
                "consistency_score": 0.0,
                "critical_issues": 0,
                "warnings": 0
            },
            "protocol_flow_map": {},
            "directive_consistency_matrix": {},
            "ai_persona_transitions": {},
            "instruction_conflict_report": {},
            "handoff_alignment": {},
            "execution_simulation": {},
            "recommendations": [],
            "issues": []
        }
        
        # Analyze each protocol
        protocol_data = {}
        for protocol_id, protocol_file in self.protocols.items():
            protocol_path = self.dev_workflow_dir / protocol_file
            
            if not protocol_path.exists():
                report["issues"].append({
                    "severity": "critical",
                    "protocol": f"protocol_{protocol_id}",
                    "message": f"Protocol file not found: {protocol_file}",
                    "fix": f"Create {protocol_path}"
                })
                continue
            
            try:
                content = protocol_path.read_text(encoding='utf-8')
                protocol_analysis = self._analyze_protocol(protocol_id, content)
                protocol_data[protocol_id] = protocol_analysis
                report["summary"]["analyzed"] += 1
                
            except Exception as e:
                report["issues"].append({
                    "severity": "critical",
                    "protocol": f"protocol_{protocol_id}",
                    "message": f"Cannot analyze protocol: {str(e)}",
                    "fix": "Check file permissions and encoding"
                })
        
        # Generate report sections
        report["protocol_flow_map"] = self._generate_protocol_flow_map(protocol_data)
        report["directive_consistency_matrix"] = self._generate_directive_matrix(protocol_data)
        report["ai_persona_transitions"] = self._generate_persona_transitions(protocol_data)
        report["instruction_conflict_report"] = self._generate_conflict_report(protocol_data)
        report["handoff_alignment"] = self._generate_handoff_alignment(protocol_data)
        report["execution_simulation"] = self._generate_execution_simulation(protocol_data)
        
        # Calculate overall consistency score
        report["summary"]["consistency_score"] = self._calculate_consistency_score(report)
        
        # Generate recommendations
        report["recommendations"] = self._generate_recommendations(report)
        
        return report
    
    def _analyze_protocol(self, protocol_id: str, content: str) -> Dict[str, Any]:
        """Analyze a single protocol for consistency."""
        analysis = {
            "protocol_id": protocol_id,
            "metadata": self.protocol_metadata.get(protocol_id, {}),
            "steps": self._extract_steps(content),
            "phases": self._extract_phases(content),
            "directives": self._extract_directives(content),
            "persona_info": self._extract_persona_info(content),
            "gates": self._extract_gates(content),
            "outputs": self._extract_outputs(content),
            "handoff_instructions": self._extract_handoff_instructions(content),
            "automation_hooks": self._extract_automation_hooks(content),
            "issues": []
        }
        
        return analysis
    
    def _extract_steps(self, content: str) -> List[Dict[str, Any]]:
        """Extract steps from protocol content."""
        steps = []
        
        step_pattern = r'###\s*STEP\s+(\d+(?:\.\d+)*):\s*(.*)'
        
        for match in re.finditer(step_pattern, content, re.IGNORECASE):
            steps.append({
                "number": match.group(1),
                "title": match.group(2).strip(),
                "line_number": content[:match.start()].count('\n') + 1
            })
        
        return sorted(steps, key=lambda x: [int(part) for part in x["number"].split('.')])
    
    def _extract_phases(self, content: str) -> List[Dict[str, Any]]:
        """Extract phases from protocol content."""
        phases = []
        
        phase_pattern = r'###\s*PHASE\s+(\d+(?:\.\d+)*):\s*(.*)'
        
        for match in re.finditer(phase_pattern, content, re.IGNORECASE):
            phases.append({
                "number": match.group(1),
                "title": match.group(2).strip(),
                "line_number": content[:match.start()].count('\n') + 1
            })
        
        return sorted(phases, key=lambda x: [int(part) for part in x["number"].split('.')])
    
    def _extract_directives(self, content: str) -> Dict[str, List[Dict[str, Any]]]:
        """Extract directives from protocol content."""
        directives = {
            "MUST": [],
            "GUIDELINE": [],
            "STRICT": [],
            "CRITICAL": [],
            "REQUIRED": [],
            "OPTIONAL": []
        }
        
        directive_patterns = {
            "MUST": r'\[MUST\]',
            "GUIDELINE": r'\[GUIDELINE\]',
            "STRICT": r'\[STRICT\]',
            "CRITICAL": r'\[CRITICAL\]',
            "REQUIRED": r'\[REQUIRED\]',
            "OPTIONAL": r'\[OPTIONAL\]'
        }
        
        for tag, pattern in directive_patterns.items():
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                directives[tag].append({
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                })
        
        return directives
    
    def _extract_persona_info(self, content: str) -> Dict[str, Any]:
        """Extract AI persona information."""
        persona_info = {
            "declared": None,
            "role_mentions": [],
            "capabilities": []
        }
        
        # Look for AI Persona section
        persona_pattern = r'##\s*AI\s+Persona\s*\n(.*?)(?=\n##|\n---|\Z)'
        match = re.search(persona_pattern, content, re.IGNORECASE | re.DOTALL)
        
        if match:
            persona_info["declared"] = {
                "content": match.group(1).strip(),
                "line_number": content[:match.start()].count('\n') + 1
            }
        
        # Look for role mentions
        role_pattern = r'(?:Role|Act as|You are)\s*:?\s*(.*?)(?:\n|$)'
        role_matches = re.finditer(role_pattern, content, re.IGNORECASE)
        
        for match in role_matches:
            persona_info["role_mentions"].append({
                "content": match.group(1).strip(),
                "line_number": content[:match.start()].count('\n') + 1
            })
        
        return persona_info
    
    def _extract_gates(self, content: str) -> List[Dict[str, Any]]:
        """Extract gates from protocol content."""
        gates = []
        
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
    
    def _extract_outputs(self, content: str) -> List[Dict[str, Any]]:
        """Extract outputs from protocol content."""
        outputs = []
        
        output_patterns = [
            r'generate\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))',
            r'create\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))',
            r'output\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))',
            r'produce\s+(?:a\s+)?([a-zA-Z0-9\-_]+\.(?:md|json|yaml|yml|txt))'
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
        """Extract handoff instructions."""
        instructions = []
        
        handoff_patterns = [
            r'handoff\s+(?:to\s+)?(?:protocol\s+)?(\d+)',
            r'proceed\s+(?:to\s+)?(?:protocol\s+)?(\d+)',
            r'continue\s+(?:to\s+)?(?:protocol\s+)?(\d+)',
            r'next\s+(?:protocol\s+)?(\d+)'
        ]
        
        for pattern in handoff_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                instructions.append({
                    "target": match.group(1) if match.groups() else None,
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                })
        
        return instructions
    
    def _extract_automation_hooks(self, content: str) -> List[Dict[str, Any]]:
        """Extract automation hooks."""
        hooks = []
        
        automation_patterns = [
            r'\[AUTOMATION\]',
            r'automation\s+hook',
            r'script\s+execution',
            r'workflow\s+integration'
        ]
        
        for pattern in automation_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                hooks.append({
                    "type": "automation",
                    "line_number": content[:match.start()].count('\n') + 1,
                    "context": self._extract_context(content, match.start(), match.end())
                })
        
        return hooks
    
    def _extract_context(self, content: str, start: int, end: int, context_lines: int = 2) -> str:
        """Extract context around a match."""
        lines = content.split('\n')
        match_line = content[:start].count('\n')
        
        start_line = max(0, match_line - context_lines)
        end_line = min(len(lines), match_line + context_lines + 1)
        
        return '\n'.join(lines[start_line:end_line])
    
    def _generate_protocol_flow_map(self, protocol_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate protocol flow map."""
        flow_map = {
            "protocols": {},
            "transitions": [],
            "automation_points": [],
            "gate_checkpoints": []
        }
        
        for protocol_id, data in protocol_data.items():
            metadata = data["metadata"]
            flow_map["protocols"][protocol_id] = {
                "name": metadata.get("name", f"Protocol {protocol_id}"),
                "ai_persona": metadata.get("ai_persona", "Unknown"),
                "purpose": metadata.get("purpose", "Unknown"),
                "steps_count": len(data["steps"]),
                "phases_count": len(data["phases"]),
                "gates_count": len(data["gates"]),
                "outputs_count": len(data["outputs"]),
                "automation_hooks_count": len(data["automation_hooks"])
            }
            
            # Add transitions
            next_protocol = metadata.get("next_protocol")
            if next_protocol:
                flow_map["transitions"].append({
                    "from": protocol_id,
                    "to": next_protocol,
                    "handoff_instructions": len(data["handoff_instructions"])
                })
            
            # Add automation points
            if data["automation_hooks"]:
                flow_map["automation_points"].append({
                    "protocol": protocol_id,
                    "hooks": len(data["automation_hooks"])
                })
            
            # Add gate checkpoints
            if data["gates"]:
                flow_map["gate_checkpoints"].append({
                    "protocol": protocol_id,
                    "gates": len(data["gates"])
                })
        
        return flow_map
    
    def _generate_directive_matrix(self, protocol_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate directive consistency matrix."""
        matrix = {
            "total_usage": {},
            "protocol_usage": {},
            "consistency_scores": {},
            "issues": []
        }
        
        # Count total usage
        total_directives = {tag: 0 for tag in ["MUST", "GUIDELINE", "STRICT", "CRITICAL", "REQUIRED", "OPTIONAL"]}
        
        for protocol_id, data in protocol_data.items():
            protocol_usage = {}
            for tag, occurrences in data["directives"].items():
                count = len(occurrences)
                protocol_usage[tag] = count
                total_directives[tag] += count
            
            matrix["protocol_usage"][protocol_id] = protocol_usage
        
        matrix["total_usage"] = total_directives
        
        # Calculate consistency scores
        total_count = sum(total_directives.values())
        if total_count > 0:
            for tag, count in total_directives.items():
                matrix["consistency_scores"][tag] = count / total_count
        
        # Check for inconsistencies
        must_count = total_directives["MUST"]
        guideline_count = total_directives["GUIDELINE"]
        
        if must_count > 0 and guideline_count > 0:
            ratio = must_count / guideline_count
            if ratio < 0.5 or ratio > 2.0:
                matrix["issues"].append({
                    "type": "directive_balance",
                    "message": f"MUST/GUIDELINE ratio is {ratio:.2f}",
                    "recommendation": "Review directive usage for appropriate balance"
                })
        
        return matrix
    
    def _generate_persona_transitions(self, protocol_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate AI persona transition analysis."""
        transitions = {
            "persona_map": {},
            "transition_points": [],
            "consistency_issues": [],
            "capability_gaps": []
        }
        
        for protocol_id, data in protocol_data.items():
            metadata = data["metadata"]
            persona_info = data["persona_info"]
            
            transitions["persona_map"][protocol_id] = {
                "declared_persona": metadata.get("ai_persona", "Unknown"),
                "has_declaration": persona_info["declared"] is not None,
                "role_mentions": len(persona_info["role_mentions"]),
                "capabilities": len(persona_info["capabilities"])
            }
            
            # Check for persona declaration
            if not persona_info["declared"]:
                transitions["consistency_issues"].append({
                    "protocol": protocol_id,
                    "issue": "Missing AI persona declaration",
                    "severity": "warning"
                })
        
        # Generate transition points
        for protocol_id, data in protocol_data.items():
            metadata = data["metadata"]
            next_protocol = metadata.get("next_protocol")
            
            if next_protocol and next_protocol in protocol_data:
                current_persona = metadata.get("ai_persona", "Unknown")
                next_metadata = protocol_data[next_protocol]["metadata"]
                next_persona = next_metadata.get("ai_persona", "Unknown")
                
                transitions["transition_points"].append({
                    "from_protocol": protocol_id,
                    "to_protocol": next_protocol,
                    "from_persona": current_persona,
                    "to_persona": next_persona,
                    "persona_change": current_persona != next_persona,
                    "handoff_clarity": len(data["handoff_instructions"]) > 0
                })
        
        return transitions
    
    def _generate_conflict_report(self, protocol_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate instruction conflict report."""
        conflict_report = {
            "contradictions": [],
            "ambiguities": [],
            "completeness_issues": [],
            "total_conflicts": 0
        }
        
        # This would integrate with the conflict detection script
        # For now, provide a basic structure
        for protocol_id, data in protocol_data.items():
            # Check for basic contradictions
            must_directives = data["directives"]["MUST"]
            strict_directives = data["directives"]["STRICT"]
            
            if len(must_directives) > 0 and len(strict_directives) > 0:
                # Check for potential conflicts
                for must_directive in must_directives:
                    for strict_directive in strict_directives:
                        if self._check_directive_conflict(must_directive["context"], strict_directive["context"]):
                            conflict_report["contradictions"].append({
                                "protocol": protocol_id,
                                "type": "must_strict_conflict",
                                "message": "Potential conflict between MUST and STRICT directives",
                                "severity": "warning"
                            })
        
        conflict_report["total_conflicts"] = (
            len(conflict_report["contradictions"]) +
            len(conflict_report["ambiguities"]) +
            len(conflict_report["completeness_issues"])
        )
        
        return conflict_report
    
    def _check_directive_conflict(self, context1: str, context2: str) -> bool:
        """Check if two directive contexts conflict."""
        # Simple conflict detection - could be enhanced
        negative_words = ["skip", "ignore", "avoid", "never", "not"]
        positive_words = ["execute", "run", "perform", "always", "must"]
        
        context1_lower = context1.lower()
        context2_lower = context2.lower()
        
        has_negative1 = any(word in context1_lower for word in negative_words)
        has_positive1 = any(word in context1_lower for word in positive_words)
        has_negative2 = any(word in context2_lower for word in negative_words)
        has_positive2 = any(word in context2_lower for word in positive_words)
        
        return (has_negative1 and has_positive2) or (has_positive1 and has_negative2)
    
    def _generate_handoff_alignment(self, protocol_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate handoff alignment analysis."""
        alignment = {
            "handoff_map": {},
            "alignment_scores": {},
            "issues": []
        }
        
        for protocol_id, data in protocol_data.items():
            metadata = data["metadata"]
            next_protocol = metadata.get("next_protocol")
            
            if next_protocol and next_protocol in protocol_data:
                current_outputs = metadata.get("outputs", [])
                next_metadata = protocol_data[next_protocol]["metadata"]
                next_inputs = self._infer_next_inputs(next_protocol, next_metadata)
                
                alignment_score = self._calculate_alignment_score(current_outputs, next_inputs)
                
                alignment["handoff_map"][f"{protocol_id}→{next_protocol}"] = {
                    "outputs": current_outputs,
                    "inputs": next_inputs,
                    "alignment_score": alignment_score,
                    "handoff_instructions": len(data["handoff_instructions"])
                }
                
                alignment["alignment_scores"][f"{protocol_id}→{next_protocol}"] = alignment_score
                
                if alignment_score < 0.7:
                    alignment["issues"].append({
                        "handoff": f"{protocol_id}→{next_protocol}",
                        "score": alignment_score,
                        "message": "Weak output-input alignment",
                        "severity": "warning"
                    })
        
        return alignment
    
    def _infer_next_inputs(self, protocol_id: str, metadata: Dict[str, Any]) -> List[str]:
        """Infer inputs for next protocol."""
        # This is a simplified inference - could be enhanced
        input_mapping = {
            "0": ["project overview", "requirements", "context"],
            "1": ["architecture context", "project setup"],
            "2": ["prd", "requirements"],
            "3": ["tasks", "execution plan"],
            "4": ["artifacts", "test results"],
            "5": ["audit report", "quality gates"]
        }
        
        return input_mapping.get(protocol_id, [])
    
    def _calculate_alignment_score(self, outputs: List[str], inputs: List[str]) -> float:
        """Calculate alignment score between outputs and inputs."""
        if not outputs or not inputs:
            return 0.0
        
        # Simple keyword matching
        output_keywords = set()
        for output in outputs:
            output_keywords.update(output.lower().replace('-', ' ').split())
        
        input_keywords = set()
        for input_item in inputs:
            input_keywords.update(input_item.lower().replace('-', ' ').split())
        
        overlap = len(output_keywords.intersection(input_keywords))
        total = len(output_keywords.union(input_keywords))
        
        return overlap / total if total > 0 else 0.0
    
    def _generate_execution_simulation(self, protocol_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate execution simulation summary."""
        simulation = {
            "protocol_simulations": {},
            "overall_success_rate": 0.0,
            "common_failure_points": [],
            "recommendations": []
        }
        
        total_protocols = len(protocol_data)
        successful_simulations = 0
        
        for protocol_id, data in protocol_data.items():
            # Simulate basic execution
            steps_count = len(data["steps"])
            gates_count = len(data["gates"])
            automation_hooks = len(data["automation_hooks"])
            
            # Simple success criteria
            has_steps = steps_count > 0
            has_gates = gates_count > 0
            has_handoffs = len(data["handoff_instructions"]) > 0
            
            simulation_success = has_steps and has_gates and has_handoffs
            
            simulation["protocol_simulations"][protocol_id] = {
                "steps_count": steps_count,
                "gates_count": gates_count,
                "automation_hooks": automation_hooks,
                "simulation_success": simulation_success,
                "success_factors": {
                    "has_steps": has_steps,
                    "has_gates": has_gates,
                    "has_handoffs": has_handoffs
                }
            }
            
            if simulation_success:
                successful_simulations += 1
            else:
                simulation["common_failure_points"].append({
                    "protocol": protocol_id,
                    "issues": [
                        "Missing steps" if not has_steps else None,
                        "Missing gates" if not has_gates else None,
                        "Missing handoffs" if not has_handoffs else None
                    ]
                })
        
        simulation["overall_success_rate"] = successful_simulations / total_protocols if total_protocols > 0 else 0.0
        
        return simulation
    
    def _calculate_consistency_score(self, report: Dict[str, Any]) -> float:
        """Calculate overall consistency score."""
        scores = []
        
        # Directive consistency score
        directive_matrix = report["directive_consistency_matrix"]
        if directive_matrix["consistency_scores"]:
            directive_score = sum(directive_matrix["consistency_scores"].values()) / len(directive_matrix["consistency_scores"])
            scores.append(directive_score)
        
        # Handoff alignment score
        handoff_alignment = report["handoff_alignment"]
        if handoff_alignment["alignment_scores"]:
            alignment_score = sum(handoff_alignment["alignment_scores"].values()) / len(handoff_alignment["alignment_scores"])
            scores.append(alignment_score)
        
        # Execution simulation score
        execution_simulation = report["execution_simulation"]
        scores.append(execution_simulation["overall_success_rate"])
        
        return sum(scores) / len(scores) if scores else 0.0
    
    def _generate_recommendations(self, report: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate actionable recommendations."""
        recommendations = []
        
        # Directive recommendations
        directive_matrix = report["directive_consistency_matrix"]
        if directive_matrix["issues"]:
            for issue in directive_matrix["issues"]:
                recommendations.append({
                    "category": "directives",
                    "priority": "medium",
                    "recommendation": issue["recommendation"],
                    "impact": "Improve directive consistency"
                })
        
        # Handoff recommendations
        handoff_alignment = report["handoff_alignment"]
        if handoff_alignment["issues"]:
            for issue in handoff_alignment["issues"]:
                recommendations.append({
                    "category": "handoffs",
                    "priority": "high",
                    "recommendation": f"Improve handoff alignment for {issue['handoff']}",
                    "impact": "Better protocol transitions"
                })
        
        # Persona recommendations
        persona_transitions = report["ai_persona_transitions"]
        if persona_transitions["consistency_issues"]:
            for issue in persona_transitions["consistency_issues"]:
                recommendations.append({
                    "category": "personas",
                    "priority": "medium",
                    "recommendation": f"Add AI persona declaration to {issue['protocol']}",
                    "impact": "Clearer AI role definition"
                })
        
        return recommendations


def main():
    """Main entry point for consistency report generation."""
    parser = argparse.ArgumentParser(description="Generate comprehensive consistency report")
    parser.add_argument("--workspace", "-w", default=".", help="Workspace root directory")
    parser.add_argument("--output", "-o", help="Output file for report (JSON)")
    parser.add_argument("--markdown", "-m", help="Output file for markdown report")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    generator = ConsistencyReportGenerator(args.workspace)
    report = generator.generate_consistency_report()
    
    # Output results
    if args.verbose or not args.output:
        print("🔍 Comprehensive Consistency Report")
        print("=" * 50)
        print(f"Generated: {report['generated_at']}")
        print(f"Workspace: {report['workspace']}")
        print(f"Consistency Score: {report['summary']['consistency_score']:.2f}")
        print(f"Protocols Analyzed: {report['summary']['analyzed']}")
        print(f"Critical Issues: {report['summary']['critical_issues']}")
        print(f"Warnings: {report['summary']['warnings']}")
        
        if report["recommendations"]:
            print("\n📋 Recommendations:")
            for rec in report["recommendations"]:
                print(f"  {rec['priority'].upper()}: {rec['recommendation']}")
    
    # Save JSON report
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"Consistency report saved to: {args.output}")
    
    # Generate markdown report
    if args.markdown:
        markdown_content = generator._generate_markdown_report(report)
        with open(args.markdown, 'w') as f:
            f.write(markdown_content)
        print(f"Markdown report saved to: {args.markdown}")
    
    # Exit with appropriate code
    if report["summary"]["critical_issues"] > 0:
        sys.exit(1)
    elif report["summary"]["warnings"] > 0:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
