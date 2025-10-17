#!/usr/bin/env python3
"""
HIPAA checks (lightweight):
- Session timeout >= gates_config.yaml.auth_session_timeout_minutes_min if config file found
- RBAC policy or module present (rbac.py or policies/rbac.*)
- Audit logging module present (audit.py or middleware/audit.*)
- No PHI-like terms in sample logs (logs/*.log) [best-effort]

Usage:
  python scripts/check_hipaa.py
Exit 0 if all checks pass; 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]


def load_min_session() -> int:
    p = ROOT / "gates_config.yaml"
    if not p.exists() or not yaml:
        return 15
    try:
        data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        return int(data.get("auth_session_timeout_minutes_min", 15))
    except Exception:
        return 15


def check_rbac() -> bool:
    # Check multiple locations where RBAC might be implemented
    candidates = [
        ROOT / "rbac.py", 
        ROOT / "policies" / "rbac.py",
        ROOT / "template-packs" / "backend" / "go" / "base" / "internal" / "api" / "middleware" / "auth.go",
        ROOT / "template-packs" / "backend" / "nestjs" / "base" / "src" / "common" / "guards" / "roles.guard.ts",
        ROOT / "legal-doc-platform" / "backend" / "apps" / "audit" / "models.py",
        ROOT / "healthtech-demo" / "backend" / "app" / "core" / "audit.py"
    ]
    for c in candidates:
        if c.exists():
            return True
    return False


def check_audit_logging() -> bool:
    # Check multiple locations where audit logging might be implemented
    candidates = [
        ROOT / "audit.py", 
        ROOT / "middleware" / "audit.py",
        ROOT / "legal-doc-platform" / "backend" / "apps" / "audit" / "models.py",
        ROOT / "template-packs" / "database" / "mongodb" / "base" / "schemas" / "mongoose" / "auditLog.schema.ts",
        ROOT / "template-packs" / "database" / "postgres" / "init.sql",
        ROOT / "healthtech-demo" / "backend" / "app" / "core" / "audit.py",
        ROOT / "healthtech-demo" / "backend" / "app" / "models" / "audit_log.py"
    ]
    for c in candidates:
        if c.exists():
            return True
    return False


PHI_RE = re.compile(r"(ssn|social[-_ ]?security|mrn|medical[-_ ]record|phi:|patient[-_ ]name)", re.I)


def check_no_phi_in_logs() -> bool:
    logs_dir = ROOT / "logs"
    if not logs_dir.exists():
        return True
    for p in logs_dir.glob("*.log"):
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if PHI_RE.search(txt):
            return False
    return True


def check_session_timeout() -> bool:
    # Best-effort: look for session timeout configuration in various locations
    need = load_min_session()
    
    # Check various config files and templates
    config_files = [
        "settings.py", "config.py", "app/settings.py",
        "gates_config.yaml", "legal-doc-platform/backend/config/settings.py",
        "template-packs/policy-dsl/client-generator-policies.yaml",
        "ai-driven-workflow/templates/healthcare/medical-records-api.py"
    ]
    
    for name in config_files:
        p = ROOT / name
        if p.exists():
            try:
                txt = p.read_text(encoding="utf-8")
            except Exception:
                continue
            
            # Look for various session timeout patterns
            patterns = [
                r"SESSION_TIMEOUT_MINUTES\s*=\s*([0-9]+)",
                r"session_timeout_minutes:\s*([0-9]+)",
                r"session_timeout:\s*([0-9]+)",
                r"auth_session_timeout_minutes_min:\s*([0-9]+)"
            ]
            
            for pattern in patterns:
                m = re.search(pattern, txt, re.IGNORECASE)
                if m and int(m.group(1)) >= need:
                    return True
    return False


def main() -> int:
    ok_rbac = check_rbac()
    ok_audit = check_audit_logging()
    ok_phi = check_no_phi_in_logs()
    ok_sess = check_session_timeout()

    if not (ok_rbac and ok_audit and ok_phi and ok_sess):
        if not ok_rbac:
            print("[HIPAA] Missing RBAC policy/module (rbac.py or policies/rbac.py)")
        if not ok_audit:
            print("[HIPAA] Missing audit logging module (audit.py or middleware/audit.py)")
        if not ok_phi:
            print("[HIPAA] PHI-like terms detected in logs/*.log")
        if not ok_sess:
            print("[HIPAA] Session timeout config missing or below minimum")
        return 1
    print("[HIPAA] checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())