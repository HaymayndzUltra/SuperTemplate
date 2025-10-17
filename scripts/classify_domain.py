#!/usr/bin/env python3
"""
Domain Classification Script

Automatically classifies project domain from job post content using keyword analysis
and pattern matching according to Protocol 00 standards.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class Domain(Enum):
    """Project domain enumeration."""
    WEB_MOBILE = "web-mobile"
    DATA_BI = "data-bi"
    ML_AI = "ml-ai"
    INFRASTRUCTURE = "infrastructure"
    OTHER = "other"


@dataclass
class DomainClassification:
    """Domain classification result."""
    primary_domain: Domain
    confidence: float
    secondary_domains: List[Domain]
    keywords_found: List[str]
    reasoning: str


class DomainClassifier:
    """Classifies project domain from job post content."""
    
    def __init__(self):
        # Domain-specific keyword patterns
        self.domain_patterns = {
            Domain.WEB_MOBILE: {
                "keywords": [
                    # Frontend technologies
                    "react", "vue", "angular", "javascript", "typescript", "html", "css",
                    "frontend", "ui", "ux", "user interface", "user experience",
                    "responsive", "mobile", "app", "website", "web application",
                    "component", "widget", "dashboard", "form", "button", "layout",
                    # Mobile specific
                    "ios", "android", "flutter", "react native", "mobile app",
                    "cross-platform", "native", "hybrid",
                    # Design
                    "design", "mockup", "wireframe", "prototype", "figma", "sketch",
                    "design system", "ui kit", "component library"
                ],
                "patterns": [
                    r'\b(?:create|build|develop|design)\s+(?:a\s+)?(?:web|mobile|app|site|interface)',
                    r'\b(?:frontend|ui|ux|user\s+interface|user\s+experience)',
                    r'\b(?:responsive|mobile-friendly|cross-platform)',
                    r'\b(?:component|widget|dashboard|form|button)\s+(?:library|kit|system)'
                ]
            },
            
            Domain.DATA_BI: {
                "keywords": [
                    # Data technologies
                    "data", "database", "sql", "analytics", "reporting", "dashboard",
                    "tableau", "power bi", "excel", "csv", "json", "api", "etl",
                    "data visualization", "charts", "graphs", "metrics", "kpi",
                    "business intelligence", "data analysis", "statistics",
                    # BI specific
                    "report", "insight", "trend", "forecast", "prediction",
                    "data warehouse", "data lake", "olap", "olap", "etl",
                    "real estate", "loan", "financial", "sales", "marketing"
                ],
                "patterns": [
                    r'\b(?:data|analytics|reporting|dashboard|visualization)',
                    r'\b(?:tableau|power\s+bi|excel|sql|database)',
                    r'\b(?:extract|visualize|analyze)\s+(?:data|information)',
                    r'\b(?:business\s+intelligence|data\s+analysis|reporting)'
                ]
            },
            
            Domain.ML_AI: {
                "keywords": [
                    # ML/AI technologies
                    "machine learning", "artificial intelligence", "ai", "ml",
                    "python", "tensorflow", "pytorch", "scikit-learn", "pandas",
                    "neural network", "deep learning", "model", "algorithm",
                    "prediction", "classification", "regression", "clustering",
                    "nlp", "natural language processing", "computer vision",
                    "data science", "jupyter", "notebook", "training", "inference"
                ],
                "patterns": [
                    r'\b(?:machine\s+learning|artificial\s+intelligence|ai|ml)',
                    r'\b(?:model|algorithm|prediction|classification|training)',
                    r'\b(?:neural\s+network|deep\s+learning|nlp|computer\s+vision)',
                    r'\b(?:tensorflow|pytorch|scikit-learn|pandas|jupyter)'
                ]
            },
            
            Domain.INFRASTRUCTURE: {
                "keywords": [
                    # Infrastructure technologies
                    "devops", "deployment", "ci/cd", "docker", "kubernetes",
                    "aws", "azure", "gcp", "cloud", "server", "hosting",
                    "monitoring", "logging", "security", "backup", "scaling",
                    "infrastructure", "environment", "production", "staging",
                    "automation", "scripting", "configuration", "terraform",
                    "jenkins", "github actions", "pipeline", "workflow"
                ],
                "patterns": [
                    r'\b(?:devops|deployment|ci/cd|infrastructure|cloud)',
                    r'\b(?:docker|kubernetes|aws|azure|gcp|server)',
                    r'\b(?:monitoring|logging|security|backup|scaling)',
                    r'\b(?:automation|pipeline|workflow|environment)'
                ]
            }
        }
        
        # General technology keywords that might indicate domain
        self.tech_keywords = {
            "frontend": ["react", "vue", "angular", "javascript", "html", "css"],
            "backend": ["node", "python", "java", "php", "ruby", "api", "server"],
            "database": ["sql", "mysql", "postgresql", "mongodb", "redis"],
            "mobile": ["ios", "android", "flutter", "react native"],
            "data": ["tableau", "power bi", "excel", "analytics", "reporting"],
            "ai": ["tensorflow", "pytorch", "machine learning", "ai"],
            "cloud": ["aws", "azure", "gcp", "docker", "kubernetes"]
        }
    
    def classify_domain(self, content: str) -> DomainClassification:
        """Classify domain from job post content."""
        content_lower = content.lower()
        
        # Calculate scores for each domain
        domain_scores = {}
        keywords_found = {}
        
        for domain, patterns in self.domain_patterns.items():
            score = 0
            found_keywords = []
            
            # Score based on keywords
            for keyword in patterns["keywords"]:
                if keyword in content_lower:
                    score += 1
                    found_keywords.append(keyword)
            
            # Score based on patterns
            for pattern in patterns["patterns"]:
                matches = re.findall(pattern, content_lower)
                score += len(matches) * 2  # Patterns are weighted higher
            
            domain_scores[domain] = score
            keywords_found[domain] = found_keywords
        
        # Determine primary domain
        if not domain_scores or max(domain_scores.values()) == 0:
            primary_domain = Domain.OTHER
            confidence = 0.0
        else:
            primary_domain = max(domain_scores, key=domain_scores.get)
            max_score = domain_scores[primary_domain]
            total_possible = len(self.domain_patterns[primary_domain]["keywords"]) + len(self.domain_patterns[primary_domain]["patterns"]) * 2
            confidence = min(1.0, max_score / total_possible) if total_possible > 0 else 0.0
        
        # Determine secondary domains (domains with > 50% of primary score)
        secondary_domains = []
        if primary_domain in domain_scores:
            primary_score = domain_scores[primary_domain]
            for domain, score in domain_scores.items():
                if domain != primary_domain and score > primary_score * 0.5:
                    secondary_domains.append(domain)
        
        # Generate reasoning
        reasoning = self._generate_reasoning(primary_domain, keywords_found.get(primary_domain, []), confidence)
        
        return DomainClassification(
            primary_domain=primary_domain,
            confidence=confidence,
            secondary_domains=secondary_domains,
            keywords_found=keywords_found.get(primary_domain, []),
            reasoning=reasoning
        )
    
    def classify_from_file(self, file_path: str) -> Dict:
        """Classify domain from a file."""
        try:
            content = Path(file_path).read_text(encoding='utf-8')
        except FileNotFoundError:
            return {
                "status": "error",
                "message": f"File not found: {file_path}",
                "classification": None
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error reading file: {str(e)}",
                "classification": None
            }
        
        classification = self.classify_domain(content)
        
        return {
            "status": "success",
            "classification": {
                "primary_domain": classification.primary_domain.value,
                "confidence": round(classification.confidence, 3),
                "secondary_domains": [d.value for d in classification.secondary_domains],
                "keywords_found": classification.keywords_found,
                "reasoning": classification.reasoning
            }
        }
    
    def _generate_reasoning(self, domain: Domain, keywords: List[str], confidence: float) -> str:
        """Generate human-readable reasoning for classification."""
        if confidence == 0.0:
            return "No clear domain indicators found in the content."
        
        domain_names = {
            Domain.WEB_MOBILE: "Web/Mobile Development",
            Domain.DATA_BI: "Data/BI Analytics", 
            Domain.ML_AI: "Machine Learning/AI",
            Domain.INFRASTRUCTURE: "Infrastructure/DevOps",
            Domain.OTHER: "Other/General"
        }
        
        reasoning_parts = [
            f"Classified as {domain_names[domain]} with {confidence:.1%} confidence."
        ]
        
        if keywords:
            top_keywords = keywords[:5]  # Show top 5 keywords
            reasoning_parts.append(f"Key indicators: {', '.join(top_keywords)}")
        
        if confidence > 0.8:
            reasoning_parts.append("High confidence classification.")
        elif confidence > 0.5:
            reasoning_parts.append("Moderate confidence classification.")
        else:
            reasoning_parts.append("Low confidence classification - manual review recommended.")
        
        return " ".join(reasoning_parts)
    
    def get_domain_adapters(self, domain: Domain) -> Dict:
        """Get domain-specific extraction patterns and templates."""
        adapters = {
            Domain.WEB_MOBILE: {
                "extraction_focus": ["UI components", "user flows", "responsive design", "interactions"],
                "common_deliverables": ["UI components", "pages", "mobile app", "responsive website"],
                "typical_constraints": ["browser compatibility", "performance", "accessibility", "mobile-first"]
            },
            Domain.DATA_BI: {
                "extraction_focus": ["data sources", "metrics", "visualization requirements", "reporting needs"],
                "common_deliverables": ["dashboard", "reports", "data visualization", "analytics platform"],
                "typical_constraints": ["data accuracy", "real-time updates", "user permissions", "data privacy"]
            },
            Domain.ML_AI: {
                "extraction_focus": ["data requirements", "model performance", "training data", "inference needs"],
                "common_deliverables": ["ML model", "prediction API", "data pipeline", "model training system"],
                "typical_constraints": ["model accuracy", "training time", "inference speed", "data quality"]
            },
            Domain.INFRASTRUCTURE: {
                "extraction_focus": ["deployment requirements", "scaling needs", "security requirements", "monitoring"],
                "common_deliverables": ["deployment pipeline", "monitoring system", "infrastructure as code", "CI/CD"],
                "typical_constraints": ["uptime", "security", "scalability", "cost optimization"]
            },
            Domain.OTHER: {
                "extraction_focus": ["general requirements", "business logic", "integration needs"],
                "common_deliverables": ["custom solution", "integration", "business application"],
                "typical_constraints": ["timeline", "budget", "quality", "maintainability"]
            }
        }
        
        return adapters.get(domain, adapters[Domain.OTHER])


def main():
    """Main entry point for domain classification."""
    parser = argparse.ArgumentParser(description="Classify project domain from job post")
    parser.add_argument("input_file", help="Path to the job post file")
    parser.add_argument("--output", "-o", help="Output file for classification results (JSON)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--adapters", "-a", action="store_true", help="Show domain adapters")
    
    args = parser.parse_args()
    
    classifier = DomainClassifier()
    results = classifier.classify_from_file(args.input_file)
    
    # Output results
    if args.verbose or not args.output:
        print(f"Domain Classification Results for: {args.input_file}")
        print(f"Status: {results['status'].upper()}")
        
        if results["status"] == "error":
            print(f"Error: {results['message']}")
        else:
            classification = results["classification"]
            print(f"Primary Domain: {classification['primary_domain']}")
            print(f"Confidence: {classification['confidence']:.1%}")
            
            if classification["secondary_domains"]:
                print(f"Secondary Domains: {', '.join(classification['secondary_domains'])}")
            
            print(f"Reasoning: {classification['reasoning']}")
            
            if classification["keywords_found"]:
                print(f"Keywords Found: {', '.join(classification['keywords_found'][:10])}")
            
            # Show domain adapters if requested
            if args.adapters:
                domain_enum = Domain(classification["primary_domain"])
                adapters = classifier.get_domain_adapters(domain_enum)
                print(f"\nDomain Adapters for {classification['primary_domain']}:")
                for key, value in adapters.items():
                    print(f"  {key}: {value}")
    
    # Save to output file if specified
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Classification results saved to: {args.output}")
    
    # Exit with appropriate code
    if results["status"] == "error":
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
