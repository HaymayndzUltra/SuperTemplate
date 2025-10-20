#!/usr/bin/env python3
"""Master orchestrator to run all protocol validators."""

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from validate_protocol_identity import ProtocolIdentityValidator
from validate_protocol_role import ProtocolRoleValidator
from validate_protocol_workflow import ProtocolWorkflowValidator
from validate_protocol_gates import ProtocolQualityGatesValidator
from validate_protocol_scripts import ProtocolScriptIntegrationValidator
from validate_protocol_communication import ProtocolCommunicationValidator
from validate_protocol_evidence import ProtocolEvidenceValidator
from validate_protocol_handoff import ProtocolHandoffValidator
from validate_protocol_reasoning import ProtocolReasoningValidator
from validate_protocol_reflection import ProtocolReflectionValidator

PASS_THRESHOLD = 0.95
WARNING_THRESHOLD = 0.80


VALIDATOR_CLASSES: Tuple[Tuple[str, type], ...] = (
    ("protocol_identity", ProtocolIdentityValidator),
    ("protocol_role", ProtocolRoleValidator),
    ("protocol_workflow", ProtocolWorkflowValidator),
    ("protocol_quality_gates", ProtocolQualityGatesValidator),
    ("protocol_script_integration", ProtocolScriptIntegrationValidator),
    ("protocol_communication", ProtocolCommunicationValidator),
    ("protocol_evidence", ProtocolEvidenceValidator),
    ("protocol_handoff", ProtocolHandoffValidator),
    ("protocol_reasoning", ProtocolReasoningValidator),
    ("protocol_reflection", ProtocolReflectionValidator),
)


class MasterProtocolValidator:
    """Runs all validators and aggregates results."""

    def __init__(self, workspace_root: Path) -> None:
        self.workspace_root = workspace_root
        self.protocols_dir = workspace_root / ".cursor" / "ai-driven-workflow"
        self.output_dir = workspace_root / ".artifacts" / "validation"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _status_from_score(self, score: float) -> str:
        if score >= PASS_THRESHOLD:
            return "pass"
        if score >= WARNING_THRESHOLD:
            return "warning"
        return "fail"

    def _list_protocol_ids(self) -> List[str]:
        protocol_files = sorted(self.protocols_dir.glob("[0-9][0-9]-*.md"))
        return [f.name.split("-", 1)[0] for f in protocol_files]

    def validate_protocol(self, protocol_id: str) -> Dict[str, Dict[str, float]]:
        protocol_id = protocol_id.zfill(2)
        validators = {}
        scores: List[float] = []
        for name, validator_cls in VALIDATOR_CLASSES:
            validator = validator_cls(self.workspace_root)
            result = validator.validate_protocol(protocol_id)
            validators[name] = {
                "score": result.get("overall_score", 0.0),
                "status": result.get("validation_status", "fail"),
                "issues": result.get("issues", []),
            }
            scores.append(result.get("overall_score", 0.0))

        overall_score = round(sum(scores) / len(scores), 4) if scores else 0.0
        status = self._status_from_score(overall_score)

        aggregated = {
            "protocol_id": protocol_id,
            "validation_timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
            "validators": validators,
            "overall_score": overall_score,
            "validation_status": status,
        }

        output_file = self.output_dir / f"protocol-{protocol_id}-master-validator.json"
        output_file.write_text(json.dumps(aggregated, indent=2), encoding="utf-8")
        return aggregated

    def validate_all(self) -> Dict[str, Dict[str, Dict[str, float]]]:
        protocol_ids = self._list_protocol_ids()
        if not protocol_ids:
            return {
                "protocols": {},
                "overall_score": 0.0,
                "validation_status": "fail",
                "issues": ["No protocols found"],
            }

        summary: Dict[str, Dict[str, Dict[str, float]]] = {
            "protocols": {},
            "overall_score": 0.0,
            "validation_status": "fail",
            "issues": [],
        }

        scores: List[float] = []
        for protocol_id in protocol_ids:
            result = self.validate_protocol(protocol_id)
            summary["protocols"][protocol_id] = result
            scores.append(result.get("overall_score", 0.0))
            for validator_name, details in result.get("validators", {}).items():
                if details.get("status") == "fail":
                    summary["issues"].append(f"{protocol_id}: {validator_name} reported failures")

        if scores:
            summary["overall_score"] = round(sum(scores) / len(scores), 4)
            summary["validation_status"] = self._status_from_score(summary["overall_score"])

        summary["validation_timestamp"] = datetime.now(UTC).isoformat().replace("+00:00", "Z")

        output_file = self.output_dir / "summary-master-validator.json"
        output_file.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        return summary

    def run_cli(self, args: Optional[List[str]] = None) -> int:
        parser = argparse.ArgumentParser(description="Run master protocol validator")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--protocol", help="Validate a single protocol ID (e.g., 01)")
        group.add_argument("--all", action="store_true", help="Validate all protocols")
        parsed = parser.parse_args(args=args)

        if parsed.protocol:
            result = self.validate_protocol(parsed.protocol)
            print(json.dumps(result, indent=2))
        else:
            result = self.validate_all()
            print(json.dumps(result, indent=2))
        return 0


def main() -> None:
    workspace_root = Path(__file__).resolve().parents[2]
    validator = MasterProtocolValidator(workspace_root)
    raise SystemExit(validator.run_cli())


if __name__ == "__main__":
    main()
