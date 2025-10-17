#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WF_DIR = ROOT / "docs" / "workflows"
REPORT = ROOT / "validation" / "compliance_report.json"

# Controls to verify in docs (case-insensitive substring checks)
CONTROLS = {
    "encryption_at_rest": [r"encryption at rest", r"encrypted at rest", r"aes-256"],
    "encryption_in_transit": [r"encryption in transit", r"tls", r"https"],
    "rbac": [r"rbac", r"role[- ]based access"],
    "audit_logging": [r"audit logging", r"audit log"],
    "session_timeout": [r"session timeout", r"15 ?min"],
    "no_phi_in_logs": [r"no phi in logs", r"no phi/pii", r"phi leakage", r"pii leakage"],
}

# Minimum mapping of which files should include which controls
EXPECTED_FILES = {
    # 02: planning mentions the plan; optional but nice to have
    "02_TECHNICAL_PLANNING.md": ["encryption_at_rest", "encryption_in_transit", "rbac", "audit_logging", "session_timeout"],
    # 08: security & compliance - must include all core controls
    "08_SECURITY_COMPLIANCE.md": ["encryption_at_rest", "encryption_in_transit", "rbac", "audit_logging", "session_timeout"],
    # 10: monitoring/logs - must include no PHI in logs
    "10_MONITORING_OBSERVABILITY.md": ["no_phi_in_logs"],
}


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def find_mentions(text: str, patterns: list[str]) -> bool:
    t = text.lower()
    for pat in patterns:
        if re.search(pat, t):
            return True
    return False


def main() -> int:
    wf_files = {p.name: p for p in WF_DIR.glob("*.md")}
    results: dict[str, dict] = {}
    missing_any = False

    for filename, controls in EXPECTED_FILES.items():
        p = wf_files.get(filename)
        status = {c: False for c in controls}
        if p and p.exists():
            txt = read_text(p)
            for control in controls:
                status[control] = find_mentions(txt, CONTROLS[control])
        else:
            # If file missing, mark all as False
            missing_any = True
        if not all(status.values()):
            missing_any = True
        results[filename] = status

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(results, indent=2))

    if missing_any:
        print("[COMPLIANCE] Missing required control mentions in docs. See:", REPORT)
        for fn, st in results.items():
            missing = [k for k, v in st.items() if not v]
            if missing:
                print(f"- {fn}: missing {missing}")
        return 2
    print("[COMPLIANCE] All required control mentions found in docs.")
    print("Report:", REPORT)
    return 0


if __name__ == "__main__":
    sys.exit(main())