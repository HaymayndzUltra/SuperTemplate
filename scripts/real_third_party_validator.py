#!/usr/bin/env python3
"""
Real Third-Party Tools Integration
Uses actual external tools and services
"""
import subprocess
import requests
import json
import os
from typing import Dict, Any

class RealThirdPartyValidator:
    def __init__(self):
        self.tools_available = self.check_tools_availability()
    
    def check_tools_availability(self) -> Dict[str, bool]:
        """Check which external tools are available"""
        tools = {}
        
        # Check for LanguageTool
        try:
            result = subprocess.run(['java', '-version'], 
                                  capture_output=True, text=True)
            tools['languagetool'] = result.returncode == 0
        except:
            tools['languagetool'] = False
        
        # Check for Bandit (security scanner)
        try:
            result = subprocess.run(['bandit', '--version'], 
                                  capture_output=True, text=True)
            tools['bandit'] = result.returncode == 0
        except:
            tools['bandit'] = False
        
        # Check for Safety (vulnerability scanner)
        try:
            result = subprocess.run(['safety', '--version'], 
                                  capture_output=True, text=True)
            tools['safety'] = result.returncode == 0
        except:
            tools['safety'] = False
        
        return tools
    
    def run_languagetool(self, text: str) -> Dict[str, Any]:
        """Run real LanguageTool grammar checking"""
        if not self.tools_available['languagetool']:
            return {"error": "LanguageTool not available"}
        
        try:
            # Write text to temporary file
            with open('/tmp/text_to_check.txt', 'w') as f:
                f.write(text)
            
            # Run LanguageTool
            result = subprocess.run([
                'java', '-jar', '/path/to/languagetool-commandline.jar',
                '/tmp/text_to_check.txt'
            ], capture_output=True, text=True)
            
            return {
                "status": "success",
                "output": result.stdout,
                "errors": result.stderr
            }
            
        except Exception as e:
            return {"error": f"LanguageTool failed: {str(e)}"}
    
    def run_security_scan(self, file_path: str) -> Dict[str, Any]:
        """Run real security scanning"""
        if not self.tools_available['bandit']:
            return {"error": "Bandit not available"}
        
        try:
            result = subprocess.run([
                'bandit', '-r', file_path, '-f', 'json'
            ], capture_output=True, text=True)
            
            return {
                "status": "success",
                "output": result.stdout,
                "errors": result.stderr
            }
            
        except Exception as e:
            return {"error": f"Security scan failed: {str(e)}"}
    
    def run_vulnerability_scan(self) -> Dict[str, Any]:
        """Run real vulnerability scanning"""
        if not self.tools_available['safety']:
            return {"error": "Safety not available"}
        
        try:
            result = subprocess.run([
                'safety', 'check', '--json'
            ], capture_output=True, text=True)
            
            return {
                "status": "success",
                "output": result.stdout,
                "errors": result.stderr
            }
            
        except Exception as e:
            return {"error": f"Vulnerability scan failed: {str(e)}"}
    
    def check_external_apis(self, text: str) -> Dict[str, Any]:
        """Check external APIs for validation"""
        results = {}
        
        # Check Grammarly API
        grammarly_key = os.getenv('GRAMMARLY_API_KEY')
        if grammarly_key:
            try:
                response = requests.post(
                    'https://api.grammarly.com/v1/check',
                    headers={'Authorization': f'Bearer {grammarly_key}'},
                    json={'text': text}
                )
                results['grammarly'] = response.json() if response.status_code == 200 else {"error": "API error"}
            except Exception as e:
                results['grammarly'] = {"error": str(e)}
        else:
            results['grammarly'] = {"error": "No API key"}
        
        # Check Readability API
        readability_key = os.getenv('READABILITY_API_KEY')
        if readability_key:
            try:
                response = requests.get(
                    'https://readability-api.com/analyze',
                    headers={'Authorization': f'Bearer {readability_key}'},
                    params={'text': text}
                )
                results['readability'] = response.json() if response.status_code == 200 else {"error": "API error"}
            except Exception as e:
                results['readability'] = {"error": str(e)}
        else:
            results['readability'] = {"error": "No API key"}
        
        return results

if __name__ == "__main__":
    validator = RealThirdPartyValidator()
    
    print("Available tools:")
    for tool, available in validator.tools_available.items():
        print(f"  {tool}: {'✅' if available else '❌'}")
    
    # Test with sample text
    sample_text = "This is a sample proposal for testing."
    
    print("\nTesting external APIs...")
    api_results = validator.check_external_apis(sample_text)
    print(f"API results: {json.dumps(api_results, indent=2)}")
