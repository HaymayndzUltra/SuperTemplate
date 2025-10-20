#!/usr/bin/env python3
"""Master orchestrator for all protocol validators."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List

from validator_utils import timestamp

from validate_protocol_identity import ProtocolIdentityValidator
from validate_protocol_role import AIRoleValidator
from validate_protocol_workflow import WorkflowValidator
from validate_protocol_gates import QualityGatesValidator
from validate_protocol_scripts import ScriptIntegrationValidator
from validate_protocol_communication import CommunicationValidator
from validate_protocol_evidence import EvidenceValidator
from validate_protocol_handoff import HandoffValidator
from validate_protocol_reasoning import ReasoningValidator
from validate_protocol_reflection import ReflectionValidator


class AllValidatorsRunner:
    def __init__(self, workspace: Path) -> None:
        self.workspace = workspace.resolve()
        identity_validator = ProtocolIdentityValidator(self.workspace)
        self.identity_output_dir = identity_validator.output_dir

        # Instantiate base validators (sharing list ability)
        self.role_validator = AIRoleValidator(self.workspace)
        self.validators = [
            {
                "slug": "protocol_identity",
                "name": "Protocol Identity Validator",
                "validate": identity_validator.validate_protocol,
                "save": lambda pid, result: self._save_identity(identity_validator, pid, result),
            },
            self._wrap(self.role_validator),
            self._wrap(WorkflowValidator(self.workspace)),
            self._wrap(QualityGatesValidator(self.workspace)),
            self._wrap(ScriptIntegrationValidator(self.workspace)),
            self._wrap(CommunicationValidator(self.workspace)),
            self._wrap(EvidenceValidator(self.workspace)),
            self._wrap(HandoffValidator(self.workspace)),
            self._wrap(ReasoningValidator(self.workspace)),
            self._wrap(ReflectionValidator(self.workspace)),
        ]
        self.output_dir = self.workspace / ".artifacts" / "validation" / "master"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def list_protocol_ids(self) -> List[str]:
        return self.role_validator.list_protocol_ids()

    def _wrap(self, validator) -> Dict[str, object]:
        return {
            "slug": validator.slug,
            "name": validator.name,
            "validator": validator,
            "validate": validator.validate_protocol,
            "save": lambda pid, result, instance=validator: instance.save_protocol_result(pid, result),
        }

    def _save_identity(self, validator: ProtocolIdentityValidator, protocol_id: str, result: Dict[str, object]) -> None:
        path = validator.output_dir / f"protocol-{protocol_id}-identity.json"
        validator.output_dir.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    def validate_protocol(self, protocol_id: str) -> Dict[str, object]:
        validator_results: Dict[str, Dict[str, object]] = {}
        issues: List[str] = []
        recommendations: List[str] = []
        scores: List[float] = []

        for entry in self.validators:
            result = entry["validate"](protocol_id)
            entry["save"](protocol_id, result)
            validator_results[entry["slug"]] = {
                "status": result["validation_status"],
                "score": result["overall_score"],
            }
            issues.extend(result.get("issues", []))
            recommendations.extend(result.get("recommendations", []))
            scores.append(result["overall_score"])

        overall_score = round(sum(scores) / len(scores), 3) if scores else 0.0
        if overall_score >= 0.9:
            status = "pass"
        elif overall_score >= 0.75:
            status = "warning"
        else:
            status = "fail"

        aggregated_result = {
            "protocol_id": protocol_id,
            "validation_timestamp": timestamp(),
            "validators": validator_results,
            "overall_score": overall_score,
            "validation_status": status,
            "issues": issues,
            "recommendations": recommendations,
        }

        output_path = self.output_dir / f"protocol-{protocol_id}-all.json"
        output_path.write_text(json.dumps(aggregated_result, indent=2), encoding="utf-8")
        return aggregated_result

    def run_all(self) -> List[Dict[str, object]]:
        results: List[Dict[str, object]] = []
        for protocol_id in self.list_protocol_ids():
            results.append(self.validate_protocol(protocol_id))
        summary = {
            "generated_at": timestamp(),
            "total_protocols": len(results),
            "status_counts": {
                "pass": sum(1 for r in results if r["validation_status"] == "pass"),
                "warning": sum(1 for r in results if r["validation_status"] == "warning"),
                "fail": sum(1 for r in results if r["validation_status"] == "fail"),
            },
            "average_score": round(sum(r["overall_score"] for r in results) / len(results), 3) if results else 0.0,
        }
        summary_path = self.output_dir / "master-summary.json"
        summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all protocol validators")
    parser.add_argument("--protocol", help="Protocol ID to validate")
    parser.add_argument("--all", action="store_true", help="Validate all protocol files")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    runner = AllValidatorsRunner(Path(args.workspace))

    if args.protocol:
        result = runner.validate_protocol(args.protocol)
        status_icon = "✅" if result["validation_status"] == "pass" else "⚠️" if result["validation_status"] == "warning" else "❌"
        print(f"{status_icon} Protocol {args.protocol}: {result['validation_status'].upper()} (score={result['overall_score']:.3f})")
        return 0 if result["validation_status"] != "fail" else 1

    if args.all:
        results = runner.run_all()
        for result in results:
            status_icon = "✅" if result["validation_status"] == "pass" else "⚠️" if result["validation_status"] == "warning" else "❌"
            print(f"{status_icon} Protocol {result['protocol_id']}: {result['validation_status'].upper()} (score={result['overall_score']:.3f})")
        fail_count = sum(1 for r in results if r["validation_status"] == "fail")
        return 1 if fail_count else 0

    print("⚠️ No protocol specified. Use --protocol XX or --all.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
