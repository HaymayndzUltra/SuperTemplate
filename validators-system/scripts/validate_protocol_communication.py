#!/usr/bin/env python3
"""Protocol Communication Validator."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

from validator_utils import (
    DEFAULT_PROTOCOL_IDS,
    DimensionEvaluation,
    aggregate_dimension_metrics,
    build_base_result,
    compute_weighted_score,
    determine_status,
    extract_section,
    gather_issues,
    generate_summary,
    get_protocol_file,
    include_documentation_protocols,
    relax_for_documentation_protocol,
    read_protocol_content,
    write_json,
)


class ProtocolCommunicationValidator:
    """Validates communication prompts, status announcements, and error handling."""

    KEY = "protocol_communication"
    DIMENSION_KEYS = [
        "status_announcements",
        "user_interaction",
        "error_messaging",
        "progress_tracking",
        "evidence_communication",
    ]

    def __init__(self, workspace_root: Path) -> None:
        self.workspace_root = workspace_root
        self.output_dir = workspace_root / ".artifacts" / "validation"

    def validate_protocol(self, protocol_id: str) -> Dict[str, Any]:
        result = build_base_result(self.KEY, protocol_id)
        protocol_file = get_protocol_file(self.workspace_root, protocol_id)
        if not protocol_file:
            result["issues"].append(f"Protocol file not found for ID {protocol_id}")
            return result

        content = read_protocol_content(protocol_file)
        if not content:
            result["issues"].append("Protocol content could not be read")
            return result

        comm_section = extract_section(content, "COMMUNICATION PROTOCOLS")
        workflow_section = extract_section(content, "WORKFLOW")
        evidence_section = extract_section(content, "EVIDENCE SUMMARY")

        dimensions = [
            self._evaluate_status_announcements(comm_section, workflow_section),
            self._evaluate_user_interaction(comm_section),
            self._evaluate_error_messaging(comm_section, workflow_section),
            self._evaluate_progress_tracking(comm_section, workflow_section),
            self._evaluate_evidence_communication(comm_section, evidence_section),
        ]

        for key, dim in zip(self.DIMENSION_KEYS, dimensions):
            result[key] = dim.to_dict()

        result["overall_score"] = compute_weighted_score(dimensions)
        result["validation_status"] = determine_status(result["overall_score"], pass_threshold=0.9, warning_threshold=0.8)

        issues, recommendations = gather_issues(dimensions)
        result["issues"].extend(issues)
        result["recommendations"].extend(recommendations)

        relax_for_documentation_protocol(
            protocol_id,
            result,
            note="Documentation-focused protocol detected; communication scaffolding treated as guidance.",
        )

        return result

    def _evaluate_status_announcements(self, comm_section: str, workflow_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("status_announcements", weight=0.25)
        combined = "\n".join(filter(None, [comm_section, workflow_section]))
        if not combined:
            dim.issues.append("Communication status prompts missing")
            return dim

        phase_mentions = re.findall(r"PHASE\s+\d|PHASE [A-Z]|PHASE COMPLETE", combined)
        master_ray_mentions = re.findall(r"MASTER RAY", combined)
        completion_mentions = re.findall(r"COMPLETE|READY", combined, flags=re.IGNORECASE)
        schedule_mentions = re.findall(r"ETA|duration|time", combined, flags=re.IGNORECASE)

        checks = {
            "phase_transitions": len(phase_mentions) >= 3,
            "branded_announcements": len(master_ray_mentions) >= 1,
            "completion_callouts": len(completion_mentions) >= 1,
            "time_estimates": len(schedule_mentions) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["phase_transitions"]:
            dim.issues.append("Phase transition announcements missing")
        if not checks["time_estimates"]:
            dim.recommendations.append("Add time or effort estimates to communication prompts")

        return dim

    def _evaluate_user_interaction(self, comm_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("user_interaction", weight=0.25)
        if not comm_section:
            dim.issues.append("COMMUNICATION PROTOCOLS section missing")
            return dim

        confirmation_prompts = re.findall(r"Reply|Confirm|Choose|Select", comm_section, flags=re.IGNORECASE)
        clarification_prompts = re.findall(r"clarify|specify|provide", comm_section, flags=re.IGNORECASE)
        decision_points = re.findall(r"option|choose|decision", comm_section, flags=re.IGNORECASE)
        feedback_requests = re.findall(r"feedback|review|does this", comm_section, flags=re.IGNORECASE)

        checks = {
            "confirmation": len(confirmation_prompts) > 0,
            "clarification": len(clarification_prompts) > 0,
            "decision_points": len(decision_points) > 0,
            "feedback": len(feedback_requests) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.issues.append(f"Missing user interaction prompts: {', '.join(missing)}")

        return dim

    def _evaluate_error_messaging(self, comm_section: str, workflow_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("error_messaging", weight=0.2)
        combined = "\n".join(filter(None, [comm_section, workflow_section]))
        if not combined:
            dim.issues.append("Error messaging not documented")
            return dim

        template_mentions = re.findall(r"\[RAY .*ERROR\]|ERROR|FAILED", combined)
        severity_mentions = re.findall(r"CRITICAL|HIGH|WARNING", combined)
        context_mentions = re.findall(r"Details|Criteria|Actual", combined)
        resolution_mentions = re.findall(r"Required action|Resolve|Fix|remediation", combined, flags=re.IGNORECASE)

        checks = {
            "templates": len(template_mentions) >= 1,
            "severity": len(severity_mentions) >= 1,
            "context": len(context_mentions) >= 1,
            "resolution": len(resolution_mentions) >= 1,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["resolution"]:
            dim.recommendations.append("Add explicit remediation instructions to error prompts")

        return dim

    def _evaluate_progress_tracking(self, comm_section: str, workflow_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("progress_tracking", weight=0.15)
        combined = "\n".join(filter(None, [comm_section, workflow_section]))
        if not combined:
            dim.issues.append("Progress tracking communications missing")
            return dim

        progress_terms = ["progress", "percent", "%", "complete", "remaining", "current activity", "next steps"]
        matches = [term for term in progress_terms if term in combined.lower()]
        timeline_mentions = re.findall(r"timeline|schedule|next", combined, flags=re.IGNORECASE)

        checks = {
            "progress_terms": len(matches) >= 3,
            "timeline": len(timeline_mentions) > 0,
            "current_activity": "currently" in combined.lower() or "now" in combined.lower(),
            "next_steps": "next" in combined.lower(),
        }

        dim.details = {"terms": matches, **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(matches) < 3:
            dim.issues.append("Limited progress terminology in communications")

        return dim

    def _evaluate_evidence_communication(self, comm_section: str, evidence_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("evidence_communication", weight=0.15)
        combined = "\n".join(filter(None, [comm_section, evidence_section]))
        if not combined:
            dim.issues.append("Evidence communication cues missing")
            return dim

        artifact_announcements = combined.count(".artifacts/")
        format_mentions = re.findall(r"markdown|json|yaml|manifest", combined, flags=re.IGNORECASE)
        location_mentions = re.findall(r"stored in|location|repository", combined, flags=re.IGNORECASE)
        validation_mentions = re.findall(r"validation|status|pass", combined, flags=re.IGNORECASE)

        checks = {
            "artifact_announcements": artifact_announcements >= 2,
            "format": len(format_mentions) >= 1,
            "location": len(location_mentions) >= 1,
            "validation": len(validation_mentions) >= 1,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if artifact_announcements < 2:
            dim.issues.append("Artifacts not announced or referenced sufficiently")

        return dim

    # Utilities -------------------------------------------------------------

    @staticmethod
    def _status_from_counts(found: int, total: int) -> str:
        if found == total:
            return "pass"
        if found >= total - 1:
            return "warning"
        return "fail"

    def save_result(self, result: Dict[str, Any]) -> Path:
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-communication.json"
        write_json(output_file, result)
        return output_file

    def generate_summary(self, results: List[Dict[str, Any]]) -> Path:
        metrics = aggregate_dimension_metrics(results, self.DIMENSION_KEYS)
        return generate_summary(self.KEY, results, self.output_dir, extra_fields={"dimensions": metrics})


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolCommunicationValidator(workspace_root)
    results: List[Dict[str, Any]] = []

    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        results.append(result)
        output_path = validator.save_result(result)
        print(f"✅ Communication validation complete for Protocol {args.protocol} -> {output_path}")
    elif args.all:
        protocol_ids = include_documentation_protocols(
            DEFAULT_PROTOCOL_IDS, include_docs=args.include_docs
        )
        for protocol_id in protocol_ids:
            result = validator.validate_protocol(protocol_id)
            results.append(result)
            validator.save_result(result)
            status_icon = "✅" if result["validation_status"] == "pass" else "⚠️" if result["validation_status"] == "warning" else "❌"
            print(
                f"{status_icon} Protocol {protocol_id}: {result['validation_status'].upper()} (score: {result['overall_score']:.3f})"
            )
    else:
        raise SystemExit("Either --protocol or --all must be supplied")

    if args.report or args.all:
        summary_path = validator.generate_summary(results)
        print(f"\n📊 Summary report: {summary_path}")

    if any(item["validation_status"] == "fail" for item in results):
        return 1
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate communication protocols for AI workflow")
    parser.add_argument("--protocol", help="Protocol ID to validate (e.g., '01')")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Include documentation protocols (24-27) when running with --all",
    )
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
