#!/usr/bin/env python3
"""Migration script for historical evidence data.

This script scans for legacy evidence files and migrates them to the unified format,
ensuring backward compatibility and data preservation.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, List, Any
import sys

# Add unified-workflow to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "unified-workflow"))

from scripts.evidence_schema_converter import EvidenceSchemaConverter

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)


class EvidenceMigrator:
    """Migrates historical evidence data from legacy to unified format."""

    def __init__(self, base_path: Path, dry_run: bool = False):
        """Initialize the migrator.

        Args:
            base_path: Base directory to scan for evidence files
            dry_run: If True, only analyze without making changes
        """
        self.base_path = Path(base_path)
        self.dry_run = dry_run
        self.stats = {
            'files_found': 0,
            'files_migrated': 0,
            'files_skipped': 0,
            'errors': 0
        }

    def find_evidence_files(self) -> List[Path]:
        """Find all evidence files in the project.

        Returns:
            List of paths to evidence files
        """
        evidence_files = []

        # Common locations for evidence files
        search_patterns = [
            "**/evidence/**/*.json",  # Evidence directories
            "**/*evidence*.json",     # Files with evidence in name
            "**/artifacts.json",      # Artifact lists
            "**/workflow_log.json",   # Workflow logs
        ]

        for pattern in search_patterns:
            for evidence_file in self.base_path.glob(pattern):
                if evidence_file.is_file():
                    evidence_files.append(evidence_file)

        logger.info(f"Found {len(evidence_files)} potential evidence files")
        return evidence_files

    def analyze_evidence_file(self, file_path: Path) -> Dict[str, Any]:
        """Analyze an evidence file to determine its format and content.

        Args:
            file_path: Path to the evidence file

        Returns:
            Analysis results
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)

            # Determine format
            if isinstance(content, list):
                # Legacy format: list of artifacts
                format_type = "legacy"
                artifact_count = len(content)
                has_phase_info = any("phase" in item for item in content)
            elif isinstance(content, dict):
                # Unified format: dict with manifest, run_log, validation
                if "manifest" in content and "run_log" in content and "validation" in content:
                    format_type = "unified"
                else:
                    format_type = "unknown_dict"
                artifact_count = len(content.get("manifest", {}).get("artifacts", []))
                has_phase_info = True  # Unified format always has phase info
            else:
                format_type = "unknown"
                artifact_count = 0
                has_phase_info = False

            return {
                'format': format_type,
                'artifact_count': artifact_count,
                'has_phase_info': has_phase_info,
                'file_size': file_path.stat().st_size,
                'needs_migration': format_type == "legacy"
            }

        except Exception as e:
            logger.error(f"Error analyzing {file_path}: {e}")
            return {
                'format': 'error',
                'artifact_count': 0,
                'has_phase_info': False,
                'file_size': file_path.stat().st_size,
                'needs_migration': False,
                'error': str(e)
            }

    def migrate_evidence_file(self, file_path: Path) -> bool:
        """Migrate a single evidence file from legacy to unified format.

        Args:
            file_path: Path to the evidence file

        Returns:
            True if migration successful, False otherwise
        """
        try:
            logger.info(f"Migrating: {file_path}")

            # Read legacy evidence
            with open(file_path, 'r', encoding='utf-8') as f:
                legacy_evidence = json.load(f)

            if not isinstance(legacy_evidence, list):
                logger.warning(f"Skipping non-legacy file: {file_path}")
                return False

            # Extract project info from path or use defaults
            project_name = self._extract_project_name(file_path)
            workflow_version = self._extract_workflow_version(file_path)

            # Convert to unified format
            unified_evidence = EvidenceSchemaConverter.legacy_to_unified(
                legacy_evidence,
                project_name=project_name,
                workflow_version=workflow_version,
                phase=0  # Default phase, can be enhanced later
            )

            if not self.dry_run:
                # Create backup
                backup_path = file_path.with_suffix('.json.backup')
                if not backup_path.exists():
                    import shutil
                    shutil.copy2(file_path, backup_path)
                    logger.info(f"Created backup: {backup_path}")

                # Write unified format
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(unified_evidence, f, indent=2)

                logger.info(f"Migrated: {file_path}")
            else:
                logger.info(f"Would migrate (dry run): {file_path}")

            return True

        except Exception as e:
            logger.error(f"Error migrating {file_path}: {e}")
            self.stats['errors'] += 1
            return False

    def _extract_project_name(self, file_path: Path) -> str:
        """Extract project name from file path or use default."""
        # Try to find project name from path components
        parts = file_path.parts
        for part in reversed(parts):
            if part not in ['evidence', 'artifacts', 'workflow']:
                return part

        # Fallback to filename
        return file_path.stem

    def _extract_workflow_version(self, file_path: Path) -> str:
        """Extract workflow version from file path or use default."""
        # Look for version indicators in path
        for part in file_path.parts:
            if 'v' in part and any(c.isdigit() for c in part):
                return part

        # Default version
        return "1.0.0"

    def run_migration(self) -> Dict[str, Any]:
        """Run the complete migration process.

        Returns:
            Migration statistics
        """
        logger.info(f"Starting evidence migration (dry_run={self.dry_run})")
        logger.info(f"Base path: {self.base_path}")

        # Find evidence files
        evidence_files = self.find_evidence_files()
        self.stats['files_found'] = len(evidence_files)

        # Analyze each file
        migration_candidates = []
        for file_path in evidence_files:
            analysis = self.analyze_evidence_file(file_path)
            if analysis['needs_migration']:
                migration_candidates.append((file_path, analysis))

        logger.info(f"Found {len(migration_candidates)} files needing migration")

        # Migrate files
        for file_path, analysis in migration_candidates:
            if self.migrate_evidence_file(file_path):
                self.stats['files_migrated'] += 1
            else:
                self.stats['files_skipped'] += 1

        logger.info("Migration completed")
        logger.info(f"Statistics: {self.stats}")

        return self.stats


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Migrate historical evidence data from legacy to unified format"
    )
    parser.add_argument(
        "--base-path",
        default=".",
        help="Base directory to scan for evidence files (default: current directory)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Analyze only, don't make changes"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Run migration
    migrator = EvidenceMigrator(Path(args.base_path), dry_run=args.dry_run)
    stats = migrator.run_migration()

    # Exit with appropriate code
    if stats['errors'] > 0:
        print(f"\n❌ Migration completed with {stats['errors']} errors")
        return 1
    elif stats['files_migrated'] > 0 or args.dry_run:
        print("\n✅ Migration completed successfully")
        return 0
    else:
        print("\nℹ️ No files needed migration")
        return 0


if __name__ == "__main__":
    exit(main())

