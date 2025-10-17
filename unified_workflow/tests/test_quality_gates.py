#!/usr/bin/env python3
"""
Test suite for Quality Gates

Tests quality validation, audit execution, and reporting functionality.
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

from quality_gates import QualityGates


class TestQualityGates:
    """Test cases for QualityGates"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.project_name = "test-project"
        self.quality_gates = QualityGates(self.project_name, self.temp_dir)
    
    def teardown_method(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir)
    
    def test_initialization(self):
        """Test QualityGates initialization"""
        assert self.quality_gates.project_name == self.project_name
        assert self.quality_gates.project_dir.exists()
        assert self.quality_gates.evidence_manager is not None
    
    def test_execute_quality_gate(self):
        """Test single quality gate execution"""
        result = self.quality_gates.execute_quality_gate("quick")
        
        assert result["mode"] == "quick"
        assert "findings" in result
        assert "score" in result
        assert "recommendations" in result
        assert "duration" in result
        assert "status" in result
        
        assert 0 <= result["score"] <= 10
        assert result["status"] in ["passed", "failed"]
        assert isinstance(result["findings"], list)
        assert isinstance(result["recommendations"], list)
    
    def test_execute_quality_gate_with_context(self):
        """Test quality gate execution with context"""
        context = {
            "project_name": self.project_name,
            "description": "Test quality gate",
            "tech_stack": ["react", "nodejs"]
        }
        
        result = self.quality_gates.execute_quality_gate("security", context)
        
        assert result["mode"] == "security"
        assert result["status"] in ["passed", "failed"]
        assert len(result["findings"]) >= 0
        assert len(result["recommendations"]) >= 0
    
    def test_execute_comprehensive_audit(self):
        """Test comprehensive audit execution"""
        result = self.quality_gates.execute_comprehensive_audit()
        
        assert result["mode"] == "comprehensive"
        assert "overall_score" in result
        assert "overall_status" in result
        assert "layer_results" in result
        assert "total_findings" in result
        assert "all_recommendations" in result
        assert "duration" in result
        
        assert 0 <= result["overall_score"] <= 10
        assert result["overall_status"] in ["passed", "failed"]
        assert len(result["layer_results"]) == 6  # All 6 layers
        assert isinstance(result["total_findings"], list)
        assert isinstance(result["all_recommendations"], list)
    
    def test_generate_findings(self):
        """Test findings generation for different modes"""
        test_modes = ["quick", "security", "architecture", "design", "ui", "deep-security"]
        
        for mode in test_modes:
            findings = self.quality_gates._generate_findings(mode, {})
            
            assert isinstance(findings, list)
            
            for finding in findings:
                assert "severity" in finding
                assert "category" in finding
                assert "description" in finding
                assert "recommendation" in finding
                
                assert finding["severity"] in ["critical", "high", "medium", "low"]
    
    def test_calculate_score(self):
        """Test score calculation"""
        # Test with no findings
        findings = []
        score = self.quality_gates._calculate_score(findings)
        assert score == 10.0
        
        # Test with different severity findings
        findings = [
            {"severity": "critical"},
            {"severity": "high"},
            {"severity": "medium"},
            {"severity": "low"}
        ]
        score = self.quality_gates._calculate_score(findings)
        assert 0 <= score <= 10
        assert score < 10.0  # Should be penalized
    
    def test_generate_recommendations(self):
        """Test recommendations generation"""
        findings = [
            {
                "severity": "high",
                "category": "security",
                "description": "Test finding",
                "recommendation": "Fix security issue"
            }
        ]
        
        recommendations = self.quality_gates._generate_recommendations(findings, "security")
        
        assert isinstance(recommendations, list)
        assert len(recommendations) > 0
        assert "Fix security issue" in recommendations
    
    def test_evidence_logging(self):
        """Test evidence logging during quality gate execution"""
        result = self.quality_gates.execute_quality_gate("quick")
        
        # Check that evidence was logged
        manifest = self.quality_gates.evidence_manager._read_json(
            self.quality_gates.evidence_manager.manifest_path
        )
        run_log = self.quality_gates.evidence_manager._read_json(
            self.quality_gates.evidence_manager.run_log_path
        )
        
        assert len(run_log["entries"]) > 0
        
        # Verify quality gate evidence
        quality_entries = [e for e in run_log["entries"] if "Quality Gate" in e["action"]]
        assert len(quality_entries) > 0
    
    def test_different_audit_modes(self):
        """Test different audit modes"""
        test_modes = ["quick", "security", "architecture", "design", "ui", "deep-security"]
        
        for mode in test_modes:
            result = self.quality_gates.execute_quality_gate(mode)
            
            assert result["mode"] == mode
            assert result["status"] in ["passed", "failed"]
            assert 0 <= result["score"] <= 10
            assert isinstance(result["findings"], list)
            assert isinstance(result["recommendations"], list)
    
    def test_comprehensive_audit_layers(self):
        """Test comprehensive audit layer execution"""
        result = self.quality_gates.execute_comprehensive_audit()
        
        # Check that all layers were executed
        expected_modes = ["quick", "security", "architecture", "design", "ui", "deep-security"]
        executed_modes = [layer["mode"] for layer in result["layer_results"]]
        
        assert set(executed_modes) == set(expected_modes)
        
        # Check that each layer has results
        for layer_result in result["layer_results"]:
            assert "mode" in layer_result
            assert "score" in layer_result
            assert "status" in layer_result
            assert "findings" in layer_result
            assert "recommendations" in layer_result
    
    def test_quality_gate_duration(self):
        """Test quality gate duration tracking"""
        result = self.quality_gates.execute_quality_gate("quick")
        
        assert "duration" in result
        assert result["duration"] > 0
        assert result["duration"] < 10  # Should be quick in test environment
    
    def test_findings_structure(self):
        """Test findings structure"""
        findings = self.quality_gates._generate_findings("security", {})
        
        for finding in findings:
            assert "severity" in finding
            assert "category" in finding
            assert "description" in finding
            assert "recommendation" in finding
            
            # Optional fields
            if "file" in finding:
                assert isinstance(finding["file"], str)
            if "line" in finding:
                assert isinstance(finding["line"], int)
    
    def test_recommendations_deduplication(self):
        """Test recommendations deduplication"""
        findings = [
            {"severity": "high", "recommendation": "Fix issue 1"},
            {"severity": "medium", "recommendation": "Fix issue 1"},  # Duplicate
            {"severity": "low", "recommendation": "Fix issue 2"}
        ]
        
        recommendations = self.quality_gates._generate_recommendations(findings, "quick")
        
        # Should not have duplicates
        assert len(recommendations) == len(set(recommendations))
        assert "Fix issue 1" in recommendations
        assert "Fix issue 2" in recommendations
    
    def test_score_boundaries(self):
        """Test score boundary conditions"""
        # Test maximum score (no findings)
        findings = []
        score = self.quality_gates._calculate_score(findings)
        assert score == 10.0
        
        # Test minimum score (many critical findings)
        findings = [{"severity": "critical"} for _ in range(10)]
        score = self.quality_gates._calculate_score(findings)
        assert score == 0.0
        
        # Test score range
        findings = [{"severity": "medium"}]
        score = self.quality_gates._calculate_score(findings)
        assert 0 <= score <= 10


if __name__ == "__main__":
    pytest.main([__file__])
