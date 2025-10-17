#!/usr/bin/env python3
"""
Evidence Manager for Unified Developer Workflow

Manages evidence artifacts including manifest.json, run.log, and validation.md
with SHA-256 checksums and ISO8601 timestamps for complete audit trail.
"""

import json
import hashlib
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import click

from .evidence_schema_converter import EvidenceSchemaConverter


class EvidenceManager:
    """Manages evidence artifacts for the unified workflow"""
    
    def __init__(self, evidence_root: str = "evidence"):
        self.evidence_root = Path(evidence_root)
        self.manifest_path = self.evidence_root / "manifest.json"
        self.run_log_path = self.evidence_root / "run.log"
        self.validation_path = self.evidence_root / "validation.md"
        
        # Ensure evidence directory exists
        self.evidence_root.mkdir(exist_ok=True)
        
        # Initialize evidence files if they don't exist
        self._initialize_evidence_files()
    
    def _initialize_evidence_files(self):
        """Initialize evidence files with proper structure"""
        
        # Initialize manifest.json
        if not self.manifest_path.exists():
            manifest = {
                "artifacts": [],
                "metadata": {
                    "project_name": "",
                    "workflow_version": "1.0.0",
                    "generated_at": self._get_timestamp(),
                    "total_artifacts": 0
                }
            }
            self._write_json(self.manifest_path, manifest)
        
        # Initialize run.log
        if not self.run_log_path.exists():
            run_log = {
                "entries": [],
                "metadata": {
                    "project_name": "",
                    "workflow_version": "1.0.0",
                    "total_entries": 0,
                    "last_updated": self._get_timestamp()
                }
            }
            self._write_json(self.run_log_path, run_log)
        
        # Initialize validation.md
        if not self.validation_path.exists():
            validation_content = """# Validation Report

## Phase Validation Status

| Phase | Status | Score | Findings | Recommendations | Validated At |
|-------|--------|-------|----------|-----------------|--------------|
"""
            self._write_file(self.validation_path, validation_content)
    
    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO8601 format"""
        return datetime.utcnow().isoformat() + "Z"
    
    def _calculate_checksum(self, file_path: Path) -> str:
        """Calculate SHA-256 checksum of a file"""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except FileNotFoundError:
            return ""
    
    def _write_json(self, file_path: Path, data: Dict[str, Any]):
        """Write JSON data to file with proper formatting"""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, sort_keys=True)
    
    def _write_file(self, file_path: Path, content: str):
        """Write content to file"""
        with open(file_path, 'w') as f:
            f.write(content)
    
    def _read_json(self, file_path: Path) -> Dict[str, Any]:
        """Read JSON data from file"""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def load_evidence(self, project_name: str = "", workflow_version: str = "1.0.0") -> Dict[str, Any]:
        """Load evidence, automatically converting from legacy format if needed.

        Args:
            project_name: Name of the project (for legacy conversion)
            workflow_version: Version of the workflow (for legacy conversion)

        Returns:
            Evidence in unified format
        """
        # Try to load as unified format first
        if self.manifest_path.exists():
            try:
                manifest = self._read_json(self.manifest_path)
                run_log = self._read_json(self.run_log_path)

                # Check if this looks like unified format
                if (isinstance(manifest, dict) and "artifacts" in manifest and
                    isinstance(run_log, dict) and "entries" in run_log):

                    # Load validation content
                    validation_content = ""
                    if self.validation_path.exists():
                        validation_content = self.validation_path.read_text()

                    return {
                        "manifest": manifest,
                        "run_log": run_log,
                        "validation": validation_content
                    }
            except Exception:
                pass

        # If not unified format, try to load as legacy format and convert
        if self.manifest_path.exists():
            try:
                legacy_evidence = self._read_json(self.manifest_path)

                # Check if this looks like legacy format (list of artifacts)
                if isinstance(legacy_evidence, list) and legacy_evidence:
                    first_item = legacy_evidence[0]
                    if isinstance(first_item, dict) and ("file" in first_item or "path" in first_item):
                        # This is legacy format, convert it
                        unified_evidence = EvidenceSchemaConverter.legacy_to_unified(
                            legacy_evidence,
                            project_name=project_name or "unknown",
                            workflow_version=workflow_version,
                            phase=0  # Default phase for legacy evidence
                        )

                        # Update our files with the converted format
                        self._write_json(self.manifest_path, unified_evidence["manifest"])
                        self._write_json(self.run_log_path, unified_evidence["run_log"])
                        self._write_file(self.validation_path, unified_evidence["validation"])

                        return unified_evidence
            except Exception:
                pass

        # If neither format works, return empty unified structure
        return {
            "manifest": {
                "artifacts": [],
                "metadata": {
                    "project_name": project_name,
                    "workflow_version": workflow_version,
                    "generated_at": self._get_timestamp(),
                    "total_artifacts": 0
                }
            },
            "run_log": {
                "entries": [],
                "metadata": {
                    "project_name": project_name,
                    "workflow_version": workflow_version,
                    "total_entries": 0,
                    "last_updated": self._get_timestamp()
                }
            },
            "validation": ""
        }
    
    def log_artifact(self, path: str, category: str, description: str, phase: int) -> bool:
        """
        Log an artifact to the manifest with checksum and timestamp
        
        Args:
            path: Relative path to the artifact
            category: Category of the artifact (documentation, code, config, etc.)
            description: Human-readable description
            phase: Phase number (0-6)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Calculate checksum if file exists (skip directories)
            file_path = Path(path)
            checksum = ""
            if file_path.exists() and file_path.is_file():
                checksum = self._calculate_checksum(file_path)
            
            # Create artifact entry
            artifact = {
                "path": path,
                "category": category,
                "description": description,
                "checksum": checksum,
                "created_at": self._get_timestamp(),
                "phase": phase
            }
            
            # Read current manifest
            manifest = self._read_json(self.manifest_path)
            
            # Add artifact
            manifest["artifacts"].append(artifact)
            manifest["metadata"]["total_artifacts"] = len(manifest["artifacts"])
            manifest["metadata"]["generated_at"] = self._get_timestamp()
            
            # Write updated manifest
            self._write_json(self.manifest_path, manifest)
            
            return True
            
        except Exception as e:
            print(f"Error logging artifact: {e}")
            return False
    
    def log_execution(self, phase: int, action: str, status: str, details: Optional[Dict] = None, duration_seconds: Optional[float] = None) -> bool:
        """
        Log execution entry to run.log
        
        Args:
            phase: Phase number (0-6)
            action: Action performed
            status: Status (started, completed, failed, skipped)
            details: Additional details
            duration_seconds: Duration in seconds
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Create execution entry
            entry = {
                "timestamp": self._get_timestamp(),
                "phase": phase,
                "action": action,
                "status": status
            }
            
            if details:
                entry["details"] = details
            
            if duration_seconds is not None:
                entry["duration_seconds"] = duration_seconds
            
            # Read current run log
            run_log = self._read_json(self.run_log_path)
            
            # Add entry
            run_log["entries"].append(entry)
            run_log["metadata"]["total_entries"] = len(run_log["entries"])
            run_log["metadata"]["last_updated"] = self._get_timestamp()
            
            # Write updated run log
            self._write_json(self.run_log_path, run_log)
            
            return True
            
        except Exception as e:
            print(f"Error logging execution: {e}")
            return False
    
    def log_validation(self, phase: int, status: str, score: float, findings: List[Dict], recommendations: List[str]) -> bool:
        """
        Log validation results to validation.md
        
        Args:
            phase: Phase number (0-6)
            status: Validation status (pending, in_progress, passed, failed, skipped)
            score: Quality score (0-10)
            findings: List of findings with severity, category, description, recommendation
            recommendations: List of recommendations
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Read current validation content
            validation_content = ""
            if self.validation_path.exists():
                with open(self.validation_path, 'r') as f:
                    validation_content = f.read()
            
            # Create validation entry
            timestamp = self._get_timestamp()
            findings_count = len(findings)
            critical_count = len([f for f in findings if f.get("severity") == "critical"])
            high_count = len([f for f in findings if f.get("severity") == "high"])
            
            # Add validation row
            validation_row = f"| {phase} | {status} | {score}/10 | {findings_count} findings ({critical_count} critical, {high_count} high) | {len(recommendations)} recommendations | {timestamp} |\n"
            
            # Append to validation content
            validation_content += validation_row
            
            # Write updated validation
            self._write_file(self.validation_path, validation_content)
            
            return True
            
        except Exception as e:
            print(f"Error logging validation: {e}")
            return False
    
    def validate_evidence(self, phase: Optional[int] = None) -> Dict[str, Any]:
        """
        Validate evidence completeness and integrity
        
        Args:
            phase: Specific phase to validate (None for all phases)
            
        Returns:
            Validation results with status and details
        """
        try:
            results = {
                "status": "passed",
                "issues": [],
                "summary": {}
            }
            
            # Read manifest
            manifest = self._read_json(self.manifest_path)
            artifacts = manifest.get("artifacts", [])
            
            # Filter by phase if specified
            if phase is not None:
                artifacts = [a for a in artifacts if a.get("phase") == phase]
            
            # Check artifact integrity
            for artifact in artifacts:
                file_path = Path(artifact["path"])
                if not file_path.exists():
                    results["issues"].append(f"Missing artifact: {artifact['path']}")
                    results["status"] = "failed"
                else:
                    # Verify checksum only for files
                    if file_path.is_file() and artifact["checksum"]:
                        current_checksum = self._calculate_checksum(file_path)
                        if current_checksum != artifact["checksum"]:
                            results["issues"].append(f"Checksum mismatch: {artifact['path']}")
                            results["status"] = "failed"
            
            # Read run log
            run_log = self._read_json(self.run_log_path)
            entries = run_log.get("entries", [])
            
            # Filter by phase if specified
            if phase is not None:
                entries = [e for e in entries if e.get("phase") == phase]
            
            # Check execution completeness
            phases_executed = set(e.get("phase") for e in entries)
            if phase is not None:
                if phase not in phases_executed:
                    results["issues"].append(f"No execution entries for phase {phase}")
                    results["status"] = "failed"
            else:
                expected_phases = set(range(7))  # 0-6
                missing_phases = expected_phases - phases_executed
                if missing_phases:
                    results["issues"].append(f"Missing execution entries for phases: {missing_phases}")
                    results["status"] = "failed"
            
            # Summary
            results["summary"] = {
                "total_artifacts": len(artifacts),
                "total_executions": len(entries),
                "phases_executed": sorted(phases_executed),
                "validation_timestamp": self._get_timestamp()
            }
            
            return results
            
        except Exception as e:
            return {
                "status": "error",
                "issues": [f"Validation error: {e}"],
                "summary": {}
            }
    
    def generate_report(self, phase_range: Optional[tuple] = None) -> Dict[str, Any]:
        """
        Generate comprehensive evidence report
        
        Args:
            phase_range: Tuple of (start_phase, end_phase) or None for all phases
            
        Returns:
            Comprehensive report with all evidence data
        """
        try:
            # Read all evidence files
            manifest = self._read_json(self.manifest_path)
            run_log = self._read_json(self.run_log_path)
            
            # Filter by phase range if specified
            if phase_range:
                start_phase, end_phase = phase_range
                manifest["artifacts"] = [
                    a for a in manifest["artifacts"] 
                    if start_phase <= a.get("phase", 0) <= end_phase
                ]
                run_log["entries"] = [
                    e for e in run_log["entries"]
                    if start_phase <= e.get("phase", 0) <= end_phase
                ]
            
            # Generate report
            report = {
                "metadata": {
                    "generated_at": self._get_timestamp(),
                    "phase_range": phase_range,
                    "total_artifacts": len(manifest["artifacts"]),
                    "total_executions": len(run_log["entries"])
                },
                "manifest": manifest,
                "run_log": run_log,
                "validation": self._read_validation_content(),
                "summary": self._generate_summary(manifest, run_log)
            }
            
            return report
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "metadata": {"generated_at": self._get_timestamp()}
            }
    
    def _read_validation_content(self) -> str:
        """Read validation.md content"""
        try:
            with open(self.validation_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ""
    
    def _generate_summary(self, manifest: Dict, run_log: Dict) -> Dict[str, Any]:
        """Generate summary statistics"""
        artifacts = manifest.get("artifacts", [])
        entries = run_log.get("entries", [])
        
        # Phase statistics
        phase_stats = {}
        for phase in range(7):
            phase_artifacts = [a for a in artifacts if a.get("phase") == phase]
            phase_entries = [e for e in entries if e.get("phase") == phase]
            
            phase_stats[phase] = {
                "artifacts": len(phase_artifacts),
                "executions": len(phase_entries),
                "categories": list(set(a.get("category", "") for a in phase_artifacts))
            }
        
        # Category statistics
        category_stats = {}
        for artifact in artifacts:
            category = artifact.get("category", "unknown")
            category_stats[category] = category_stats.get(category, 0) + 1
        
        # Status statistics
        status_stats = {}
        for entry in entries:
            status = entry.get("status", "unknown")
            status_stats[status] = status_stats.get(status, 0) + 1
        
        return {
            "phase_stats": phase_stats,
            "category_stats": category_stats,
            "status_stats": status_stats,
            "total_duration": sum(e.get("duration_seconds", 0) for e in entries)
        }


# CLI Interface
@click.group()
def cli():
    """Evidence Manager CLI for Unified Developer Workflow"""
    pass


@cli.command()
@click.option('--path', required=True, help='Path to artifact')
@click.option('--category', required=True, help='Category of artifact')
@click.option('--description', required=True, help='Description of artifact')
@click.option('--phase', type=int, required=True, help='Phase number (0-6)')
def log_artifact(path, category, description, phase):
    """Log an artifact to the manifest"""
    manager = EvidenceManager()
    success = manager.log_artifact(path, category, description, phase)
    if success:
        click.echo(f"✅ Artifact logged: {path}")
    else:
        click.echo(f"❌ Failed to log artifact: {path}")
        exit(1)


@cli.command()
@click.option('--phase', type=int, required=True, help='Phase number (0-6)')
@click.option('--action', required=True, help='Action performed')
@click.option('--status', required=True, help='Status (started, completed, failed, skipped)')
@click.option('--details', help='Additional details (JSON)')
@click.option('--duration', type=float, help='Duration in seconds')
def log_execution(phase, action, status, details, duration):
    """Log execution entry to run.log"""
    manager = EvidenceManager()
    
    # Parse details if provided
    details_dict = None
    if details:
        try:
            details_dict = json.loads(details)
        except json.JSONDecodeError:
            click.echo("❌ Invalid JSON in details")
            exit(1)
    
    success = manager.log_execution(phase, action, status, details_dict, duration)
    if success:
        click.echo(f"✅ Execution logged: Phase {phase} - {action} - {status}")
    else:
        click.echo(f"❌ Failed to log execution")
        exit(1)


@cli.command()
@click.option('--phase', type=int, help='Specific phase to validate')
def validate(phase):
    """Validate evidence completeness and integrity"""
    manager = EvidenceManager()
    results = manager.validate_evidence(phase)
    
    if results["status"] == "passed":
        click.echo("✅ Evidence validation passed")
    elif results["status"] == "failed":
        click.echo("❌ Evidence validation failed")
        for issue in results["issues"]:
            click.echo(f"  - {issue}")
    else:
        click.echo("❌ Evidence validation error")
        for issue in results["issues"]:
            click.echo(f"  - {issue}")
    
    # Print summary
    summary = results.get("summary", {})
    if summary:
        click.echo(f"\nSummary:")
        click.echo(f"  Total artifacts: {summary.get('total_artifacts', 0)}")
        click.echo(f"  Total executions: {summary.get('total_executions', 0)}")
        click.echo(f"  Phases executed: {summary.get('phases_executed', [])}")


@cli.command()
@click.option('--start-phase', type=int, help='Start phase for range')
@click.option('--end-phase', type=int, help='End phase for range')
@click.option('--output', help='Output file path')
def report(start_phase, end_phase, output):
    """Generate comprehensive evidence report"""
    manager = EvidenceManager()
    
    # Determine phase range
    phase_range = None
    if start_phase is not None and end_phase is not None:
        phase_range = (start_phase, end_phase)
    
    # Generate report
    report_data = manager.generate_report(phase_range)
    
    # Output report
    if output:
        with open(output, 'w') as f:
            json.dump(report_data, f, indent=2, sort_keys=True)
        click.echo(f"✅ Report generated: {output}")
    else:
        click.echo(json.dumps(report_data, indent=2, sort_keys=True))


if __name__ == "__main__":
    cli()
