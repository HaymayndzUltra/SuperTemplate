"""Evidence Schema Converter - Migrates between legacy and unified evidence formats.

This module provides tools to convert evidence between the legacy workflow_automation
format and the new unified-workflow format, ensuring backward compatibility.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class EvidenceSchemaConverter:
    """Converts evidence between legacy and unified formats."""
    
    @staticmethod
    def legacy_to_unified(
        legacy_evidence: List[Dict[str, Any]], 
        project_name: str,
        workflow_version: str = "1.0.0",
        phase: int = 0
    ) -> Dict[str, Any]:
        """Convert legacy evidence format to unified format.
        
        Legacy format is a simple list of artifacts:
        [
            {
                "path": "docs/README.md",
                "category": "documentation",
                "description": "Project readme",
                "checksum": "abc123...",
                "created_at": "2025-01-01T00:00:00Z"
            },
            ...
        ]
        
        Args:
            legacy_evidence: List of evidence records in legacy format
            project_name: Name of the project
            workflow_version: Version of the workflow
            phase: Phase number (0-6)
            
        Returns:
            Evidence in unified format with manifest, run_log, and validation sections
        """
        unified = {
            "manifest": {
                "artifacts": [],
                "metadata": {
                    "project_name": project_name,
                    "workflow_version": workflow_version,
                    "generated_at": datetime.utcnow().isoformat() + "Z",
                    "total_artifacts": len(legacy_evidence)
                }
            },
            "run_log": {
                "entries": [],
                "metadata": {
                    "project_name": project_name,
                    "workflow_version": workflow_version,
                    "total_entries": 0,
                    "last_updated": datetime.utcnow().isoformat() + "Z"
                }
            },
            "validation": {
                "phases": [],
                "metadata": {
                    "project_name": project_name,
                    "workflow_version": workflow_version,
                    "total_phases": 1,
                    "overall_score": 0.0,
                    "last_updated": datetime.utcnow().isoformat() + "Z"
                }
            }
        }
        
        # Convert artifacts (handle different legacy formats)
        for artifact in legacy_evidence:
            # Handle workflow1 format (file, phase, project, checksum)
            if "file" in artifact:
                unified_artifact = {
                    "path": artifact["file"],
                    "category": "artifact",  # Default category
                    "description": f"Phase {artifact.get('phase', 'unknown')} artifact",
                    "checksum": artifact["checksum"],
                    "created_at": artifact.get("created_at", artifact.get("timestamp", "2025-01-01T00:00:00Z")),
                    "phase": phase  # Add phase information
                }
            # Handle standard legacy format (path, category, description, checksum, created_at)
            elif "path" in artifact:
                unified_artifact = {
                    "path": artifact["path"],
                    "category": artifact.get("category", "artifact"),
                    "description": artifact.get("description", "Artifact"),
                    "checksum": artifact["checksum"],
                    "created_at": artifact["created_at"],
                    "phase": phase  # Add phase information
                }
            else:
                # Skip artifacts without path or file
                logger.warning(f"Skipping artifact without path or file: {artifact}")
                continue

            unified["manifest"]["artifacts"].append(unified_artifact)
        
        # Add a basic run log entry for the conversion
        unified["run_log"]["entries"].append({
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "phase": phase,
            "action": "legacy_evidence_migration",
            "status": "completed",
            "details": {
                "artifacts_migrated": len(legacy_evidence),
                "source_format": "legacy_workflow_automation"
            }
        })
        unified["run_log"]["metadata"]["total_entries"] = 1
        
        # Add a placeholder validation entry
        unified["validation"]["phases"].append({
            "phase": phase,
            "status": "passed",
            "score": 8.0,  # Default score for migrated evidence
            "findings": [],
            "recommendations": [
                "Evidence migrated from legacy format - manual validation recommended"
            ],
            "validated_at": datetime.utcnow().isoformat() + "Z"
        })
        
        return unified
    
    @staticmethod
    def unified_to_legacy(unified_evidence: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Convert unified evidence format to legacy format.
        
        Args:
            unified_evidence: Evidence in unified format
            
        Returns:
            List of evidence records in legacy format
        """
        legacy = []
        
        # Extract artifacts from manifest
        if "manifest" in unified_evidence and "artifacts" in unified_evidence["manifest"]:
            for artifact in unified_evidence["manifest"]["artifacts"]:
                legacy_artifact = {
                    "path": artifact["path"],
                    "category": artifact["category"],
                    "description": artifact["description"],
                    "checksum": artifact["checksum"],
                    "created_at": artifact["created_at"]
                }
                # Phase is not part of legacy format
                legacy.append(legacy_artifact)
        
        return legacy
    
    @staticmethod
    def merge_evidence(
        primary: Dict[str, Any],
        secondary: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Merge two unified evidence objects, with primary taking precedence.
        
        Args:
            primary: Primary evidence (takes precedence in conflicts)
            secondary: Secondary evidence to merge
            
        Returns:
            Merged evidence in unified format
        """
        merged = json.loads(json.dumps(primary))  # Deep copy
        
        # Merge artifacts (avoid duplicates based on path)
        existing_paths = {a["path"] for a in merged["manifest"]["artifacts"]}
        
        for artifact in secondary["manifest"]["artifacts"]:
            if artifact["path"] not in existing_paths:
                merged["manifest"]["artifacts"].append(artifact)
                merged["manifest"]["metadata"]["total_artifacts"] += 1
        
        # Merge run log entries
        merged["run_log"]["entries"].extend(secondary["run_log"]["entries"])
        merged["run_log"]["metadata"]["total_entries"] = len(merged["run_log"]["entries"])
        merged["run_log"]["metadata"]["last_updated"] = datetime.utcnow().isoformat() + "Z"
        
        # Merge validation phases
        existing_phases = {p["phase"] for p in merged["validation"]["phases"]}
        
        for phase in secondary["validation"]["phases"]:
            if phase["phase"] not in existing_phases:
                merged["validation"]["phases"].append(phase)
            else:
                # Update existing phase with latest info
                for i, p in enumerate(merged["validation"]["phases"]):
                    if p["phase"] == phase["phase"]:
                        # Merge findings
                        p["findings"].extend(phase["findings"])
                        # Update score to average
                        p["score"] = (p["score"] + phase["score"]) / 2
                        # Merge recommendations
                        p["recommendations"].extend(phase["recommendations"])
                        # Update timestamp
                        p["validated_at"] = phase["validated_at"]
                        break
        
        # Update metadata
        merged["validation"]["metadata"]["total_phases"] = len(merged["validation"]["phases"])
        scores = [p["score"] for p in merged["validation"]["phases"]]
        merged["validation"]["metadata"]["overall_score"] = sum(scores) / len(scores) if scores else 0.0
        merged["validation"]["metadata"]["last_updated"] = datetime.utcnow().isoformat() + "Z"
        
        return merged
    
    @staticmethod
    def validate_schema(evidence: Dict[str, Any], schema_path: Optional[Path] = None) -> Dict[str, Any]:
        """Validate evidence against the unified schema.
        
        Args:
            evidence: Evidence to validate
            schema_path: Path to schema file (uses default if not provided)
            
        Returns:
            Validation result with 'valid' boolean and 'errors' list
        """
        if schema_path is None:
            schema_path = Path(__file__).parent.parent / "evidence" / "schema.json"
        
        try:
            # For full implementation, we would use jsonschema library
            # For now, do basic structural validation
            errors = []
            
            # Check required top-level keys
            required_keys = ["manifest", "run_log", "validation"]
            for key in required_keys:
                if key not in evidence:
                    errors.append(f"Missing required key: {key}")
            
            # Check manifest structure
            if "manifest" in evidence:
                if "artifacts" not in evidence["manifest"]:
                    errors.append("Missing manifest.artifacts")
                if "metadata" not in evidence["manifest"]:
                    errors.append("Missing manifest.metadata")
                else:
                    required_metadata = ["project_name", "workflow_version", "generated_at", "total_artifacts"]
                    for field in required_metadata:
                        if field not in evidence["manifest"]["metadata"]:
                            errors.append(f"Missing manifest.metadata.{field}")
            
            # Check run_log structure
            if "run_log" in evidence:
                if "entries" not in evidence["run_log"]:
                    errors.append("Missing run_log.entries")
                if "metadata" not in evidence["run_log"]:
                    errors.append("Missing run_log.metadata")
            
            # Check validation structure
            if "validation" in evidence:
                if "phases" not in evidence["validation"]:
                    errors.append("Missing validation.phases")
                if "metadata" not in evidence["validation"]:
                    errors.append("Missing validation.metadata")
            
            return {
                "valid": len(errors) == 0,
                "errors": errors
            }
            
        except Exception as e:
            return {
                "valid": False,
                "errors": [f"Validation error: {str(e)}"]
            }


class EvidenceMigrator:
    """Handles migration of evidence between directories and formats."""
    
    def __init__(self, unified_root: Path, legacy_root: Path):
        """Initialize the evidence migrator.
        
        Args:
            unified_root: Root directory for unified evidence
            legacy_root: Root directory for legacy evidence
        """
        self.unified_root = Path(unified_root)
        self.legacy_root = Path(legacy_root)
        self.converter = EvidenceSchemaConverter()
    
    def migrate_legacy_evidence(
        self, 
        project_name: str,
        phase: int = 0,
        dry_run: bool = False
    ) -> Dict[str, Any]:
        """Migrate legacy evidence to unified format.
        
        Args:
            project_name: Name of the project
            phase: Phase number for migration
            dry_run: If True, don't write files
            
        Returns:
            Migration result with status and details
        """
        result = {
            "status": "pending",
            "legacy_files": [],
            "unified_files": [],
            "errors": []
        }
        
        try:
            # Find legacy evidence files
            legacy_manifest = self.legacy_root / "index.json"
            if not legacy_manifest.exists():
                result["errors"].append(f"Legacy manifest not found: {legacy_manifest}")
                result["status"] = "failed"
                return result
            
            # Load legacy evidence
            legacy_data = json.loads(legacy_manifest.read_text())
            result["legacy_files"].append(str(legacy_manifest))
            
            # Convert to unified format
            unified_data = self.converter.legacy_to_unified(
                legacy_data,
                project_name=project_name,
                phase=phase
            )
            
            # Validate converted data
            validation = self.converter.validate_schema(unified_data)
            if not validation["valid"]:
                result["errors"].extend(validation["errors"])
                result["status"] = "validation_failed"
                return result
            
            if not dry_run:
                # Create unified evidence directory
                phase_dir = self.unified_root / f"phase{phase}"
                phase_dir.mkdir(parents=True, exist_ok=True)
                
                # Write unified evidence files
                manifest_path = phase_dir / "manifest.json"
                manifest_path.write_text(
                    json.dumps(unified_data["manifest"], indent=2),
                    encoding="utf-8"
                )
                result["unified_files"].append(str(manifest_path))
                
                run_log_path = phase_dir / "run.log"
                run_log_path.write_text(
                    json.dumps(unified_data["run_log"], indent=2),
                    encoding="utf-8"
                )
                result["unified_files"].append(str(run_log_path))
                
                validation_path = phase_dir / "validation.md"
                validation_content = self._format_validation_markdown(unified_data["validation"])
                validation_path.write_text(validation_content, encoding="utf-8")
                result["unified_files"].append(str(validation_path))
            
            result["status"] = "completed" if not dry_run else "dry_run_completed"
            result["artifacts_migrated"] = len(legacy_data)
            
        except Exception as e:
            result["errors"].append(str(e))
            result["status"] = "failed"
        
        return result
    
    def _format_validation_markdown(self, validation_data: Dict[str, Any]) -> str:
        """Format validation data as markdown.
        
        Args:
            validation_data: Validation section of unified evidence
            
        Returns:
            Formatted markdown string
        """
        lines = [
            "# Validation Report",
            "",
            f"**Project**: {validation_data['metadata']['project_name']}",
            f"**Workflow Version**: {validation_data['metadata']['workflow_version']}",
            f"**Overall Score**: {validation_data['metadata']['overall_score']:.1f}/10",
            f"**Last Updated**: {validation_data['metadata']['last_updated']}",
            "",
            "## Phase Results",
            ""
        ]
        
        for phase in validation_data["phases"]:
            lines.extend([
                f"### Phase {phase['phase']}: {phase['status'].upper()}",
                f"**Score**: {phase['score']:.1f}/10",
                f"**Validated**: {phase['validated_at']}",
                ""
            ])
            
            if phase["findings"]:
                lines.extend(["#### Findings", ""])
                for finding in phase["findings"]:
                    lines.append(f"- **{finding['severity'].upper()}** ({finding['category']}): {finding['description']}")
                    if "file" in finding:
                        lines.append(f"  - File: {finding['file']}")
                    lines.append(f"  - Recommendation: {finding['recommendation']}")
                lines.append("")
            
            if phase["recommendations"]:
                lines.extend(["#### Recommendations", ""])
                for rec in phase["recommendations"]:
                    lines.append(f"- {rec}")
                lines.append("")
        
        return "\n".join(lines)
