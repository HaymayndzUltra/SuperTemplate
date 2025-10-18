"""GitHub pull request comparison utility.

This script fetches metadata for multiple pull requests and renders a
summary tailored for prioritisation discussions.  It is designed to help
reviewers quickly understand which PRs are blocked, which are merge-ready,
and how dependencies should influence review order.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Iterable, Sequence
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_ROOT = "https://api.github.com"
LABEL_RISK_PREFIXES = ("risk:", "risk-", "risk/")
LABEL_PRIORITY_PREFIXES = ("priority:", "priority-", "priority/")
DEPENDENCY_PATTERNS = (
    re.compile(r"depends on\s*#(\d+)", re.IGNORECASE),
    re.compile(r"blocked by\s*#(\d+)", re.IGNORECASE),
    re.compile(r"requires\s*#(\d+)", re.IGNORECASE),
)


@dataclass
class PullRequest:
    number: int
    title: str
    state: str
    draft: bool
    html_url: str
    mergeable_state: str | None
    requested_reviewers: list[str] = field(default_factory=list)
    requested_teams: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)
    commits: int | None = None
    additions: int | None = None
    deletions: int | None = None
    changed_files: int | None = None
    updated_at: str | None = None
    body: str | None = None
    head_ref: str | None = None
    base_ref: str | None = None
    draft_reason: str | None = None

    @property
    def risk(self) -> str:
        return _classify_by_label(self.labels, LABEL_RISK_PREFIXES, default="Unknown")

    @property
    def priority(self) -> str:
        return _classify_by_label(self.labels, LABEL_PRIORITY_PREFIXES, default="Normal")

    @property
    def dependencies(self) -> set[int]:
        if not self.body:
            return set()
        deps: set[int] = set()
        for pattern in DEPENDENCY_PATTERNS:
            for match in pattern.findall(self.body):
                try:
                    deps.add(int(match))
                except ValueError:
                    continue
        return deps

    def action_hint(self) -> str:
        if self.state != "open":
            return "ℹ️ Closed"
        if self.draft:
            return "📝 Draft – finish implementation"
        if self.mergeable_state in {"dirty", "blocked"}:
            return "🚧 Resolve merge conflicts"
        if self.requested_reviewers or self.requested_teams:
            reviewers = ", ".join(sorted(self.requested_reviewers + self.requested_teams))
            return f"👀 Awaiting review from {reviewers}" if reviewers else "👀 Awaiting review"
        if self.mergeable_state == "clean":
            return "✅ Ready to merge"
        if self.mergeable_state == "unstable":
            return "⚠️ Check failing checks"
        return "🔍 Needs review"

    def status_label(self) -> str:
        status = "Draft" if self.draft else self.state.title()
        if self.mergeable_state and self.state == "open":
            status = f"{status} ({self.mergeable_state})"
        return status

    def updated_timestamp(self) -> str:
        if not self.updated_at:
            return "unknown"
        try:
            dt = datetime.fromisoformat(self.updated_at.rstrip("Z")).replace(tzinfo=timezone.utc)
        except ValueError:
            return self.updated_at
        return dt.astimezone().strftime("%Y-%m-%d %H:%M %Z")


def _classify_by_label(labels: Iterable[str], prefixes: Sequence[str], default: str) -> str:
    for label in labels:
        label_lower = label.lower()
        for prefix in prefixes:
            if label_lower.startswith(prefix):
                value = label[len(prefix):].strip()
                if value:
                    return value.capitalize()
        if "high" in label_lower and "risk" in label_lower:
            return "High"
        if "medium" in label_lower and "risk" in label_lower:
            return "Medium"
        if "low" in label_lower and "risk" in label_lower:
            return "Low"
        if "high" in label_lower and "priority" in label_lower:
            return "High"
        if "medium" in label_lower and "priority" in label_lower:
            return "Medium"
        if "low" in label_lower and "priority" in label_lower:
            return "Low"
    return default


def github_get(path: str, token: str | None, params: dict[str, str] | None = None) -> dict:
    url = f"{API_ROOT}{path}"
    if params:
        url = f"{url}?{urlencode(params)}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "supertemplate-pr-compare",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    try:
        with urlopen(request) as response:
            return json.load(response)
    except HTTPError as exc:  # pragma: no cover - network error path
        error_payload = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"GitHub API error {exc.code} for {url}: {error_payload}") from exc


def fetch_pull_request(repo: str, number: int, token: str | None) -> PullRequest:
    data = github_get(f"/repos/{repo}/pulls/{number}", token)
    return PullRequest(
        number=number,
        title=data.get("title", "(no title)"),
        state=data.get("state", "unknown"),
        draft=bool(data.get("draft")),
        html_url=data.get("html_url", ""),
        mergeable_state=data.get("mergeable_state"),
        requested_reviewers=[item.get("login", "") for item in data.get("requested_reviewers", []) if item.get("login")],
        requested_teams=[item.get("slug", "") for item in data.get("requested_teams", []) if item.get("slug")],
        labels=[label.get("name", "") for label in data.get("labels", []) if label.get("name")],
        commits=data.get("commits"),
        additions=data.get("additions"),
        deletions=data.get("deletions"),
        changed_files=data.get("changed_files"),
        updated_at=data.get("updated_at"),
        body=data.get("body"),
        head_ref=data.get("head", {}).get("ref"),
        base_ref=data.get("base", {}).get("ref"),
        draft_reason=data.get("draft_reason"),
    )


def build_summary_table(prs: Sequence[PullRequest]) -> str:
    headers = ("PR", "Title", "Status", "Risk", "Priority", "Action")
    rows = [headers]
    for pr in prs:
        rows.append(
            (
                f"#{pr.number}",
                pr.title,
                pr.status_label(),
                pr.risk,
                pr.priority,
                pr.action_hint(),
            )
        )
    widths = [max(len(str(row[idx])) for row in rows) for idx in range(len(headers))]
    lines = []
    for ridx, row in enumerate(rows):
        pieces = [str(value).ljust(widths[idx]) for idx, value in enumerate(row)]
        line = " | ".join(pieces)
        lines.append(line)
        if ridx == 0:
            lines.append("-|-".join("-" * width for width in widths))
    return "\n".join(lines)


def build_dependency_map(prs: Sequence[PullRequest]) -> str:
    lines: list[str] = []
    for pr in prs:
        deps = sorted(dep for dep in pr.dependencies if dep in {p.number for p in prs})
        if deps:
            arrow = ", ".join(f"#{dep}" for dep in deps)
            lines.append(f"#{pr.number} ← depends on {arrow}")
    return "\n".join(lines) if lines else "(no explicit dependencies detected)"


def risk_buckets(prs: Sequence[PullRequest]) -> dict[str, list[int]]:
    bucket: dict[str, list[int]] = defaultdict(list)
    for pr in prs:
        bucket[pr.risk].append(pr.number)
    return bucket


def priority_score(priority: str) -> int:
    lookup = {"Critical": 3, "High": 2, "Medium": 1, "Low": 0, "Normal": 1, "Unknown": 1}
    return lookup.get(priority, 1)


def risk_score(risk: str) -> int:
    lookup = {"High": 3, "Medium": 2, "Low": 1, "Unknown": 2}
    return lookup.get(risk, 2)


def topo_sort(prs: Sequence[PullRequest]) -> list[PullRequest]:
    numbers = {pr.number for pr in prs}
    indegree: dict[int, int] = {pr.number: 0 for pr in prs}
    graph: dict[int, set[int]] = {pr.number: set() for pr in prs}
    for pr in prs:
        for dep in pr.dependencies:
            if dep in numbers:
                graph[dep].add(pr.number)
                indegree[pr.number] += 1

    queue: deque[int] = deque(sorted(num for num, deg in indegree.items() if deg == 0))
    ordered: list[int] = []
    while queue:
        current = queue.popleft()
        ordered.append(current)
        for neighbour in sorted(graph[current]):
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(ordered) != len(prs):
        # Cycle or external dependency. Fallback to risk/priority weighting.
        return sorted(
            prs,
            key=lambda pr: (
                -risk_score(pr.risk),
                -priority_score(pr.priority),
                pr.number,
            ),
        )

    order_lookup = {number: idx for idx, number in enumerate(ordered)}
    return sorted(prs, key=lambda pr: order_lookup[pr.number])


def render_text_report(repo: str, prs: Sequence[PullRequest]) -> str:
    lines: list[str] = []
    lines.append(f"Pull Request Comparison for {repo}")
    lines.append("=")
    lines.append("")
    lines.append("Summary Table")
    lines.append("-------------")
    lines.append(build_summary_table(prs))
    lines.append("")
    lines.append("Dependencies")
    lines.append("------------")
    lines.append(build_dependency_map(prs))
    lines.append("")
    lines.append("Risk Overview")
    lines.append("-------------")
    buckets = risk_buckets(prs)
    for risk, numbers in sorted(buckets.items(), key=lambda item: -risk_score(item[0])):
        formatted = ", ".join(f"#{num}" for num in sorted(numbers))
        lines.append(f"- {risk}: {formatted}")
    lines.append("")
    lines.append("Recommended Merge Order")
    lines.append("------------------------")
    ordered = topo_sort(prs)
    for idx, pr in enumerate(ordered, start=1):
        reason = pr.action_hint()
        lines.append(f"{idx}. #{pr.number} – {pr.title} ({reason})")
    lines.append("")
    lines.append("Detailed Notes")
    lines.append("--------------")
    for pr in prs:
        lines.append(f"### PR #{pr.number}: {pr.title}")
        lines.append(f"- Status: {pr.status_label()} (updated {pr.updated_timestamp()})")
        if pr.head_ref and pr.base_ref:
            lines.append(f"- Branch: {pr.head_ref} → {pr.base_ref}")
        if pr.commits is not None:
            lines.append(
                f"- Commits: {pr.commits}, Changes: +{pr.additions or 0} / -{pr.deletions or 0}, Files: {pr.changed_files or 0}"
            )
        if pr.dependencies:
            internal = [f"#{dep}" for dep in sorted(pr.dependencies)]
            lines.append("- Dependencies: " + ", ".join(internal))
        if pr.requested_reviewers or pr.requested_teams:
            reviewers = sorted(pr.requested_reviewers + pr.requested_teams)
            lines.append("- Awaiting review from: " + ", ".join(reviewers))
        if pr.draft_reason:
            lines.append(f"- Draft reason: {pr.draft_reason}")
        lines.append(f"- Suggested action: {pr.action_hint()}")
        lines.append(f"- Link: {pr.html_url}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def render_json_report(repo: str, prs: Sequence[PullRequest]) -> str:
    payload = {
        "repository": repo,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "pull_requests": [
            {
                "number": pr.number,
                "title": pr.title,
                "url": pr.html_url,
                "status": pr.status_label(),
                "risk": pr.risk,
                "priority": pr.priority,
                "action": pr.action_hint(),
                "dependencies": sorted(pr.dependencies),
                "metrics": {
                    "commits": pr.commits,
                    "additions": pr.additions,
                    "deletions": pr.deletions,
                    "changed_files": pr.changed_files,
                },
                "branch": {
                    "head": pr.head_ref,
                    "base": pr.base_ref,
                },
                "updated_at": pr.updated_timestamp(),
            }
            for pr in prs
        ],
        "recommended_order": [pr.number for pr in topo_sort(prs)],
    }
    return json.dumps(payload, indent=2)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare multiple GitHub pull requests")
    parser.add_argument("numbers", metavar="PR", nargs="+", type=int, help="Pull request numbers to analyse")
    parser.add_argument(
        "--repo",
        default=os.getenv("GITHUB_REPOSITORY"),
        help="Target repository in 'owner/name' form (default: $GITHUB_REPOSITORY)",
    )
    parser.add_argument(
        "--token",
        default=os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN"),
        help="GitHub token with `repo` or `public_repo` scope (default: $GITHUB_TOKEN)",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format (default: text)",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if not args.repo:
        print("--repo is required (or set GITHUB_REPOSITORY)", file=sys.stderr)
        return 2

    prs: list[PullRequest] = []
    for number in args.numbers:
        try:
            prs.append(fetch_pull_request(args.repo, number, args.token))
        except RuntimeError as exc:
            print(exc, file=sys.stderr)
            return 1

    if args.format == "json":
        print(render_json_report(args.repo, prs))
    else:
        print(render_text_report(args.repo, prs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
