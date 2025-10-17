#!/usr/bin/env python3
"""
Test suite for AI Executor

Tests AI execution, phase management, and workflow orchestration.
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

from ai_executor import AIExecutor


class TestAIExecutor:
    """Test cases for AIExecutor"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.project_name = "test-project"
        self.ai_executor = AIExecutor(self.project_name, self.temp_dir)
    
    def teardown_method(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir)
    
    def test_initialization(self):
        """Test AIExecutor initialization"""
        assert self.ai_executor.project_name == self.project_name
        assert self.ai_executor.project_dir.exists()
        assert self.ai_executor.evidence_manager is not None
        assert self.ai_executor.config is not None
    
    def test_project_config_creation(self):
        """Test project configuration creation"""
        config_path = self.ai_executor.project_dir / "project-config.json"
        assert config_path.exists()
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        assert config["project"]["name"] == self.project_name
        assert config["project"]["type"] == "web-app"
        assert "stack" in config["project"]
        assert "workflow" in config
    
    def test_execute_single_phase(self):
        """Test single phase execution"""
        result = self.ai_executor.execute_single_phase(0)
        
        assert result["status"] == "success"
        assert result["phase"] == 0
        assert result["phase_name"] == "Bootstrap & Context Engineering"
        assert "duration" in result
        assert result["duration"] > 0
    
    def test_execute_single_phase_invalid(self):
        """Test single phase execution with invalid phase"""
        with pytest.raises(ValueError):
            self.ai_executor.execute_single_phase(10)
    
    def test_execute_full_workflow(self):
        """Test full workflow execution"""
        report = self.ai_executor.execute_full_workflow()
        
        assert "metadata" in report
        assert "phase_results" in report
        assert "artifacts" in report
        assert "evidence" in report
        
        assert report["metadata"]["project_name"] == self.project_name
        assert report["metadata"]["total_phases"] == 7
        assert len(report["phase_results"]) == 7
        
        # Check that all phases completed successfully
        for result in report["phase_results"]:
            assert result["status"] == "success"
    
    def test_phase_outputs_generation(self):
        """Test phase outputs generation"""
        outputs = self.ai_executor._generate_phase_outputs(0, "Bootstrap")
        
        assert "artifacts" in outputs
        assert "validation" in outputs
        assert len(outputs["artifacts"]) > 0
        assert outputs["validation"]["status"] == "passed"
        assert outputs["validation"]["score"] > 0
    
    def test_final_report_generation(self):
        """Test final report generation"""
        # Mock phase results
        mock_results = [
            {
                "status": "success",
                "phase": 0,
                "phase_name": "Bootstrap",
                "duration": 1.0,
                "outputs": {
                    "artifacts": [{"path": "test.txt", "category": "test", "description": "Test"}],
                    "validation": {"score": 8.0}
                }
            }
        ]
        
        report = self.ai_executor._generate_final_report(mock_results, "success")
        
        assert report["metadata"]["overall_status"] == "success"
        assert report["metadata"]["total_duration"] == 1.0
        assert report["metadata"]["successful_phases"] == 1
        assert report["metadata"]["total_phases"] == 1
        assert report["metadata"]["average_quality_score"] == 8.0
    
    def test_evidence_logging(self):
        """Test evidence logging during execution"""
        # Execute a phase
        result = self.ai_executor.execute_single_phase(0)
        
        # Check that evidence was logged
        manifest = self.ai_executor.evidence_manager._read_json(
            self.ai_executor.evidence_manager.manifest_path
        )
        run_log = self.ai_executor.evidence_manager._read_json(
            self.ai_executor.evidence_manager.run_log_path
        )
        
        assert len(manifest["artifacts"]) > 0
        assert len(run_log["entries"]) > 0
        
        # Verify phase-specific evidence
        phase_artifacts = [a for a in manifest["artifacts"] if a["phase"] == 0]
        phase_entries = [e for e in run_log["entries"] if e["phase"] == 0]
        
        assert len(phase_artifacts) > 0
        assert len(phase_entries) > 0
    
    def test_workflow_error_handling(self):
        """Test workflow error handling"""
        # Mock a phase failure by modifying the phase execution
        original_execute_phase = self.ai_executor._execute_phase
        
        def mock_failing_phase(phase, phase_name, phase_file):
            return {
                "status": "error",
                "phase": phase,
                "phase_name": phase_name,
                "error": "Mock error",
                "duration": 0.1
            }
        
        self.ai_executor._execute_phase = mock_failing_phase
        
        # Execute workflow
        report = self.ai_executor.execute_full_workflow()
        
        # Check that workflow stopped at first error
        assert report["metadata"]["overall_status"] == "error"
        assert len(report["phase_results"]) == 1
        assert report["phase_results"][0]["status"] == "error"
        
        # Restore original method
        self.ai_executor._execute_phase = original_execute_phase
    
    def test_phase_duration_tracking(self):
        """Test phase duration tracking"""
        # Execute multiple phases
        results = []
        for phase in range(3):
            result = self.ai_executor.execute_single_phase(phase)
            results.append(result)
        
        # Check that durations are tracked
        for result in results:
            assert "duration" in result
            assert result["duration"] > 0
        
        # Check that durations are reasonable
        total_duration = sum(r["duration"] for r in results)
        assert total_duration > 0
        assert total_duration < 10  # Should be quick in test environment
    
    def test_artifact_generation(self):
        """Test artifact generation for different phases"""
        # Test different phases
        test_phases = [0, 1, 2, 3, 4, 5, 6]
        
        for phase in test_phases:
            result = self.ai_executor.execute_single_phase(phase)
            
            assert result["status"] == "success"
            assert "outputs" in result
            assert "artifacts" in result["outputs"]
            assert len(result["outputs"]["artifacts"]) > 0
            
            # Check artifact structure
            for artifact in result["outputs"]["artifacts"]:
                assert "path" in artifact
                assert "category" in artifact
                assert "description" in artifact
    
    def test_validation_generation(self):
        """Test validation generation for different phases"""
        # Test different phases
        test_phases = [0, 1, 2, 3, 4, 5, 6]
        
        for phase in test_phases:
            result = self.ai_executor.execute_single_phase(phase)
            
            assert result["status"] == "success"
            assert "outputs" in result
            assert "validation" in result["outputs"]
            
            validation = result["outputs"]["validation"]
            assert "status" in validation
            assert "score" in validation
            assert "findings" in validation
            assert "recommendations" in validation
            
            # Check validation structure
            assert validation["status"] in ["passed", "failed", "pending"]
            assert 0 <= validation["score"] <= 10
            assert isinstance(validation["findings"], list)
            assert isinstance(validation["recommendations"], list)


if __name__ == "__main__":
    pytest.main([__file__])
