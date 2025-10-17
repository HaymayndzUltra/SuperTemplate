#!/usr/bin/env python3
"""
Workflow Integration Validation Script

Comprehensive validation script that checks:
1. Protocol alignment - All protocols reference correct scripts
2. Connectivity validation - Protocol outputs match next protocol inputs
3. Conflict detection - No contradicting directives between protocols
4. Script validation - All referenced scripts exist and are executable
5. Documentation validation - README and guides are complete and accurate
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any


class WorkflowValidator:
    """Validates ai-driven-workflow integration for alignment, connectivity, and conflicts."""
    
    def __init__(self, workspace_root: str = "."):
        self.workspace_root = Path(workspace_root)
        self.ai_driven_workflow_dir = self.workspace_root / ".cursor" / "ai-driven-workflow"
        # Backward-compatible alias used elsewhere in the script
        self.dev_workflow_dir = self.ai_driven_workflow_dir
        self.scripts_dir = self.workspace_root / "scripts"
        
        # Protocol definitions
        self.protocols = {
            "00": {
                "file": "00-client-discovery.md",
                "scripts": ["validate_brief.py", "score_risks.py", "classify_domain.py"],
                "integration_point": "Phase 5.5",
                "gate_criteria": "Brief score ≥ 80"
            },
            "0": {
                "file": "0-bootstrap-your-project.md", 
                "scripts": ["normalize_project_rules.py", "rules_audit_quick.py"],
                "integration_point": "Steps 6.5, 7.5",
                "gate_criteria": "All rules validated"
            },
            "1": {
                "file": "1-create-prd.md",
                "scripts": ["validate_prd_gate.py", "generate_prd_assets.py"],
                "integration_point": "Phase 4.5",
                "gate_criteria": "PRD score ≥ 85"
            },
            "2": {
                "file": "2-generate-tasks.md",
                "scripts": ["validate_tasks.py", "enrich_tasks.py"],
                "integration_point": "Phase 4.5",
                "gate_criteria": "All tasks enhanced"
            },
            "3": {
                "file": "3-process-tasks.md",
                "scripts": ["update_task_state.py", "evidence_report.py"],
                "integration_point": "Steps 3.5, 3.6",
                "gate_criteria": "State synchronized"
            },
            "4": {
                "file": "4-quality-audit.md",
                "scripts": ["run_workflow.py", "aggregate_coverage.py"],
                "integration_point": "Pre-Audit",
                "gate_criteria": "CI status checked"
            },
            "5": {
                "file": "5-implementation-retrospective.md",
                "scripts": ["retrospective_rules_audit.py", "retrospective_evidence_report.py"],
                "integration_point": "Pre-Retrospective",
                "gate_criteria": "Audit complete"
            }
        }
        
        # Expected connectivity flow
        self.connectivity_flow = [
            ("00", "0", "brief.md", ["project-overview", "objectives", "deliverables"]),
            ("0", "1", "context-kit/", ["README.md", "rules/"]),
            ("1", "2", "prd-{name}.md", ["functional-specifications", "technical-specifications"]),
            ("2", "3", "tasks-{name}.md", ["automation-hooks", "why-statements"]),
            ("3", "4", ".artifacts/", ["test-results", "coverage", "evidence"]),
            ("4", "5", "audit-report.md", ["quality-scores", "ci-results"])
        ]
        
        # Standard communication prefixes
        self.standard_prefixes = [
            "[AUTOMATION]", "[GATE PASSED]", "[GATE FAILED]", 
            "[CONTEXT LOADED]", "[NEXT TASK]", "[TASK COMPLETE]",
            "[QUALITY GATE]", "[QUALITY REPORT]", "[EVIDENCE CAPTURED]"
        ]
        
        # Standard directive tags
        self.standard_directives = ["[MUST]", "[GUIDELINE]", "[CRITICAL]", "[STRICT]"]
    
    def validate_workflow_integration(self) -> Dict[str, Any]:
        """Run comprehensive workflow validation."""
        results = {
            "status": "pass",
            "summary": {
                "total_checks": 0,
                "passed": 0,
                "failed": 0,
                "warnings": 0
            },
            "alignment": {},
            "connectivity": {},
            "conflicts": [],
            "issues": [],
            "recommendations": []
        }
        
        # Run all validation checks
        checks = [
            self._validate_protocol_alignment,
            self._validate_connectivity,
            self._validate_conflicts,
            self._validate_scripts,
            self._validate_documentation
        ]
        
        for check in checks:
            try:
                check_results = check()
                self._merge_results(results, check_results)
            except Exception as e:
                results["issues"].append({
                    "severity": "error",
                    "check": check.__name__,
                    "message": f"Validation check failed: {str(e)}",
                    "fix": "Review validation logic"
                })
                results["summary"]["failed"] += 1
        
        # Calculate final status
        results["summary"]["total_checks"] = sum(results["summary"].values())
        if results["summary"]["failed"] > 0:
            results["status"] = "fail"
        elif results["summary"]["warnings"] > 0:
            results["status"] = "warning"
        
        return results
    
    def _validate_protocol_alignment(self) -> Dict[str, Any]:
        """Validate that all protocols reference correct scripts."""
        results = {
            "alignment": {},
            "issues": [],
            "summary": {"passed": 0, "failed": 0, "warnings": 0}
        }
        
        for protocol_id, protocol_info in self.protocols.items():
            protocol_file = self.dev_workflow_dir / protocol_info["file"]
            
            if not protocol_file.exists():
                results["issues"].append({
                    "severity": "error",
                    "protocol": f"protocol_{protocol_id}",
                    "message": f"Protocol file not found: {protocol_file}",
                    "fix": f"Create {protocol_file}"
                })
                results["summary"]["failed"] += 1
                results["alignment"][f"protocol_{protocol_id}"] = "❌ missing"
                continue
            
            # Read protocol content
            try:
                content = protocol_file.read_text(encoding='utf-8')
            except Exception as e:
                results["issues"].append({
                    "severity": "error",
                    "protocol": f"protocol_{protocol_id}",
                    "message": f"Cannot read protocol file: {str(e)}",
                    "fix": "Check file permissions and encoding"
                })
                results["summary"]["failed"] += 1
                results["alignment"][f"protocol_{protocol_id}"] = "❌ unreadable"
                continue
            
            # Check script references
            script_issues = []
            for script in protocol_info["scripts"]:
                script_path = self.scripts_dir / script
                
                # Check if script exists
                if not script_path.exists():
                    script_issues.append({
                        "severity": "error",
                        "message": f"Script not found: {script}",
                        "fix": f"Create {script_path}"
                    })
                    continue
                
                # Check if script is executable
                if not os.access(script_path, os.X_OK):
                    script_issues.append({
                        "severity": "warning",
                        "message": f"Script not executable: {script}",
                        "fix": f"Run: chmod +x {script_path}"
                    })
                
                # Check if script is referenced in protocol
                script_ref_pattern = rf"python\s+scripts/{re.escape(script)}"
                if not re.search(script_ref_pattern, content):
                    script_issues.append({
                        "severity": "warning",
                        "message": f"Script not referenced in protocol: {script}",
                        "fix": f"Add script reference to {protocol_info['file']}"
                    })
            
            # Check integration point
            integration_point = protocol_info["integration_point"]
            if integration_point not in content:
                script_issues.append({
                    "severity": "warning",
                    "message": f"Integration point not found: {integration_point}",
                    "fix": f"Add {integration_point} to {protocol_info['file']}"
                })
            
            # Update results
            if script_issues:
                results["issues"].extend([{
                    "severity": issue["severity"],
                    "protocol": f"protocol_{protocol_id}",
                    "message": issue["message"],
                    "fix": issue["fix"]
                } for issue in script_issues])
                
                failed_count = sum(1 for issue in script_issues if issue["severity"] == "error")
                warning_count = sum(1 for issue in script_issues if issue["severity"] == "warning")
                
                results["summary"]["failed"] += failed_count
                results["summary"]["warnings"] += warning_count
                
                if failed_count > 0:
                    results["alignment"][f"protocol_{protocol_id}"] = "❌ failed"
                else:
                    results["alignment"][f"protocol_{protocol_id}"] = "⚠️ warnings"
            else:
                results["summary"]["passed"] += 1
                results["alignment"][f"protocol_{protocol_id}"] = "✅ aligned"
        
        return results
    
    def _validate_connectivity(self) -> Dict[str, Any]:
        """Validate that protocol outputs match next protocol inputs."""
        results = {
            "connectivity": {},
            "issues": [],
            "summary": {"passed": 0, "failed": 0, "warnings": 0}
        }
        
        for from_protocol, to_protocol, expected_output, required_sections in self.connectivity_flow:
            connectivity_key = f"{from_protocol}→{to_protocol}"
            
            # Check if output artifacts exist or are properly referenced
            output_path = self.workspace_root / expected_output
            
            if expected_output.endswith("/"):
                # Directory check
                if output_path.exists() and output_path.is_dir():
                    results["summary"]["passed"] += 1
                    results["connectivity"][connectivity_key] = "✅ connected"
                else:
                    results["issues"].append({
                        "severity": "warning",
                        "connectivity": connectivity_key,
                        "message": f"Output directory not found: {expected_output}",
                        "fix": f"Ensure {from_protocol} creates {expected_output}"
                    })
                    results["summary"]["warnings"] += 1
                    results["connectivity"][connectivity_key] = "⚠️ missing"
            else:
                # File check
                if output_path.exists() and output_path.is_file():
                    # Check required sections
                    try:
                        content = output_path.read_text(encoding='utf-8')
                        missing_sections = []
                        for section in required_sections:
                            if section not in content:
                                missing_sections.append(section)
                        
                        if missing_sections:
                            results["issues"].append({
                                "severity": "warning",
                                "connectivity": connectivity_key,
                                "message": f"Missing required sections: {missing_sections}",
                                "fix": f"Add sections to {expected_output}"
                            })
                            results["summary"]["warnings"] += 1
                            results["connectivity"][connectivity_key] = "⚠️ incomplete"
                        else:
                            results["summary"]["passed"] += 1
                            results["connectivity"][connectivity_key] = "✅ connected"
                    except Exception as e:
                        results["issues"].append({
                            "severity": "error",
                            "connectivity": connectivity_key,
                            "message": f"Cannot read output file: {str(e)}",
                            "fix": f"Check {expected_output} permissions"
                        })
                        results["summary"]["failed"] += 1
                        results["connectivity"][connectivity_key] = "❌ unreadable"
                else:
                    results["issues"].append({
                        "severity": "warning",
                        "connectivity": connectivity_key,
                        "message": f"Output file not found: {expected_output}",
                        "fix": f"Ensure {from_protocol} creates {expected_output}"
                    })
                    results["summary"]["warnings"] += 1
                    results["connectivity"][connectivity_key] = "⚠️ missing"
        
        return results
    
    def _validate_conflicts(self) -> Dict[str, Any]:
        """Detect conflicts and contradictions between protocols."""
        results = {
            "conflicts": [],
            "issues": [],
            "summary": {"passed": 0, "failed": 0, "warnings": 0}
        }
        
        # Check directive consistency
        directive_usage = {}
        announcement_usage = {}
        
        for protocol_id, protocol_info in self.protocols.items():
            protocol_file = self.dev_workflow_dir / protocol_info["file"]
            
            if not protocol_file.exists():
                continue
            
            try:
                content = protocol_file.read_text(encoding='utf-8')
                
                # Check directive usage
                for directive in self.standard_directives:
                    count = content.count(directive)
                    if directive not in directive_usage:
                        directive_usage[directive] = {}
                    directive_usage[directive][protocol_id] = count
                
                # Check announcement usage
                for prefix in self.standard_prefixes:
                    count = content.count(prefix)
                    if prefix not in announcement_usage:
                        announcement_usage[prefix] = {}
                    announcement_usage[prefix][protocol_id] = count
                
            except Exception:
                continue
        
        # Check for inconsistent directive usage
        for directive, usage in directive_usage.items():
            protocols_with_directive = [pid for pid, count in usage.items() if count > 0]
            if len(protocols_with_directive) > 0 and len(protocols_with_directive) < len(self.protocols):
                results["issues"].append({
                    "severity": "warning",
                    "check": "directive_consistency",
                    "message": f"Directive {directive} used inconsistently across protocols",
                    "fix": f"Use {directive} consistently in all protocols"
                })
                results["summary"]["warnings"] += 1
        
        # Check for duplicate automation hooks
        automation_hooks = {}
        for protocol_id, protocol_info in self.protocols.items():
            protocol_file = self.dev_workflow_dir / protocol_info["file"]
            
            if not protocol_file.exists():
                continue
            
            try:
                content = protocol_file.read_text(encoding='utf-8')
                
                # Find automation hook patterns
                hook_pattern = r'python\s+scripts/([a-zA-Z0-9_-]+\.py)'
                matches = re.findall(hook_pattern, content)
                
                for script in matches:
                    if script not in automation_hooks:
                        automation_hooks[script] = []
                    automation_hooks[script].append(protocol_id)
                
            except Exception:
                continue
        
        # Check for duplicate hooks
        for script, protocols in automation_hooks.items():
            if len(protocols) > 1:
                results["conflicts"].append({
                    "type": "duplicate_automation_hook",
                    "script": script,
                    "protocols": protocols,
                    "message": f"Script {script} referenced in multiple protocols: {protocols}",
                    "severity": "warning"
                })
                results["summary"]["warnings"] += 1
        
        if not results["conflicts"] and not results["issues"]:
            results["summary"]["passed"] += 1
        
        return results
    
    def _validate_scripts(self) -> Dict[str, Any]:
        """Validate that all referenced scripts exist and are executable."""
        results = {
            "issues": [],
            "summary": {"passed": 0, "failed": 0, "warnings": 0}
        }
        
        # Collect all unique scripts
        all_scripts = set()
        for protocol_info in self.protocols.values():
            all_scripts.update(protocol_info["scripts"])
        
        for script in all_scripts:
            script_path = self.scripts_dir / script
            
            if not script_path.exists():
                results["issues"].append({
                    "severity": "error",
                    "script": script,
                    "message": f"Script file not found: {script_path}",
                    "fix": f"Create {script_path}"
                })
                results["summary"]["failed"] += 1
                continue
            
            if not os.access(script_path, os.X_OK):
                results["issues"].append({
                    "severity": "warning",
                    "script": script,
                    "message": f"Script not executable: {script_path}",
                    "fix": f"Run: chmod +x {script_path}"
                })
                results["summary"]["warnings"] += 1
                continue
            
            # Check if script has proper shebang
            try:
                with open(script_path, 'r') as f:
                    first_line = f.readline().strip()
                    if not first_line.startswith('#!'):
                        results["issues"].append({
                            "severity": "warning",
                            "script": script,
                            "message": f"Script missing shebang: {script_path}",
                            "fix": f"Add shebang to {script_path}"
                        })
                        results["summary"]["warnings"] += 1
                        continue
            except Exception:
                results["issues"].append({
                    "severity": "error",
                    "script": script,
                    "message": f"Cannot read script file: {script_path}",
                    "fix": f"Check {script_path} permissions"
                })
                results["summary"]["failed"] += 1
                continue
            
            results["summary"]["passed"] += 1
        
        return results
    
    def _validate_documentation(self) -> Dict[str, Any]:
        """Validate documentation completeness and accuracy."""
        results = {
            "issues": [],
            "summary": {"passed": 0, "failed": 0, "warnings": 0}
        }
        
        # Check README.md
        readme_path = self.dev_workflow_dir / "README.md"
        if not readme_path.exists():
            results["issues"].append({
                "severity": "error",
                "documentation": "README.md",
                "message": "README.md not found",
                "fix": "Create README.md in .cursor/ai-driven-workflow/"
            })
            results["summary"]["failed"] += 1
        else:
            try:
                readme_content = readme_path.read_text(encoding='utf-8')
                
                # Check for required sections
                required_sections = [
                    "Automation Integration Architecture",
                    "Script Reference Table",
                    "Integration Checkpoints",
                    "Quality Gates per Protocol"
                ]
                
                missing_sections = []
                for section in required_sections:
                    if section not in readme_content:
                        missing_sections.append(section)
                
                if missing_sections:
                    results["issues"].append({
                        "severity": "warning",
                        "documentation": "README.md",
                        "message": f"Missing required sections: {missing_sections}",
                        "fix": "Add missing sections to README.md"
                    })
                    results["summary"]["warnings"] += 1
                else:
                    results["summary"]["passed"] += 1
                    
            except Exception as e:
                results["issues"].append({
                    "severity": "error",
                    "documentation": "README.md",
                    "message": f"Cannot read README.md: {str(e)}",
                    "fix": "Check README.md permissions"
                })
                results["summary"]["failed"] += 1
        
        # Check INTEGRATION-GUIDE.md
        integration_guide_path = self.dev_workflow_dir / "INTEGRATION-GUIDE.md"
        if not integration_guide_path.exists():
            results["issues"].append({
                "severity": "warning",
                "documentation": "INTEGRATION-GUIDE.md",
                "message": "INTEGRATION-GUIDE.md not found",
                "fix": "Create INTEGRATION-GUIDE.md in .cursor/ai-driven-workflow/"
            })
            results["summary"]["warnings"] += 1
        else:
            results["summary"]["passed"] += 1
        
        return results
    
    def _merge_results(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        """Merge validation results from different checks."""
        # Merge summaries
        for key in ["passed", "failed", "warnings"]:
            target["summary"][key] += source["summary"].get(key, 0)
        
        # Merge alignment results
        if "alignment" in source:
            target["alignment"].update(source["alignment"])
        
        # Merge connectivity results
        if "connectivity" in source:
            target["connectivity"].update(source["connectivity"])
        
        # Merge conflicts
        if "conflicts" in source:
            target["conflicts"].extend(source["conflicts"])
        
        # Merge issues
        if "issues" in source:
            target["issues"].extend(source["issues"])
        
        # Merge recommendations
        if "recommendations" in source:
            target["recommendations"].extend(source["recommendations"])


def main():
    """Main entry point for workflow validation."""
    parser = argparse.ArgumentParser(description="Validate ai-driven-workflow integration")
    parser.add_argument("--workspace", "-w", default=".", help="Workspace root directory")
    parser.add_argument("--output", "-o", help="Output file for validation results (JSON)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--fix", action="store_true", help="Attempt to fix common issues")
    
    args = parser.parse_args()
    
    validator = WorkflowValidator(args.workspace)
    results = validator.validate_workflow_integration()
    
    # Output results
    if args.verbose or not args.output:
        print("🔍 Dev-Workflow Integration Validation")
        print("=" * 50)
        print(f"Status: {results['status'].upper()}")
        print(f"Total Checks: {results['summary']['total_checks']}")
        print(f"Passed: {results['summary']['passed']}")
        print(f"Failed: {results['summary']['failed']}")
        print(f"Warnings: {results['summary']['warnings']}")
        
        if results["alignment"]:
            print("\n📋 Protocol Alignment:")
            for protocol, status in results["alignment"].items():
                print(f"  {protocol}: {status}")
        
        if results["connectivity"]:
            print("\n🔗 Connectivity:")
            for connection, status in results["connectivity"].items():
                print(f"  {connection}: {status}")
        
        if results["conflicts"]:
            print("\n⚠️ Conflicts:")
            for conflict in results["conflicts"]:
                print(f"  {conflict['type']}: {conflict['message']}")
        
        if results["issues"]:
            print("\n❌ Issues:")
            for issue in results["issues"]:
                print(f"  {issue['severity'].upper()}: {issue['message']}")
                print(f"    Fix: {issue['fix']}")
        
        if results["recommendations"]:
            print("\n💡 Recommendations:")
            for rec in results["recommendations"]:
                print(f"  - {rec}")
    
    # Save to output file if specified
    if args.output:
        out_path = Path(args.output)
        try:
            out_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
        with open(out_path, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Validation results saved to: {args.output}")
    
    # Attempt fixes if requested
    if args.fix:
        print("\n🔧 Attempting to fix common issues...")
        fix_count = 0
        
        for issue in results["issues"]:
            if issue["severity"] == "warning" and "not executable" in issue["message"]:
                script_path = issue.get("script")
                if script_path:
                    try:
                        os.chmod(validator.scripts_dir / script_path, 0o755)
                        print(f"  ✅ Made {script_path} executable")
                        fix_count += 1
                    except Exception as e:
                        print(f"  ❌ Failed to fix {script_path}: {e}")
        
        print(f"Fixed {fix_count} issues")
    
    # Exit with appropriate code
    if results["status"] == "fail":
        sys.exit(1)
    elif results["status"] == "warning":
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
