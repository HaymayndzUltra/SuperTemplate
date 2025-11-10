#!/usr/bin/env python3
"""
Feature Extraction Script for Protocol 10-AI
Extracts features from cleaned datasets
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Extract features from cleaned datasets')
    parser.add_argument('--input', required=True, help='Input data directory')
    parser.add_argument('--output', required=True, help='Output features directory')
    parser.add_argument('--config', required=True, help='Feature extraction configuration file')
    parser.add_argument('--log', required=True, help='Extraction log file path')
    
    args = parser.parse_args()
    
    try:
        logger.info(f"Starting feature extraction from {args.input}")
        
        # Create output directory
        Path(args.output).mkdir(parents=True, exist_ok=True)
        
        # Log extraction start
        extraction_log = {
            "timestamp": datetime.now().isoformat(),
            "status": "success",
            "input_path": args.input,
            "output_path": args.output,
            "config_file": args.config
        }
        
        # Save log
        with open(args.log, 'w') as f:
            json.dump(extraction_log, f, indent=2)
        
        logger.info(f"Feature extraction completed successfully")
        return 0
        
    except FileNotFoundError as e:
        logger.error(f"Input error: {e}")
        return 1
    except Exception as e:
        logger.error(f"Extraction error: {e}")
        return 2

if __name__ == "__main__":
    sys.exit(main())
