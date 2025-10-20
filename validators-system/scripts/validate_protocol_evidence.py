#!/usr/bin/env python3
"""Protocol Evidence Package Validator."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

from validator_utils import (
    DimensionEvaluation,
    aggregate_dimension_metrics,
    build_base_result,
    compute_weighted_score,
    determine_status,
    documentation_protocol_recommendation,
    extract_section,
    gather_issues,
    generate_summary,
    get_protocol_file,
    is_documentation_protocol,
    read_protocol_content,
    resolve_protocol_ids,
    status_icon,
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
        if is_documentation_protocol(protocol_id):
            result["validation_status"] = "warning"
            result["recommendations"].append(documentation_protocol_recommendation())
            return result
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

        return result

    def _evaluate_artifact_generation(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("artifact_generation", weight=0.3)
        if not section:
            dim.issues.append("EVIDENCE SUMMARY section missing")
            return dim

        lines = section.splitlines()
        artifact_header = next(
            (line for line in lines if "|" in line and "Artifact" in line and "Location" in line),
            "",
        )
        artifact_rows = [line for line in lines if line.strip().startswith("|") and ".artifacts/" in line]
        metrics_header = next((line for line in lines if "|" in line and "Metric" in line and "Target" in line), "")
        unique_extensions = set(re.findall(r"\.(json|ya?ml|md|csv|zip|pdf)", section.lower()))
        column_coverage = "purpose" in artifact_header.lower() and "consumer" in artifact_header.lower()

        checks = {
            "artifact_table": bool(artifact_header),
            "row_count": len(artifact_rows) >= 3,
            "column_coverage": column_coverage,
        }

        optional_checks = {
            "format_diversity": len(unique_extensions) >= 2,
            "metrics_table": bool(metrics_header),
        }

        optional_score = (
            sum(1 for value in optional_checks.values() if value) / len(optional_checks)
            if optional_checks
            else 0.0
        )
        core_score = sum(1 for value in checks.values() if value) / len(checks)
        dim.score = min(1.0, 0.75 * core_score + 0.25 * optional_score)
        dim.status = determine_status(dim.score, pass_threshold=0.9, warning_threshold=0.75)

        dim.details = {
            **checks,
            **optional_checks,
            "artifact_rows": len(artifact_rows),
            "unique_extensions": sorted(unique_extensions),
        }

        if not checks["artifact_table"]:
            dim.issues.append("Evidence summary should include an artifact table with locations and consumers")
        if len(artifact_rows) < 3:
            dim.issues.append("Evidence table lacks sufficient artifact coverage")
        if not column_coverage:
            dim.recommendations.append("Include Purpose and Consumer columns for downstream clarity")
        if not optional_checks["format_diversity"]:
            dim.recommendations.append("Capture multiple artifact formats (JSON, Markdown, archives) when available")

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
        coverage_claims = re.findall(r"100%|complete|fully", section, flags=re.IGNORECASE)
        artifact_references = re.findall(r"\.artifacts/[\w\-/\.]+", section)

        manifest_promised = bool(
            re.search(r"\[\s*MUST\s*].*manifest", section, flags=re.IGNORECASE)
            or re.search(r"###\s+Manifest", section, flags=re.IGNORECASE)
        )

        core_checks = {
            "artifact_references": len(artifact_references) >= 2,
            "dependency_links": len(dependency_mentions) > 0,
        }
        optional_checks = {
            "manifest_reference": len(manifest_mentions) > 0,
            "metadata": len(metadata_mentions) >= 2,
            "coverage": len(coverage_claims) > 0,
        }

        optional_score = (
            sum(1 for value in optional_checks.values() if value) / len(optional_checks)
            if optional_checks
            else 0.0
        )
        core_score = sum(1 for value in core_checks.values() if value) / len(core_checks)
        dim.score = min(1.0, 0.7 * core_score + 0.3 * optional_score)
        dim.status = determine_status(dim.score, pass_threshold=0.9, warning_threshold=0.75)

        dim.details = {
            **core_checks,
            **optional_checks,
            "manifest_promised": manifest_promised,
            "artifact_references": artifact_references[:5],
        }

        if not core_checks["artifact_references"]:
            dim.issues.append("List artifacts in the manifest narrative to aid traceability")
        if manifest_promised and not optional_checks["manifest_reference"]:
            dim.issues.append("Manifest was promised but no manifest file or registry was referenced")
        if not manifest_promised and not optional_checks["manifest_reference"]:
            dim.recommendations.append("Mention manifest or inventory files when available (optional)")
        if not optional_checks["metadata"]:
            dim.recommendations.append("Capture metadata such as timestamps or checksums for evidence manifests")

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
            dim.recommendations.append("Document archival strategy when evidence needs long-term storage")
            return dim

        compression_mentions = re.findall(r"zip|archive|compress", section, flags=re.IGNORECASE)
        retention_mentions = re.findall(r"retention|retain|30 days|90 days|duration", section, flags=re.IGNORECASE)
        retrieval_mentions = re.findall(r"retrieve|access|restore", section, flags=re.IGNORECASE)
        cleanup_mentions = re.findall(r"cleanup|delete|purge", section, flags=re.IGNORECASE)

        archival_promised = bool(
            re.search(r"\[\s*MUST\s*].*archive", section, flags=re.IGNORECASE)
            or re.search(r"archival strategy", section, flags=re.IGNORECASE)
            or re.search(r"###\s+Archival", section, flags=re.IGNORECASE)
        )

        checks = {
            "compression": len(compression_mentions) > 0,
            "retention": len(retention_mentions) > 0,
            "retrieval": len(retrieval_mentions) > 0,
            "cleanup": len(cleanup_mentions) > 0,
        }

        if not archival_promised and not any(checks.values()):
            dim.score = 1.0
            dim.status = "pass"
            dim.details = {"archival_promised": False}
            dim.recommendations.append("Outline archival/retention guidance when it becomes available")
            return dim

        dim.details = {**checks, "archival_promised": archival_promised}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.issues.append(f"Archival strategy missing components: {', '.join(missing)}")

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
        status = result.get("validation_status")
        icon = status_icon(status)
        score = result.get("overall_score")
        score_text = (
            f" (score: {score:.3f})" if isinstance(score, (int, float)) else ""
        )
        print(
            f"{icon} Evidence validation complete for Protocol {args.protocol} -> {output_path}{score_text}"
        )
        if status:
            print(f"   Status: {status.upper()}")
    elif args.all:
        for protocol_id in resolve_protocol_ids(include_docs=args.include_docs):
            result = validator.validate_protocol(protocol_id)
            results.append(result)
            validator.save_result(result)
            icon = status_icon(result.get("validation_status"))
            print(
                f"{icon} Protocol {protocol_id}: {result['validation_status'].upper()} (score: {result['overall_score']:.3f})"
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
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Include documentation protocols 24-27 in iteration",
    )
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
