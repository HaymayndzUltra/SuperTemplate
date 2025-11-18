#!/usr/bin/env python3
"""
Script: version_dataset.py
Protocol: 11 - AI Dataset Preparation & Splitting
Purpose: Version datasets using DVC or Git LFS with complete audit trails
"""

import json
import logging
import argparse
import subprocess
import hashlib
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def calculate_checksum(file_path: str) -> str:
    """Calculate SHA-256 checksum for a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_file_size(file_path: str) -> int:
    """Get file size in bytes."""
    return os.path.getsize(file_path)


def init_dvc(dataset_dir: str) -> Dict[str, Any]:
    """Initialize DVC for dataset versioning."""
    logger.info("Initializing DVC for dataset versioning")
    
    try:
        # Check if DVC is installed
        subprocess.run(["dvc", "--version"], capture_output=True, check=True)
        logger.info("DVC is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.error("DVC is not installed. Install with: pip install dvc")
        return {"status": "error", "message": "DVC not installed"}
    
    try:
        # Initialize DVC in current directory
        result = subprocess.run(
            ["dvc", "init", "--no-scm"],
            cwd=dataset_dir,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0 or "already initialized" in result.stderr.lower():
            logger.info("DVC initialized successfully")
            return {"status": "success", "message": "DVC initialized"}
        else:
            logger.error(f"DVC initialization failed: {result.stderr}")
            return {"status": "error", "message": result.stderr}
    
    except Exception as e:
        logger.error(f"Error initializing DVC: {e}")
        return {"status": "error", "message": str(e)}


def add_datasets_to_dvc(dataset_dir: str, version: str) -> Dict[str, Any]:
    """Add datasets to DVC tracking."""
    logger.info(f"Adding datasets to DVC with version {version}")
    
    dataset_path = Path(dataset_dir)
    results = {
        "added_files": [],
        "errors": []
    }
    
    try:
        # Find all parquet files
        parquet_files = list(dataset_path.glob("*.parquet"))
        
        if not parquet_files:
            logger.warning("No parquet files found in dataset directory")
            return {"status": "warning", "message": "No parquet files found"}
        
        for file_path in parquet_files:
            try:
                # Add file to DVC
                result = subprocess.run(
                    ["dvc", "add", str(file_path)],
                    cwd=str(dataset_path.parent),
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    logger.info(f"Added {file_path.name} to DVC")
                    results["added_files"].append(str(file_path))
                else:
                    logger.error(f"Failed to add {file_path.name}: {result.stderr}")
                    results["errors"].append({"file": file_path.name, "error": result.stderr})
            
            except Exception as e:
                logger.error(f"Error adding {file_path.name} to DVC: {e}")
                results["errors"].append({"file": file_path.name, "error": str(e)})
        
        return {"status": "success", "results": results}
    
    except Exception as e:
        logger.error(f"Error adding datasets to DVC: {e}")
        return {"status": "error", "message": str(e)}


def init_git_lfs(dataset_dir: str) -> Dict[str, Any]:
    """Initialize Git LFS for dataset versioning."""
    logger.info("Initializing Git LFS for dataset versioning")
    
    try:
        # Check if Git LFS is installed
        subprocess.run(["git", "lfs", "--version"], capture_output=True, check=True)
        logger.info("Git LFS is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.error("Git LFS is not installed. Install with: git lfs install")
        return {"status": "error", "message": "Git LFS not installed"}
    
    try:
        # Initialize Git LFS
        result = subprocess.run(
            ["git", "lfs", "install"],
            cwd=dataset_dir,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            logger.info("Git LFS initialized successfully")
            return {"status": "success", "message": "Git LFS initialized"}
        else:
            logger.error(f"Git LFS initialization failed: {result.stderr}")
            return {"status": "error", "message": result.stderr}
    
    except Exception as e:
        logger.error(f"Error initializing Git LFS: {e}")
        return {"status": "error", "message": str(e)}


def add_datasets_to_git_lfs(dataset_dir: str, version: str) -> Dict[str, Any]:
    """Add datasets to Git LFS tracking."""
    logger.info(f"Adding datasets to Git LFS with version {version}")
    
    dataset_path = Path(dataset_dir)
    results = {
        "tracked_files": [],
        "errors": []
    }
    
    try:
        # Find all parquet files
        parquet_files = list(dataset_path.glob("*.parquet"))
        
        if not parquet_files:
            logger.warning("No parquet files found in dataset directory")
            return {"status": "warning", "message": "No parquet files found"}
        
        for file_path in parquet_files:
            try:
                # Track file with Git LFS
                result = subprocess.run(
                    ["git", "lfs", "track", file_path.name],
                    cwd=str(dataset_path),
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    logger.info(f"Tracked {file_path.name} with Git LFS")
                    results["tracked_files"].append(file_path.name)
                else:
                    logger.error(f"Failed to track {file_path.name}: {result.stderr}")
                    results["errors"].append({"file": file_path.name, "error": result.stderr})
            
            except Exception as e:
                logger.error(f"Error tracking {file_path.name} with Git LFS: {e}")
                results["errors"].append({"file": file_path.name, "error": str(e)})
        
        return {"status": "success", "results": results}
    
    except Exception as e:
        logger.error(f"Error adding datasets to Git LFS: {e}")
        return {"status": "error", "message": str(e)}


def create_version_metadata(
    dataset_dir: str,
    version: str,
    version_method: str
) -> Dict[str, Any]:
    """Create version metadata for datasets."""
    logger.info(f"Creating version metadata for {version}")
    
    dataset_path = Path(dataset_dir)
    metadata = {
        "version": version,
        "version_method": version_method,
        "timestamp": datetime.now().isoformat(),
        "datasets": []
    }
    
    try:
        # Find all parquet files
        parquet_files = sorted(dataset_path.glob("*.parquet"))
        
        for file_path in parquet_files:
            file_size = get_file_size(str(file_path))
            checksum = calculate_checksum(str(file_path))
            
            metadata["datasets"].append({
                "filename": file_path.name,
                "path": str(file_path),
                "size_bytes": file_size,
                "size_mb": round(file_size / (1024 * 1024), 2),
                "checksum_sha256": checksum,
                "modified_time": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
            })
            
            logger.info(f"Metadata for {file_path.name}: {file_size} bytes, checksum={checksum[:16]}...")
        
        return {"status": "success", "metadata": metadata}
    
    except Exception as e:
        logger.error(f"Error creating version metadata: {e}")
        return {"status": "error", "message": str(e)}


def validate_dataset_integrity(
    dataset_dir: str,
    metadata: Dict[str, Any]
) -> Dict[str, Any]:
    """Validate dataset integrity against metadata."""
    logger.info("Validating dataset integrity")
    
    dataset_path = Path(dataset_dir)
    validation_results = {
        "valid_files": [],
        "invalid_files": [],
        "missing_files": [],
        "all_valid": True
    }
    
    try:
        for dataset_info in metadata.get("datasets", []):
            filename = dataset_info["filename"]
            file_path = dataset_path / filename
            expected_checksum = dataset_info["checksum_sha256"]
            
            if not file_path.exists():
                logger.warning(f"File not found: {filename}")
                validation_results["missing_files"].append(filename)
                validation_results["all_valid"] = False
                continue
            
            # Calculate actual checksum
            actual_checksum = calculate_checksum(str(file_path))
            
            if actual_checksum == expected_checksum:
                logger.info(f"Checksum valid for {filename}")
                validation_results["valid_files"].append(filename)
            else:
                logger.error(f"Checksum mismatch for {filename}")
                logger.error(f"  Expected: {expected_checksum}")
                logger.error(f"  Actual: {actual_checksum}")
                validation_results["invalid_files"].append({
                    "filename": filename,
                    "expected_checksum": expected_checksum,
                    "actual_checksum": actual_checksum
                })
                validation_results["all_valid"] = False
        
        return {"status": "success", "validation": validation_results}
    
    except Exception as e:
        logger.error(f"Error validating dataset integrity: {e}")
        return {"status": "error", "message": str(e)}


def main(
    dataset_dir: str,
    version_method: str = "dvc",
    version_tag: str = "v1.0.0",
    output_metadata: str = None
) -> Dict[str, Any]:
    """
    Main execution function.
    
    Args:
        dataset_dir: Directory containing datasets to version
        version_method: Versioning method (dvc or git-lfs)
        version_tag: Version tag (e.g., v1.0.0)
        output_metadata: Path to save metadata
        
    Returns:
        Result dictionary with versioning results
    """
    try:
        logger.info("[PROTOCOL 11 | DATASET VERSIONING START]")
        
        dataset_path = Path(dataset_dir)
        if not dataset_path.exists():
            raise ValueError(f"Dataset directory not found: {dataset_dir}")
        
        results = {
            "status": "success",
            "version_tag": version_tag,
            "version_method": version_method,
            "steps": {}
        }
        
        # Initialize version control
        if version_method.lower() == "dvc":
            logger.info("Using DVC for dataset versioning")
            init_result = init_dvc(str(dataset_path))
            results["steps"]["init"] = init_result
            
            if init_result["status"] != "error":
                add_result = add_datasets_to_dvc(str(dataset_path), version_tag)
                results["steps"]["add"] = add_result
        
        elif version_method.lower() == "git-lfs":
            logger.info("Using Git LFS for dataset versioning")
            init_result = init_git_lfs(str(dataset_path))
            results["steps"]["init"] = init_result
            
            if init_result["status"] != "error":
                add_result = add_datasets_to_git_lfs(str(dataset_path), version_tag)
                results["steps"]["add"] = add_result
        
        else:
            raise ValueError(f"Unknown version method: {version_method}")
        
        # Create version metadata
        metadata_result = create_version_metadata(str(dataset_path), version_tag, version_method)
        results["steps"]["metadata"] = metadata_result
        
        if metadata_result["status"] == "success":
            metadata = metadata_result["metadata"]
            
            # Validate integrity
            validation_result = validate_dataset_integrity(str(dataset_path), metadata)
            results["steps"]["validation"] = validation_result
            
            # Save metadata if output path provided
            if output_metadata:
                output_path = Path(output_metadata)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'w') as f:
                    json.dump(metadata, f, indent=2)
                logger.info(f"Metadata saved to {output_metadata}")
                results["metadata_file"] = output_metadata
            
            results["metadata"] = metadata
        
        logger.info("[PROTOCOL 11 | DATASET VERSIONING COMPLETE]")
        
        return results
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Version datasets using DVC or Git LFS")
    parser.add_argument("--dataset-dir", required=True, help="Directory containing datasets")
    parser.add_argument("--version-method", choices=["dvc", "git-lfs"], default="dvc", help="Versioning method")
    parser.add_argument("--version-tag", default="v1.0.0", help="Version tag")
    parser.add_argument("--output-metadata", help="Path to save metadata")
    
    args = parser.parse_args()
    
    result = main(
        dataset_dir=args.dataset_dir,
        version_method=args.version_method,
        version_tag=args.version_tag,
        output_metadata=args.output_metadata
    )
    
    exit(0 if result["status"] == "success" else 1)
