#!/usr/bin/env python3
"""
Brief Validation Script

Validates project brief completeness and quality according to Protocol 00 standards.
Ensures all required sections are present and meet quality criteria.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class BriefValidator:
    """Validates project brief files against Protocol 00 standards."""
    
    def __init__(self):
        self.required_sections = [
            "project-overview",
            "objectives", 
            "target-users",
            "deliverables",
            "constraints",
            "success-metrics",
            "risks-dependencies",
            "acceptance-criteria"
        ]
        
        self.quality_checks = {
            "objectives": {"min_length": 50, "keywords": ["problem", "solution", "value"]},
            "deliverables": {"min_items": 1, "keywords": ["build", "create", "develop", "deliver"]},
            "constraints": {"min_items": 1, "keywords": ["time", "budget", "technology", "compliance"]},
            "success-metrics": {"min_items": 1, "keywords": ["measure", "metric", "kpi", "success"]},
            "acceptance-criteria": {"min_items": 3, "keywords": ["must", "should", "criteria"]}
        }
    
    def validate_brief_file(self, brief_path: str) -> Dict:
        """Validate a brief file and return validation results."""
        try:
            brief_content = Path(brief_path).read_text(encoding='utf-8')
        except FileNotFoundError:
            return {
                "status": "error",
                "message": f"Brief file not found: {brief_path}",
                "score": 0
            }
        except Exception as e:
            return {
                "status": "error", 
                "message": f"Error reading brief file: {str(e)}",
                "score": 0
            }
        
        validation_results = {
            "status": "success",
            "score": 0,
            "issues": [],
            "warnings": [],
            "sections_found": [],
            "quality_scores": {}
        }
        
        # Check for required sections
        section_results = self._check_required_sections(brief_content)
        validation_results["sections_found"] = section_results["found"]
        validation_results["issues"].extend(section_results["missing"])
        
        # Check section quality
        quality_results = self._check_section_quality(brief_content)
        validation_results["quality_scores"] = quality_results["scores"]
        validation_results["issues"].extend(quality_results["issues"])
        validation_results["warnings"].extend(quality_results["warnings"])
        
        # Calculate overall score
        validation_results["score"] = self._calculate_score(
            section_results["found"],
            quality_results["scores"]
        )
        
        # Determine final status
        if validation_results["score"] >= 80:
            validation_results["status"] = "pass"
        elif validation_results["score"] >= 60:
            validation_results["status"] = "warning"
        else:
            validation_results["status"] = "fail"
        
        return validation_results
    
    def _check_required_sections(self, content: str) -> Dict:
        """Check if all required sections are present."""
        found_sections = []
        missing_sections = []
        
        # Look for section headers (## or ###)
        section_pattern = r'^#{2,3}\s+(.+)$'
        sections = re.findall(section_pattern, content, re.MULTILINE)
        
        # Normalize section names for comparison
        normalized_sections = [self._normalize_section_name(s) for s in sections]
        
        for required in self.required_sections:
            if required in normalized_sections:
                found_sections.append(required)
            else:
                missing_sections.append(f"Missing required section: {required}")
        
        return {
            "found": found_sections,
            "missing": missing_sections
        }
    
    def _check_section_quality(self, content: str) -> Dict:
        """Check quality of individual sections."""
        scores = {}
        issues = []
        warnings = []
        
        # Extract sections
        sections = self._extract_sections(content)
        
        for section_name, section_content in sections.items():
            if section_name in self.quality_checks:
                quality_result = self._assess_section_quality(
                    section_name, 
                    section_content,
                    self.quality_checks[section_name]
                )
                scores[section_name] = quality_result["score"]
                issues.extend(quality_result["issues"])
                warnings.extend(quality_result["warnings"])
        
        return {
            "scores": scores,
            "issues": issues,
            "warnings": warnings
        }
    
    def _extract_sections(self, content: str) -> Dict[str, str]:
        """Extract sections from markdown content."""
        sections = {}
        
        # Split by headers
        parts = re.split(r'^#{2,3}\s+(.+)$', content, flags=re.MULTILINE)
        
        for i in range(1, len(parts), 2):
            if i + 1 < len(parts):
                section_name = self._normalize_section_name(parts[i])
                section_content = parts[i + 1].strip()
                sections[section_name] = section_content
        
        return sections
    
    def _assess_section_quality(self, section_name: str, content: str, criteria: Dict) -> Dict:
        """Assess quality of a specific section."""
        score = 100
        issues = []
        warnings = []
        
        # Check minimum length
        if "min_length" in criteria and len(content) < criteria["min_length"]:
            score -= 30
            issues.append(f"{section_name}: Content too short ({len(content)} chars, min {criteria['min_length']})")
        
        # Check minimum items (for list-like sections)
        if "min_items" in criteria:
            items = self._count_list_items(content)
            if items < criteria["min_items"]:
                score -= 25
                issues.append(f"{section_name}: Too few items ({items}, min {criteria['min_items']})")
        
        # Check for required keywords
        if "keywords" in criteria:
            found_keywords = sum(1 for keyword in criteria["keywords"] if keyword.lower() in content.lower())
            keyword_score = (found_keywords / len(criteria["keywords"])) * 20
            score += keyword_score - 20  # Adjust base score
            
            if found_keywords < len(criteria["keywords"]):
                missing = [kw for kw in criteria["keywords"] if kw.lower() not in content.lower()]
                warnings.append(f"{section_name}: Missing keywords: {', '.join(missing)}")
        
        return {
            "score": max(0, min(100, score)),
            "issues": issues,
            "warnings": warnings
        }
    
    def _count_list_items(self, content: str) -> int:
        """Count list items in markdown content."""
        # Count bullet points and numbered lists
        bullet_items = len(re.findall(r'^\s*[-*+]\s+', content, re.MULTILINE))
        numbered_items = len(re.findall(r'^\s*\d+\.\s+', content, re.MULTILINE))
        return bullet_items + numbered_items
    
    def _normalize_section_name(self, name: str) -> str:
        """Normalize section name for comparison."""
        return re.sub(r'[^a-z0-9-]', '-', name.lower().strip())
    
    def _calculate_score(self, found_sections: List[str], quality_scores: Dict[str, int]) -> int:
        """Calculate overall validation score."""
        if not found_sections:
            return 0
        
        # Section completeness (60% of score)
        section_score = (len(found_sections) / len(self.required_sections)) * 60
        
        # Quality scores (40% of score)
        if quality_scores:
            avg_quality = sum(quality_scores.values()) / len(quality_scores)
            quality_score = avg_quality * 0.4
        else:
            quality_score = 0
        
        return int(section_score + quality_score)


def main():
    """Main entry point for brief validation."""
    parser = argparse.ArgumentParser(description="Validate project brief files")
    parser.add_argument("brief_file", help="Path to the brief file to validate")
    parser.add_argument("--output", "-o", help="Output file for validation results (JSON)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    validator = BriefValidator()
    results = validator.validate_brief_file(args.brief_file)
    
    # Output results
    if args.verbose or not args.output:
        print(f"Brief Validation Results for: {args.brief_file}")
        print(f"Status: {results['status'].upper()}")
        print(f"Score: {results['score']}/100")
        
        if results["issues"]:
            print("\nIssues:")
            for issue in results["issues"]:
                print(f"  ❌ {issue}")
        
        if results["warnings"]:
            print("\nWarnings:")
            for warning in results["warnings"]:
                print(f"  ⚠️  {warning}")
        
        if results["sections_found"]:
            print(f"\nSections Found: {len(results['sections_found'])}/{len(validator.required_sections)}")
            for section in results["sections_found"]:
                print(f"  ✅ {section}")
    
    # Save to output file if specified
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Validation results saved to: {args.output}")
    
    # Exit with appropriate code
    if results["status"] == "error":
        sys.exit(2)
    elif results["status"] == "fail":
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
