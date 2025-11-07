#!/usr/bin/env python3
"""Protocol 18: AI Model Packaging - Model serialization with multiple formats."""

import json
import sys
from pathlib import Path
from typing import Dict, Any
import joblib
import pickle
import hashlib
from datetime import datetime
import pandas as pd
import numpy as np

# Optional formats
try:
    import onnx
    import skl2onnx
    from skl2onnx import convert_sklearn
    from skl2onnx.common.data_types import FloatTensorType
    ONNX_AVAILABLE = True
except ImportError:
    ONNX_AVAILABLE = False

try:
    import tensorflow as tf
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False


def calculate_checksum(file_path: Path) -> str:
    """Calculate MD5 checksum of file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def serialize_sklearn_model(model, output_dir: Path, model_name: str) -> Dict[str, Any]:
    """Serialize scikit-learn model in multiple formats."""
    results = {}
    
    # Joblib format (recommended for sklearn)
    joblib_path = output_dir / f"{model_name}.joblib"
    joblib.dump(model, joblib_path)
    results["joblib"] = {
        "path": str(joblib_path),
        "size_mb": joblib_path.stat().st_size / (1024 * 1024),
        "checksum": calculate_checksum(joblib_path)
    }
    
    # Pickle format (compatibility)
    pickle_path = output_dir / f"{model_name}.pkl"
    with open(pickle_path, 'wb') as f:
        pickle.dump(model, f)
    results["pickle"] = {
        "path": str(pickle_path),
        "size_mb": pickle_path.stat().st_size / (1024 * 1024),
        "checksum": calculate_checksum(pickle_path)
    }
    
    # ONNX format (cross-platform)
    if ONNX_AVAILABLE:
        try:
            # Determine input type
            if hasattr(model, 'n_features_in_'):
                n_features = model.n_features_in_
            else:
                n_features = 10  # Default
            
            initial_type = [('float_input', FloatTensorType([None, n_features]))]
            onnx_model = convert_sklearn(model, initial_types=initial_type)
            
            onnx_path = output_dir / f"{model_name}.onnx"
            with open(onnx_path, "wb") as f:
                f.write(onnx_model.SerializeToString())
            
            results["onnx"] = {
                "path": str(onnx_path),
                "size_mb": onnx_path.stat().st_size / (1024 * 1024),
                "checksum": calculate_checksum(onnx_path)
            }
        except Exception as e:
            results["onnx"] = {"error": str(e)}
    
    return results


def create_model_metadata(model, model_name: str, serialization_results: Dict) -> Dict[str, Any]:
    """Create comprehensive model metadata."""
    metadata = {
        "model_name": model_name,
        "timestamp": datetime.now().isoformat(),
        "model_type": type(model).__name__,
        "serialization_formats": list(serialization_results.keys()),
        "model_info": {}
    }
    
    # Extract model-specific info
    if hasattr(model, 'get_params'):
        metadata["model_info"]["parameters"] = model.get_params()
    
    if hasattr(model, 'n_features_in_'):
        metadata["model_info"]["n_features"] = int(model.n_features_in_)
    
    if hasattr(model, 'feature_importances_'):
        metadata["model_info"]["has_feature_importance"] = True
    
    if hasattr(model, 'classes_'):
        metadata["model_info"]["n_classes"] = len(model.classes_)
        metadata["model_info"]["classes"] = model.classes_.tolist()
    
    # Add serialization info
    metadata["serialization"] = serialization_results
    
    return metadata


def package_model(
    model_path: Path,
    output_dir: Path,
    model_name: str,
    include_metadata: bool = True
) -> Dict[str, Any]:
    """Package model with all necessary files."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load model
    model = joblib.load(model_path)
    
    # Serialize in multiple formats
    serialization_results = serialize_sklearn_model(model, output_dir, model_name)
    
    # Create metadata
    if include_metadata:
        metadata = create_model_metadata(model, model_name, serialization_results)
        
        metadata_path = output_dir / f"{model_name}_metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2, default=str)
        
        serialization_results["metadata"] = {
            "path": str(metadata_path),
            "size_mb": metadata_path.stat().st_size / (1024 * 1024)
        }
    
    # Create requirements.txt
    requirements = [
        "scikit-learn>=1.0.0",
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "joblib>=1.0.0"
    ]
    
    if ONNX_AVAILABLE and "onnx" in serialization_results:
        requirements.extend(["onnx>=1.10.0", "skl2onnx>=1.10.0"])
    
    req_path = output_dir / "requirements.txt"
    with open(req_path, 'w') as f:
        f.write('\n'.join(requirements))
    
    serialization_results["requirements"] = str(req_path)
    
    return serialization_results


def main():
    if len(sys.argv) < 4:
        print("Usage: python serialize_model.py <model_file> <output_dir> <model_name>")
        sys.exit(1)
    
    model_path = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    model_name = sys.argv[3]
    
    if not model_path.exists():
        print(f"Error: Model file {model_path} not found")
        sys.exit(1)
    
    print(f"Packaging model: {model_name}")
    results = package_model(model_path, output_dir, model_name)
    
    print(f"\nSerialization Summary:")
    for format_name, info in results.items():
        if isinstance(info, dict) and "path" in info:
            print(f"  {format_name}: {info['path']} ({info['size_mb']:.2f} MB)")
        elif isinstance(info, dict) and "error" in info:
            print(f"  {format_name}: Failed - {info['error']}")
    
    print(f"\nModel package saved to: {output_dir}")
    sys.exit(0)


if __name__ == "__main__":
    main()
