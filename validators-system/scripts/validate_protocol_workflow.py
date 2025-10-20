#!/usr/bin/env python3
"""Protocol Workflow Algorithm Validator."""

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


class ProtocolWorkflowValidator:
    """Validates workflow structure, steps, markers, and evidence hooks."""

    KEY = "protocol_workflow"
    DIMENSION_KEYS = [
        "workflow_structure",
        "step_definitions",
        "action_markers",
        "halt_conditions",
        "evidence_tracking",
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

        workflow_section = extract_section(content, "WORKFLOW")
        evidence_section = extract_section(content, "EVIDENCE SUMMARY")

        dimensions = [
            self._evaluate_structure(workflow_section),
            self._evaluate_steps(workflow_section),
            self._evaluate_markers(workflow_section),
            self._evaluate_halt_conditions(workflow_section),
            self._evaluate_evidence(workflow_section, evidence_section),
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
            note="Documentation-focused protocol detected; workflow automation cues treated as optional guidance.",
        )

        return result

    def _evaluate_structure(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("workflow_structure", weight=0.2)
        if not section:
            dim.issues.append("WORKFLOW section missing")
            return dim

        step_matches = re.findall(r"STEP\s+(\d+)", section)
        unique_steps = sorted({int(n) for n in step_matches})
        has_sequence = unique_steps == list(range(1, len(unique_steps) + 1)) if unique_steps else False

        checks = {
            "section_present": True,
            "step_headings": len(unique_steps) >= 2,
            "sequential": has_sequence,
            "completeness": "### STEP" in section,
        }

        dim.details = {"steps": unique_steps, **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["step_headings"]:
            dim.issues.append("Less than two workflow steps defined")
        if not checks["sequential"]:
            dim.issues.append("Step numbering is not sequential")
        if not checks["completeness"]:
            dim.recommendations.append("Use '### STEP X' headings for clarity")

        return dim

    def _evaluate_steps(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("step_definitions", weight=0.25)
        if not section:
            dim.issues.append("Workflow steps missing")
            return dim

        step_blocks = re.split(r"###\s+STEP\s+\d+.*\n", section)
        step_blocks = [block.strip() for block in step_blocks if block.strip()]
        actions = sum(1 for block in step_blocks if "**Action:**".lower() in block.lower())
        communications = sum(1 for block in step_blocks if "Communication:" in block)
        evidences = sum(1 for block in step_blocks if "Evidence:" in block)

        total = max(len(step_blocks), 1)
        ratios = {
            "action_coverage": actions / total,
            "communication_coverage": communications / total,
            "evidence_coverage": evidences / total,
        }

        dim.details = {"steps": len(step_blocks), **ratios}
        dim.score = min(1.0, sum(ratios.values()) / len(ratios))
        dim.status = determine_status(dim.score, pass_threshold=0.9, warning_threshold=0.75)

        if actions < total:
            dim.issues.append("Not all steps define explicit actions")
        if communications < total:
            dim.recommendations.append("Document communication prompts per step")
        if evidences < total:
            dim.issues.append("Evidence expectations missing in some steps")

        return dim

    def _evaluate_markers(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("action_markers", weight=0.15)
        if not section:
            dim.issues.append("Action markers absent because workflow missing")
            return dim

        step_count = max(1, len(re.findall(r"###\s+STEP\s+\d+", section)))
        imperative_count = len(
            re.findall(r"\[(?:MUST|CRITICAL)\]|\bmust\b|\brequire|\bensure", section, flags=re.IGNORECASE)
        )
        action_prompts = len(re.findall(r"\*\*Action\*\*|Action:\s", section, flags=re.IGNORECASE))
        context_prompts = len(
            re.findall(r"Communication:|Evidence:|Halt condition|status", section, flags=re.IGNORECASE)
        )
        optional_guidance = len(re.findall(r"\[OPTIONAL\]|optional", section, flags=re.IGNORECASE))
        cautionary = len(re.findall(r"never|do not|avoid", section, flags=re.IGNORECASE))

        checks = {
            "imperative_balance": imperative_count >= max(1, step_count // 2),
            "action_clarity": action_prompts >= max(1, step_count // 2),
            "contextual_support": context_prompts >= max(1, step_count // 2),
        }

        dim.details = {
            **checks,
            "step_count": step_count,
            "imperative_count": imperative_count,
            "action_prompts": action_prompts,
            "context_prompts": context_prompts,
            "optional_guidance": optional_guidance,
            "cautionary_statements": cautionary,
        }
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["imperative_balance"]:
            dim.issues.append("Workflow steps lack imperative guidance (MUST/CRITICAL instructions)")
        if not checks["action_clarity"]:
            dim.issues.append("Several workflow steps omit explicit action prompts")
        if not checks["contextual_support"]:
            dim.recommendations.append("Reference communication, evidence, or halt cues alongside actions")
        if optional_guidance == 0 and cautionary == 0:
            dim.recommendations.append(
                "Optional or cautionary guidance can highlight operator judgement without blocking validation"
            )

        return dim

    def _evaluate_halt_conditions(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("halt_conditions", weight=0.2)
        if not section:
            dim.issues.append("No workflow content to evaluate halt conditions")
            return dim

        halt_mentions = re.findall(r"Halt condition|halt|stop if", section, flags=re.IGNORECASE)
        gate_mentions = re.findall(r"gate", section, flags=re.IGNORECASE)
        rollback_mentions = re.findall(r"rollback|retry", section, flags=re.IGNORECASE)

        checks = {
            "halt_defined": len(halt_mentions) >= 2,
            "validation_gates": len(gate_mentions) > 0,
            "rollback_steps": len(rollback_mentions) > 0,
            "user_confirmation": "confirm" in section.lower() or "approval" in section.lower(),
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["halt_defined"]:
            dim.issues.append("Halt conditions rarely documented")
        if not checks["rollback_steps"]:
            dim.recommendations.append("Add rollback or retry guidance for failure scenarios")
        if not checks["user_confirmation"]:
            dim.issues.append("User confirmation steps not described")

        return dim

    def _evaluate_evidence(self, workflow_section: str, evidence_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("evidence_tracking", weight=0.2)
        combined = "\n".join(filter(None, [workflow_section, evidence_section]))
        if not combined:
            dim.issues.append("Evidence tracking missing from workflow and summary")
            return dim

        evidence_mentions = combined.lower().count("evidence")
        artifact_mentions = combined.count(".artifacts/")
        manifest_mentions = combined.lower().count("manifest")
        consumer_mentions = combined.lower().count("consumer")

        checks = {
            "evidence_tags": evidence_mentions >= 3,
            "artifact_locations": artifact_mentions >= 2,
            "manifest": manifest_mentions > 0,
            "downstream_trace": consumer_mentions > 0 or "outputs to" in combined.lower(),
        }

        dim.details = {**checks, "evidence_mentions": evidence_mentions, "artifact_mentions": artifact_mentions}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["manifest"]:
            dim.recommendations.append("Document evidence manifests or registries")
        if artifact_mentions < 2:
            dim.issues.append("Evidence storage paths under-specified")
        if not checks["downstream_trace"]:
            dim.issues.append("Downstream consumer mapping missing")

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
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-workflow.json"
        write_json(output_file, result)
        return output_file

    def generate_summary(self, results: List[Dict[str, Any]]) -> Path:
        metrics = aggregate_dimension_metrics(results, self.DIMENSION_KEYS)
        return generate_summary(self.KEY, results, self.output_dir, extra_fields={"dimensions": metrics})


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolWorkflowValidator(workspace_root)
    results: List[Dict[str, Any]] = []

    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        results.append(result)
        output_path = validator.save_result(result)
        print(f"✅ Workflow validation complete for Protocol {args.protocol} -> {output_path}")
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
    parser = argparse.ArgumentParser(description="Validate workflow algorithm for AI-driven protocols")
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
