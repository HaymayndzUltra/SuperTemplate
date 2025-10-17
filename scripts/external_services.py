"""External Services Integration for Unified Workflow.

This module provides integration with external services like Git, AI Governor,
and Policy DSL, ensuring they're available at the appropriate workflow phases.
"""

from __future__ import annotations

import logging
import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# Setup proper imports
import sys

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from project_generator.integrations.git import (
    init_repository,
    add_and_commit,
    get_current_branch
)
from project_generator.integrations.ai_governor import AIGovernorIntegration

logger = logging.getLogger(__name__)


class ExternalServicesManager:
    """Manages integration with external services across workflow phases."""
    
    def __init__(self, project_root: Path):
        """Initialize external services manager.
        
        Args:
            project_root: Root directory of the project
        """
        self.project_root = Path(project_root)
        self._services = {}
        self._initialize_services()
    
    def _initialize_services(self) -> None:
        """Initialize all external service connections."""
        # Git integration
        self._services['git'] = GitService(self.project_root)
        
        # AI Governor integration
        self._services['ai_governor'] = AIGovernorService(self.project_root)
        
        # Policy DSL integration
        self._services['policy_dsl'] = PolicyDSLService(self.project_root)
        
        logger.info(f"Initialized {len(self._services)} external services")
    
    def get_service(self, service_name: str) -> Optional[Any]:
        """Get a specific service by name.
        
        Args:
            service_name: Name of the service
            
        Returns:
            Service instance or None if not found
        """
        return self._services.get(service_name)
    
    def validate_services(self) -> Dict[str, Dict[str, Any]]:
        """Validate all services are properly configured.
        
        Returns:
            Validation results for each service
        """
        results = {}
        
        for name, service in self._services.items():
            try:
                results[name] = service.validate()
            except Exception as e:
                results[name] = {
                    "status": "error",
                    "message": str(e),
                    "available": False
                }
        
        return results
    
    def get_phase_services(self, phase: int) -> Dict[str, Any]:
        """Get services relevant for a specific phase.
        
        Args:
            phase: Phase number (0-6)
            
        Returns:
            Dictionary of relevant services for the phase
        """
        phase_map = {
            0: ['git', 'ai_governor'],  # Bootstrap
            1: ['ai_governor'],          # PRD Creation
            2: ['ai_governor'],          # Task Generation
            3: ['ai_governor', 'policy_dsl'],  # Implementation
            4: ['policy_dsl'],           # Quality Audit
            5: ['git'],                  # Retrospective
            6: ['ai_governor', 'policy_dsl']  # Operations
        }
        
        services = {}
        for service_name in phase_map.get(phase, []):
            if service_name in self._services:
                services[service_name] = self._services[service_name]
        
        return services


class GitService:
    """Git integration service for version control operations."""
    
    def __init__(self, project_root: Path):
        """Initialize Git service.
        
        Args:
            project_root: Root directory of the project
        """
        self.project_root = Path(project_root)
    
    def validate(self) -> Dict[str, Any]:
        """Validate Git is available and configured.
        
        Returns:
            Validation result
        """
        try:
            result = subprocess.run(
                ['git', '--version'],
                capture_output=True,
                text=True,
                check=True
            )
            
            # Check if repository is initialized
            is_repo = (self.project_root / '.git').exists()
            
            return {
                "status": "ok",
                "available": True,
                "version": result.stdout.strip(),
                "repository_initialized": is_repo,
                "current_branch": get_current_branch(self.project_root) if is_repo else None
            }
        except subprocess.CalledProcessError as e:
            return {
                "status": "error",
                "available": False,
                "message": f"Git not available: {e}"
            }
    
    def initialize_repository(self) -> bool:
        """Initialize a new Git repository.
        
        Returns:
            True if successful, False otherwise
        """
        return init_repository(self.project_root)
    
    def commit_phase_artifacts(self, phase: int, message: Optional[str] = None) -> bool:
        """Commit artifacts for a specific phase.
        
        Args:
            phase: Phase number
            message: Commit message (auto-generated if not provided)
            
        Returns:
            True if successful, False otherwise
        """
        if message is None:
            message = f"Phase {phase} artifacts completed"
        
        return add_and_commit(self.project_root, message)
    
    def create_phase_branch(self, phase: int) -> bool:
        """Create a branch for a specific phase.
        
        Args:
            phase: Phase number
            
        Returns:
            True if successful, False otherwise
        """
        branch_name = f"phase-{phase}-implementation"
        try:
            subprocess.run(
                ['git', 'checkout', '-b', branch_name],
                cwd=self.project_root,
                check=True,
                capture_output=True
            )
            return True
        except subprocess.CalledProcessError:
            return False


class AIGovernorService:
    """AI Governor integration service for rule validation and workflow routing."""
    
    def __init__(self, project_root: Path):
        """Initialize AI Governor service.
        
        Args:
            project_root: Root directory of the project
        """
        self.project_root = Path(project_root)
        self.integration = AIGovernorIntegration(project_root)
    
    def validate(self) -> Dict[str, Any]:
        """Validate AI Governor is available and configured.
        
        Returns:
            Validation result
        """
        governor_available = self.integration.governor_root is not None
        
        result = {
            "status": "ok" if governor_available else "warning",
            "available": governor_available,
            "governor_root": str(self.integration.governor_root) if governor_available else None
        }
        
        if governor_available:
            # Check for required directories
            result["rules_available"] = self.integration.rules_dir.exists()
            result["workflows_available"] = self.integration.workflows_dir.exists()
            
            # Count available rules
            if self.integration.rules_dir and self.integration.rules_dir.exists():
                rule_count = len(list(self.integration.rules_dir.rglob("*.md")))
                result["rule_count"] = rule_count
        
        return result
    
    def validate_project_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validate project configuration against AI Governor policies.
        
        Args:
            config: Project configuration
            
        Returns:
            Validation result
        """
        return self.integration.validate_project_config(config)
    
    def copy_master_rules(self, target: Optional[Path] = None) -> List[str]:
        """Copy master rules to the project."""

        destination = Path(target) if target else self.project_root
        return self.integration.copy_master_rules(destination)

    def create_workflow_config(self, phase: int) -> Dict[str, Any]:
        """Create workflow configuration for a phase.
        
        Args:
            phase: Phase number
            
        Returns:
            Workflow configuration
        """
        return self.integration.create_workflow_config({
            "phase": phase,
            "project_root": str(self.project_root)
        })


class PolicyDSLService:
    """Policy DSL service for compliance and security policy validation."""

    def __init__(self, project_root: Path):
        """Initialize Policy DSL service.

        Args:
            project_root: Root directory of the project
        """
        self.project_root = Path(project_root)
        self.policy_dir = self.project_root / "policies"
        self.policy_templates = self.project_root / "template-packs" / "policy-dsl"

    def validate(self) -> Dict[str, Any]:
        """Validate Policy DSL is available and configured."""

        templates_available = self.policy_templates.exists()
        policies_exist = self.policy_dir.exists() and any(self.policy_dir.glob("*.yaml"))

        return {
            "status": "ok" if templates_available else "warning",
            "available": templates_available,
            "templates_path": str(self.policy_templates) if templates_available else None,
            "policies_configured": policies_exist,
            "policy_count": len(list(self.policy_dir.glob("*.yaml"))) if policies_exist else 0,
        }

    def ensure_policy_bundle(self) -> Dict[str, Any]:
        """Ensure policy templates are copied into the project workspace."""

        self.policy_dir.mkdir(parents=True, exist_ok=True)

        created: List[str] = []
        if self.policy_templates.exists():
            for template in self.policy_templates.glob("*.yaml"):
                target = self.policy_dir / template.name
                if not target.exists():
                    shutil.copy2(template, target)
                    created.append(str(target))

        return {
            "policy_directory": str(self.policy_dir),
            "created": created,
        }

    def available_policies(self) -> List[str]:
        """Return the list of available policy identifiers."""

        if not self.policy_dir.exists():
            return []

        return sorted(path.stem for path in self.policy_dir.glob("*.yaml"))

    def load_policy(self, policy_name: str) -> Optional[Dict[str, Any]]:
        """Load a specific policy by name.
        
        Args:
            policy_name: Name of the policy
            
        Returns:
            Policy configuration or None if not found
        """
        policy_file = self.policy_dir / f"{policy_name}.yaml"
        if not policy_file.exists():
            return None
        
        try:
            import yaml
            with open(policy_file, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Failed to load policy {policy_name}: {e}")
            return None
    
    def validate_compliance(self, compliance_type: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validate compliance against a specific policy.
        
        Args:
            compliance_type: Type of compliance (hipaa, soc2, pci, gdpr)
            config: Configuration to validate
            
        Returns:
            Validation result
        """
        policy = self.load_policy(compliance_type)
        if not policy:
            return {
                "valid": False,
                "errors": [f"Policy {compliance_type} not found"],
                "compliance_type": compliance_type
            }
        
        # Simple validation logic - in real implementation would be more complex
        errors = []
        warnings = []
        
        # Check required fields
        for required in policy.get("required_fields", []):
            if required not in config:
                errors.append(f"Missing required field: {required}")
        
        # Check security requirements
        security = policy.get("security", {})
        if security.get("encryption_required", False):
            if not config.get("encryption_enabled", False):
                errors.append("Encryption is required but not enabled")
        
        if security.get("audit_logging_required", False):
            if not config.get("audit_logging_enabled", False):
                errors.append("Audit logging is required but not enabled")
        
        # Check data retention
        retention = policy.get("data_retention", {})
        if retention:
            max_days = retention.get("max_retention_days")
            config_days = config.get("data_retention_days", 0)
            if max_days and config_days > max_days:
                errors.append(f"Data retention exceeds maximum allowed: {max_days} days")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "compliance_type": compliance_type,
            "policy_version": policy.get("version", "1.0.0")
        }
    
    def generate_compliance_report(self, phase: int) -> Dict[str, Any]:
        """Generate compliance report for a phase.
        
        Args:
            phase: Phase number
            
        Returns:
            Compliance report
        """
        report = {
            "phase": phase,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "compliance_checks": {}
        }
        
        # Check all available policies
        if self.policy_dir.exists():
            for policy_file in self.policy_dir.glob("*.yaml"):
                compliance_type = policy_file.stem
                # Mock config for demonstration
                config = {
                    "encryption_enabled": True,
                    "audit_logging_enabled": True,
                    "data_retention_days": 90
                }
                result = self.validate_compliance(compliance_type, config)
                report["compliance_checks"][compliance_type] = result
        
        return report


# Utility functions for phase-specific integration

def get_phase_0_services(project_root: Path) -> Dict[str, Any]:
    """Get services for Phase 0 (Bootstrap).
    
    Args:
        project_root: Project root directory
        
    Returns:
        Dictionary of services needed for bootstrap
    """
    manager = ExternalServicesManager(project_root)
    return {
        "git": manager.get_service("git"),
        "ai_governor": manager.get_service("ai_governor")
    }


def get_phase_3_services(project_root: Path) -> Dict[str, Any]:
    """Get services for Phase 3 (Implementation).
    
    Args:
        project_root: Project root directory
        
    Returns:
        Dictionary of services needed for implementation
    """
    manager = ExternalServicesManager(project_root)
    return {
        "ai_governor": manager.get_service("ai_governor"),
        "policy_dsl": manager.get_service("policy_dsl")
    }


# Add missing import
from datetime import datetime
