#!/usr/bin/env python3
"""
Validation Gates for Unified Developer Workflow

Implements human validation checkpoints for each phase with
approval workflows and evidence tracking.
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import click

from .evidence_manager import EvidenceManager
from .review_protocol_loader import ReviewProtocol, ReviewProtocolLoader


class ValidationGates:
    """Human validation gates for unified workflow"""
    
    def __init__(self, project_name: str, evidence_root: str = "evidence"):
        self.project_name = project_name
        self.evidence_manager = EvidenceManager(evidence_root)
        repo_root = Path(__file__).resolve().parent.parent
        self.workflow_home = repo_root / "unified_workflow"
        self.review_loader = ReviewProtocolLoader(repo_root)
        
        # Ensure project directory exists
        self.project_dir = Path(project_name)
        self.project_dir.mkdir(exist_ok=True)
        
        # Load validation configuration
        self.config = self._load_validation_config()
    
    def _load_validation_config(self) -> Dict[str, Any]:
        """Load validation configuration"""
        config_path = self.project_dir / "validation-config.json"
        
        if config_path.exists():
            with open(config_path, 'r') as f:
                return json.load(f)
        else:
            # Default configuration
            config = {
                "validation": {
                    "human_approval_required": True,
                    "checkpoints": [
                        "phase_0_completion",
                        "phase_1_approval",
                        "phase_2_confirmation",
                        "phase_3_review",
                        "phase_4_audit_results",
                        "phase_5_retrospective",
                        "phase_6_operations_readiness"
                    ],
                    "approval_timeout": 3600,  # 1 hour in seconds
                    "escalation_enabled": True
                }
            }
            
            # Save default configuration
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=2)
            
            return config
    
    def _get_validation_checkpoint(self, phase: int) -> Dict[str, Any]:
        """Get validation checkpoint for phase"""
        
        checkpoints = {
            0: {
                "name": "phase_0_completion",
                "title": "Bootstrap & Context Engineering Complete",
                "description": "Validate context kit and project rules",
                "required_approvals": ["technical_lead", "product_owner"],
                "artifacts": ["context-kit/README.md", "project-rules/"],
                "validation_criteria": [
                    "Context kit provides clear project overview",
                    "Project rules are properly configured",
                    "Architecture principles are validated",
                    "Evidence trail is complete"
                ]
            },
            1: {
                "name": "phase_1_approval",
                "title": "PRD Creation Approval",
                "description": "Approve Product Requirements Document",
                "required_approvals": ["product_owner", "stakeholder"],
                "artifacts": ["prd-{project}.md"],
                "validation_criteria": [
                    "Business goals are clearly defined",
                    "Technical specifications are complete",
                    "User stories are testable",
                    "API contracts are specified",
                    "Security model is defined"
                ]
            },
            2: {
                "name": "phase_2_confirmation",
                "title": "Task Generation Confirmation",
                "description": "Confirm technical task breakdown",
                "required_approvals": ["technical_lead", "developer"],
                "artifacts": ["tasks-{project}.md"],
                "validation_criteria": [
                    "All high-level tasks are generated",
                    "Dependencies are mapped correctly",
                    "Complexity is assessed accurately",
                    "Rules are applied to sub-tasks",
                    "Model personas are assigned"
                ]
            },
            3: {
                "name": "phase_3_review",
                "title": "Implementation Review",
                "description": "Review implemented features",
                "required_approvals": ["technical_lead", "code_reviewer"],
                "artifacts": ["src/", "tests/"],
                "validation_criteria": [
                    "All sub-tasks are completed",
                    "Code quality standards are met",
                    "Tests are written and passing",
                    "Documentation is updated",
                    "Security requirements are satisfied"
                ]
            },
            4: {
                "name": "phase_4_audit_results",
                "title": "Quality Audit Results Review",
                "description": "Review quality audit findings",
                "required_approvals": ["quality_engineer", "technical_lead"],
                "artifacts": ["audit-reports/"],
                "validation_criteria": [
                    "Quality gates pass with acceptable scores",
                    "Critical issues are addressed",
                    "Recommendations are actionable",
                    "Evidence trail is complete",
                    "Ready for retrospective"
                ]
            },
            5: {
                "name": "phase_5_retrospective",
                "title": "Retrospective Validation",
                "description": "Validate retrospective findings",
                "required_approvals": ["process_owner", "team_lead"],
                "artifacts": ["retrospective-notes.md"],
                "validation_criteria": [
                    "Retrospective is unbiased and accurate",
                    "Genuine improvement opportunities identified",
                    "Actionable recommendations provided",
                    "Process improvements documented",
                    "Ready for operations"
                ]
            },
            6: {
                "name": "phase_6_operations_readiness",
                "title": "Operations Readiness",
                "description": "Validate operations readiness",
                "required_approvals": ["operations_lead", "technical_lead"],
                "artifacts": ["monitoring-dashboards/", "incident-reports/"],
                "validation_criteria": [
                    "SLO monitoring is configured",
                    "Incident response procedures are documented",
                    "Postmortem process is established",
                    "Continuous improvement process is active",
                    "Operations team is trained"
                ]
            }
        }
        
        return checkpoints.get(phase, {
            "name": f"phase_{phase}_validation",
            "title": f"Phase {phase} Validation",
            "description": f"Validate Phase {phase} completion",
            "required_approvals": ["technical_lead"],
            "artifacts": [],
            "validation_criteria": ["Phase completed successfully"]
        })
    
    def _phase_review_protocol(self, phase: int) -> Optional[ReviewProtocol]:
        """Select the review protocol associated with a validation phase."""

        protocol_mapping = {
            0: "architecture-review",
            1: "design-system",
            2: "code-review",
            3: "code-review",
            4: "pre-production",
            5: "ui-accessibility",
            6: "security-check",
        }

        slug = protocol_mapping.get(phase)
        if not slug:
            return None

        try:
            return self.review_loader.load(slug)
        except FileNotFoundError:
            return None

    def _create_validation_request(self, phase: int, context: Dict[str, Any]) -> Dict[str, Any]:
        """Create validation request for phase"""

        checkpoint = self._get_validation_checkpoint(phase)
        protocol = self._phase_review_protocol(phase)
        
        validation_request = {
            "phase": phase,
            "checkpoint": checkpoint,
            "context": context,
            "request_id": f"validation_{phase}_{int(time.time())}",
            "created_at": datetime.utcnow().isoformat() + "Z",
            "status": "pending",
            "approvals": {},
            "comments": [],
            "artifacts": checkpoint["artifacts"],
            "validation_criteria": list(checkpoint["validation_criteria"]),
        }

        if protocol:
            validation_request["review_protocol"] = protocol.to_dict()
            combined_criteria = validation_request["validation_criteria"] + protocol.checklist
            deduped: List[str] = []
            for item in combined_criteria:
                if item not in deduped:
                    deduped.append(item)
            validation_request["validation_criteria"] = deduped

            self.evidence_manager.log_execution(
                phase=phase,
                action="Review Protocol Linked",
                status="completed",
                details={
                    "checkpoint": checkpoint["name"],
                    "protocol": protocol.path.name,
                    "checklist_items": len(protocol.checklist),
                },
            )

        return validation_request
    
    def _save_validation_request(self, validation_request: Dict[str, Any]):
        """Save validation request to file"""
        
        request_id = validation_request["request_id"]
        request_path = self.project_dir / "validation-requests" / f"{request_id}.json"
        
        # Ensure directory exists
        request_path.parent.mkdir(exist_ok=True)
        
        with open(request_path, 'w') as f:
            json.dump(validation_request, f, indent=2)
    
    def _load_validation_request(self, request_id: str) -> Optional[Dict[str, Any]]:
        """Load validation request from file"""
        
        request_path = self.project_dir / "validation-requests" / f"{request_id}.json"
        
        if request_path.exists():
            with open(request_path, 'r') as f:
                return json.load(f)
        
        return None
    
    def request_validation(self, phase: int, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Request validation for a phase"""
        
        if context is None:
            context = {
                "project_name": self.project_name,
                "description": f"Validation request for Phase {phase}"
            }
        
        # Create validation request
        validation_request = self._create_validation_request(phase, context)
        
        # Save request
        self._save_validation_request(validation_request)
        
        # Log validation request
        self.evidence_manager.log_execution(
            phase=phase,
            action=f"Validation Request: {validation_request['checkpoint']['title']}",
            status="started",
            details={"request_id": validation_request["request_id"]}
        )
        
        print(f"🔍 Validation Request Created")
        print(f"📋 Phase: {phase}")
        print(f"🎯 Checkpoint: {validation_request['checkpoint']['title']}")
        print(f"🆔 Request ID: {validation_request['request_id']}")
        print(f"👥 Required Approvals: {', '.join(validation_request['checkpoint']['required_approvals'])}")
        if "review_protocol" in validation_request:
            protocol_info = validation_request["review_protocol"]
            print(
                f"🧭 Review Protocol: {protocol_info['title']} "
                f"({protocol_info['path']})"
            )
            print(
                f"✅ Checklist Items: {len(protocol_info.get('checklist', []))}"
            )

        return validation_request
    
    def approve_validation(self, request_id: str, approver: str, approval: bool, comments: Optional[str] = None) -> Dict[str, Any]:
        """Approve or reject validation request"""
        
        # Load validation request
        validation_request = self._load_validation_request(request_id)
        
        if not validation_request:
            raise ValueError(f"Validation request not found: {request_id}")
        
        if validation_request["status"] != "pending":
            raise ValueError(f"Validation request is not pending: {request_id}")
        
        # Add approval
        validation_request["approvals"][approver] = {
            "approved": approval,
            "comments": comments or "",
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        
        # Add comment if provided
        if comments:
            validation_request["comments"].append({
                "author": approver,
                "comment": comments,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })
        
        # Check if all required approvals are received
        required_approvals = validation_request["checkpoint"]["required_approvals"]
        received_approvals = set(validation_request["approvals"].keys())
        
        if received_approvals.issuperset(set(required_approvals)):
            # All approvals received
            all_approved = all(
                validation_request["approvals"][approver]["approved"]
                for approver in required_approvals
            )
            
            validation_request["status"] = "approved" if all_approved else "rejected"
            validation_request["completed_at"] = datetime.utcnow().isoformat() + "Z"
        
        # Save updated request
        self._save_validation_request(validation_request)
        
        # Log approval
        self.evidence_manager.log_execution(
            phase=validation_request["phase"],
            action=f"Validation Approval: {approver}",
            status="completed" if approval else "failed",
            details={"request_id": request_id, "approval": approval}
        )
        
        print(f"✅ Validation {approval and 'Approved' or 'Rejected'}")
        print(f"👤 Approver: {approver}")
        print(f"🆔 Request ID: {request_id}")
        print(f"📊 Status: {validation_request['status']}")
        
        return validation_request
    
    def get_validation_status(self, request_id: str) -> Dict[str, Any]:
        """Get validation request status"""
        
        validation_request = self._load_validation_request(request_id)
        
        if not validation_request:
            raise ValueError(f"Validation request not found: {request_id}")
        
        # Calculate status summary
        required_approvals = validation_request["checkpoint"]["required_approvals"]
        received_approvals = set(validation_request["approvals"].keys())
        pending_approvals = set(required_approvals) - received_approvals
        
        status_summary = {
            "request_id": request_id,
            "phase": validation_request["phase"],
            "status": validation_request["status"],
            "required_approvals": required_approvals,
            "received_approvals": list(received_approvals),
            "pending_approvals": list(pending_approvals),
            "approval_details": validation_request["approvals"],
            "comments": validation_request["comments"]
        }
        
        return status_summary
    
    def list_pending_validations(self) -> List[Dict[str, Any]]:
        """List all pending validation requests"""
        
        validation_requests_dir = self.project_dir / "validation-requests"
        
        if not validation_requests_dir.exists():
            return []
        
        pending_requests = []
        
        for request_file in validation_requests_dir.glob("*.json"):
            with open(request_file, 'r') as f:
                request = json.load(f)
            
            if request["status"] == "pending":
                pending_requests.append({
                    "request_id": request["request_id"],
                    "phase": request["phase"],
                    "checkpoint": request["checkpoint"]["title"],
                    "created_at": request["created_at"],
                    "required_approvals": request["checkpoint"]["required_approvals"],
                    "received_approvals": list(request["approvals"].keys())
                })
        
        return pending_requests
    
    def execute_interactive_validation(self, phase: int) -> Dict[str, Any]:
        """Execute interactive validation for phase"""
        
        print(f"🔍 Interactive Validation for Phase {phase}")
        print("=" * 60)
        
        # Create validation request
        validation_request = self.request_validation(phase)
        
        # Show validation criteria
        print(f"\n📋 Validation Criteria:")
        for i, criteria in enumerate(validation_request["validation_criteria"], 1):
            print(f"  {i}. {criteria}")
        
        # Show artifacts
        if validation_request["artifacts"]:
            print(f"\n📁 Artifacts to Review:")
            for artifact in validation_request["artifacts"]:
                print(f"  - {artifact}")
        
        # Interactive approval process
        print(f"\n👥 Required Approvals: {', '.join(validation_request['checkpoint']['required_approvals'])}")
        
        for approver in validation_request["checkpoint"]["required_approvals"]:
            print(f"\n👤 {approver.upper()} Approval:")
            
            while True:
                approval_input = input("Approve? (y/n): ").strip().lower()
                if approval_input in ['y', 'yes']:
                    approval = True
                    break
                elif approval_input in ['n', 'no']:
                    approval = False
                    break
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            
            comments = input("Comments (optional): ").strip()
            
            # Process approval
            validation_request = self.approve_validation(
                validation_request["request_id"],
                approver,
                approval,
                comments
            )
            
            if validation_request["status"] != "pending":
                break
        
        print(f"\n🎉 Validation Complete!")
        print(f"📊 Final Status: {validation_request['status'].upper()}")
        
        return validation_request


# CLI Interface
@click.group()
def cli():
    """Validation Gates CLI for Unified Developer Workflow"""
    pass


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--phase', type=int, required=True, help='Phase number (0-6)')
@click.option('--context', help='Context JSON string')
def request(project, phase, context):
    """Request validation for a phase"""
    validation_gates = ValidationGates(project)
    
    # Parse context if provided
    context_dict = None
    if context:
        try:
            context_dict = json.loads(context)
        except json.JSONDecodeError:
            print("❌ Invalid JSON in context")
            exit(1)
    
    validation_request = validation_gates.request_validation(phase, context_dict)
    
    print(f"📊 Validation request saved: {validation_request['request_id']}")


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--request-id', required=True, help='Validation request ID')
@click.option('--approver', required=True, help='Approver name')
@click.option('--approval', is_flag=True, help='Approve (use --no-approval to reject)')
@click.option('--comments', help='Approval comments')
def approve(project, request_id, approver, approval, comments):
    """Approve or reject validation request"""
    validation_gates = ValidationGates(project)
    
    validation_request = validation_gates.approve_validation(request_id, approver, approval, comments)
    
    print(f"📊 Validation request updated: {request_id}")


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--request-id', required=True, help='Validation request ID')
def status(project, request_id):
    """Get validation request status"""
    validation_gates = ValidationGates(project)
    
    status_summary = validation_gates.get_validation_status(request_id)
    
    print(json.dumps(status_summary, indent=2))


@cli.command()
@click.option('--project', required=True, help='Project name')
def list_pending(project):
    """List pending validation requests"""
    validation_gates = ValidationGates(project)
    
    pending_requests = validation_gates.list_pending_validations()
    
    if not pending_requests:
        print("No pending validation requests")
    else:
        print("Pending validation requests:")
        for request in pending_requests:
            print(f"  {request['request_id']}: Phase {request['phase']} - {request['checkpoint']}")


@cli.command()
@click.option('--project', required=True, help='Project name')
@click.option('--phase', type=int, required=True, help='Phase number (0-6)')
def interactive(project, phase):
    """Execute interactive validation for phase"""
    validation_gates = ValidationGates(project)
    
    validation_request = validation_gates.execute_interactive_validation(phase)
    
    print(f"📊 Validation complete: {validation_request['request_id']}")


if __name__ == "__main__":
    cli()
