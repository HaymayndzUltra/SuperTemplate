#!/usr/bin/env python3
"""
Test suite for Evidence Manager

Tests evidence tracking, validation, and reporting functionality.
"""

import pytest
import json
import tempfile
import shutil
from pathlib import Path
from datetime import datetime
import sys
import os

# Add the automation directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "automation"))

from evidence_manager import EvidenceManager


class TestEvidenceManager:
    """Test cases for EvidenceManager"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.evidence_manager = EvidenceManager(self.temp_dir)
    
    def teardown_method(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir)
    
    def test_initialization(self):
        """Test EvidenceManager initialization"""
        assert self.evidence_manager.evidence_root.exists()
        assert self.evidence_manager.manifest_path.exists()
        assert self.evidence_manager.run_log_path.exists()
        assert self.evidence_manager.validation_path.exists()
    
    def test_log_artifact(self):
        """Test artifact logging"""
        # Create a test file
        test_file = Path(self.temp_dir) / "test.txt"
        test_file.write_text("test content")
        
        # Log artifact
        success = self.evidence_manager.log_artifact(
            path=str(test_file),
            category="test",
            description="Test artifact",
            phase=0
        )
        
        assert success
        
        # Verify manifest
        manifest = self.evidence_manager._read_json(self.evidence_manager.manifest_path)
        assert len(manifest["artifacts"]) == 1
        assert manifest["artifacts"][0]["path"] == str(test_file)
        assert manifest["artifacts"][0]["category"] == "test"
        assert manifest["artifacts"][0]["phase"] == 0
    
    def test_log_execution(self):
        """Test execution logging"""
        # Log execution
        success = self.evidence_manager.log_execution(
            phase=0,
            action="test_action",
            status="completed",
            details={"test": "value"},
            duration_seconds=1.5
        )
        
        assert success
        
        # Verify run log
        run_log = self.evidence_manager._read_json(self.evidence_manager.run_log_path)
        assert len(run_log["entries"]) == 1
        assert run_log["entries"][0]["phase"] == 0
        assert run_log["entries"][0]["action"] == "test_action"
        assert run_log["entries"][0]["status"] == "completed"
        assert run_log["entries"][0]["duration_seconds"] == 1.5
    
    def test_log_validation(self):
        """Test validation logging"""
        # Log validation
        success = self.evidence_manager.log_validation(
            phase=0,
            status="passed",
            score=8.5,
            findings=[
                {
                    "severity": "medium",
                    "category": "test",
                    "description": "Test finding",
                    "recommendation": "Test recommendation"
                }
            ],
            recommendations=["Test recommendation"]
        )
        
        assert success
        
        # Verify validation file was updated
        validation_content = self.evidence_manager._read_validation_content()
        assert "0" in validation_content
        assert "passed" in validation_content
        assert "8.5" in validation_content
    
    def test_validate_evidence(self):
        """Test evidence validation"""
        # Create test file
        test_file = Path("test.txt")
        test_file.write_text("Test content")
        
        # Log some test data
        self.evidence_manager.log_artifact(
            path="test.txt",
            category="test",
            description="Test artifact",
            phase=0
        )
        
        self.evidence_manager.log_execution(
            phase=0,
            action="test_action",
            status="completed"
        )
        
        # Validate evidence for specific phase
        results = self.evidence_manager.validate_evidence(phase=0)
        
        # Clean up
        test_file.unlink()
        
        assert results["status"] == "passed"
        assert results["summary"]["total_artifacts"] == 1
        assert results["summary"]["total_executions"] == 1
    
    def test_validate_evidence_missing_file(self):
        """Test evidence validation with missing file"""
        # Log artifact for non-existent file
        self.evidence_manager.log_artifact(
            path="nonexistent.txt",
            category="test",
            description="Non-existent artifact",
            phase=0
        )
        
        # Validate evidence
        results = self.evidence_manager.validate_evidence()
        
        assert results["status"] == "failed"
        assert len(results["issues"]) > 0
        assert "Missing artifact" in results["issues"][0]
    
    def test_generate_report(self):
        """Test report generation"""
        # Log some test data
        self.evidence_manager.log_artifact(
            path="test.txt",
            category="test",
            description="Test artifact",
            phase=0
        )
        
        self.evidence_manager.log_execution(
            phase=0,
            action="test_action",
            status="completed"
        )
        
        # Generate report
        report = self.evidence_manager.generate_report()
        
        assert "metadata" in report
        assert "manifest" in report
        assert "run_log" in report
        assert "validation" in report
        assert "summary" in report
        
        assert report["metadata"]["total_artifacts"] == 1
        assert report["metadata"]["total_executions"] == 1
    
    def test_generate_report_phase_range(self):
        """Test report generation with phase range"""
        # Log data for different phases
        for phase in range(3):
            self.evidence_manager.log_artifact(
                path=f"test{phase}.txt",
                category="test",
                description=f"Test artifact {phase}",
                phase=phase
            )
        
        # Generate report for phases 1-2
        report = self.evidence_manager.generate_report((1, 2))
        
        assert report["metadata"]["total_artifacts"] == 2
        assert report["metadata"]["phase_range"] == (1, 2)
    
    def test_checksum_calculation(self):
        """Test checksum calculation"""
        # Create test file
        test_file = Path(self.temp_dir) / "checksum_test.txt"
        test_file.write_text("test content for checksum")
        
        # Calculate checksum
        checksum = self.evidence_manager._calculate_checksum(test_file)
        
        assert len(checksum) == 64  # SHA-256 hex length
        assert checksum.isalnum()
    
    def test_checksum_verification(self):
        """Test checksum verification"""
        # Create test file
        test_file = Path(self.temp_dir) / "checksum_verify.txt"
        test_file.write_text("test content")
        
        # Log artifact
        self.evidence_manager.log_artifact(
            path=str(test_file),
            category="test",
            description="Test artifact",
            phase=0
        )
        
        # Modify file
        test_file.write_text("modified content")
        
        # Validate evidence
        results = self.evidence_manager.validate_evidence()
        
        assert results["status"] == "failed"
        assert len(results["issues"]) > 0
        assert "Checksum mismatch" in results["issues"][0]


if __name__ == "__main__":
    pytest.main([__file__])
