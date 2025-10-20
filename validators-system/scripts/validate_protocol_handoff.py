#!/usr/bin/env python3
"""Protocol Handoff Checklist Validator."""

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


class ProtocolHandoffValidator:
    """Validates handoff readiness, verification, and next-step alignment."""

    KEY = "protocol_handoff"
    DIMENSION_KEYS = [
        "checklist_completeness",
        "verification_procedures",
        "stakeholder_signoff",
        "documentation_requirements",
        "next_protocol_alignment",
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

        handoff_section = extract_section(content, "HANDOFF CHECKLIST")
        workflow_section = extract_section(content, "WORKFLOW")
        evidence_section = extract_section(content, "EVIDENCE SUMMARY")

        dimensions = [
            self._evaluate_checklist(handoff_section),
            self._evaluate_verification(handoff_section, workflow_section),
            self._evaluate_signoff(handoff_section),
            self._evaluate_documentation(handoff_section, evidence_section),
            self._evaluate_next_protocol(handoff_section),
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
            note="Documentation-focused protocol detected; handoff expectations recorded as recommendations.",
        )

        return result

    def _evaluate_checklist(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("checklist_completeness", weight=0.3)
        if not section:
            dim.issues.append("HANDOFF CHECKLIST section missing")
            return dim

        checklist_items = re.findall(r"- \[ \]|- \[x\]|- \[[^\]]\]", section, flags=re.IGNORECASE)
        categories = re.findall(r"Prerequisite|Workflow|Quality|Evidence|Integration|Automation", section, flags=re.IGNORECASE)
        dependencies = re.findall(r"before|after|next", section, flags=re.IGNORECASE)

        checks = {
            "items": len(checklist_items) >= 6,
            "categories": len(categories) >= 3,
            "dependencies": len(dependencies) > 0,
            "status_markers": any("[x]" in item.lower() or "[✓" in item for item in checklist_items),
        }

        dim.details = {"item_count": len(checklist_items), **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(checklist_items) < 6:
            dim.issues.append("Checklist lacks sufficient coverage of required items")

        return dim

    def _evaluate_verification(self, handoff_section: str, workflow_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("verification_procedures", weight=0.2)
        combined = "\n".join(filter(None, [handoff_section, workflow_section]))
        if not combined:
            dim.issues.append("Verification steps not documented")
            return dim

        verification_terms = ["validate", "ensure", "confirm", "verify", "gate"]
        counts = {term: combined.lower().count(term) for term in verification_terms}
        qa_mentions = re.findall(r"QA|quality|review", combined, flags=re.IGNORECASE)
        automation_mentions = re.findall(r"automation|script|command", combined, flags=re.IGNORECASE)

        checks = {
            "verification_terms": sum(counts.values()) >= 4,
            "qa_involvement": len(qa_mentions) > 0,
            "automation_reference": len(automation_mentions) > 0,
            "evidence_reference": combined.lower().count("evidence") > 1,
        }

        dim.details = {"term_counts": counts, **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if sum(counts.values()) < 4:
            dim.issues.append("Limited verification language detected")

        return dim

    def _evaluate_signoff(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("stakeholder_signoff", weight=0.2)
        if not section:
            dim.issues.append("Stakeholder sign-off section missing")
            return dim

        approval_mentions = re.findall(r"approval|sign-off|sign off|authorization", section, flags=re.IGNORECASE)
        reviewer_mentions = re.findall(r"reviewer|lead|stakeholder", section, flags=re.IGNORECASE)
        evidence_mentions = re.findall(r"evidence|package|manifest", section, flags=re.IGNORECASE)
        confirmation_mentions = re.findall(r"confirm|acknowledge", section, flags=re.IGNORECASE)

        checks = {
            "approvals": len(approval_mentions) > 0,
            "reviewers": len(reviewer_mentions) > 0,
            "evidence_reference": len(evidence_mentions) > 0,
            "confirmation": len(confirmation_mentions) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.issues.append(f"Sign-off guidance missing: {', '.join(missing)}")

        return dim

    def _evaluate_documentation(self, handoff_section: str, evidence_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("documentation_requirements", weight=0.15)
        combined = "\n".join(filter(None, [handoff_section, evidence_section]))
        if not combined:
            dim.issues.append("Documentation requirements not described")
            return dim

        doc_terms = ["log", "brief", "notes", "transcript", "manifest", "report"]
        matches = [term for term in doc_terms if term in combined.lower()]
        storage_mentions = re.findall(r"stored|save|archive", combined, flags=re.IGNORECASE)
        reviewer_docs = re.findall(r"reviewer|handoff|summary", combined, flags=re.IGNORECASE)

        checks = {
            "doc_terms": len(matches) >= 3,
            "storage": len(storage_mentions) > 0,
            "reviewer_docs": len(reviewer_docs) > 0,
            "format": any(ext in combined.lower() for ext in [".md", ".json", ".yaml"]),
        }

        dim.details = {"terms": matches, **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(matches) < 3:
            dim.issues.append("Documentation expectations under-specified")

        return dim

    def _evaluate_next_protocol(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("next_protocol_alignment", weight=0.15)
        if not section:
            dim.issues.append("Next protocol alignment missing")
            return dim

        ready_statements = re.findall(r"Ready for Protocol", section, flags=re.IGNORECASE)
        next_commands = re.findall(r"@apply|run|trigger", section, flags=re.IGNORECASE)
        dependency_mentions = re.findall(r"requires|after|before", section, flags=re.IGNORECASE)
        continuation_scripts = re.findall(r"generate_session_continuation|continuation", section, flags=re.IGNORECASE)

        checks = {
            "ready_statements": len(ready_statements) > 0,
            "next_commands": len(next_commands) > 0,
            "dependencies": len(dependency_mentions) > 0,
            "continuation": len(continuation_scripts) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(ready_statements) == 0:
            dim.issues.append("Ready-for-next-protocol statement missing")

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
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-handoff.json"
        write_json(output_file, result)
        return output_file

    def generate_summary(self, results: List[Dict[str, Any]]) -> Path:
        metrics = aggregate_dimension_metrics(results, self.DIMENSION_KEYS)
        return generate_summary(self.KEY, results, self.output_dir, extra_fields={"dimensions": metrics})


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolHandoffValidator(workspace_root)
    results: List[Dict[str, Any]] = []

    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        results.append(result)
        output_path = validator.save_result(result)
        print(f"✅ Handoff validation complete for Protocol {args.protocol} -> {output_path}")
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
    parser = argparse.ArgumentParser(description="Validate protocol handoff readiness")
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
