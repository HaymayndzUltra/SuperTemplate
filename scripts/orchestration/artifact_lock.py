#!/usr/bin/env python3
"""
Artifact Lock Module
Provides file-level locking for safe parallel protocol execution.
"""
import argparse
import json
import sys
import os
import time
import fcntl
from pathlib import Path
from datetime import datetime
from contextlib import contextmanager

class ArtifactLock:
    """File-based locking for artifacts."""
    
    def __init__(self, workspace: Path):
        self.workspace = workspace
        self.locks_dir = workspace / '.artifacts' / 'locks'
        self.locks_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = self.locks_dir / 'lock-log.json'
        self._load_log()
    
    def _load_log(self):
        """Load lock log from disk."""
        if self.log_path.exists():
            with open(self.log_path, 'r', encoding='utf-8') as f:
                self.log = json.load(f)
        else:
            self.log = {"locks": [], "active": {}}
    
    def _save_log(self):
        """Save lock log to disk."""
        with open(self.log_path, 'w', encoding='utf-8') as f:
            json.dump(self.log, f, indent=2)
    
    def _get_lock_file(self, resource: str) -> Path:
        """Get lock file path for a resource."""
        # Sanitize resource name for filename
        safe_name = resource.replace('/', '_').replace('\\', '_')
        return self.locks_dir / f"{safe_name}.lock"
    
    def acquire(self, resource: str, timeout: float = 30.0, holder: str = None) -> bool:
        """
        Acquire lock on a resource.
        
        Args:
            resource: Resource path to lock
            timeout: Maximum time to wait for lock (seconds)
            holder: Identifier for lock holder
        
        Returns:
            True if lock acquired, False if timeout
        """
        lock_file = self._get_lock_file(resource)
        holder = holder or f"pid-{os.getpid()}"
        
        start_time = time.time()
        
        while True:
            try:
                # Create lock file if doesn't exist
                fd = os.open(str(lock_file), os.O_CREAT | os.O_RDWR)
                
                # Try to acquire exclusive lock
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                
                # Write lock info
                lock_info = {
                    "resource": resource,
                    "holder": holder,
                    "acquired_at": datetime.now().isoformat(),
                    "pid": os.getpid()
                }
                os.write(fd, json.dumps(lock_info).encode())
                
                # Log acquisition
                self.log["active"][resource] = lock_info
                self.log["locks"].append({
                    "action": "acquire",
                    "resource": resource,
                    "holder": holder,
                    "timestamp": datetime.now().isoformat()
                })
                self._save_log()
                
                return True
                
            except (IOError, OSError):
                # Lock held by another process
                if time.time() - start_time > timeout:
                    return False
                time.sleep(0.1)
    
    def release(self, resource: str) -> bool:
        """
        Release lock on a resource.
        
        Args:
            resource: Resource path to unlock
        
        Returns:
            True if released, False if not held
        """
        lock_file = self._get_lock_file(resource)
        
        if not lock_file.exists():
            return False
        
        try:
            fd = os.open(str(lock_file), os.O_RDWR)
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)
            
            # Clean up lock file
            lock_file.unlink(missing_ok=True)
            
            # Log release
            if resource in self.log["active"]:
                del self.log["active"][resource]
            self.log["locks"].append({
                "action": "release",
                "resource": resource,
                "timestamp": datetime.now().isoformat()
            })
            self._save_log()
            
            return True
            
        except (IOError, OSError):
            return False
    
    def is_locked(self, resource: str) -> bool:
        """Check if resource is locked."""
        lock_file = self._get_lock_file(resource)
        
        if not lock_file.exists():
            return False
        
        try:
            fd = os.open(str(lock_file), os.O_RDONLY)
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)
            return False
        except (IOError, OSError):
            return True
    
    def get_lock_info(self, resource: str) -> dict:
        """Get information about a lock."""
        lock_file = self._get_lock_file(resource)
        
        if not lock_file.exists():
            return {"locked": False}
        
        try:
            with open(lock_file, 'r') as f:
                info = json.load(f)
                info["locked"] = self.is_locked(resource)
                return info
        except (json.JSONDecodeError, IOError):
            return {"locked": self.is_locked(resource)}
    
    @contextmanager
    def lock(self, resource: str, timeout: float = 30.0, holder: str = None):
        """Context manager for acquiring and releasing locks."""
        if not self.acquire(resource, timeout, holder):
            raise TimeoutError(f"Could not acquire lock on {resource} within {timeout}s")
        try:
            yield
        finally:
            self.release(resource)


def main():
    parser = argparse.ArgumentParser(description='Artifact locking utility')
    parser.add_argument('action', choices=['acquire', 'release', 'status', 'list'],
                       help='Lock action to perform')
    parser.add_argument('--resource', help='Resource path to lock/unlock')
    parser.add_argument('--holder', help='Lock holder identifier')
    parser.add_argument('--timeout', type=float, default=30.0, help='Lock timeout in seconds')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    lock_manager = ArtifactLock(workspace)
    
    if args.action == 'acquire':
        if not args.resource:
            print("[ERROR] --resource required for acquire action")
            return 1
        
        if lock_manager.acquire(args.resource, args.timeout, args.holder):
            print(f"[LOCK] Acquired lock on: {args.resource}")
            return 0
        else:
            print(f"[ERROR] Failed to acquire lock on: {args.resource}")
            return 1
    
    elif args.action == 'release':
        if not args.resource:
            print("[ERROR] --resource required for release action")
            return 1
        
        if lock_manager.release(args.resource):
            print(f"[LOCK] Released lock on: {args.resource}")
            return 0
        else:
            print(f"[ERROR] Failed to release lock on: {args.resource}")
            return 1
    
    elif args.action == 'status':
        if not args.resource:
            print("[ERROR] --resource required for status action")
            return 1
        
        info = lock_manager.get_lock_info(args.resource)
        print(json.dumps(info, indent=2))
        return 0
    
    elif args.action == 'list':
        print(json.dumps(lock_manager.log, indent=2))
        return 0
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

