#!/usr/bin/env python3
"""
AI Executor for Unified Developer Workflow

Main orchestrator that executes the complete unified workflow from bootstrap to operations
with AI automation and human validation gates.
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import click

from .evidence_manager import EvidenceManager
from .external_services import ExternalServicesManager


class AIExecutor:
    """Main AI executor for the unified workflow"""
    
    def __init__(self, project_name: str, evidence_root: str = "evidence"):
        self.project_name = project_name
        self.evidence_manager = EvidenceManager(evidence_root)
        repo_root = Path(__file__).resolve().parent.parent
        self.workflow_home = repo_root / "unified_workflow"
        self.phases_dir = self.workflow_home / "phases"

        # Ensure project directory exists
        self.project_dir = Path(project_name)
        self.project_dir.mkdir(exist_ok=True)

        # Initialize project configuration
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
                    "quality_gates": {
                        "security": True,
                        "performance": True,
                        "accessibility": True
                    },
                    "compliance": ["gdpr"],
                },
                "workflow": {
                    "version": "1.0.0",
                    "evidence_root": "evidence",
                    "quality_gates_mode": "comprehensive"
                }
            }
            
            # Save default configuration
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=2)
            
            return config
    
    def _save_project_config(self):
        """Save project configuration"""
        config_path = self.project_dir / "project-config.json"
        with open(config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
    
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

        return {
            "name": project_config.get("name", self.project_name),
            "industry": project_config.get("industry", context.get("industry", "saas")),
            "project_type": project_config.get("type", context.get("project_type", "fullstack")),
            "stack": stack,
            "compliance": context.get("compliance") or project_config.get("compliance", []),
        }

    def _prepare_phase_integrations(self, phase: int, phase_name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare external integrations before executing a phase."""

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

    def _log_phase_start(self, phase: int, phase_name: str):
        """Log phase start"""
        self.evidence_manager.log_execution(
            phase=phase,
            action=f"Start {phase_name}",
            status="started",
            details={"phase_name": phase_name}
        )
    
    def _log_phase_end(self, phase: int, phase_name: str, status: str, duration: float):
        """Log phase end"""
        self.evidence_manager.log_execution(
            phase=phase,
            action=f"Complete {phase_name}",
            status=status,
            duration_seconds=duration
        )
    
    def _execute_phase(self, phase: int, phase_name: str, phase_file: str) -> Dict[str, Any]:
        """Execute a single phase"""
        start_time = time.time()
        
        # Log phase start
        self._log_phase_start(phase, phase_name)
        service_summary = self._prepare_phase_integrations(phase, phase_name, {
            "project_type": self.config.get("project", {}).get("type"),
            "industry": self.config.get("project", {}).get("industry"),
            "compliance": self.config.get("project", {}).get("compliance"),
        })

        try:
            # Load phase protocol
            phase_path = self.phases_dir / phase_file
            
            if not phase_path.exists():
                raise FileNotFoundError(f"Phase protocol not found: {phase_file}")
            
            # Read phase protocol
            with open(phase_path, 'r') as f:
                phase_content = f.read()
            
            # Execute phase (simulated - in real implementation, this would call AI)
            print(f"🚀 Executing Phase {phase}: {phase_name}")
            print(f"📋 Protocol: {phase_file}")
            
            # Simulate phase execution
            time.sleep(1)  # Simulate processing time
            
            # Generate phase outputs (simulated)
            outputs = self._generate_phase_outputs(phase, phase_name)
            
            # Create and log artifacts
            for output in outputs.get("artifacts", []):
                artifact_path = Path(output["path"])
                
                # Create artifact file/directory
                if artifact_path.suffix:  # File
                    artifact_path.parent.mkdir(parents=True, exist_ok=True)
                    artifact_path.write_text(f"Generated artifact for {phase_name}")
                else:  # Directory
                    artifact_path.mkdir(parents=True, exist_ok=True)
                    (artifact_path / "README.md").write_text(f"Generated directory for {phase_name}")
                
                self.evidence_manager.log_artifact(
                    path=output["path"],
                    category=output["category"],
                    description=output["description"],
                    phase=phase
                )
            
            # Log validation results
            if outputs.get("validation"):
                validation = outputs["validation"]
                self.evidence_manager.log_validation(
                    phase=phase,
                    status=validation["status"],
                    score=validation["score"],
                    findings=validation["findings"],
                    recommendations=validation["recommendations"]
                )
            
            duration = time.time() - start_time
            self._log_phase_end(phase, phase_name, "completed", duration)
            
            result_payload = {
                "status": "success",
                "phase": phase,
                "phase_name": phase_name,
                "outputs": outputs,
                "duration": duration,
            }

            self._finalize_phase_integrations(phase, phase_name, result_payload, service_summary)
            result_payload["external_services"] = service_summary

            return result_payload

        except Exception as e:
            duration = time.time() - start_time
            self._log_phase_end(phase, phase_name, "failed", duration)

            error_result = {
                "status": "error",
                "phase": phase,
                "phase_name": phase_name,
                "error": str(e),
                "duration": duration,
            }
            error_result["external_services"] = service_summary

            return error_result
    
    def _generate_phase_outputs(self, phase: int, phase_name: str) -> Dict[str, Any]:
        """Generate simulated phase outputs"""
        
        phase_outputs = {
            0: {
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
                    "recommendations": ["Continue to Phase 1"]
                }
            },
            1: {
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
                    "recommendations": ["Proceed to task generation"]
                }
            },
            2: {
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
                    "recommendations": ["Begin implementation"]
                }
            },
            3: {
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
                    "recommendations": ["Refactor complex functions", "Add more unit tests"]
                }
            },
            4: {
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
                    "recommendations": ["Quality gates passed", "Ready for retrospective"]
                }
            },
            5: {
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
                    "recommendations": ["Process improvements identified", "Ready for operations"]
                }
            },
            6: {
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
                    "recommendations": ["Operations ready", "Monitoring configured"]
                }
            }
        }
        
        return phase_outputs.get(phase, {
            "artifacts": [],
            "validation": {
                "status": "pending",
                "score": 0.0,
                "findings": [],
                "recommendations": []
            }
        })
    
    def execute_full_workflow(self) -> Dict[str, Any]:
        """Execute the complete unified workflow"""
        print(f"🎯 Starting Unified Developer Workflow for: {self.project_name}")
        print("=" * 60)
        
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
        
        results = []
        overall_status = "success"
        
        for phase_num, phase_name, phase_file in phases:
            print(f"\n📋 Phase {phase_num}: {phase_name}")
            print("-" * 40)
            
            # Execute phase
            result = self._execute_phase(phase_num, phase_name, phase_file)
            results.append(result)
            
            # Check for errors
            if result["status"] == "error":
                overall_status = "error"
                print(f"❌ Phase {phase_num} failed: {result['error']}")
                break
            else:
                print(f"✅ Phase {phase_num} completed successfully")
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

        if overall_status == "error":
            self._print_service_summary(result.get("external_services", {}))
        
        # Generate final report
        final_report = self._generate_final_report(results, overall_status)
        
        print("\n" + "=" * 60)
        print("🎉 Unified Developer Workflow Complete!")
        print(f"📊 Overall Status: {overall_status.upper()}")
        print(f"⏱️  Total Duration: {sum(r['duration'] for r in results):.2f} seconds")
        print(f"📁 Project Directory: {self.project_dir}")
        print(f"📋 Evidence Directory: {self.evidence_manager.evidence_root}")
        
        return final_report
    
    def _generate_final_report(self, results: List[Dict], overall_status: str) -> Dict[str, Any]:
        """Generate final workflow report"""
        
        # Calculate statistics
        total_duration = sum(r["duration"] for r in results)
        successful_phases = len([r for r in results if r["status"] == "success"])
        total_phases = len(results)
        
        # Collect all artifacts
        all_artifacts = []
        for result in results:
            if result["status"] == "success":
                all_artifacts.extend(result["outputs"].get("artifacts", []))
        
        # Collect validation scores
        validation_scores = []
        for result in results:
            if result["status"] == "success" and result["outputs"].get("validation"):
                validation_scores.append(result["outputs"]["validation"]["score"])
        
        avg_score = sum(validation_scores) / len(validation_scores) if validation_scores else 0
        
        return {
            "metadata": {
                "project_name": self.project_name,
                "workflow_version": "1.0.0",
                "execution_date": datetime.utcnow().isoformat() + "Z",
                "overall_status": overall_status,
                "total_duration": total_duration,
                "successful_phases": successful_phases,
                "total_phases": total_phases,
                "average_quality_score": avg_score
            },
            "phase_results": results,
            "artifacts": all_artifacts,
            "evidence": {
                "manifest_path": str(self.evidence_manager.manifest_path),
                "run_log_path": str(self.evidence_manager.run_log_path),
                "validation_path": str(self.evidence_manager.validation_path)
            }
        }
    
    def execute_single_phase(self, phase: int) -> Dict[str, Any]:
        """Execute a single phase"""
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
        
        print(f"🎯 Executing Phase {phase_num}: {phase_name}")
        print("=" * 60)
        
        result = self._execute_phase(phase_num, phase_name, phase_file)

        if result["status"] == "success":
            print(f"✅ Phase {phase_num} completed successfully")
            print(f"⏱️  Duration: {result['duration']:.2f} seconds")
        else:
            print(f"❌ Phase {phase_num} failed: {result['error']}")

        self._print_service_summary(result.get("external_services", {}))

        return result


# CLI Interface
@click.group()
def cli():
    """AI Executor CLI for Unified Developer Workflow"""
    pass


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--evidence-root', default='evidence', help='Evidence directory')
def init(project, evidence_root):
    """Initialize workflow for a project"""
    executor = AIExecutor(project, evidence_root)
    print(f"✅ Initialized workflow for project: {project}")
    print(f"📁 Project directory: {executor.project_dir}")
    print(f"📋 Evidence directory: {executor.evidence_manager.evidence_root}")


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--evidence-root', default='evidence', help='Evidence directory')
def full_workflow(project, evidence_root):
    """Execute full unified workflow"""
    executor = AIExecutor(project, evidence_root)
    report = executor.execute_full_workflow()
    
    # Save report
    report_path = executor.project_dir / "workflow-report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"📊 Report saved: {report_path}")


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--phase', type=int, required=True, help='Phase number (0-6)')
@click.option('--evidence-root', default='evidence', help='Evidence directory')
def phase(project, phase, evidence_root):
    """Execute single phase"""
    executor = AIExecutor(project, evidence_root)
    result = executor.execute_single_phase(phase)
    
    # Save result
    result_path = executor.project_dir / f"phase-{phase}-result.json"
    with open(result_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"📊 Result saved: {result_path}")


if __name__ == "__main__":
    cli()
