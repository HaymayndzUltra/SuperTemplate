#!/usr/bin/env python3
"""Master orchestrator for protocol validators."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

# Ensure sibling scripts are importable
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))

from validator_utils import (  # noqa: E402
    DEFAULT_PROTOCOL_IDS,
    build_base_result,
    include_documentation_protocols,
    write_json,
)

from validate_protocol_identity import ProtocolIdentityValidator  # noqa: E402
from validate_protocol_role import ProtocolRoleValidator  # noqa: E402
from validate_protocol_workflow import ProtocolWorkflowValidator  # noqa: E402
from validate_protocol_gates import ProtocolQualityGatesValidator  # noqa: E402
from validate_protocol_scripts import ProtocolScriptIntegrationValidator  # noqa: E402
from validate_protocol_communication import ProtocolCommunicationValidator  # noqa: E402
from validate_protocol_evidence import ProtocolEvidenceValidator  # noqa: E402
from validate_protocol_handoff import ProtocolHandoffValidator  # noqa: E402
from validate_protocol_reasoning import ProtocolReasoningValidator  # noqa: E402
from validate_protocol_reflection import ProtocolReflectionValidator  # noqa: E402


VALIDATOR_FACTORIES = [
    ("protocol_identity", ProtocolIdentityValidator, "identity"),
    ("protocol_role", ProtocolRoleValidator, "role"),
    ("protocol_workflow", ProtocolWorkflowValidator, "workflow"),
    ("protocol_quality_gates", ProtocolQualityGatesValidator, "quality-gates"),
    ("protocol_scripts", ProtocolScriptIntegrationValidator, "scripts"),
    ("protocol_communication", ProtocolCommunicationValidator, "communication"),
    ("protocol_evidence", ProtocolEvidenceValidator, "evidence"),
    ("protocol_handoff", ProtocolHandoffValidator, "handoff"),
    ("protocol_reasoning", ProtocolReasoningValidator, "reasoning"),
    ("protocol_reflection", ProtocolReflectionValidator, "reflection"),
]


class MasterProtocolValidator:
    """Runs all validators and aggregates the results."""

    def __init__(self, workspace_root: Path) -> None:
        self.workspace_root = workspace_root
        self.output_dir = workspace_root / ".artifacts" / "validation"
        self.validators = {
            key: factory(workspace_root)
            for key, factory, _ in VALIDATOR_FACTORIES
        }
        self.file_suffix = {key: suffix for key, _, suffix in VALIDATOR_FACTORIES}

    def validate_protocol(self, protocol_id: str) -> Dict[str, Dict[str, Any]]:
        protocol_results: Dict[str, Dict[str, Any]] = {}
        for key, validator in self.validators.items():
            result = validator.validate_protocol(protocol_id)
            protocol_results[key] = result
            self._persist_individual_result(result, key)
        return protocol_results

    def _persist_individual_result(self, result: Dict[str, Any], key: str) -> None:
        suffix = self.file_suffix.get(key, key.split("_")[-1])
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-{suffix}.json"
        write_json(output_file, result)

    def aggregate_protocol_result(self, protocol_id: str, results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        combined = build_base_result("master_validator", protocol_id)
        combined["validators"] = {}

        scores: List[float] = []
        statuses: List[str] = []

        for key, result in results.items():
            combined["validators"][key] = {
                "status": result.get("validation_status"),
                "score": result.get("overall_score"),
            }
            if "overall_score" in result:
                scores.append(result["overall_score"])
            if "validation_status" in result:
                statuses.append(result["validation_status"])

        combined["overall_score"] = sum(scores) / len(scores) if scores else 0.0
        combined["validation_status"] = self._resolve_status(statuses)
        combined.pop("issues", None)
        combined.pop("recommendations", None)
        combined["issues"] = [
            issue
            for result in results.values()
            for issue in result.get("issues", [])
        ]
        combined["recommendations"] = [
            rec
            for result in results.values()
            for rec in result.get("recommendations", [])
        ]

        return combined

    @staticmethod
    def _resolve_status(statuses: List[str]) -> str:
        if not statuses:
            return "fail"
        if any(status == "fail" for status in statuses):
            return "fail"
        if any(status == "warning" for status in statuses):
            return "warning"
        return "pass"

    def save_master_result(self, result: Dict[str, Any]) -> Path:
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-master-report.json"
        write_json(output_file, result)
        return output_file

    def generate_master_summary(self, protocol_results: List[Dict[str, Any]]) -> Path:
        summary = {
            "validator": "master_validator",
            "validation_timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "total_protocols": len(protocol_results),
            "pass_count": sum(1 for r in protocol_results if r.get("validation_status") == "pass"),
            "warning_count": sum(1 for r in protocol_results if r.get("validation_status") == "warning"),
            "fail_count": sum(1 for r in protocol_results if r.get("validation_status") == "fail"),
            "average_score": (
                sum(r.get("overall_score", 0.0) for r in protocol_results) / len(protocol_results)
                if protocol_results
                else 0.0
            ),
            "protocols": [
                {
                    "protocol_id": r.get("protocol_id"),
                    "status": r.get("validation_status"),
                    "score": r.get("overall_score"),
                }
                for r in protocol_results
            ],
            "validators": {},
        }

        # Per-validator aggregates
        for key in self.validators:
            validator_scores = [
                protocol["validators"].get(key, {}).get("score")
                for protocol in protocol_results
                if key in protocol.get("validators", {})
            ]
            validator_statuses = [
                protocol["validators"].get(key, {}).get("status")
                for protocol in protocol_results
                if key in protocol.get("validators", {})
            ]
            summary["validators"][key] = {
                "average_score": (
                    sum(score for score in validator_scores if score is not None) / len(validator_scores)
                    if validator_scores
                    else 0.0
                ),
                "pass_count": sum(1 for status in validator_statuses if status == "pass"),
                "warning_count": sum(1 for status in validator_statuses if status == "warning"),
                "fail_count": sum(1 for status in validator_statuses if status == "fail"),
            }

        output_path = self.output_dir / "master-validation-summary.json"
        write_json(output_path, summary)
        return output_path


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    orchestrator = MasterProtocolValidator(workspace_root)

    protocol_results: List[Dict[str, Any]] = []

    if args.protocol:
        validator_outputs = orchestrator.validate_protocol(args.protocol)
        combined = orchestrator.aggregate_protocol_result(args.protocol, validator_outputs)
        output_path = orchestrator.save_master_result(combined)
        protocol_results.append(combined)
        print(f"✅ Master validation complete for Protocol {args.protocol} -> {output_path}")
    elif args.all:
        protocol_ids = include_documentation_protocols(
            DEFAULT_PROTOCOL_IDS, include_docs=args.include_docs
        )
        for protocol_id in protocol_ids:
            validator_outputs = orchestrator.validate_protocol(protocol_id)
            combined = orchestrator.aggregate_protocol_result(protocol_id, validator_outputs)
            orchestrator.save_master_result(combined)
            protocol_results.append(combined)
            status_icon = "✅" if combined["validation_status"] == "pass" else "⚠️" if combined["validation_status"] == "warning" else "❌"
            print(
                f"{status_icon} Protocol {protocol_id}: {combined['validation_status'].upper()} (score: {combined['overall_score']:.3f})"
            )
    else:
        raise SystemExit("Either --protocol or --all must be supplied")

    if args.report or args.all:
        summary_path = orchestrator.generate_master_summary(protocol_results)
        print(f"\n📊 Master summary report: {summary_path}")

    if any(result.get("validation_status") == "fail" for result in protocol_results):
        return 1
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Run all protocol validators and aggregate results")
    parser.add_argument("--protocol", help="Protocol ID to validate (e.g., '01')")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Include documentation protocols (24-27) when running with --all",
    )
    parser.add_argument("--report", action="store_true", help="Generate master summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
