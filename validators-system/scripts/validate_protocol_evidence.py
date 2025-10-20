#!/usr/bin/env python3
"""Protocol Evidence Package Validator."""

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


class ProtocolEvidenceValidator:
    """Validates evidence generation, storage, manifesting, and traceability."""

    KEY = "protocol_evidence"
    DIMENSION_KEYS = [
        "artifact_generation",
        "storage_structure",
        "manifest_completeness",
        "traceability",
        "archival",
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

        evidence_section = extract_section(content, "EVIDENCE SUMMARY")
        workflow_section = extract_section(content, "WORKFLOW")
        handoff_section = extract_section(content, "HANDOFF CHECKLIST")

        dimensions = [
            self._evaluate_artifact_generation(evidence_section),
            self._evaluate_storage_structure(evidence_section, workflow_section),
            self._evaluate_manifest(evidence_section),
            self._evaluate_traceability(evidence_section, workflow_section, handoff_section),
            self._evaluate_archival(evidence_section),
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
            note="Documentation-focused protocol detected; evidence manifest cues tracked as recommendations.",
        )

        return result

    def _evaluate_artifact_generation(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("artifact_generation", weight=0.3)
        if not section:
            dim.issues.append("EVIDENCE SUMMARY section missing")
            return dim

        table_lines = [line for line in section.splitlines() if line.strip().startswith("|")]
        header = table_lines[0] if table_lines else ""
        row_count = max(0, len(table_lines) - 2) if table_lines else 0
        artifact_mentions = len(re.findall(r"\.artifacts/[\w\-/]+", section))
        metric_mentions = len(re.findall(r"metric|score|confidence|coverage", section, flags=re.IGNORECASE))

        checks = {
            "table_present": bool(table_lines),
            "artifact_column": "artifact" in header.lower(),
            "metrics_column": any(keyword in header.lower() for keyword in ["metric", "evidence", "result"]),
            "row_coverage": row_count >= 2 or artifact_mentions >= 3,
        }

        dim.details = {
            **checks,
            "table_rows": row_count,
            "artifact_mentions": artifact_mentions,
            "metric_mentions": metric_mentions,
        }
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = determine_status(dim.score, pass_threshold=0.9, warning_threshold=0.75)

        if not checks["table_present"]:
            dim.issues.append("Evidence summary should include a table of artifacts and outcomes")
        if not checks["row_coverage"]:
            dim.recommendations.append("List multiple artifacts with associated metrics or outcomes")
        if metric_mentions == 0:
            dim.recommendations.append("Add performance or validation metrics for listed artifacts")

        return dim

    def _evaluate_storage_structure(self, evidence_section: str, workflow_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("storage_structure", weight=0.2)
        combined = "\n".join(filter(None, [evidence_section, workflow_section]))
        if not combined:
            dim.issues.append("Storage structure not documented")
            return dim

        protocol_dirs = re.findall(r"\.artifacts/protocol-\d+/", combined)
        subdirs = re.findall(r"/([\w-]+/)", "\n".join(protocol_dirs))
        permissions = re.findall(r"read|write|access", combined, flags=re.IGNORECASE)
        naming = re.findall(r"naming|convention|structure", combined, flags=re.IGNORECASE)

        checks = {
            "protocol_directory": len(protocol_dirs) > 0,
            "subdirectories": len(subdirs) > 0,
            "permissions": len(permissions) > 0,
            "naming": len(naming) > 0,
        }

        dim.details = {"directories": protocol_dirs[:5], **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(protocol_dirs) == 0:
            dim.issues.append("Protocol evidence directory not referenced")
        if not checks["permissions"]:
            dim.recommendations.append("Document storage permissions or access requirements")

        return dim

    def _evaluate_manifest(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("manifest_completeness", weight=0.2)
        if not section:
            dim.issues.append("Manifest not documented")
            return dim

        manifest_mentions = re.findall(r"manifest|inventory|index", section, flags=re.IGNORECASE)
        metadata_mentions = re.findall(r"timestamp|size|hash|checksum", section, flags=re.IGNORECASE)
        dependency_mentions = re.findall(r"dependency|input|output", section, flags=re.IGNORECASE)
        coverage = section.lower().count("100%") or section.lower().count("complete")

        if not manifest_mentions:
            dim.details = {
                "manifest_reference": False,
                "metadata": len(metadata_mentions),
                "dependencies": len(dependency_mentions),
                "coverage": coverage,
            }
            dim.score = 1.0
            dim.status = "pass"
            dim.recommendations.append("Optionally reference a manifest file or inventory for quick lookup")
            return dim

        checks = {
            "manifest_reference": True,
            "metadata": len(metadata_mentions) >= 1,
            "dependencies": len(dependency_mentions) > 0,
            "coverage": coverage > 0,
        }

        dim.details = {
            **checks,
            "metadata_mentions": len(metadata_mentions),
            "dependency_mentions": len(dependency_mentions),
        }
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = determine_status(dim.score, pass_threshold=0.85, warning_threshold=0.6)

        if not checks["metadata"]:
            dim.recommendations.append("Document timestamps or hashes for manifest entries")
        if not checks["dependencies"]:
            dim.recommendations.append("Link artifacts to their inputs/outputs inside the manifest")

        return dim

    def _evaluate_traceability(self, evidence_section: str, workflow_section: str, handoff_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("traceability", weight=0.15)
        combined = "\n".join(filter(None, [evidence_section, workflow_section, handoff_section]))
        if not combined:
            dim.issues.append("Traceability information missing")
            return dim

        input_mentions = re.findall(r"Inputs? From", combined, flags=re.IGNORECASE)
        output_mentions = re.findall(r"Outputs? To", combined, flags=re.IGNORECASE)
        transformation_mentions = re.findall(r"transform|derive|generate", combined, flags=re.IGNORECASE)
        audit_mentions = re.findall(r"audit|log|history", combined, flags=re.IGNORECASE)

        checks = {
            "inputs": len(input_mentions) > 0,
            "outputs": len(output_mentions) > 0,
            "transformations": len(transformation_mentions) > 0,
            "audit": len(audit_mentions) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.issues.append(f"Traceability gaps: {', '.join(missing)}")

        return dim

    def _evaluate_archival(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("archival", weight=0.15)
        if not section:
            dim.issues.append("Archival strategy not documented")
            return dim

        compression_mentions = re.findall(r"zip|archive|compress", section, flags=re.IGNORECASE)
        retention_mentions = re.findall(r"retention|retain|30 days|90 days|duration", section, flags=re.IGNORECASE)
        retrieval_mentions = re.findall(r"retrieve|access|restore", section, flags=re.IGNORECASE)
        cleanup_mentions = re.findall(r"cleanup|delete|purge", section, flags=re.IGNORECASE)

        if not (compression_mentions or retention_mentions or retrieval_mentions or cleanup_mentions):
            dim.details = {"archival_reference": False}
            dim.score = 1.0
            dim.status = "pass"
            dim.recommendations.append("Optionally outline archival format, retention, retrieval, and cleanup steps")
            return dim

        checks = {
            "compression": len(compression_mentions) > 0,
            "retention": len(retention_mentions) > 0,
            "retrieval": len(retrieval_mentions) > 0,
            "cleanup": len(cleanup_mentions) > 0,
        }

        dim.details = {
            **checks,
            "compression_mentions": len(compression_mentions),
            "retention_mentions": len(retention_mentions),
        }
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = determine_status(dim.score, pass_threshold=0.85, warning_threshold=0.6)

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.recommendations.append(
                "Enhance archival plan with: " + ", ".join(sorted(missing))
            )

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
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-evidence.json"
        write_json(output_file, result)
        return output_file

    def generate_summary(self, results: List[Dict[str, Any]]) -> Path:
        metrics = aggregate_dimension_metrics(results, self.DIMENSION_KEYS)
        return generate_summary(self.KEY, results, self.output_dir, extra_fields={"dimensions": metrics})


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolEvidenceValidator(workspace_root)
    results: List[Dict[str, Any]] = []

    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        results.append(result)
        output_path = validator.save_result(result)
        print(f"✅ Evidence validation complete for Protocol {args.protocol} -> {output_path}")
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
    parser = argparse.ArgumentParser(description="Validate evidence packages for AI workflow protocols")
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
