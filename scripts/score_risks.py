#!/usr/bin/env python3
"""
Risk Scoring Script

Automatically scores risks by impact and likelihood according to Protocol 00 standards.
Generates risk matrix and prioritization recommendations.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class RiskLevel(Enum):
    """Risk level enumeration."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class Risk:
    """Risk data structure."""
    description: str
    impact: RiskLevel
    likelihood: RiskLevel
    category: str
    mitigation: Optional[str] = None
    owner: Optional[str] = None
    
    @property
    def score(self) -> int:
        """Calculate risk score (impact * likelihood)."""
        return self.impact.value * self.likelihood.value
    
    @property
    def level(self) -> RiskLevel:
        """Determine overall risk level."""
        if self.score >= 12:
            return RiskLevel.CRITICAL
        elif self.score >= 9:
            return RiskLevel.HIGH
        elif self.score >= 4:
            return RiskLevel.MEDIUM
        else:
            return RiskLevel.LOW


class RiskScorer:
    """Automatically scores risks from project briefs."""
    
    def __init__(self):
        # Risk keywords and their associated levels
        self.impact_keywords = {
            RiskLevel.CRITICAL: [
                "critical", "severe", "catastrophic", "complete failure", 
                "data loss", "security breach", "compliance violation",
                "project failure", "budget overrun", "timeline failure"
            ],
            RiskLevel.HIGH: [
                "major", "significant", "substantial", "serious",
                "performance impact", "user experience", "reputation",
                "delivery delay", "cost increase", "scope creep"
            ],
            RiskLevel.MEDIUM: [
                "moderate", "some", "limited", "partial",
                "minor delay", "small increase", "manageable",
                "temporary", "short-term", "localized"
            ],
            RiskLevel.LOW: [
                "minimal", "negligible", "minor", "low",
                "cosmetic", "non-critical", "optional",
                "nice-to-have", "enhancement", "optimization"
            ]
        }
        
        self.likelihood_keywords = {
            RiskLevel.CRITICAL: [
                "certain", "guaranteed", "definite", "inevitable",
                "always", "every time", "consistently", "recurring"
            ],
            RiskLevel.HIGH: [
                "likely", "probable", "frequent", "common",
                "often", "regularly", "typically", "usually"
            ],
            RiskLevel.MEDIUM: [
                "possible", "occasional", "sometimes", "moderate",
                "intermittent", "periodic", "variable", "uncertain"
            ],
            RiskLevel.LOW: [
                "unlikely", "rare", "seldom", "infrequent",
                "remote", "minimal", "low", "uncommon"
            ]
        }
        
        self.risk_categories = [
            "technical", "business", "operational", "security",
            "compliance", "resource", "timeline", "budget",
            "quality", "integration", "user", "vendor"
        ]
    
    def score_risks_from_brief(self, brief_path: str) -> Dict:
        """Extract and score risks from a project brief."""
        try:
            brief_content = Path(brief_path).read_text(encoding='utf-8')
        except FileNotFoundError:
            return {
                "status": "error",
                "message": f"Brief file not found: {brief_path}",
                "risks": []
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error reading brief file: {str(e)}",
                "risks": []
            }
        
        # Extract risks section
        risks_section = self._extract_risks_section(brief_content)
        if not risks_section:
            return {
                "status": "warning",
                "message": "No risks section found in brief",
                "risks": [],
                "risk_matrix": {"critical": [], "high": [], "medium": [], "low": []},
                "recommendations": [],
                "summary": {"total": 0, "average_score": 0, "distribution": {}}
            }
        
        # Parse individual risks
        risks = self._parse_risks(risks_section)
        
        # Score each risk
        scored_risks = []
        for risk_text in risks:
            risk = self._score_individual_risk(risk_text)
            if risk:
                scored_risks.append(risk)
        
        # Generate risk matrix and recommendations
        risk_matrix = self._generate_risk_matrix(scored_risks)
        recommendations = self._generate_recommendations(scored_risks)
        
        return {
            "status": "success",
            "total_risks": len(scored_risks),
            "risks": [self._risk_to_dict(r) for r in scored_risks],
            "risk_matrix": risk_matrix,
            "recommendations": recommendations,
            "summary": self._generate_summary(scored_risks)
        }
    
    def _extract_risks_section(self, content: str) -> Optional[str]:
        """Extract the risks section from brief content."""
        # Look for risks section
        patterns = [
            r'##\s+Risks?\s*?\n(.*?)(?=\n##|\Z)',
            r'##\s+Risks?\s+and\s+Dependencies?\s*?\n(.*?)(?=\n##|\Z)',
            r'###\s+Risks?\s*?\n(.*?)(?=\n###|\n##|\Z)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None
    
    def _parse_risks(self, risks_section: str) -> List[str]:
        """Parse individual risks from the risks section."""
        risks = []
        
        # Split by bullet points or numbered lists
        lines = risks_section.split('\n')
        current_risk = []
        
        for line in lines:
            line = line.strip()
            if not line:
                if current_risk:
                    risks.append('\n'.join(current_risk))
                    current_risk = []
            elif re.match(r'^\s*[-*+]\s+', line) or re.match(r'^\s*\d+\.\s+', line):
                if current_risk:
                    risks.append('\n'.join(current_risk))
                current_risk = [line]
            else:
                current_risk.append(line)
        
        if current_risk:
            risks.append('\n'.join(current_risk))
        
        return risks
    
    def _score_individual_risk(self, risk_text: str) -> Optional[Risk]:
        """Score an individual risk based on its text content."""
        # Extract description (first line, cleaned)
        lines = risk_text.split('\n')
        description = lines[0].strip()
        description = re.sub(r'^\s*[-*+]\s+', '', description)
        description = re.sub(r'^\s*\d+\.\s+', '', description)
        
        if not description:
            return None
        
        # Determine impact level
        impact = self._determine_level(risk_text, self.impact_keywords)
        
        # Determine likelihood level
        likelihood = self._determine_level(risk_text, self.likelihood_keywords)
        
        # Determine category
        category = self._determine_category(risk_text)
        
        # Extract mitigation if present
        mitigation = self._extract_mitigation(risk_text)
        
        return Risk(
            description=description,
            impact=impact,
            likelihood=likelihood,
            category=category,
            mitigation=mitigation
        )
    
    def _determine_level(self, text: str, keyword_map: Dict[RiskLevel, List[str]]) -> RiskLevel:
        """Determine risk level based on keywords."""
        text_lower = text.lower()
        
        # Check for highest level first
        for level in [RiskLevel.CRITICAL, RiskLevel.HIGH, RiskLevel.MEDIUM, RiskLevel.LOW]:
            for keyword in keyword_map[level]:
                if keyword in text_lower:
                    return level
        
        # Default to medium if no keywords found
        return RiskLevel.MEDIUM
    
    def _determine_category(self, text: str) -> str:
        """Determine risk category based on content."""
        text_lower = text.lower()
        
        category_keywords = {
            "technical": ["technical", "technology", "code", "development", "bug", "error"],
            "business": ["business", "market", "customer", "revenue", "profit"],
            "operational": ["operational", "process", "workflow", "procedure"],
            "security": ["security", "privacy", "breach", "vulnerability", "attack"],
            "compliance": ["compliance", "regulation", "legal", "audit", "policy"],
            "resource": ["resource", "staff", "personnel", "team", "expertise"],
            "timeline": ["timeline", "schedule", "deadline", "delay", "time"],
            "budget": ["budget", "cost", "financial", "money", "expense"],
            "quality": ["quality", "testing", "validation", "verification"],
            "integration": ["integration", "api", "interface", "connection"],
            "user": ["user", "customer", "end-user", "experience", "usability"],
            "vendor": ["vendor", "supplier", "third-party", "external"]
        }
        
        for category, keywords in category_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                return category
        
        return "general"
    
    def _extract_mitigation(self, text: str) -> Optional[str]:
        """Extract mitigation strategy if present."""
        mitigation_patterns = [
            r'mitigation[:\s]+(.+?)(?:\n|$)',
            r'mitigate[:\s]+(.+?)(?:\n|$)',
            r'solution[:\s]+(.+?)(?:\n|$)',
            r'address[:\s]+(.+?)(?:\n|$)'
        ]
        
        for pattern in mitigation_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None
    
    def _generate_risk_matrix(self, risks: List[Risk]) -> Dict:
        """Generate risk matrix visualization data."""
        matrix = {
            "critical": [],
            "high": [],
            "medium": [],
            "low": []
        }
        
        for risk in risks:
            matrix[risk.level.name.lower()].append({
                "description": risk.description,
                "score": risk.score,
                "category": risk.category
            })
        
        return matrix
    
    def _generate_recommendations(self, risks: List[Risk]) -> List[str]:
        """Generate risk management recommendations."""
        recommendations = []
        
        # Count risks by level
        level_counts = {}
        for risk in risks:
            level = risk.level.name.lower()
            level_counts[level] = level_counts.get(level, 0) + 1
        
        # Generate recommendations based on risk distribution
        if level_counts.get("critical", 0) > 0:
            recommendations.append("🚨 CRITICAL: Address critical risks immediately before project start")
        
        if level_counts.get("high", 0) > 3:
            recommendations.append("⚠️ HIGH: Consider reducing scope or extending timeline for high-risk items")
        
        if level_counts.get("medium", 0) > 5:
            recommendations.append("📋 MEDIUM: Implement regular risk monitoring and mitigation planning")
        
        # Category-specific recommendations
        categories = {}
        for risk in risks:
            cat = risk.category
            categories[cat] = categories.get(cat, 0) + 1
        
        for category, count in categories.items():
            if count > 2:
                recommendations.append(f"🎯 {category.title()}: Focus risk management efforts on {category} risks")
        
        return recommendations
    
    def _generate_summary(self, risks: List[Risk]) -> Dict:
        """Generate risk summary statistics."""
        if not risks:
            return {"total": 0, "average_score": 0, "distribution": {}}
        
        total_score = sum(risk.score for risk in risks)
        avg_score = total_score / len(risks)
        
        distribution = {}
        for risk in risks:
            level = risk.level.name.lower()
            distribution[level] = distribution.get(level, 0) + 1
        
        return {
            "total": len(risks),
            "average_score": round(avg_score, 2),
            "distribution": distribution,
            "highest_risk": max(risks, key=lambda r: r.score).description if risks else None
        }
    
    def _risk_to_dict(self, risk: Risk) -> Dict:
        """Convert Risk object to dictionary."""
        return {
            "description": risk.description,
            "impact": risk.impact.name.lower(),
            "likelihood": risk.likelihood.name.lower(),
            "category": risk.category,
            "score": risk.score,
            "level": risk.level.name.lower(),
            "mitigation": risk.mitigation
        }


def main():
    """Main entry point for risk scoring."""
    parser = argparse.ArgumentParser(description="Score risks from project brief")
    parser.add_argument("brief_file", help="Path to the brief file containing risks")
    parser.add_argument("--output", "-o", help="Output file for risk scores (JSON)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    scorer = RiskScorer()
    results = scorer.score_risks_from_brief(args.brief_file)
    
    # Output results
    if args.verbose or not args.output:
        print(f"Risk Scoring Results for: {args.brief_file}")
        print(f"Status: {results['status'].upper()}")
        
        if results["status"] == "error":
            print(f"Error: {results['message']}")
        else:
            summary = results["summary"]
            print(f"Total Risks: {summary['total']}")
            print(f"Average Score: {summary['average_score']}")
            
            if results["risks"]:
                print("\nRisk Breakdown:")
                for risk in results["risks"]:
                    print(f"  {risk['level'].upper()}: {risk['description'][:60]}...")
                    print(f"    Score: {risk['score']} | Category: {risk['category']}")
            
            if results["recommendations"]:
                print("\nRecommendations:")
                for rec in results["recommendations"]:
                    print(f"  {rec}")
    
    # Save to output file if specified
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Risk scores saved to: {args.output}")
    
    # Exit with appropriate code
    if results["status"] == "error":
        sys.exit(2)
    elif results["summary"]["total"] == 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
