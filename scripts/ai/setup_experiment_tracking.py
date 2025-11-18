#!/usr/bin/env python3
"""
Script: setup_experiment_tracking.py
Protocol: 12 - AI Algorithm Selection & Baseline Model
Purpose: Setup MLflow or Weights & Biases experiment tracking
"""

import json
import logging
import argparse
import yaml
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_mlflow(project_name: str, baseline_metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Setup MLflow experiment tracking."""
    logger.info(f"Setting up MLflow for project: {project_name}")
    
    try:
        import mlflow
        
        # Set experiment
        mlflow.set_experiment(project_name)
        
        # Start run
        with mlflow.start_run():
            run_id = mlflow.active_run().info.run_id
            
            # Log metrics
            for metric_name, metric_value in baseline_metrics.items():
                if isinstance(metric_value, (int, float)):
                    mlflow.log_metric(metric_name, metric_value)
            
            # Log parameters
            mlflow.log_param("model_type", "baseline")
            mlflow.log_param("algorithm", "random-forest")
            
            logger.info(f"MLflow run created: {run_id}")
            
            return {
                'platform': 'mlflow',
                'project': project_name,
                'run_id': run_id,
                'status': 'success'
            }
    except Exception as e:
        logger.error(f"MLflow setup error: {e}")
        return {'platform': 'mlflow', 'status': 'error', 'error': str(e)}

def setup_wandb(project_name: str, baseline_metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Setup Weights & Biases experiment tracking."""
    logger.info(f"Setting up Weights & Biases for project: {project_name}")
    
    try:
        import wandb
        
        # Initialize run
        run = wandb.init(project=project_name, name="baseline-model")
        
        # Log metrics
        wandb.log(baseline_metrics)
        
        # Log config
        wandb.config.update({"model_type": "baseline", "algorithm": "random-forest"})
        
        run_id = run.id
        logger.info(f"W&B run created: {run_id}")
        
        return {
            'platform': 'wandb',
            'project': project_name,
            'run_id': run_id,
            'status': 'success'
        }
    except Exception as e:
        logger.error(f"W&B setup error: {e}")
        return {'platform': 'wandb', 'status': 'error', 'error': str(e)}

def main(platform: str = "mlflow", project_name: str = "ai-model-training", baseline_model: str = None, baseline_metrics: str = None, output_config: str = None) -> Dict[str, Any]:
    """Main execution function."""
    try:
        logger.info("[PROTOCOL 12 | EXPERIMENT TRACKING SETUP START]")
        
        # Load baseline metrics
        metrics_data = {}
        if baseline_metrics and Path(baseline_metrics).exists():
            with open(baseline_metrics, 'r') as f:
                metrics_file = json.load(f)
                metrics_data = metrics_file.get('metrics', {})
        
        # Setup tracking platform
        if platform.lower() == "mlflow":
            result = setup_mlflow(project_name, metrics_data)
        elif platform.lower() == "wandb":
            result = setup_wandb(project_name, metrics_data)
        else:
            raise ValueError(f"Unknown platform: {platform}")
        
        # Save configuration
        if output_config:
            output_path = Path(output_config)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            config = {
                'timestamp': datetime.now().isoformat(),
                'platform': platform,
                'project': project_name,
                'tracking_info': result,
                'baseline_model': baseline_model,
                'status': 'configured'
            }
            with open(output_path, 'w') as f:
                yaml.dump(config, f)
            logger.info(f"Experiment tracking configuration saved to {output_config}")
        
        logger.info("[PROTOCOL 12 | EXPERIMENT TRACKING SETUP COMPLETE]")
        return {"status": "success", "data": result}
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Setup experiment tracking")
    parser.add_argument("--platform", default="mlflow", help="Tracking platform (mlflow or wandb)")
    parser.add_argument("--project-name", default="ai-model-training", help="Project name")
    parser.add_argument("--baseline-model", help="Path to baseline model")
    parser.add_argument("--baseline-metrics", help="Path to baseline metrics")
    parser.add_argument("--output-config", help="Output configuration file path")
    
    args = parser.parse_args()
    result = main(args.platform, args.project_name, args.baseline_model, args.baseline_metrics, args.output_config)
    exit(0 if result["status"] == "success" else 1)
