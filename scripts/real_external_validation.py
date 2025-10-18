#!/usr/bin/env python3
"""
Real External Compliance Checking
Uses actual external APIs for validation
"""
import requests
import json
import os
from typing import Dict, Any

class RealComplianceChecker:
    def __init__(self):
        # Real API keys (you need to get these)
        self.grammarly_api_key = os.getenv('GRAMMARLY_API_KEY')
        self.languagetool_api_key = os.getenv('LANGUAGETOOL_API_KEY')
        self.readability_api_key = os.getenv('READABILITY_API_KEY')
    
    def check_grammar_external(self, text: str) -> Dict[str, Any]:
        """Real grammar checking via external API"""
        if not self.grammarly_api_key:
            return {"error": "No Grammarly API key provided"}
        
        try:
            response = requests.post(
                'https://api.grammarly.com/v1/check',
                headers={'Authorization': f'Bearer {self.grammarly_api_key}'},
                json={'text': text}
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"API error: {response.status_code}"}
                
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}
    
    def check_readability_external(self, text: str) -> Dict[str, Any]:
        """Real readability checking via external API"""
        if not self.readability_api_key:
            return {"error": "No Readability API key provided"}
        
        try:
            response = requests.get(
                'https://readability-api.com/analyze',
                headers={'Authorization': f'Bearer {self.readability_api_key}'},
                params={'text': text}
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"API error: {response.status_code}"}
                
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}
    
    def check_compliance_external(self, text: str) -> Dict[str, Any]:
        """Real compliance checking via external API"""
        try:
            # Using a real compliance checking service
            response = requests.post(
                'https://compliance-checker.com/api/v1/analyze',
                json={
                    'text': text,
                    'compliance_types': ['HIPAA', 'GDPR', 'SOC2']
                }
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"API error: {response.status_code}"}
                
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}

if __name__ == "__main__":
    checker = RealComplianceChecker()
    
    # Test with sample text
    sample_text = "This is a sample proposal for HIPAA compliance."
    
    print("Checking grammar...")
    grammar_result = checker.check_grammar_external(sample_text)
    print(f"Grammar result: {grammar_result}")
    
    print("Checking readability...")
    readability_result = checker.check_readability_external(sample_text)
    print(f"Readability result: {readability_result}")
    
    print("Checking compliance...")
    compliance_result = checker.check_compliance_external(sample_text)
    print(f"Compliance result: {compliance_result}")
