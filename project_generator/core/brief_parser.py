"""
Brief parser that extracts a ScaffoldSpec from a brief.md file.

Heuristics:
- Prefer YAML frontmatter keys: name, industry, project_type, frontend, backend, database, auth, deploy, compliance, features
- Fallback to body keyword extraction with simple regexes and known vocab
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Dict, Any


FRONTENDS = {"nextjs", "nuxt", "angular", "expo", "none"}
BACKENDS = {"fastapi", "django", "nestjs", "go", "none"}
DATABASES = {"postgres", "mongodb", "firebase", "none"}
AUTHS = {"auth0", "firebase", "cognito", "custom", "none"}
DEPLOYS = {"aws", "azure", "gcp", "vercel", "self-hosted"}
INDUSTRIES = {"healthcare", "finance", "ecommerce", "saas", "enterprise"}
PROJECT_TYPES = {"web", "mobile", "api", "fullstack", "microservices"}


@dataclass
class ScaffoldSpec:
    name: str
    industry: str
    project_type: str
    frontend: str = "none"
    backend: str = "none"
    database: str = "none"
    auth: str = "none"
    deploy: str = "aws"
    compliance: List[str] = field(default_factory=list)
    features: List[str] = field(default_factory=list)
    separate_repos: bool = True


class BriefParser:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def parse(self) -> ScaffoldSpec:
        content = self.path.read_text(encoding="utf-8")
        norm_body = self._normalize_text(content)
        meta = self._parse_frontmatter(content)
        body = self._strip_frontmatter(content)
        norm = self._normalize_text(body)

        # Required fields: name, industry, project_type
        name = (meta.get("name") or self._guess_name(body) or self._guess_name_from_title(body) or "my-app").strip()
        industry = (meta.get("industry") or self._guess_industry(norm) or "saas").strip().lower()
        project_type = (meta.get("project_type") or meta.get("project-type") or self._guess_project_type(norm) or "fullstack").strip().lower()

        frontend = (meta.get("frontend") or self._guess_frontend(norm) or ("nextjs" if project_type != "api" else "none")).strip().lower()
        backend = (meta.get("backend") or self._guess_backend(norm) or ("fastapi" if project_type != "web" else "none")).strip().lower()
        database = (meta.get("database") or self._guess_database(norm) or ("postgres" if backend != "none" else "none")).strip().lower()
        auth = (meta.get("auth") or self._guess_auth(norm, industry, project_type, frontend) or "auth0").strip().lower()
        deploy = (meta.get("deploy") or self._guess_deploy(norm) or "aws").strip().lower()

        compliance_val = meta.get("compliance") or self._guess_compliance(norm) or []
        if isinstance(compliance_val, str):
            compliance = [c.strip().lower() for c in compliance_val.split(',') if c.strip()]
        else:
            compliance = [str(c).strip().lower() for c in compliance_val]

        features_val = meta.get("features") or self._guess_features(body) or []
        if isinstance(features_val, str):
            features = [f.strip() for f in features_val.split(',') if f.strip()]
        else:
            features = [str(f).strip() for f in features_val]

        # Clamp to vocab where applicable
        industry = industry if industry in INDUSTRIES else "healthcare"
        project_type = project_type if project_type in PROJECT_TYPES else "fullstack"
        frontend = frontend if frontend in FRONTENDS else ("nextjs" if project_type != "api" else "none")
        backend = backend if backend in BACKENDS else ("fastapi" if project_type != "web" else "none")
        database = database if database in DATABASES else ("postgres" if backend != "none" else "none")
        auth = auth if auth in AUTHS else "auth0"
        deploy = deploy if deploy in DEPLOYS else "aws"

        return ScaffoldSpec(
            name=name,
            industry=industry,
            project_type=project_type,
            frontend=frontend,
            backend=backend,
            database=database,
            auth=auth,
            deploy=deploy,
            compliance=compliance,
            features=features,
            separate_repos=True,
        )

    # ---- helpers ----
    def _parse_frontmatter(self, content: str) -> Dict[str, Any]:
        if not content.startswith("---\n"):
            return {}
        end = content.find("\n---\n", 4)
        if end == -1:
            return {}
        fm = content[4:end]
        meta: Dict[str, Any] = {}
        for line in fm.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip().lower()] = v.strip().strip('"\'')
        return meta

    def _strip_frontmatter(self, content: str) -> str:
        if not content.startswith("---\n"):
            return content
        end = content.find("\n---\n", 4)
        if end == -1:
            return content
        return content[end + len("\n---\n"):]

    def _normalize_text(self, s: str) -> str:
        # Lowercase and normalize various hyphen characters to '-'
        if not s:
            return ""
        s2 = s.lower()
        # Normalize unicode hyphens/dashes
        for ch in ["\u2010", "\u2011", "\u2012", "\u2013", "\u2014", "\u2212"]:
            s2 = s2.replace(ch, "-")
        return s2

    def _guess_name_from_title(self, text: str) -> Optional[str]:
        # Use first non-empty line as title → slugify to 2 tokens
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            # Keep letters/numbers and replace spaces with '-'
            words = re.findall(r"[a-zA-Z0-9]+", line)
            if not words:
                continue
            slug = "-".join(words[:3]).lower()
            return slug
        return None

    def _guess_name(self, text: str) -> Optional[str]:
        m = re.search(r"project\s+name[:\-]\s*([A-Za-z0-9\-\_]+)", text, re.IGNORECASE)
        return m.group(1) if m else None

    def _guess_industry(self, text: str) -> Optional[str]:
        buckets = {
            "ecommerce": [
                "ecommerce", "e-commerce", "e -commerce", "marketplace", "marketplaces",
                "cart", "checkout", "sku", "order", "re-order", "reorder", "merchandiser",
                "category", "lazada", "shopee", "tokopedia", "amazon"
            ],
            "healthcare": ["hipaa", "patient", "ehr", "phi", "clinic", "hospital", "telehealth", "medical"],
            "finance": ["sox", "pci", "fintech", "bank", "trading", "ledger", "loan", "cardholder"],
            "enterprise": ["sso", "rbac", "okta", "azure ad", "saml", "enterprise"],
            "saas": ["subscription", "billing", "multi-tenant", "tenant", "b2b", "saas"],
        }
        best = None
        best_score = 0
        for ind, kws in buckets.items():
            score = sum(1 for kw in kws if kw in text)
            if score > best_score:
                best_score = score
                best = ind
        return best

    def _guess_project_type(self, text: str) -> Optional[str]:
        # Signals
        ui_signals = ["dashboard", "frontend", "next.js", "nextjs", "react", "angular", "nuxt", "vue", "ui", "chart", "visual"]
        api_signals = ["api-only", "api only", "api service", "backend-only", "rest api", "http api", "graphql api"]
        mobile_signals = ["mobile app", "ios", "android", "react native", "expo"]
        micro_signals = ["microservices", "micro-service"]

        if any(s in text for s in mobile_signals):
            return "mobile"
        if any(s in text for s in micro_signals):
            return "microservices"
        # If API signals present and few/no UI signals → api
        if any(s in text for s in api_signals) and not any(s in text for s in ui_signals):
            return "api"
        # If UI signals present and also backend keywords → fullstack, else web
        be_kws = ["fastapi", "django", "nestjs", "go backend", "backend", "api"]
        has_ui = any(s in text for s in ui_signals)
        has_be = any(s in text for s in be_kws)
        if has_ui and has_be:
            return "fullstack"
        if has_ui:
            return "web"
        # Fallback: fullstack (safer default)
        return "fullstack"

    def _guess_frontend(self, text: str) -> Optional[str]:
        mapping = {
            "nextjs": ["next.js", "nextjs"],
            "nuxt": ["nuxt", "nuxt.js"],
            "angular": ["angular"],
            "expo": ["expo", "react native"],
        }
        for fe, kws in mapping.items():
            if any(kw in text for kw in kws):
                return fe
        # If mentions dashboard/visualization and no FE specified → default nextjs
        if "dashboard" in text or "chart" in text or "visual" in text:
            return "nextjs"
        return None

    def _guess_backend(self, text: str) -> Optional[str]:
        mapping = {
            "fastapi": ["fastapi"],
            "django": ["django"],
            "nestjs": ["nestjs", "nest.js"],
            "go": [" go ", "golang", "go backend"],
        }
        for be, kws in mapping.items():
            if any(kw in text for kw in kws):
                return be
        # If API is mentioned but no backend specified → default fastapi
        if "api" in text:
            return "fastapi"
        return None

    def _guess_database(self, text: str) -> Optional[str]:
        mapping = {
            "postgres": ["postgres", "postgre", "postgre sql", "postgre-sql"],
            "mongodb": ["mongodb", "mongo"],
            "firebase": ["firebase"],
        }
        for db, kws in mapping.items():
            if any(kw in text for kw in kws):
                return db
        return None

    def _guess_auth(self, text: str, industry: str, project_type: str, frontend: str) -> Optional[str]:
        # Prefer explicit providers
        if "auth0" in text:
            return "auth0"
        if "cognito" in text:
            return "cognito"
        if "firebase auth" in text:
            return "firebase"
        # Signals: SSO / RBAC → prefer Auth0 (enterprise: Cognito acceptable)
        if "sso" in text or "single sign-on" in text or "rbac" in text:
            return "cognito" if industry == "enterprise" else "auth0"
        # Okta/Azure AD/Keycloak hints → map to closest available
        if "okta" in text or "azure ad" in text or "saml" in text or "keycloak" in text:
            return "auth0"
        return None

    def _guess_deploy(self, text: str) -> Optional[str]:
        for d in DEPLOYS:
            if re.search(rf"\b{re.escape(d)}\b", text, re.IGNORECASE):
                return d
        return None

    def _guess_compliance(self, text: str) -> List[str]:
        hits: List[str] = []
        for c in ["hipaa", "gdpr", "sox", "pci", "soc2"]:
            if re.search(rf"\b{c}\b", text, re.IGNORECASE):
                hits.append(c)
        return hits

    def _guess_features(self, text: str) -> List[str]:
        # Capture comma-separated list after keywords like features:, capabilities:, include:
        m = re.search(r"\b(features|capabilities|include)[:\-]\s*([^\n]+)", text, re.IGNORECASE)
        if not m:
            return []
        return [f.strip() for f in m.group(2).split(',') if f.strip()]

