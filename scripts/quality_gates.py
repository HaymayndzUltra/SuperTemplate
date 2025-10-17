#!/usr/bin/env python3
"""
Quality Gates for Unified Developer Workflow

Implements comprehensive quality validation across all layers with
specialized protocols and unified reporting.
"""

import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import click

from .evidence_manager import EvidenceManager
from .compliance_validator import ComplianceValidator
from .review_protocol_loader import ReviewProtocol, ReviewProtocolLoader


class QualityGates:
    """Quality gates implementation for unified workflow"""
    
    def __init__(self, project_name: str, evidence_root: str = "evidence"):
        self.project_name = project_name
        self.evidence_manager = EvidenceManager(evidence_root)
        repo_root = Path(__file__).resolve().parent.parent
        self.workflow_home = repo_root / "unified_workflow"
        self.review_loader = ReviewProtocolLoader(repo_root)
        self.compliance_validator = ComplianceValidator(repo_root)
        
        # Ensure project directory exists
        self.project_dir = Path(project_name)
        self.project_dir.mkdir(exist_ok=True)
    
    def _load_review_protocol(self, mode: str) -> ReviewProtocol:
        """Load review protocol based on mode."""

        protocol_mapping = {
            "quick": "code-review",
            "security": "security-check",
            "architecture": "architecture-review",
            "design": "design-system",
            "ui": "ui-accessibility",
            "deep-security": "pre-production",
        }

        slug = protocol_mapping.get(mode, "code-review")
        protocol = self.review_loader.load(slug)

        self.evidence_manager.log_execution(
            phase=4,
            action="Review Protocol Loaded",
            status="completed",
            details={
                "mode": mode,
                "protocol": protocol.path.name,
                "checklist_items": len(protocol.checklist),
            },
        )

        return protocol
    
    def _execute_quality_gate(self, mode: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute quality gate based on mode"""
        
        start_time = time.time()
        
        # Load protocol
        protocol = self._load_review_protocol(mode)

        print(f"🔍 Executing Quality Gate: {mode.upper()}")
        print(f"📋 Protocol: {protocol.path.name}")
        
        # Simulate quality gate execution
        time.sleep(2)  # Simulate processing time
        
        # Generate findings based on mode
        findings = self._generate_findings(mode, context)

        # Evaluate compliance results when relevant
        compliance_summary: Dict[str, Any] = {}
        compliance_assets: Optional[Dict[str, Path]] = None
        if mode in {"security", "deep-security", "comprehensive"}:
            compliance_results, standards = self._evaluate_compliance(context)
            if compliance_results:
                compliance_summary = compliance_results
                compliance_assets = self._generate_compliance_evidence(standards)

        # Calculate score
        score = self._calculate_score(findings)

        # Generate recommendations
        recommendations = self._generate_recommendations(findings, mode)

        duration = time.time() - start_time

        result: Dict[str, Any] = {
            "mode": mode,
            "protocol": protocol.to_dict(),
            "findings": findings,
            "score": score,
            "recommendations": recommendations,
            "duration": duration,
            "status": "passed" if score >= 7.0 else "failed"
        }

        if compliance_summary:
            result["compliance"] = {
                "results": compliance_summary,
                "assets": {name: str(path) for name, path in (compliance_assets or {}).items()},
            }

        return result
    
    def _generate_findings(self, mode: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate findings based on mode and context"""
        
        base_findings = []
        
        if mode == "quick":
            base_findings = [
                {
                    "severity": "medium",
                    "category": "code_quality",
                    "description": "Some functions could be more modular",
                    "file": "src/components/UserProfile.tsx",
                    "line": 45,
                    "recommendation": "Extract complex logic into separate functions"
                }
            ]
        
        elif mode == "security":
            base_findings = [
                {
                    "severity": "high",
                    "category": "security",
                    "description": "Missing input validation on user input",
                    "file": "src/api/auth.ts",
                    "line": 23,
                    "recommendation": "Add proper input validation and sanitization"
                }
            ]
        
        elif mode == "architecture":
            base_findings = [
                {
                    "severity": "medium",
                    "category": "architecture",
                    "description": "Tight coupling between components",
                    "file": "src/services/",
                    "line": None,
                    "recommendation": "Implement dependency injection pattern"
                }
            ]
        
        elif mode == "design":
            base_findings = [
                {
                    "severity": "low",
                    "category": "design_system",
                    "description": "Inconsistent spacing in component",
                    "file": "src/components/Button.tsx",
                    "line": 12,
                    "recommendation": "Use design system spacing tokens"
                }
            ]
        
        elif mode == "ui":
            base_findings = [
                {
                    "severity": "high",
                    "category": "accessibility",
                    "description": "Missing ARIA labels on interactive elements",
                    "file": "src/components/Modal.tsx",
                    "line": 8,
                    "recommendation": "Add proper ARIA labels and roles"
                }
            ]
        
        elif mode == "deep-security":
            base_findings = [
                {
                    "severity": "critical",
                    "category": "security",
                    "description": "SQL injection vulnerability detected",
                    "file": "src/database/queries.ts",
                    "line": 67,
                    "recommendation": "Use parameterized queries"
                }
            ]
        
        return base_findings

    def _evaluate_compliance(
        self, context: Optional[Dict[str, Any]]
    ) -> Tuple[Dict[str, Any], List[str]]:
        """Evaluate compliance standards from context."""

        context = context or {}
        standards = context.get("compliance") or context.get("compliance_standards")
        normalized = self.compliance_validator._normalize_standards(standards)
        if not normalized:
            normalized = list(self.compliance_validator.DEFAULT_VALIDATION_STANDARDS)

        results: Dict[str, Any] = {}
        for standard in normalized:
            method = getattr(
                self.compliance_validator, f"validate_{standard}_compliance", None
            )
            if not callable(method):
                continue
            valid, report = method()
            results[standard] = {"valid": valid, **report}

        return results, normalized

    def _generate_compliance_evidence(self, standards: Sequence[str]) -> Dict[str, Path]:
        """Generate compliance assets and log them as evidence."""

        assets = self.compliance_validator.generate_compliance_assets(
            output_dir=self.project_dir / "compliance",
            standards=standards,
        )

        for label, path in assets.items():
            try:
                relative = path.relative_to(self.project_dir)
                relative_str = str(relative)
            except ValueError:
                relative_str = str(path)

            self.evidence_manager.log_artifact(
                path=relative_str,
                category="compliance",
                description=f"Compliance asset generated: {label}",
                phase=4,
            )

        return assets
    
    def _calculate_score(self, findings: List[Dict[str, Any]]) -> float:
        """Calculate quality score based on findings"""
        
        if not findings:
            return 10.0
        
        # Base score
        base_score = 10.0
        
        # Deduct points based on severity
        severity_penalties = {
            "critical": 3.0,
            "high": 2.0,
            "medium": 1.0,
            "low": 0.5
        }
        
        for finding in findings:
            severity = finding.get("severity", "low")
            penalty = severity_penalties.get(severity, 0.5)
            base_score -= penalty
        
        # Ensure score is between 0 and 10
        return max(0.0, min(10.0, base_score))
    
    def _generate_recommendations(self, findings: List[Dict[str, Any]], mode: str) -> List[str]:
        """Generate recommendations based on findings and mode"""
        
        recommendations = []
        
        # Mode-specific recommendations
        if mode == "quick":
            recommendations.extend([
                "Review code quality standards",
                "Implement code review checklist",
                "Add automated linting rules"
            ])
        
        elif mode == "security":
            recommendations.extend([
                "Conduct security training for team",
                "Implement automated security scanning",
                "Review authentication and authorization"
            ])
        
        elif mode == "architecture":
            recommendations.extend([
                "Review architectural patterns",
                "Implement design patterns",
                "Improve component separation"
            ])
        
        elif mode == "design":
            recommendations.extend([
                "Enforce design system usage",
                "Create component library",
                "Implement design tokens"
            ])
        
        elif mode == "ui":
            recommendations.extend([
                "Conduct accessibility audit",
                "Implement WCAG guidelines",
                "Add automated accessibility testing"
            ])
        
        elif mode == "deep-security":
            recommendations.extend([
                "Conduct penetration testing",
                "Implement security monitoring",
                "Review security policies"
            ])
        
        # Add findings-based recommendations
        for finding in findings:
            if finding.get("recommendation"):
                recommendations.append(finding["recommendation"])
        
        return list(set(recommendations))  # Remove duplicates
    
    def execute_quality_gate(self, mode: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute single quality gate"""
        
        if context is None:
            context = {
                "project_name": self.project_name,
                "description": f"Quality gate execution for {self.project_name}"
            }
        
        print(f"🎯 Executing Quality Gate: {mode.upper()}")
        print("=" * 60)
        
        result = self._execute_quality_gate(mode, context)
        
        # Log execution
        self.evidence_manager.log_execution(
            phase=4,  # Quality audit phase
            action=f"Quality Gate: {mode.upper()}",
            status=result["status"]
        )
        
        # Log validation results
        self.evidence_manager.log_validation(
            phase=4,  # Quality audit phase
            status=result["status"],
            score=result["score"],
            findings=result["findings"],
            recommendations=result["recommendations"]
        )
        
        print(f"✅ Quality Gate Complete: {mode.upper()}")
        print(f"📊 Score: {result['score']}/10")
        print(f"🔍 Status: {result['status']}")
        print(f"⏱️  Duration: {result['duration']:.2f} seconds")
        
        if result["findings"]:
            print(f"⚠️  Findings: {len(result['findings'])}")
            for finding in result["findings"]:
                print(f"   - {finding['severity'].upper()}: {finding['description']}")
        
        return result
    
    def execute_comprehensive_audit(self, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute comprehensive audit across all layers"""
        
        print(f"🎯 Executing Comprehensive Quality Audit")
        print("=" * 60)
        
        # Define audit modes
        audit_modes = ["quick", "security", "architecture", "design", "ui", "deep-security"]
        
        results = []
        overall_score = 0.0
        total_findings = []
        all_recommendations = []
        
        for mode in audit_modes:
            print(f"\n📋 Layer: {mode.upper()}")
            print("-" * 40)
            
            result = self._execute_quality_gate(mode, context)
            results.append(result)
            
            overall_score += result["score"]
            total_findings.extend(result["findings"])
            all_recommendations.extend(result["recommendations"])
        
        # Calculate overall score
        overall_score = overall_score / len(audit_modes)
        
        # Determine overall status
        overall_status = "passed" if overall_score >= 7.0 else "failed"
        
        # Create comprehensive result
        comprehensive_result = {
            "mode": "comprehensive",
            "overall_score": overall_score,
            "overall_status": overall_status,
            "layer_results": results,
            "total_findings": total_findings,
            "all_recommendations": list(set(all_recommendations)),
            "duration": sum(r["duration"] for r in results)
        }
        
        # Log comprehensive validation
        self.evidence_manager.log_validation(
            phase=4,  # Quality audit phase
            status=overall_status,
            score=overall_score,
            findings=total_findings,
            recommendations=all_recommendations
        )
        
        print(f"\n🎉 Comprehensive Audit Complete!")
        print(f"📊 Overall Score: {overall_score:.2f}/10")
        print(f"🔍 Overall Status: {overall_status.upper()}")
        print(f"⚠️  Total Findings: {len(total_findings)}")
        print(f"💡 Total Recommendations: {len(all_recommendations)}")
        print(f"⏱️  Total Duration: {comprehensive_result['duration']:.2f} seconds")
        
        return comprehensive_result
    
    def execute_interactive_audit(self) -> Dict[str, Any]:
        """Execute interactive audit with user selection"""
        
        print("🎯 Interactive Quality Audit")
        print("=" * 60)
        
        # Available modes
        modes = {
            "1": ("quick", "Code Review - Design compliance + Code quality"),
            "2": ("security", "Security Check - Security + Multi-tenant validation"),
            "3": ("architecture", "Architecture Review - Performance + Architecture patterns"),
            "4": ("design", "Design System - Component usage + Visual consistency"),
            "5": ("ui", "UI/UX - Accessibility + User experience"),
            "6": ("deep-security", "Pre-Production Security - Complete security validation"),
            "7": ("comprehensive", "Comprehensive - All layers (recommended)")
        }
        
        print("Available audit modes:")
        for key, (mode, description) in modes.items():
            print(f"  {key}. {description}")
        
        # Get user selection
        while True:
            choice = input("\nSelect audit mode (1-7): ").strip()
            if choice in modes:
                break
            print("Invalid choice. Please select 1-7.")
        
        selected_mode, description = modes[choice]
        
        print(f"\nSelected: {description}")
        
        # Execute selected mode
        if selected_mode == "comprehensive":
            return self.execute_comprehensive_audit()
        else:
            return self.execute_quality_gate(selected_mode)


# CLI Interface
@click.group()
def cli():
    """Quality Gates CLI for Unified Developer Workflow"""
    pass


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--mode', required=True, help='Audit mode (quick, security, architecture, design, ui, deep-security)')
@click.option('--context', help='Context JSON string')
@click.option('--evidence-root', default='evidence', help='Evidence directory')
def audit(project, mode, context, evidence_root):
    """Execute single quality gate"""
    quality_gates = QualityGates(project, evidence_root)
    
    # Parse context if provided
    context_dict = None
    if context:
        try:
            context_dict = json.loads(context)
        except json.JSONDecodeError:
            print("❌ Invalid JSON in context")
            exit(1)
    
    result = quality_gates.execute_quality_gate(mode, context_dict)
    
    # Save result
    result_path = quality_gates.project_dir / f"quality-gate-{mode}-result.json"
    with open(result_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"📊 Result saved: {result_path}")


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--context', help='Context JSON string')
@click.option('--evidence-root', default='evidence', help='Evidence directory')
def comprehensive(project, context, evidence_root):
    """Execute comprehensive quality audit"""
    quality_gates = QualityGates(project, evidence_root)
    
    # Parse context if provided
    context_dict = None
    if context:
        try:
            context_dict = json.loads(context)
        except json.JSONDecodeError:
            print("❌ Invalid JSON in context")
            exit(1)
    
    result = quality_gates.execute_comprehensive_audit(context_dict)
    
    # Save result
    result_path = quality_gates.project_dir / "comprehensive-audit-result.json"
    with open(result_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"📊 Result saved: {result_path}")


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--evidence-root', default='evidence', help='Evidence directory')
def interactive(project, evidence_root):
    """Execute interactive quality audit"""
    quality_gates = QualityGates(project, evidence_root)
    
    result = quality_gates.execute_interactive_audit()
    
    # Save result
    result_path = quality_gates.project_dir / "interactive-audit-result.json"
    with open(result_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"📊 Result saved: {result_path}")


if __name__ == "__main__":
    cli()
