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
    extract_section,
    gather_issues,
    generate_summary,
    get_protocol_file,
    read_protocol_content,
    resolve_protocol_ids,
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

        return result

    def _evaluate_artifact_generation(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("artifact_generation", weight=0.3)
        if not section:
            dim.issues.append("EVIDENCE SUMMARY section missing")
            return dim

        table_lines = [line.strip() for line in section.splitlines() if line.strip().startswith("|")]
        header = table_lines[0] if table_lines else ""
        divider_offset = 1 if len(table_lines) > 1 and set(table_lines[1].replace("|", "").strip()) <= {"-", ":"} else 0
        data_rows = table_lines[1 + divider_offset :]

        columns = [col.strip().lower() for col in header.strip("|").split("|") if col.strip()] if header else []
        artifact_column = any("artifact" in col for col in columns)
        metrics_column = any("metric" in col or "kpi" in col for col in columns)
        row_count = len([row for row in data_rows if row and not set(row.replace("|", "").strip()) <= {"-"}])
        artifact_mentions = sum(1 for row in data_rows if ".artifacts" in row.lower() or "artifact" in row.lower())
        metric_mentions = sum(1 for row in data_rows if re.search(r"\d", row) or "%" in row)

        checks = {
            "table_present": bool(table_lines),
            "artifact_column": artifact_column,
            "metrics_column": metrics_column or metric_mentions >= max(1, row_count // 2),
            "row_coverage": row_count >= 2,
            "artifact_references": artifact_mentions >= 1,
        }

        dim.details = {
            "rows": row_count,
            "columns": columns,
            "artifact_rows": artifact_mentions,
            "metric_rows": metric_mentions,
            **checks,
        }
        true_count = sum(1 for value in checks.values() if value)
        dim.score = true_count / len(checks)
        dim.status = self._status_from_counts(true_count, len(checks))

        if not checks["table_present"]:
            dim.issues.append("Evidence summary should include a table of artifacts and metrics")
        elif row_count < 2:
            dim.issues.append("Evidence table lacks sufficient artifact coverage")
        if not checks["metrics_column"]:
            dim.recommendations.append("Include metric columns or values to show evidence quality")

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
                "manifest_reference": 0,
                "metadata": len(metadata_mentions),
                "dependencies": len(dependency_mentions),
                "coverage": coverage,
                "manifest_expected": False,
            }
            dim.score = 1.0
            dim.status = "pass"
            dim.recommendations.append("Optional: include manifest/index details when available")
            return dim

        checks = {
            "manifest_reference": len(manifest_mentions) > 0,
            "metadata": len(metadata_mentions) >= 2,
            "dependencies": len(dependency_mentions) > 0,
            "coverage": coverage > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["metadata"]:
            dim.recommendations.append("Add metadata (timestamps, hashes) to the manifest description")
        if not checks["dependencies"]:
            dim.recommendations.append("Note upstream/downstream dependencies tracked in the manifest")
        if not checks["coverage"]:
            dim.recommendations.append("State manifest coverage expectations (e.g., 100% of artifacts)")

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

        archival_keywords = re.findall(r"archive|retention|backup|compress|snapshot|s3|cold", section, flags=re.IGNORECASE)
        if not archival_keywords:
            dim.details = {"archival_expected": False}
            dim.score = 1.0
            dim.status = "pass"
            dim.recommendations.append("Optional: describe archival or retention strategy when commitments exist")
            return dim

        compression_mentions = re.findall(r"zip|archive|compress", section, flags=re.IGNORECASE)
        retention_mentions = re.findall(r"retention|retain|30 days|90 days|duration", section, flags=re.IGNORECASE)
        retrieval_mentions = re.findall(r"retrieve|access|restore", section, flags=re.IGNORECASE)
        cleanup_mentions = re.findall(r"cleanup|delete|purge", section, flags=re.IGNORECASE)

        checks = {
            "compression": len(compression_mentions) > 0,
            "retention": len(retention_mentions) > 0,
            "retrieval": len(retrieval_mentions) > 0,
            "cleanup": len(cleanup_mentions) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.recommendations.append(
                "Enhance archival strategy with: " + ", ".join(missing)
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
        for protocol_id in resolve_protocol_ids(include_docs=args.include_docs):
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
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Include documentation protocols (24-27) when running --all",
    )

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
