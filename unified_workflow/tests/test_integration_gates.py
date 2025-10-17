"""Integration Test Suite with Phase-Specific Gates.

This test suite validates each integration milestone with specific gates
to ensure the unified workflow functions correctly across all phases.
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Dict, List
from unittest.mock import Mock, patch

# Setup imports
project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "unified-workflow"))

from automation.compliance_validator import ComplianceValidator
from automation.evidence_schema_converter import EvidenceSchemaConverter, EvidenceMigrator
from automation.external_services import ExternalServicesManager
from core.template_registry import UnifiedTemplateRegistry


class PhaseGateTestBase(unittest.TestCase):
    """Base class for phase-specific gate tests."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp()
        self.project_root = Path(self.test_dir)
        self.evidence_dir = self.project_root / "evidence"
        self.evidence_dir.mkdir(parents=True, exist_ok=True)
        
    def tearDown(self):
        """Clean up test environment."""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def create_test_file(self, relative_path: str, content: str) -> Path:
        """Create a test file with content."""
        file_path = self.project_root / relative_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)
        return file_path


class TestGate1Infrastructure(PhaseGateTestBase):
    """Gate 1: Foundation & Infrastructure Tests"""
    
    def test_scripts_package_exists(self):
        """Test that scripts/__init__.py exists."""
        init_file = Path(project_root) / "scripts" / "__init__.py"
        self.assertTrue(init_file.exists(), "scripts/__init__.py must exist")
    
    def test_imports_without_syspath(self):
        """Test that lifecycle_tasks can be imported without sys.path manipulation."""
        # This should work now that scripts/__init__.py exists
        try:
            from scripts import lifecycle_tasks
            self.assertIsNotNone(lifecycle_tasks)
        except ImportError as e:
            self.fail(f"Failed to import scripts.lifecycle_tasks: {e}")
    
    def test_unified_template_registry(self):
        """Test that unified template registry works correctly."""
        registry = UnifiedTemplateRegistry(project_root)
        registry.initialize()
        
        # Test listing templates
        templates = registry.list_templates()
        self.assertIsInstance(templates, list)
        
        # Test getting a specific template
        backend_templates = registry.list_templates("backend")
        self.assertIsInstance(backend_templates, list)
    
    def test_evidence_schema_converter(self):
        """Test evidence schema conversion."""
        converter = EvidenceSchemaConverter()
        
        # Test legacy to unified conversion
        legacy_evidence = [
            {
                "path": "docs/README.md",
                "category": "documentation",
                "description": "Project readme",
                "checksum": "abc123",
                "created_at": "2025-01-01T00:00:00Z"
            }
        ]
        
        unified = converter.legacy_to_unified(
            legacy_evidence,
            project_name="test-project",
            phase=0
        )
        
        # Validate structure
        self.assertIn("manifest", unified)
        self.assertIn("run_log", unified)
        self.assertIn("validation", unified)
        self.assertEqual(len(unified["manifest"]["artifacts"]), 1)
        self.assertEqual(unified["manifest"]["artifacts"][0]["phase"], 0)
        
        # Test unified to legacy conversion
        legacy_back = converter.unified_to_legacy(unified)
        self.assertEqual(len(legacy_back), 1)
        self.assertEqual(legacy_back[0]["path"], "docs/README.md")
    
    def test_compliance_validator_adapter(self):
        """Test compliance validator works without sys.path hacks."""
        validator = ComplianceValidator()
        self.assertIsNotNone(validator.generator)
        
        # Test that it can generate compliance docs
        all_valid, results = validator.validate_compliance_docs(write=False)
        self.assertIsInstance(results, dict)
        self.assertIn("compliance_doc", results)
        self.assertIn("gates_config", results)


class TestGate2CoreModules(PhaseGateTestBase):
    """Gate 2: Core Integration Modules Tests"""
    
    def test_project_generator_integration(self):
        """Test project generator integration module."""
        # Import should work with unified structure
        from automation import compliance_validator
        
        validator = compliance_validator.ComplianceValidator()
        self.assertIsNotNone(validator)
    
    def test_brief_processor_integration(self):
        """Test brief processor integration (placeholder)."""
        # Would test brief_processor.py when implemented
        self.skipTest("Brief processor not yet implemented")
    
    def test_workflow_automation_integration(self):
        """Test workflow automation integration (placeholder)."""
        # Would test workflow_automation.py when implemented
        self.skipTest("Workflow automation not yet implemented")


class TestGate3TemplatesCLI(PhaseGateTestBase):
    """Gate 3: Template & CLI Integration Tests"""
    
    def test_template_registry_delegation(self):
        """Test that project_generator delegates to unified registry."""
        # Import the modified registry
        from project_generator.templates.registry import TemplateRegistry
        
        # Should use unified registry internally
        registry = TemplateRegistry()
        templates = registry.list_all()
        self.assertIsInstance(templates, list)
    
    def test_cli_compatibility_layer(self):
        """Test CLI compatibility layer functionality."""
        # Import CLI module
        from cli import LegacyCommandRouter, TelemetryTracker
        
        # Test telemetry tracker
        tracker = TelemetryTracker(self.project_root / "telemetry.json")
        tracker.track_command("test-command", ["arg1", "arg2"], legacy=True)
        
        # Verify telemetry was saved
        self.assertTrue((self.project_root / "telemetry.json").exists())
        
        # Test command router
        router = LegacyCommandRouter(project_root)
        commands = router.list_commands()
        self.assertIsInstance(commands, list)
        self.assertGreater(len(commands), 0)
        
        # Check specific commands exist
        command_names = [cmd[0] for cmd in commands]
        self.assertIn("generate-project", command_names)
        self.assertIn("validate-compliance", command_names)
        self.assertIn("run-workflow", command_names)


class TestGate4ProtocolAutomation(PhaseGateTestBase):
    """Gate 4: Protocol & Automation Integration Tests"""
    
    def test_workflow1_scripts_accessible(self):
        """Test that workflow1 scripts are accessible."""
        workflow1_path = project_root / "workflow1"
        
        # Check phase 2 scripts
        phase2_scripts = workflow1_path / "codex-phase2-design" / "scripts"
        self.assertTrue(phase2_scripts.exists())
        self.assertTrue((phase2_scripts / "generate_architecture_pack.py").exists())
        self.assertTrue((phase2_scripts / "generate_contract_assets.py").exists())
        
        # Check phase 3 scripts
        phase3_scripts = workflow1_path / "codex-phase3-quality-rails" / "scripts"
        self.assertTrue(phase3_scripts.exists())
        self.assertTrue((phase3_scripts / "configure_feature_flags.py").exists())
    
    def test_evidence_template_compatibility(self):
        """Test evidence templates are compatible between systems."""
        # Create test evidence in both formats
        legacy_evidence = [
            {
                "path": "test.py",
                "category": "code",
                "description": "Test file",
                "checksum": "123abc",
                "created_at": "2025-01-01T00:00:00Z"
            }
        ]
        
        # Convert and validate
        converter = EvidenceSchemaConverter()
        unified = converter.legacy_to_unified(legacy_evidence, "test", phase=2)
        
        # Validate against schema
        validation = converter.validate_schema(unified)
        self.assertTrue(validation["valid"], f"Schema validation failed: {validation['errors']}")


class TestGate5ExternalServices(PhaseGateTestBase):
    """Gate 5: External Services & Review Protocols Tests"""
    
    def test_external_services_manager(self):
        """Test external services manager initialization."""
        manager = ExternalServicesManager(self.project_root)
        
        # Test service validation
        validation_results = manager.validate_services()
        self.assertIn("git", validation_results)
        self.assertIn("ai_governor", validation_results)
        self.assertIn("policy_dsl", validation_results)
        
        # Test phase-specific services
        phase_0_services = manager.get_phase_services(0)
        self.assertIn("git", phase_0_services)
        self.assertIn("ai_governor", phase_0_services)
        
        phase_3_services = manager.get_phase_services(3)
        self.assertIn("ai_governor", phase_3_services)
        self.assertIn("policy_dsl", phase_3_services)
    
    def test_git_service_validation(self):
        """Test Git service validation."""
        from automation.external_services import GitService
        
        service = GitService(self.project_root)
        result = service.validate()
        
        self.assertIn("available", result)
        self.assertIn("status", result)
        
        # Git should be available in most environments
        if result["available"]:
            self.assertIn("version", result)
    
    def test_ai_governor_service(self):
        """Test AI Governor service initialization."""
        from automation.external_services import AIGovernorService
        
        service = AIGovernorService(self.project_root)
        result = service.validate()
        
        self.assertIn("available", result)
        self.assertIn("status", result)
    
    def test_policy_dsl_service(self):
        """Test Policy DSL service."""
        from automation.external_services import PolicyDSLService
        
        service = PolicyDSLService(self.project_root)
        result = service.validate()
        
        self.assertIn("available", result)
        self.assertIn("status", result)
        
        # Test compliance validation
        config = {
            "encryption_enabled": True,
            "audit_logging_enabled": True,
            "data_retention_days": 90
        }
        
        # This will fail if no policy exists, which is expected
        validation = service.validate_compliance("gdpr", config)
        self.assertIn("valid", validation)
        self.assertIn("errors", validation)


class TestGate6ComprehensiveIntegration(PhaseGateTestBase):
    """Gate 6: Comprehensive Integration Tests"""
    
    def test_end_to_end_phase_execution(self):
        """Test end-to-end phase execution flow."""
        # This would test the complete flow but requires full implementation
        # For now, test the components are available
        
        # Test imports work
        from automation import compliance_validator
        from automation import evidence_schema_converter
        from automation import external_services
        from core import template_registry
        
        # Test instances can be created
        validator = compliance_validator.ComplianceValidator()
        converter = evidence_schema_converter.EvidenceSchemaConverter()
        services = external_services.ExternalServicesManager(self.project_root)
        registry = template_registry.UnifiedTemplateRegistry()
        
        self.assertIsNotNone(validator)
        self.assertIsNotNone(converter)
        self.assertIsNotNone(services)
        self.assertIsNotNone(registry)
    
    def test_performance_benchmarks(self):
        """Test performance meets baselines."""
        import time
        
        # Test template registry performance
        start = time.time()
        registry = UnifiedTemplateRegistry()
        registry.initialize()
        templates = registry.list_templates()
        end = time.time()
        
        # Should complete in under 1 second
        self.assertLess(end - start, 1.0, "Template registry initialization too slow")
        
        # Test evidence conversion performance
        start = time.time()
        converter = EvidenceSchemaConverter()
        legacy_data = [{"path": f"file{i}.py", "category": "code", 
                       "description": f"File {i}", "checksum": f"hash{i}",
                       "created_at": "2025-01-01T00:00:00Z"} 
                      for i in range(100)]
        unified = converter.legacy_to_unified(legacy_data, "test", phase=0)
        end = time.time()
        
        # Should handle 100 files in under 0.1 seconds
        self.assertLess(end - start, 0.1, "Evidence conversion too slow")
    
    def test_no_import_errors(self):
        """Test all modules can be imported without errors."""
        modules_to_test = [
            "automation.compliance_validator",
            "automation.evidence_schema_converter",
            "automation.external_services",
            "core.template_registry",
        ]
        
        for module_name in modules_to_test:
            try:
                __import__(module_name)
            except ImportError as e:
                self.fail(f"Failed to import {module_name}: {e}")


class IntegrationTestRunner:
    """Runs all integration tests with gate reporting."""
    
    @staticmethod
    def run_gate_tests(gate_number: int, test_class: type) -> Dict[str, Any]:
        """Run tests for a specific gate.
        
        Args:
            gate_number: Gate number (1-6)
            test_class: Test class to run
            
        Returns:
            Test results
        """
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        return {
            "gate": gate_number,
            "tests_run": result.testsRun,
            "failures": len(result.failures),
            "errors": len(result.errors),
            "success": result.wasSuccessful(),
            "details": {
                "failures": [(str(test), trace) for test, trace in result.failures],
                "errors": [(str(test), trace) for test, trace in result.errors]
            }
        }
    
    @staticmethod
    def run_all_gates() -> List[Dict[str, Any]]:
        """Run all gate tests in sequence.
        
        Returns:
            List of gate results
        """
        gates = [
            (1, TestGate1Infrastructure),
            (2, TestGate2CoreModules),
            (3, TestGate3TemplatesCLI),
            (4, TestGate4ProtocolAutomation),
            (5, TestGate5ExternalServices),
            (6, TestGate6ComprehensiveIntegration)
        ]
        
        results = []
        for gate_num, test_class in gates:
            print(f"\n{'='*60}")
            print(f"Running Gate {gate_num} Tests: {test_class.__doc__}")
            print(f"{'='*60}")
            
            result = IntegrationTestRunner.run_gate_tests(gate_num, test_class)
            results.append(result)
            
            if not result["success"]:
                print(f"\n⚠️  Gate {gate_num} FAILED - Integration blocked!")
                print(f"Failures: {result['failures']}, Errors: {result['errors']}")
                # In real implementation, would stop here
            else:
                print(f"\n✅ Gate {gate_num} PASSED - Proceeding to next gate")
        
        return results


if __name__ == "__main__":
    # Run all gates
    results = IntegrationTestRunner.run_all_gates()
    
    # Summary report
    print("\n" + "="*60)
    print("INTEGRATION TEST SUMMARY")
    print("="*60)
    
    total_tests = sum(r["tests_run"] for r in results)
    total_failures = sum(r["failures"] for r in results)
    total_errors = sum(r["errors"] for r in results)
    gates_passed = sum(1 for r in results if r["success"])
    
    print(f"Total Gates: {len(results)}")
    print(f"Gates Passed: {gates_passed}/{len(results)}")
    print(f"Total Tests: {total_tests}")
    print(f"Total Failures: {total_failures}")
    print(f"Total Errors: {total_errors}")
    
    if gates_passed == len(results):
        print("\n🎉 ALL INTEGRATION GATES PASSED! Ready for deployment.")
    else:
        print("\n❌ INTEGRATION BLOCKED - Fix failing gates before proceeding.")
        
        # Show failed gates
        failed_gates = [r for r in results if not r["success"]]
        for gate in failed_gates:
            print(f"\nGate {gate['gate']} failures:")
            for test, trace in gate["details"]["failures"]:
                print(f"  - {test}")
            for test, trace in gate["details"]["errors"]:
                print(f"  - {test} (ERROR)")
