"""Unified compliance validation module.

This module integrates compliance validation from the legacy scripts
and provides a clean interface for the unified workflow.
"""

from __future__ import annotations

import difflib
import json
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

# Import project generator components using proper package imports
# Since we're in unified-workflow, we need to go up to access project_generator
import sys

root_path = Path(__file__).resolve().parent.parent
project_root = str(root_path)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from project_generator.core.generator import ProjectGenerator
from project_generator.core.industry_config import IndustryConfig
from project_generator.core.validator import ProjectValidator


class ComplianceValidator:
    """Validates compliance documentation and gate configurations."""

    DEFAULT_STACK = {
        "name": "portfolio-dashboard",
        "industry": "saas",
        "project_type": "fullstack",
        "frontend": "nextjs",
        "backend": "fastapi",
        "database": "postgres",
        "auth": "auth0",
        "deploy": "vercel",
        "compliance": ["gdpr"],
    }

    HIPAA_CONTROLS: List[Dict[str, str]] = [
        {
            "id": "HIPAA-01",
            "name": "Encryption at Rest",
            "config_key": "encryption_at_rest",
            "description": "PHI data stores enforce AES-256 encryption at rest.",
            "remediation": "Enable storage-level encryption on all PHI repositories.",
            "policy": "HIPAA Security Rule 164.312(a)(2)(iv)",
        },
        {
            "id": "HIPAA-02",
            "name": "Encryption in Transit",
            "config_key": "encryption_in_transit",
            "description": "Transport encryption (TLS 1.2+) is enforced for PHI flows.",
            "remediation": "Require HTTPS/TLS for every service handling PHI.",
            "policy": "HIPAA Security Rule 164.312(e)(1)",
        },
        {
            "id": "HIPAA-03",
            "name": "Audit Logging",
            "config_key": "audit_logging_enabled",
            "description": "Access to PHI is captured in immutable audit logs.",
            "remediation": "Enable audit logging with six-year retention and review cadence.",
            "policy": "HIPAA Security Rule 164.312(b)",
        },
        {
            "id": "HIPAA-04",
            "name": "Access Reviews",
            "config_key": "access_reviews_enabled",
            "description": "Periodic access reviews ensure minimum necessary access.",
            "remediation": "Schedule quarterly PHI access reviews for all roles.",
            "policy": "HIPAA Security Rule 164.308(a)(4)",
        },
        {
            "id": "HIPAA-05",
            "name": "Incident Response Plan",
            "config_key": "breach_response_playbook",
            "description": "Documented breach response plan covers notification timelines.",
            "remediation": "Publish and rehearse the HIPAA incident response playbook annually.",
            "policy": "HIPAA Security Rule 164.308(a)(6)",
        },
    ]

    SOC2_CONTROLS: List[Dict[str, str]] = [
        {
            "id": "SOC2-01",
            "name": "Change Management",
            "config_key": "change_management_process",
            "description": "Changes follow peer review and approval workflows.",
            "remediation": "Adopt pull-request approvals and change tickets for production updates.",
            "policy": "SOC 2 CC8.1",
        },
        {
            "id": "SOC2-02",
            "name": "Incident Response",
            "config_key": "incident_response_plan",
            "description": "Documented incident response procedures exist and are tested.",
            "remediation": "Publish an incident response plan with tabletop exercises each quarter.",
            "policy": "SOC 2 CC7.3",
        },
        {
            "id": "SOC2-03",
            "name": "Security Monitoring",
            "config_key": "security_monitoring_enabled",
            "description": "Centralized monitoring captures security and availability events.",
            "remediation": "Deploy centralized logging with automated alerting.",
            "policy": "SOC 2 CC7.2",
        },
        {
            "id": "SOC2-04",
            "name": "Vendor Risk Management",
            "config_key": "vendor_risk_program",
            "description": "Third-party services undergo risk assessments and contract reviews.",
            "remediation": "Maintain a vendor inventory with annual compliance attestations.",
            "policy": "SOC 2 CC3.2",
        },
        {
            "id": "SOC2-05",
            "name": "Business Continuity",
            "config_key": "disaster_recovery_plan",
            "description": "Disaster recovery runbooks and backups support availability commitments.",
            "remediation": "Create and test recovery plans covering RTO/RPO targets.",
            "policy": "SOC 2 CC7.4",
        },
    ]

    PCI_CONTROLS: List[Dict[str, str]] = [
        {
            "id": "PCI-01",
            "name": "Network Segmentation",
            "config_key": "network_segmentation",
            "description": "Cardholder data environment is isolated from other networks.",
            "remediation": "Implement firewall rules isolating the CDE from untrusted networks.",
            "policy": "PCI DSS 1.2",
        },
        {
            "id": "PCI-02",
            "name": "Vulnerability Management",
            "config_key": "vulnerability_scanning",
            "description": "Quarterly scanning and annual penetration testing are scheduled.",
            "remediation": "Integrate automated vulnerability scans with remediation tracking.",
            "policy": "PCI DSS 11.2",
        },
        {
            "id": "PCI-03",
            "name": "Cardholder Data Protection",
            "config_key": "cardholder_data_encrypted",
            "description": "Stored cardholder data uses strong cryptography and key management.",
            "remediation": "Apply tokenization or AES-256 encryption with managed keys.",
            "policy": "PCI DSS 3",
        },
        {
            "id": "PCI-04",
            "name": "Access Control",
            "config_key": "access_control_restricted",
            "description": "Access to cardholder data is restricted to authorized personnel.",
            "remediation": "Enforce RBAC and multi-factor authentication for CDE access.",
            "policy": "PCI DSS 7",
        },
        {
            "id": "PCI-05",
            "name": "Logging and Monitoring",
            "config_key": "logging_centralized",
            "description": "Logging captures user access and critical events with daily reviews.",
            "remediation": "Deploy centralized logging with retention and review procedures.",
            "policy": "PCI DSS 10",
        },
    ]
    
    DEFAULT_VALIDATION_STANDARDS: Sequence[str] = ("hipaa", "soc2", "pci")

    def __init__(self, root_path: Optional[Path] = None):
        """Initialize the compliance validator.

        Args:
            root_path: Root path of the project. If None, uses parent of unified-workflow.
        """
        self.root = root_path or Path(__file__).resolve().parents[2]
        self.generator = self._build_generator()

    def _normalize_list(self, value: Union[str, Sequence[Any], None]) -> List[str]:
        """Normalize a string or sequence into a list of trimmed strings."""

        if value is None:
            return []

        if isinstance(value, str):
            raw_values = value.split(",")
        else:
            raw_values = value

        normalized: List[str] = []
        for item in raw_values:
            if item is None:
                continue
            text = str(item).strip()
            if text:
                normalized.append(text)
        return normalized

    def _normalize_standards(
        self, standards: Union[str, Sequence[str], None]
    ) -> List[str]:
        """Normalize compliance standards to lowercase identifiers."""

        return [value.lower() for value in self._normalize_list(standards)]

    def _build_generator(self, overrides: Optional[Dict[str, Any]] = None) -> ProjectGenerator:
        """Build a project generator instance with optional overrides."""

        stack = dict(self.DEFAULT_STACK)
        if overrides:
            stack.update(overrides)

        compliance_values = self._normalize_list(stack.get("compliance"))
        features_values = self._normalize_list(stack.get("features"))

        args = SimpleNamespace(
            name=stack.get("name", "portfolio-dashboard"),
            industry=stack.get("industry", "saas"),
            project_type=stack.get("project_type", "fullstack"),
            frontend=stack.get("frontend", "none"),
            backend=stack.get("backend", "none"),
            database=stack.get("database", "none"),
            auth=stack.get("auth", "auth0"),
            deploy=stack.get("deploy", "aws"),
            compliance=",".join(compliance_values),
            features=",".join(features_values),
            output_dir=".",
            no_git=True,
            no_install=True,
            include_cursor_assets=False,
            no_cursor_assets=True,
            minimal_cursor=False,
            rules_manifest=None,
            rules_mode="auto",
            include_project_rules=False,
            workers=2,
            category=stack.get("category", "example"),
            skip_system_checks=True,
            force=False,
        )
        validator = ProjectValidator()
        config = IndustryConfig(args.industry)
        return ProjectGenerator(args, validator, config)

    def _default_control_config(self, standard: str) -> Dict[str, Any]:
        """Return baseline configuration for a compliance standard."""

        defaults = {
            "hipaa": {
                "encryption_at_rest": True,
                "encryption_in_transit": True,
                "audit_logging_enabled": True,
                "access_reviews_enabled": True,
                "breach_response_playbook": True,
            },
            "soc2": {
                "change_management_process": True,
                "incident_response_plan": True,
                "security_monitoring_enabled": True,
                "vendor_risk_program": True,
                "disaster_recovery_plan": True,
            },
            "pci": {
                "network_segmentation": True,
                "vulnerability_scanning": True,
                "cardholder_data_encrypted": True,
                "access_control_restricted": True,
                "logging_centralized": True,
            },
        }

        return defaults.get(standard.lower(), {}).copy()

    def _run_control_checks(
        self,
        standard: str,
        controls: Sequence[Dict[str, str]],
        config: Dict[str, Any],
    ) -> Tuple[bool, Dict[str, Any]]:
        """Evaluate a set of compliance controls against a configuration."""

        evaluated_at = datetime.utcnow().isoformat() + "Z"
        control_results: List[Dict[str, Any]] = []
        passed = 0
        failed = 0

        for control in controls:
            key = control["config_key"]
            status = bool(config.get(key, False))
            if status:
                passed += 1
            else:
                failed += 1

            control_results.append(
                {
                    "id": control["id"],
                    "name": control["name"],
                    "status": "pass" if status else "fail",
                    "description": control["description"],
                    "policy_reference": control.get("policy"),
                    "remediation": control.get("remediation"),
                    "evidence": config.get(f"{key}_evidence"),
                }
            )

        total = len(controls)
        summary = {
            "passed": passed,
            "failed": failed,
            "total": total,
            "compliance_score": round((passed / total) * 100, 2) if total else 100.0,
        }

        report = {
            "standard": standard.upper(),
            "evaluated_at": evaluated_at,
            "controls": control_results,
            "summary": summary,
            "config_snapshot": config,
        }

        return failed == 0, report
    
    def validate_compliance_docs(
        self,
        write: bool = False,
        standards: Union[str, Sequence[str], None] = None,
    ) -> Tuple[bool, Dict[str, str]]:
        """Validate compliance documentation against generator output.

        Args:
            write: If True, update files with generator output instead of just checking.
            standards: Optional list of compliance standards to evaluate.

        Returns:
            Tuple of (all_valid, results_dict) where results_dict contains
            validation status and diffs for each file.
        """
        results = {}
        all_valid = True

        # Generate expected content
        normalized_standards = None
        if standards is not None:
            normalized_standards = self._normalize_standards(standards)

        current_standards = self._normalize_standards(self.generator.args.compliance)
        generator = (
            self.generator
            if normalized_standards in (None, current_standards)
            else self._build_generator({"compliance": normalized_standards})
        )

        compliance_doc = generator._generate_compliance_documentation().strip() + "\n"
        gates_yaml = generator._generate_gates_config()
        
        # Define paths
        compliance_path = self.root / "docs" / "COMPLIANCE.md"
        gates_path = self.root / "gates_config.yaml"
        
        # Validate compliance doc
        doc_valid, doc_diff = self._compare_file(
            compliance_path, compliance_doc, write, "COMPLIANCE.md"
        )
        results["compliance_doc"] = {
            "valid": doc_valid,
            "path": str(compliance_path),
            "diff": doc_diff
        }
        all_valid &= doc_valid
        
        # Validate gates config
        gates_valid, gates_diff = self._compare_file(
            gates_path, gates_yaml, write, "gates_config.yaml"
        )
        results["gates_config"] = {
            "valid": gates_valid,
            "path": str(gates_path),
            "diff": gates_diff
        }
        all_valid &= gates_valid
        
        return all_valid, results
    
    def _compare_file(self, path: Path, expected: str, write: bool, name: str) -> Tuple[bool, Optional[str]]:
        """Compare file content with expected and optionally update.
        
        Args:
            path: Path to the file to check
            expected: Expected content
            write: If True, write expected content to file
            name: Name for logging
            
        Returns:
            Tuple of (is_valid, diff_text)
        """
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        
        if current == expected:
            print(f"[COMPLIANCE] {name} is up to date.")
            return True, None
        
        if write:
            path.write_text(expected, encoding="utf-8")
            print(f"[COMPLIANCE] Updated {name} from generator output.")
            return True, None
        
        print(f"[COMPLIANCE] Drift detected in {name} (run with --write to update).")
        diff = list(difflib.unified_diff(
            current.splitlines(),
            expected.splitlines(),
            fromfile=str(path),
            tofile="generator",
        ))
        diff_text = "\n".join(diff)
        return False, diff_text
    
    def validate_hipaa_compliance(
        self, config: Optional[Dict[str, Any]] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """Run HIPAA-specific compliance checks."""

        baseline = self._default_control_config("hipaa")
        if config:
            baseline.update(config)
        return self._run_control_checks("hipaa", self.HIPAA_CONTROLS, baseline)

    def validate_soc2_compliance(
        self, config: Optional[Dict[str, Any]] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """Run SOC2-specific compliance checks."""

        baseline = self._default_control_config("soc2")
        if config:
            baseline.update(config)
        return self._run_control_checks("soc2", self.SOC2_CONTROLS, baseline)

    def validate_pci_compliance(
        self, config: Optional[Dict[str, Any]] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """Run PCI-specific compliance checks."""

        baseline = self._default_control_config("pci")
        if config:
            baseline.update(config)
        return self._run_control_checks("pci", self.PCI_CONTROLS, baseline)

    def generate_compliance_assets(
        self,
        output_dir: Optional[Union[str, Path]] = None,
        standards: Union[str, Sequence[str], None] = None,
        include_documentation: bool = True,
    ) -> Dict[str, Path]:
        """Generate compliance reports and documentation for selected standards."""

        selected = self._normalize_standards(standards) or list(self.DEFAULT_VALIDATION_STANDARDS)
        output_path = Path(output_dir) if output_dir else self.root / "artifacts" / "compliance"
        output_path.mkdir(parents=True, exist_ok=True)

        generator = self._build_generator({"compliance": selected})
        compliance_doc = generator._generate_compliance_documentation().strip() + "\n"
        gates_yaml = generator._generate_gates_config()

        assets: Dict[str, Path] = {}

        if include_documentation:
            doc_path = output_path / "COMPLIANCE.md"
            doc_path.write_text(compliance_doc, encoding="utf-8")
            assets["documentation"] = doc_path

        gates_path = output_path / "gates_config.yaml"
        gates_path.write_text(gates_yaml, encoding="utf-8")
        assets["gates_config"] = gates_path

        summary_lines = [
            "# Compliance Validation Summary",
            "",
            f"Generated: {datetime.utcnow().isoformat()}Z",
            "",
        ]

        for standard in selected:
            method = getattr(self, f"validate_{standard}_compliance", None)
            if not callable(method):
                continue
            valid, report = method()
            report_payload = {"valid": valid, **report}
            report_path = output_path / f"{standard}_report.json"
            report_path.write_text(json.dumps(report_payload, indent=2), encoding="utf-8")
            assets[f"{standard}_report"] = report_path

            status = "PASS" if valid else "FAIL"
            summary_lines.append(f"## {standard.upper()} ({status})")
            summary_lines.append(f"- Controls passed: {report['summary']['passed']}")
            summary_lines.append(f"- Controls failed: {report['summary']['failed']}")
            summary_lines.append("")

        summary_content = "\n".join(summary_lines).rstrip() + "\n"
        summary_path = output_path / "SUMMARY.md"
        summary_path.write_text(summary_content, encoding="utf-8")
        assets["summary"] = summary_path

        return assets


# CLI compatibility function for direct script replacement
def main() -> int:
    """CLI entry point for backward compatibility with validate_compliance_assets.py."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate that compliance docs and gate config match generator output."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Rewrite compliance assets instead of exiting with an error when drift is detected.",
    )
    args = parser.parse_args()
    
    validator = ComplianceValidator()
    all_valid, results = validator.validate_compliance_docs(write=args.write)
    
    # Print any diffs
    for name, result in results.items():
        if not result["valid"] and result.get("diff"):
            print(result["diff"])
    
    return 0 if all_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
