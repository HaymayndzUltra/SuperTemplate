#!/usr/bin/env python3
"""
Script: protocol-01-extract-requirements.py
Protocol: 01 - Validator Requirements Analysis
Purpose: Extract validation requirements from all validator scripts
"""

import json
import re
import sys
import os
from pathlib import Path
from typing import Dict, List, Any, Tuple
import ast

class ValidatorAnalyzer:
    """Analyzes validator scripts to extract requirements."""
    
    def __init__(self, validators_dir: str):
        self.validators_dir = Path(validators_dir)
        self.requirements = {}
        self.errors = []
        self.warnings = []
        
    def discover_validators(self) -> List[Path]:
        """Discover all validator scripts."""
        validators = sorted(self.validators_dir.glob("validate_protocol_*.py"))
        if len(validators) != 10:
            self.errors.append(f"Expected 10 validators, found {len(validators)}")
        return validators
    
    def extract_class_docstring(self, content: str) -> str:
        """Extract class docstring."""
        match = re.search(r'class\s+\w+.*?:\s*"""(.*?)"""', content, re.DOTALL)
        if match:
            return match.group(1).strip().split('\n')[0]
        return "No description available"
    
    def extract_validation_methods(self, content: str) -> Dict[str, int]:
        """Extract validation method names and line numbers."""
        methods = {}
        for match in re.finditer(r'def\s+(_validate_\w+)\(self', content):
            method_name = match.group(1)
            line_num = content[:match.start()].count('\n') + 1
            methods[method_name] = line_num
        return methods
    
    def extract_evaluate_methods(self, content: str) -> Dict[str, Dict[str, Any]]:
        """Extract evaluate methods with weights and checks."""
        evaluate_methods = {}
        
        for match in re.finditer(r'def\s+(_evaluate_\w+)\(self.*?weight=([\d.]+)', content):
            method_name = match.group(1)
            weight = float(match.group(2))
            line_num = content[:match.start()].count('\n') + 1
            
            # Find checks dictionary within 50 lines after method def
            method_start = match.start()
            method_section = content[method_start:method_start+3000]
            
            checks = {}
            checks_match = re.search(r'checks\s*=\s*\{(.*?)\}', method_section, re.DOTALL)
            if checks_match:
                checks_text = checks_match.group(1)
                for check_match in re.finditer(r'"(\w+)":', checks_text):
                    check_name = check_match.group(1)
                    checks[check_name] = True
            
            evaluate_methods[method_name] = {
                'weight': weight,
                'line': line_num,
                'checks': checks
            }
        
        return evaluate_methods
    
    def extract_thresholds(self, content: str) -> Dict[str, float]:
        """Extract pass and warning thresholds."""
        thresholds = {'pass': 0.95, 'warning': 0.80}  # defaults
        
        # Look for determine_status calls
        match = re.search(r'determine_status\(.*?pass_threshold=([\d.]+)', content)
        if match:
            thresholds['pass'] = float(match.group(1))
        
        match = re.search(r'determine_status\(.*?warning_threshold=([\d.]+)', content)
        if match:
            thresholds['warning'] = float(match.group(1))
        
        return thresholds
    
    def extract_patterns(self, content: str) -> Dict[str, str]:
        """Extract required patterns (regex and literal strings)."""
        patterns = {}
        
        # Find regex patterns
        for match in re.finditer(r"re\.(search|match|findall)\(r'([^']+)'", content):
            pattern_type = match.group(1)
            pattern = match.group(2)
            pattern_key = f"regex_{len(patterns)}"
            patterns[pattern_key] = {'pattern': pattern, 'type': 'regex', 'context': pattern_type}
        
        # Find literal string patterns
        for match in re.finditer(r'"([^"]{10,}?)"\s+(in|==|startswith)', content):
            pattern = match.group(1)
            operator = match.group(2)
            pattern_key = f"literal_{len(patterns)}"
            patterns[pattern_key] = {'pattern': pattern, 'type': 'literal', 'context': operator}
        
        return patterns
    
    def extract_count_requirements(self, content: str) -> Dict[str, int]:
        """Extract count requirements (len >= N, etc)."""
        counts = {}
        
        for match in re.finditer(r'len\((\w+)\)\s*([><=]+)\s*(\d+)', content):
            element = match.group(1)
            operator = match.group(2)
            threshold = int(match.group(3))
            
            if '>=' in operator or '>' in operator:
                key = f"count_{element}"
                if key not in counts or counts[key] < threshold:
                    counts[key] = threshold
        
        return counts
    
    def analyze_validator(self, validator_path: Path) -> Dict[str, Any]:
        """Analyze a single validator script."""
        try:
            with open(validator_path, 'r') as f:
                content = f.read()
            
            # Validate Python syntax
            try:
                ast.parse(content)
            except SyntaxError as e:
                self.errors.append(f"Syntax error in {validator_path.name}: {e}")
                return None
            
            validator_name = validator_path.stem.replace('validate_protocol_', '').replace('.py', '')
            
            return {
                'name': validator_name,
                'file': validator_path.name,
                'purpose': self.extract_class_docstring(content),
                'validation_methods': self.extract_validation_methods(content),
                'evaluate_methods': self.extract_evaluate_methods(content),
                'thresholds': self.extract_thresholds(content),
                'patterns': self.extract_patterns(content),
                'count_requirements': self.extract_count_requirements(content),
                'total_lines': len(content.split('\n'))
            }
        
        except Exception as e:
            self.errors.append(f"Error analyzing {validator_path.name}: {e}")
            return None
    
    def run(self) -> Dict[str, Any]:
        """Run complete analysis."""
        print("[ANALYSIS START] Discovering validators...")
        validators = self.discover_validators()
        
        if not validators:
            print("[ERROR] No validators found")
            return None
        
        print(f"[✓] Found {len(validators)} validators")
        
        for validator_path in validators:
            print(f"[ANALYSIS] Processing {validator_path.name}...")
            result = self.analyze_validator(validator_path)
            if result:
                self.requirements[result['name']] = result
                print(f"[✓] Extracted requirements from {result['name']}")
        
        # Validation
        if len(self.requirements) != 10:
            self.errors.append(f"Expected 10 validators, analyzed {len(self.requirements)}")
        
        return {
            'validators': self.requirements,
            'errors': self.errors,
            'warnings': self.warnings,
            'total_validators': len(self.requirements),
            'total_dimensions': sum(len(v.get('validate_methods', {})) for v in self.requirements.values()),
            'total_patterns': sum(len(v.get('patterns', {})) for v in self.requirements.values()),
            'total_counts': sum(len(v.get('count_requirements', {})) for v in self.requirements.values())
        }

def main():
    """Main entry point."""
    validators_dir = "validators-system/scripts"
    
    if not Path(validators_dir).exists():
        print(f"[ERROR] Validators directory not found: {validators_dir}")
        sys.exit(1)
    
    analyzer = ValidatorAnalyzer(validators_dir)
    result = analyzer.run()
    
    if result is None:
        sys.exit(1)
    
    # Save raw extraction
    output_file = ".artifacts/protocol-creation/validator-requirements-raw.json"
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n[ARTIFACTS GENERATED] Saved to {output_file}")
    print(f"[SUMMARY] Validators: {result['total_validators']}/10")
    print(f"[SUMMARY] Dimensions: {result['total_dimensions']}")
    print(f"[SUMMARY] Patterns: {result['total_patterns']}")
    print(f"[SUMMARY] Count Requirements: {result['total_counts']}")
    
    if result['errors']:
        print(f"\n[ERRORS] {len(result['errors'])} error(s):")
        for error in result['errors']:
            print(f"  - {error}")
        sys.exit(1)
    
    print("\n[PROTOCOL 1 | STEP 1 COMPLETE] Validator discovery and analysis successful")

if __name__ == "__main__":
    main()
