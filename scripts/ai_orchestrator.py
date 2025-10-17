#!/usr/bin/env python3
"""
AI Orchestrator for Unified Developer Workflow

Orchestrates AI execution of individual phases with context management,
rule compliance, and evidence tracking.
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import click

from .evidence_manager import EvidenceManager
from .external_services import ExternalServicesManager


class AIOrchestrator:
    """AI orchestrator for individual phase execution"""
    
    def __init__(self, project_name: str, evidence_root: str = "evidence"):
        self.project_name = project_name
        self.evidence_manager = EvidenceManager(evidence_root)
        repo_root = Path(__file__).resolve().parent.parent
        self.workflow_home = repo_root / "unified_workflow"
        self.phases_dir = self.workflow_home / "phases"

        # Ensure project directory exists
        self.project_dir = Path(project_name)
        self.project_dir.mkdir(exist_ok=True)

        # Load project configuration
        self.config = self._load_project_config()
        self.external_services = ExternalServicesManager(self.project_dir)
    
    def _load_project_config(self) -> Dict[str, Any]:
        """Load project configuration"""
        config_path = self.project_dir / "project-config.json"
        
        if config_path.exists():
            with open(config_path, 'r') as f:
                return json.load(f)
        else:
            # Default configuration
            config = {
                "project": {
                    "name": self.project_name,
                    "type": "web-app",
                    "industry": "saas",
                    "stack": {
                        "frontend": "react",
                        "backend": "nodejs",
                        "database": "postgresql",
                        "auth": "auth0",
                        "deploy": "vercel",
                    },
                    "compliance": ["gdpr"],
                },
                "workflow": {
                    "version": "1.0.0",
                    "evidence_root": "evidence"
                }
            }
            
            # Save default configuration
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=2)
            
            return config
    
    def _load_phase_protocol(self, phase_file: str) -> str:
        """Load phase protocol content"""
        phase_path = self.phases_dir / phase_file
        
        if not phase_path.exists():
            raise FileNotFoundError(f"Phase protocol not found: {phase_file}")
        
        with open(phase_path, 'r') as f:
            return f.read()
    
    def _build_governor_payload(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a payload for AI Governor validation."""

        project_config = self.config.get("project", {})
        stack = project_config.get("stack", {})

        if isinstance(stack, list):
            stack = {
                "frontend": stack[0] if stack else None,
                "backend": stack[1] if len(stack) > 1 else None,
                "database": stack[2] if len(stack) > 2 else None,
            }

        payload = {
            "name": project_config.get("name", self.project_name),
            "industry": project_config.get("industry", context.get("industry", "saas")),
            "project_type": project_config.get("type", context.get("project_type", "fullstack")),
            "stack": stack,
            "compliance": context.get("compliance") or project_config.get("compliance", []),
        }

        return payload

    def _prepare_phase_integrations(self, phase: int, phase_name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare external integrations for a phase."""

        services = self.external_services.get_phase_services(phase)
        summary: Dict[str, Any] = {}

        git_service = services.get("git")
        if git_service:
            git_summary: Dict[str, Any] = {"validation": git_service.validate()}
            if not git_summary["validation"].get("repository_initialized"):
                initialized = git_service.initialize_repository()
                git_summary["initialized"] = initialized
                self.evidence_manager.log_execution(
                    phase=phase,
                    action="Git Repository Initialization",
                    status="completed" if initialized else "failed",
                    details={"phase_name": phase_name},
                )
            summary["git"] = git_summary

        governor_service = services.get("ai_governor")
        if governor_service:
            payload = self._build_governor_payload(context)
            validation = governor_service.validate_project_config(payload)
            summary["ai_governor"] = validation
            self.evidence_manager.log_execution(
                phase=phase,
                action="AI Governor Policy Check",
                status="completed" if validation.get("valid", True) else "failed",
                details=validation,
            )

            if phase == 0:
                copied_rules = governor_service.copy_master_rules(self.project_dir)
                summary["ai_governor"]["copied_rules"] = copied_rules

        policy_service = services.get("policy_dsl")
        if policy_service:
            bundle_info = policy_service.ensure_policy_bundle()
            available = policy_service.available_policies()
            summary["policy_dsl"] = {
                "bundle": bundle_info,
                "available_policies": available,
            }
            self.evidence_manager.log_execution(
                phase=phase,
                action="Policy DSL Prepared",
                status="completed",
                details={"available_policies": available},
            )

        return summary

    def _finalize_phase_integrations(self, phase: int, phase_name: str, execution_result: Dict[str, Any], summary: Dict[str, Any]) -> None:
        """Finalize integrations after phase execution."""

        services = self.external_services.get_phase_services(phase)
        git_service = services.get("git")

        if (
            git_service
            and execution_result.get("status") == "success"
            and execution_result.get("outputs", {}).get("artifacts")
        ):
            commit_message = f"Phase {phase}: {phase_name} deliverables"
            committed = git_service.commit_phase_artifacts(phase, commit_message)
            summary.setdefault("git", {})["commit"] = {
                "message": commit_message,
                "committed": committed,
            }
            self.evidence_manager.log_execution(
                phase=phase,
                action="Git Commit",
                status="completed" if committed else "failed",
                details={"message": commit_message},
            )

    def _print_service_summary(self, summary: Dict[str, Any]) -> None:
        """Pretty print external service summary."""

        if not summary:
            return

        print("🔗 External Services Summary:")
        print(json.dumps(summary, indent=2))

    def _execute_ai_phase(self, phase: int, phase_name: str, phase_file: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute AI phase with context and rules"""
        start_time = time.time()
        
        # Log phase start
        self.evidence_manager.log_execution(
            phase=phase,
            action=f"AI Start {phase_name}",
            status="started",
            details={"phase_name": phase_name, "context": context}
        )
        
        service_summary = self._prepare_phase_integrations(phase, phase_name, context)

        try:
            # Load phase protocol
            protocol_content = self._load_phase_protocol(phase_file)
            
            print(f"🤖 AI Executing Phase {phase}: {phase_name}")
            print(f"📋 Protocol: {phase_file}")
            print(f"🎯 Context: {context.get('description', 'No description')}")
            
            # Simulate AI execution based on phase type
            result = self._simulate_ai_execution(phase, phase_name, protocol_content, context)
            
            # Log artifacts
            for artifact in result.get("artifacts", []):
                self.evidence_manager.log_artifact(
                    path=artifact["path"],
                    category=artifact["category"],
                    description=artifact["description"],
                    phase=phase
                )
            
            # Log validation results
            if result.get("validation"):
                validation = result["validation"]
                self.evidence_manager.log_validation(
                    phase=phase,
                    status=validation["status"],
                    score=validation["score"],
                    findings=validation["findings"],
                    recommendations=validation["recommendations"]
                )
            
            duration = time.time() - start_time
            self.evidence_manager.log_execution(
                phase=phase,
                action=f"AI Complete {phase_name}",
                status="completed",
                duration_seconds=duration
            )
            
            result_payload = {
                "status": "success",
                "phase": phase,
                "phase_name": phase_name,
                "ai_role": result.get("ai_role", "AI Assistant"),
                "outputs": result,
                "duration": duration,
            }

            self._finalize_phase_integrations(phase, phase_name, result_payload, service_summary)
            result_payload["external_services"] = service_summary

            return result_payload

        except Exception as e:
            duration = time.time() - start_time
            self.evidence_manager.log_execution(
                phase=phase,
                action=f"AI Failed {phase_name}",
                status="failed",
                duration_seconds=duration,
                details={"error": str(e)}
            )
            
            error_result = {
                "status": "error",
                "phase": phase,
                "phase_name": phase_name,
                "error": str(e),
                "duration": duration,
            }
            error_result["external_services"] = service_summary

            return error_result
    
    def _simulate_ai_execution(self, phase: int, phase_name: str, protocol_content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate AI execution based on phase protocol"""
        
        # Extract AI role from protocol
        ai_role = "AI Assistant"
        if "AI Role" in protocol_content:
            lines = protocol_content.split('\n')
            for line in lines:
                if line.startswith("**") and "Role" in line:
                    ai_role = line.replace("**", "").replace("*", "").strip()
                    break
        
        # Simulate processing time based on phase complexity
        processing_time = {
            0: 2,  # Bootstrap - quick setup
            1: 3,  # PRD - moderate analysis
            2: 2,  # Task generation - quick breakdown
            3: 5,  # Implementation - longer execution
            4: 3,  # Quality audit - moderate review
            5: 2,  # Retrospective - quick analysis
            6: 4   # Operations - ongoing monitoring
        }
        
        time.sleep(processing_time.get(phase, 1))
        
        # Generate phase-specific outputs
        if phase == 0:  # Bootstrap
            return {
                "ai_role": ai_role,
                "artifacts": [
                    {
                        "path": f"{self.project_name}/context-kit/README.md",
                        "category": "documentation",
                        "description": "Project context and architecture overview"
                    },
                    {
                        "path": f"{self.project_name}/project-rules/",
                        "category": "config",
                        "description": "Project-specific rules and governance"
                    }
                ],
                "validation": {
                    "status": "passed",
                    "score": 9.0,
                    "findings": [],
                    "recommendations": ["Context kit generated successfully", "Rules configured properly"]
                }
            }
        
        elif phase == 1:  # PRD Creation
            return {
                "ai_role": ai_role,
                "artifacts": [
                    {
                        "path": f"{self.project_name}/prd-{self.project_name}.md",
                        "category": "documentation",
                        "description": "Product Requirements Document"
                    }
                ],
                "validation": {
                    "status": "passed",
                    "score": 8.5,
                    "findings": [],
                    "recommendations": ["PRD complete and validated", "Ready for task generation"]
                }
            }
        
        elif phase == 2:  # Task Generation
            return {
                "ai_role": ai_role,
                "artifacts": [
                    {
                        "path": f"{self.project_name}/tasks-{self.project_name}.md",
                        "category": "documentation",
                        "description": "Technical task breakdown"
                    }
                ],
                "validation": {
                    "status": "passed",
                    "score": 8.0,
                    "findings": [],
                    "recommendations": ["Task plan generated", "Dependencies mapped", "Ready for implementation"]
                }
            }
        
        elif phase == 3:  # Implementation
            return {
                "ai_role": ai_role,
                "artifacts": [
                    {
                        "path": f"{self.project_name}/src/",
                        "category": "code",
                        "description": "Implemented source code"
                    },
                    {
                        "path": f"{self.project_name}/tests/",
                        "category": "test",
                        "description": "Unit and integration tests"
                    }
                ],
                "validation": {
                    "status": "passed",
                    "score": 7.5,
                    "findings": [
                        {
                            "severity": "medium",
                            "category": "code_quality",
                            "description": "Some functions could be more modular",
                            "file": "src/components/UserProfile.tsx",
                            "line": 45,
                            "recommendation": "Extract complex logic into separate functions"
                        }
                    ],
                    "recommendations": ["Implementation complete", "Code quality acceptable", "Tests written"]
                }
            }
        
        elif phase == 4:  # Quality Audit
            return {
                "ai_role": ai_role,
                "artifacts": [
                    {
                        "path": f"{self.project_name}/audit-reports/",
                        "category": "evidence",
                        "description": "Quality audit reports"
                    }
                ],
                "validation": {
                    "status": "passed",
                    "score": 8.5,
                    "findings": [],
                    "recommendations": ["Quality gates passed", "Security validated", "Performance acceptable"]
                }
            }
        
        elif phase == 5:  # Retrospective
            return {
                "ai_role": ai_role,
                "artifacts": [
                    {
                        "path": f"{self.project_name}/retrospective-notes.md",
                        "category": "documentation",
                        "description": "Implementation retrospective and learnings"
                    }
                ],
                "validation": {
                    "status": "passed",
                    "score": 9.0,
                    "findings": [],
                    "recommendations": ["Process improvements identified", "Lessons learned documented", "Ready for operations"]
                }
            }
        
        elif phase == 6:  # Operations
            return {
                "ai_role": ai_role,
                "artifacts": [
                    {
                        "path": f"{self.project_name}/monitoring-dashboards/",
                        "category": "config",
                        "description": "Production monitoring configuration"
                    },
                    {
                        "path": f"{self.project_name}/incident-reports/",
                        "category": "evidence",
                        "description": "Incident management documentation"
                    }
                ],
                "validation": {
                    "status": "passed",
                    "score": 8.0,
                    "findings": [],
                    "recommendations": ["Operations ready", "Monitoring configured", "Incident procedures documented"]
                }
            }
        
        else:
            return {
                "ai_role": ai_role,
                "artifacts": [],
                "validation": {
                    "status": "pending",
                    "score": 0.0,
                    "findings": [],
                    "recommendations": []
                }
            }
    
    def execute_phase(self, phase: int, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute a single phase with AI orchestration"""
        
        # Define phases
        phases = [
            (0, "Bootstrap & Context Engineering", "0-bootstrap.md"),
            (1, "PRD Creation", "1-prd-creation.md"),
            (2, "Task Generation", "2-task-generation.md"),
            (3, "Implementation", "3-implementation.md"),
            (4, "Quality Audit", "4-quality-audit.md"),
            (5, "Retrospective", "5-retrospective.md"),
            (6, "Operations", "6-operations.md")
        ]
        
        if phase < 0 or phase >= len(phases):
            raise ValueError(f"Invalid phase number: {phase}. Must be 0-{len(phases)-1}")
        
        phase_num, phase_name, phase_file = phases[phase]
        
        # Default context if not provided
        if context is None:
            context = {
                "description": f"Executing {phase_name} for project {self.project_name}",
                "project_type": self.config["project"]["type"],
                "tech_stack": self.config["project"]["stack"],
                "compliance": self.config["project"].get("compliance", []),
                "industry": self.config["project"].get("industry"),
            }
        
        print(f"🎯 AI Orchestrating Phase {phase_num}: {phase_name}")
        print("=" * 60)
        
        result = self._execute_ai_phase(phase_num, phase_name, phase_file, context)
        
        if result["status"] == "success":
            print(f"✅ Phase {phase_num} completed successfully")
            print(f"🤖 AI Role: {result['ai_role']}")
            print(f"⏱️  Duration: {result['duration']:.2f} seconds")
            
            # Show validation results
            if result["outputs"].get("validation"):
                validation = result["outputs"]["validation"]
                print(f"📊 Quality Score: {validation['score']}/10")
                print(f"🔍 Status: {validation['status']}")

                if validation["findings"]:
                    print(f"⚠️  Findings: {len(validation['findings'])}")
                    for finding in validation["findings"]:
                        print(f"   - {finding['severity'].upper()}: {finding['description']}")

            self._print_service_summary(result.get("external_services", {}))
        else:
            print(f"❌ Phase {phase_num} failed: {result['error']}")
            self._print_service_summary(result.get("external_services", {}))

        return result
    
    def execute_phase_sequence(self, start_phase: int, end_phase: int, context: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Execute a sequence of phases"""
        
        if start_phase < 0 or end_phase >= 7 or start_phase > end_phase:
            raise ValueError("Invalid phase range")
        
        print(f"🎯 AI Orchestrating Phases {start_phase}-{end_phase}")
        print("=" * 60)
        
        results = []
        
        for phase in range(start_phase, end_phase + 1):
            print(f"\n📋 Phase {phase}")
            print("-" * 40)
            
            result = self.execute_phase(phase, context)
            results.append(result)
            
            # Check for errors
            if result["status"] == "error":
                print(f"❌ Sequence stopped at phase {phase}")
                break
        
        return results


# CLI Interface
@click.group()
def cli():
    """AI Orchestrator CLI for Unified Developer Workflow"""
    pass


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--phase', type=int, required=True, help='Phase number (0-6)')
@click.option('--context', help='Context JSON string')
@click.option('--evidence-root', default='evidence', help='Evidence directory')
def phase(project, phase, context, evidence_root):
    """Execute single phase with AI orchestration"""
    orchestrator = AIOrchestrator(project, evidence_root)
    
    # Parse context if provided
    context_dict = None
    if context:
        try:
            context_dict = json.loads(context)
        except json.JSONDecodeError:
            print("❌ Invalid JSON in context")
            exit(1)
    
    result = orchestrator.execute_phase(phase, context_dict)
    
    # Save result
    result_path = orchestrator.project_dir / f"ai-phase-{phase}-result.json"
    with open(result_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"📊 Result saved: {result_path}")


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--start-phase', type=int, required=True, help='Start phase number')
@click.option('--end-phase', type=int, required=True, help='End phase number')
@click.option('--context', help='Context JSON string')
@click.option('--evidence-root', default='evidence', help='Evidence directory')
def sequence(project, start_phase, end_phase, context, evidence_root):
    """Execute phase sequence with AI orchestration"""
    orchestrator = AIOrchestrator(project, evidence_root)
    
    # Parse context if provided
    context_dict = None
    if context:
        try:
            context_dict = json.loads(context)
        except json.JSONDecodeError:
            print("❌ Invalid JSON in context")
            exit(1)
    
    results = orchestrator.execute_phase_sequence(start_phase, end_phase, context_dict)
    
    # Save results
    results_path = orchestrator.project_dir / f"ai-sequence-{start_phase}-{end_phase}-results.json"
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"📊 Results saved: {results_path}")


if __name__ == "__main__":
    cli()
