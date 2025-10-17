"""Utility helpers for lifecycle planning tasks.

The previous implementation inside ``plan_from_brief`` and
``pre_lifecycle_plan`` duplicated a static set of backend and frontend
tasks.  This module centralises the logic and makes it data-driven so
lane contents can adapt to the parsed brief and workflow configuration.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence

from project_generator.core.brief_parser import ScaffoldSpec


@dataclass
class Task:
    """Serializable structure describing a work item in the plan."""

    id: str
    title: str
    area: str
    blocked_by: Sequence[str] = ()
    labels: Sequence[str] = ()
    estimate: str = "1d"
    acceptance: Sequence[str] = ()
    dod: Sequence[str] = ()

    def as_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "area": self.area,
            "estimate": self.estimate,
            "blocked_by": list(self.blocked_by),
            "labels": list(self.labels),
            "acceptance": list(self.acceptance),
            "dod": list(self.dod),
            "state": "pending",
        }


def _requires_backend(spec: ScaffoldSpec) -> bool:
    return spec.backend != "none"


def _requires_frontend(spec: ScaffoldSpec) -> bool:
    return spec.frontend != "none"


def _requires_database(spec: ScaffoldSpec, cfg: Dict) -> bool:
    db = cfg.get("database", spec.database)
    return db not in {"", "none", None}


def _requires_auth(spec: ScaffoldSpec, cfg: Dict) -> bool:
    auth = cfg.get("auth", spec.auth)
    return auth not in {"", "none", None}


def _requires_compliance(spec: ScaffoldSpec, cfg: Dict) -> bool:
    compliance = cfg.get("compliance", spec.compliance)
    if isinstance(compliance, str):
        compliance = [c.strip().lower() for c in compliance.split(",") if c.strip()]
    return bool(compliance)


def _features(spec: ScaffoldSpec, cfg: Dict) -> Iterable[str]:
    raw = cfg.get("features") or spec.features
    if isinstance(raw, str):
        return [p.strip().lower() for p in raw.split(",") if p.strip()]
    return [str(p).strip().lower() for p in raw]


def _project_type(spec: ScaffoldSpec, cfg: Dict) -> str:
    return (cfg.get("project_type") or spec.project_type or "fullstack").lower()


def _normalise_capability(value) -> str:
    if isinstance(value, str):
        return value.lower()
    return str(value).lower()


def _task(*args, **kwargs) -> Task:
    return Task(*args, **kwargs)


def _backend_api_tasks(has_analytics: bool) -> List[Task]:
    api_tasks = [
        _task(
            "BE-API-KPI",
            "GET /api/v1/kpis",
            "backend",
            blocked_by=["BE-MDL"],
            acceptance=["returns totals/deltas", "OpenAPI updated"],
        ),
        _task(
            "BE-API-REV",
            "GET /api/v1/revenue",
            "backend",
            blocked_by=["BE-MDL"],
            acceptance=["time series ok", "OpenAPI updated"],
        ),
        _task("BE-API-CAT", "GET /api/v1/categories", "backend", blocked_by=["BE-MDL"]),
        _task("BE-API-PLT", "GET /api/v1/platforms", "backend", blocked_by=["BE-MDL"]),
        _task("BE-API-CUS", "GET /api/v1/customers/insights", "backend", blocked_by=["BE-MDL"]),
        _task("BE-API-FDB", "GET /api/v1/feedback", "backend", blocked_by=["BE-MDL"]),
        _task(
            "BE-EXP",
            "GET /api/v1/export/csv",
            "backend",
            blocked_by=[
                "BE-API-KPI",
                "BE-API-REV",
                "BE-API-CAT",
                "BE-API-PLT",
                "BE-API-CUS",
                "BE-API-FDB",
            ],
        ),
    ]
    if has_analytics:
        api_tasks.insert(
            0,
            _task(
                "BE-ANALYTICS",
                "Aggregate analytics pipelines",
                "backend",
                blocked_by=["BE-MDL"],
                labels=["analytics"],
                acceptance=["aggregations exposed", "metrics documented"],
            ),
        )
    return api_tasks


def _frontend_feature_tasks(features: Iterable[str]) -> List[Task]:
    features = list(dict.fromkeys(features))  # stable unique order
    tasks: List[Task] = []
    feature_map = {
        "realtime": _task(
            "FE-REALTIME",
            "Real-time data channel",
            "frontend",
            blocked_by=["FE-DSN"],
            labels=["realtime"],
            acceptance=["live updates", "fallback poll implemented"],
        ),
        "collaboration": _task(
            "FE-COLLAB",
            "Collaboration widgets",
            "frontend",
            blocked_by=["FE-DSN", "FE-MOCKS"],
            acceptance=["status badges rendered", "activity feed updates"],
        ),
        "analytics": _task(
            "FE-ANALYTICS",
            "Analytics visualisations",
            "frontend",
            blocked_by=["FE-DSN", "FE-TYPES"],
            acceptance=["charts responsive", "tooltips accessible"],
        ),
        "offline": _task(
            "FE-OFFLINE",
            "Offline caching strategy",
            "frontend",
            blocked_by=["FE-DSN"],
            labels=["pwa"],
            acceptance=["core routes cached", "sync strategy documented"],
        ),
    }
    for feature in features:
        if feature in feature_map:
            tasks.append(feature_map[feature])
    return tasks


def build_plan(spec: ScaffoldSpec, workflow_config: Dict | None = None) -> Dict[str, List[Dict]]:
    """Create backend/frontend lanes derived from the brief and config."""

    cfg: Dict = workflow_config.copy() if workflow_config else {}
    lanes: Dict[str, List[Task]] = {"backend": [], "frontend": []}

    requires_backend = _requires_backend(spec)
    requires_frontend = _requires_frontend(spec)
    requires_db = _requires_database(spec, cfg)
    requires_auth = _requires_auth(spec, cfg)
    requires_compliance = _requires_compliance(spec, cfg)
    project_type = _project_type(spec, cfg)
    features = list(_features(spec, cfg))
    has_analytics = any("analytics" in f for f in features)

    if requires_backend:
        backend_lane = lanes["backend"]
        if requires_db:
            backend_lane.extend(
                [
                    _task(
                        "BE-SCH",
                        "Design DB schema",
                        "backend",
                        acceptance=["ERD drafted", "tables defined", "naming conventions applied"],
                    ),
                    _task(
                        "BE-SEED",
                        "Seed loaders (CSV/mock)",
                        "backend",
                        blocked_by=["BE-SCH"],
                        acceptance=["seed scripts run", "sample rows present"],
                    ),
                    _task(
                        "BE-MDL",
                        "Model domain aggregates",
                        "backend",
                        blocked_by=["BE-SEED"],
                        acceptance=["views or services created", "query p95 < 400ms (seed)"],
                    ),
                ]
            )
        else:
            backend_lane.append(
                _task(
                    "BE-DATA-CONTRACTS",
                    "Define service/data contracts",
                    "backend",
                    acceptance=["pydantic/dto layer defined", "error schema documented"],
                )
            )

        if project_type in {"api", "fullstack", "microservices"}:
            backend_lane.extend(_backend_api_tasks(has_analytics))

        if requires_auth:
            backend_lane.append(
                _task(
                    "BE-AUTH",
                    f"{_normalise_capability(cfg.get('auth', spec.auth)).upper()} integration",
                    "backend",
                    labels=["security"],
                    acceptance=["role checks present", "token validation wired"],
                )
            )

        backend_lane.append(
            _task(
                "BE-OBS",
                "Structured logs + correlation IDs",
                "backend",
                labels=["observability"],
                acceptance=["request id on logs"],
            )
        )

        if "realtime" in features:
            backend_lane.append(
                _task(
                    "BE-REALTIME",
                    "Realtime channel / websocket broker",
                    "backend",
                    blocked_by=["BE-OBS"],
                    acceptance=["pub/sub working", "fallback documented"],
                )
            )

        if requires_compliance:
            backend_lane.append(
                _task(
                    "BE-COMPLIANCE",
                    "Compliance hardening & audit logging",
                    "backend",
                    labels=["compliance"],
                    acceptance=[
                        "audit logs persisted",
                        "data retention documented",
                        "access controls reviewed",
                    ],
                )
            )

        backend_lane.append(
            _task(
                "BE-TST",
                "Unit + integration tests",
                "backend",
                blocked_by=[t.id for t in backend_lane if t.id.startswith("BE-API")][:2],
                acceptance=["pytest green", ">= minimal coverage"],
            )
        )

    if requires_frontend:
        frontend_lane = lanes["frontend"]
        frontend_lane.extend(
            [
                _task(
                    "FE-DSN",
                    "Shell/Layout/Routes",
                    "frontend",
                    acceptance=["routes wired", "base theme applied"],
                ),
                _task(
                    "FE-TYPES",
                    "Typed API client",
                    "frontend",
                    blocked_by=["FE-DSN"],
                    acceptance=["types generated", "client builds"],
                ),
                _task(
                    "FE-MOCKS",
                    "MSW/Prism mocks",
                    "frontend",
                    acceptance=["mocks respond", "dev proxy configured"],
                ),
            ]
        )

        frontend_lane.extend(
            [
                _task(
                    "FE-KPI",
                    "KPI cards + filters",
                    "frontend",
                    blocked_by=["FE-DSN", "FE-TYPES"],
                    acceptance=["renders", "no console errors"],
                ),
                _task(
                    "FE-REV",
                    "Revenue or trend chart",
                    "frontend",
                    blocked_by=["FE-DSN", "FE-TYPES"],
                    acceptance=["renders", "no console errors"],
                ),
                _task("FE-PLT", "Segment distribution", "frontend", blocked_by=["FE-DSN", "FE-TYPES"]),
                _task("FE-CAT", "Category ranks", "frontend", blocked_by=["FE-DSN", "FE-TYPES"]),
                _task("FE-CUS", "Customer insights", "frontend", blocked_by=["FE-DSN", "FE-TYPES"]),
                _task(
                    "FE-FDB",
                    "Feedback or activity timeline",
                    "frontend",
                    blocked_by=["FE-DSN", "FE-TYPES"],
                ),
                _task(
                    "FE-EXP",
                    "Exports (CSV/PNG)",
                    "frontend",
                    blocked_by=[
                        "FE-KPI",
                        "FE-REV",
                        "FE-PLT",
                        "FE-CAT",
                        "FE-CUS",
                        "FE-FDB",
                    ],
                    acceptance=["Exports working"],
                ),
            ]
        )

        frontend_lane.extend(_frontend_feature_tasks(features))

        if requires_compliance:
            frontend_lane.append(
                _task(
                    "FE-COMPLIANCE",
                    "Accessibility + compliance evidence",
                    "frontend",
                    labels=["compliance"],
                    acceptance=["WCAG AA", "policies documented"],
                )
            )

        frontend_lane.append(
            _task(
                "FE-A11Y-PERF",
                "WCAG + performance tuning",
                "frontend",
                labels=["a11y", "performance"],
            )
        )
        frontend_lane.append(
            _task(
                "FE-TST",
                "Component + E2E smoke",
                "frontend",
                blocked_by=["FE-KPI", "FE-REV"],
                acceptance=["tests green"],
            )
        )

    return {lane: [task.as_dict() for task in tasks] for lane, tasks in lanes.items()}

