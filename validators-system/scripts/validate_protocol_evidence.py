#!/usr/bin/env python3
"""Validator 7 - Evidence Package"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

from validator_utils import (
    BaseProtocolValidator,
    DimensionResult,
    collect_section_text,
    normalize_score,
    run_cli,
)


class EvidenceValidator(BaseProtocolValidator):
    slug = "evidence"
    name = "Evidence Package Validator"
    dimension_weights = {
        "artifact_generation": 0.30,
        "storage_structure": 0.20,
        "manifest_completeness": 0.20,
        "traceability": 0.15,
        "archival": 0.15,
    }
    pass_threshold = 0.9
    warning_threshold = 0.75

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        evidence_text = collect_section_text(content, ["EVIDENCE", "ARTIFACT", "SUMMARY", "MANIFEST"])
        workflow_text = collect_section_text(content, ["WORKFLOW"])
        combined_text = "\n".join(filter(None, [evidence_text, workflow_text]))
        dimensions: Dict[str, DimensionResult] = {}

        # Dimension 7.1 - Artifact Generation
        artifact_lines = [line for line in combined_text.splitlines() if ".artifacts" in line or "Generate" in line or "Evidence" in line]
        artifact_findings = {
            "artifact_lines": artifact_lines[:10],
            "count": len(artifact_lines),
        }
        artifact_issues = []
        if not artifact_lines:
            artifact_issues.append("No evidence artifacts referenced.")
        if len(artifact_lines) >= 4:
            artifact_status = "pass"
        elif artifact_lines:
            artifact_status = "warning"
        else:
            artifact_status = "fail"
        artifact_score = normalize_score(artifact_status)
        dimensions["artifact_generation"] = DimensionResult(
            artifact_status,
            artifact_score,
            artifact_findings,
            artifact_issues,
            [],
        )

        # Dimension 7.2 - Storage Structure
        storage_keywords = [".artifacts/protocol", "transcripts", "evidence", "storage", "directory"]
        storage_lines = [line for line in evidence_text.splitlines() if any(keyword in line for keyword in storage_keywords)]
        structure_findings = {
            "storage_lines": storage_lines[:10],
            "count": len(storage_lines),
        }
        structure_issues = []
        if not storage_lines:
            structure_issues.append("Storage structure not described.")
        if len(storage_lines) >= 3:
            structure_status = "pass"
        elif storage_lines:
            structure_status = "warning"
        else:
            structure_status = "fail"
        structure_score = normalize_score(structure_status)
        dimensions["storage_structure"] = DimensionResult(
            structure_status,
            structure_score,
            structure_findings,
            structure_issues,
            [],
        )

        # Dimension 7.3 - Manifest Completeness
        manifest_keywords = ["manifest", "inventory", "index", "catalog"]
        manifest_lines = [line for line in evidence_text.splitlines() if any(keyword in line.lower() for keyword in manifest_keywords)]
        manifest_findings = {
            "manifest_lines": manifest_lines[:10],
            "count": len(manifest_lines),
        }
        manifest_issues = []
        if not manifest_lines:
            manifest_issues.append("Evidence manifest not referenced.")
        if len(manifest_lines) >= 2:
            manifest_status = "pass"
        elif manifest_lines:
            manifest_status = "warning"
        else:
            manifest_status = "fail"
        manifest_score = normalize_score(manifest_status)
        dimensions["manifest_completeness"] = DimensionResult(
            manifest_status,
            manifest_score,
            manifest_findings,
            manifest_issues,
            [],
        )

        # Dimension 7.4 - Traceability
        trace_keywords = ["trace", "input", "output", "link", "dependency", "audit"]
        trace_lines = [line for line in combined_text.splitlines() if any(keyword in line.lower() for keyword in trace_keywords)]
        trace_findings = {
            "traceability_lines": trace_lines[:10],
            "count": len(trace_lines),
        }
        trace_issues = []
        if not trace_lines:
            trace_issues.append("Traceability between inputs and outputs not documented.")
        if len(trace_lines) >= 3:
            trace_status = "pass"
        elif trace_lines:
            trace_status = "warning"
        else:
            trace_status = "fail"
        trace_score = normalize_score(trace_status)
        dimensions["traceability"] = DimensionResult(
            trace_status,
            trace_score,
            trace_findings,
            trace_issues,
            [],
        )

        # Dimension 7.5 - Archival
        archival_keywords = ["archive", "zip", "retention", "cleanup", "storage duration", "backup"]
        archival_lines = [line for line in evidence_text.splitlines() if any(keyword in line.lower() for keyword in archival_keywords)]
        archival_findings = {
            "archival_lines": archival_lines[:10],
            "count": len(archival_lines),
        }
        archival_issues = []
        if not archival_lines:
            archival_issues.append("Archival process not described.")
        if len(archival_lines) >= 2:
            archival_status = "pass"
        elif archival_lines:
            archival_status = "warning"
        else:
            archival_status = "fail"
        archival_score = normalize_score(archival_status)
        dimensions["archival"] = DimensionResult(
            archival_status,
            archival_score,
            archival_findings,
            archival_issues,
            [],
        )

        return dimensions


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate evidence package guidance")
    parser.add_argument("--protocol", help="Protocol ID to validate")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--summary", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    validator = EvidenceValidator(Path(args.workspace))
    return run_cli(validator, args.protocol, args.all, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())
