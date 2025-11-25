#!/usr/bin/env python3
"""
Evidence Integrity Module
Provides checksums, signing, and verification for evidence artifacts.
"""
import argparse
import json
import sys
import hashlib
import hmac
import os
from pathlib import Path
from datetime import datetime

class EvidenceIntegrity:
    """Evidence integrity management."""
    
    def __init__(self, workspace: Path, secret_key: str = None):
        self.workspace = workspace
        self.secret_key = secret_key or os.environ.get('EVIDENCE_SECRET_KEY', 'default-key-change-in-production')
    
    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of a file."""
        sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            return f"error:{str(e)}"
    
    def generate_checksums(self, directory: Path) -> dict:
        """Generate checksums for all files in a directory."""
        checksums = {}
        
        if not directory.exists():
            return checksums
        
        for file_path in directory.rglob('*'):
            if file_path.is_file() and file_path.name != 'checksums.sha256':
                rel_path = str(file_path.relative_to(directory))
                checksums[rel_path] = self.calculate_file_hash(file_path)
        
        return checksums
    
    def write_checksums_file(self, directory: Path, checksums: dict) -> Path:
        """Write checksums to a checksums.sha256 file."""
        checksums_path = directory / 'checksums.sha256'
        
        lines = []
        for path, hash_value in sorted(checksums.items()):
            lines.append(f"{hash_value}  {path}")
        
        with open(checksums_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        return checksums_path
    
    def verify_checksums(self, directory: Path) -> dict:
        """Verify checksums against checksums.sha256 file."""
        checksums_path = directory / 'checksums.sha256'
        
        if not checksums_path.exists():
            return {
                "verified": False,
                "error": "checksums.sha256 not found",
                "files_checked": 0,
                "files_passed": 0,
                "files_failed": 0
            }
        
        # Load expected checksums
        expected = {}
        with open(checksums_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and '  ' in line:
                    hash_value, path = line.split('  ', 1)
                    expected[path] = hash_value
        
        # Verify each file
        results = {
            "verified": True,
            "files_checked": 0,
            "files_passed": 0,
            "files_failed": 0,
            "failures": []
        }
        
        for path, expected_hash in expected.items():
            file_path = directory / path
            results["files_checked"] += 1
            
            if not file_path.exists():
                results["verified"] = False
                results["files_failed"] += 1
                results["failures"].append({
                    "file": path,
                    "error": "File not found"
                })
                continue
            
            actual_hash = self.calculate_file_hash(file_path)
            if actual_hash == expected_hash:
                results["files_passed"] += 1
            else:
                results["verified"] = False
                results["files_failed"] += 1
                results["failures"].append({
                    "file": path,
                    "expected": expected_hash,
                    "actual": actual_hash
                })
        
        return results
    
    def sign_manifest(self, manifest: dict) -> str:
        """Generate HMAC signature for manifest."""
        manifest_str = json.dumps(manifest, sort_keys=True)
        signature = hmac.new(
            self.secret_key.encode(),
            manifest_str.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature
    
    def verify_signature(self, manifest: dict, signature: str) -> bool:
        """Verify HMAC signature of manifest."""
        expected_signature = self.sign_manifest(manifest)
        return hmac.compare_digest(signature, expected_signature)
    
    def create_signed_manifest(self, directory: Path, metadata: dict = None) -> dict:
        """Create a signed evidence manifest."""
        checksums = self.generate_checksums(directory)
        
        manifest = {
            "version": "1.0.0",
            "created_at": datetime.now().isoformat(),
            "directory": str(directory),
            "files": checksums,
            "file_count": len(checksums),
            "metadata": metadata or {}
        }
        
        # Sign the manifest
        signature = self.sign_manifest(manifest)
        manifest["signature"] = signature
        
        return manifest
    
    def verify_manifest(self, manifest: dict) -> dict:
        """Verify a signed manifest."""
        if "signature" not in manifest:
            return {
                "verified": False,
                "error": "No signature in manifest"
            }
        
        # Extract signature and verify
        signature = manifest.pop("signature")
        is_valid = self.verify_signature(manifest, signature)
        manifest["signature"] = signature  # Restore
        
        return {
            "verified": is_valid,
            "signature_valid": is_valid,
            "manifest_version": manifest.get("version"),
            "file_count": manifest.get("file_count", 0)
        }


def main():
    parser = argparse.ArgumentParser(description='Evidence integrity utility')
    parser.add_argument('action', choices=['checksum', 'verify', 'sign', 'verify-manifest'],
                       help='Action to perform')
    parser.add_argument('--directory', help='Directory to process')
    parser.add_argument('--manifest', help='Manifest file path')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--secret-key', help='Secret key for signing')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    integrity = EvidenceIntegrity(workspace, args.secret_key)
    
    if args.action == 'checksum':
        if not args.directory:
            print("[ERROR] --directory required for checksum action")
            return 1
        
        directory = Path(args.directory)
        if not directory.is_absolute():
            directory = workspace / directory
        
        checksums = integrity.generate_checksums(directory)
        checksums_path = integrity.write_checksums_file(directory, checksums)
        
        print(f"[INTEGRITY] Generated checksums for {len(checksums)} files")
        print(f"  - Output: {checksums_path}")
        return 0
    
    elif args.action == 'verify':
        if not args.directory:
            print("[ERROR] --directory required for verify action")
            return 1
        
        directory = Path(args.directory)
        if not directory.is_absolute():
            directory = workspace / directory
        
        result = integrity.verify_checksums(directory)
        print(json.dumps(result, indent=2))
        
        return 0 if result["verified"] else 1
    
    elif args.action == 'sign':
        if not args.directory:
            print("[ERROR] --directory required for sign action")
            return 1
        
        directory = Path(args.directory)
        if not directory.is_absolute():
            directory = workspace / directory
        
        manifest = integrity.create_signed_manifest(directory)
        
        if args.output:
            output_path = Path(args.output)
        else:
            output_path = directory / 'evidence-manifest-signed.json'
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"[INTEGRITY] Created signed manifest")
        print(f"  - Files: {manifest['file_count']}")
        print(f"  - Output: {output_path}")
        return 0
    
    elif args.action == 'verify-manifest':
        if not args.manifest:
            print("[ERROR] --manifest required for verify-manifest action")
            return 1
        
        manifest_path = Path(args.manifest)
        if not manifest_path.is_absolute():
            manifest_path = workspace / manifest_path
        
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        
        result = integrity.verify_manifest(manifest)
        print(json.dumps(result, indent=2))
        
        return 0 if result["verified"] else 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

