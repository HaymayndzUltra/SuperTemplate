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
    get_protocol_id_list,
    is_documentation_protocol,
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

        if is_documentation_protocol(protocol_id):
            result["overall_score"] = 1.0
            result["validation_status"] = "warning"
            result["recommendations"].append(
                "Documentation protocols (24-27) provide references; evidence validation skipped."
            )
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

        table_lines = [line for line in section.splitlines() if line.strip().startswith("|")]
        header = table_lines[0].lower() if table_lines else ""
        has_artifact_column = "artifact" in header
        has_metric_column = any(term in header for term in ["metric", "score", "status"])
        data_rows = [line for line in table_lines[2:]] if len(table_lines) >= 3 else []
        artifact_rows = [
            line
            for line in data_rows
            if ".artifacts/" in line or re.search(r"protocol-\d+", line)
        ]

        checks = {
            "table_present": bool(table_lines),
            "artifacts_listed": len(artifact_rows) >= 2,
            "metrics_documented": has_metric_column or any(
                re.search(r"(metric|score|result|confidence)", line, re.IGNORECASE) for line in data_rows
            ),
            "formats_referenced": any(ext in section.lower() for ext in [".json", ".md", ".csv", ".yaml", ".yml"]),
        }

        dim.details = {
            "table_rows": len(table_lines),
            "artifact_rows": len(artifact_rows),
            **checks,
        }
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["table_present"]:
            dim.issues.append("Evidence summary table not found")
        if table_lines and len(artifact_rows) < 2:
            dim.issues.append("Evidence table should list at least two artifacts with storage paths")

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
        manifest_promised = bool(manifest_mentions)
        dim.details["manifest_promised"] = manifest_promised

        if not manifest_promised:
            dim.score = 1.0
            dim.status = "pass"
            dim.recommendations.append("Optional: include manifest metadata when available")
            return dim

        metadata_mentions = re.findall(r"timestamp|size|hash|checksum", section, flags=re.IGNORECASE)
        dependency_mentions = re.findall(r"dependency|input|output", section, flags=re.IGNORECASE)
        coverage = section.lower().count("100%") or section.lower().count("complete")

        checks = {
            "metadata": len(metadata_mentions) >= 1,
            "dependencies": len(dependency_mentions) > 0,
            "coverage": coverage > 0,
        }

        dim.details.update({"metadata_mentions": len(metadata_mentions), "dependency_mentions": len(dependency_mentions)})
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.issues.append("Manifest details missing components: " + ", ".join(missing))

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

        archival_promised = bool(re.findall(r"archive|archival|retention", section, flags=re.IGNORECASE))
        dim.details["archival_promised"] = archival_promised

        if not archival_promised:
            dim.score = 1.0
            dim.status = "pass"
            dim.recommendations.append("Optional: describe archival or retention strategy when committed")
            return dim

        checks = {
            "compression": len(compression_mentions) > 0,
            "retention": len(retention_mentions) > 0,
            "retrieval": len(retrieval_mentions) > 0,
            "cleanup": len(cleanup_mentions) > 0,
        }

        dim.details.update({
            "compression_mentions": len(compression_mentions),
            "retention_mentions": len(retention_mentions),
            "retrieval_mentions": len(retrieval_mentions),
            "cleanup_mentions": len(cleanup_mentions),
        })
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
        print(f"✅ Evidence validation complete for Protocol {args.protocol} -> {output_path}")
    elif args.all:
        protocol_ids = get_protocol_id_list(include_docs=args.include_docs)
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
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Include documentation protocols (24-27) during --all runs",
    )

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
