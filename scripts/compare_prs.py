"""CLI utility for comparing multiple GitHub pull requests.

This script fetches metadata for pull requests from the GitHub REST API and
produces a consolidated review report with risk scoring, dependency analysis,
and action recommendations. It is designed to help reviewers quickly
understand which pull requests are ready to merge and which need attention.
"""
from __future__ import annotations

import argparse
import os
import re
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import requests

API_ROOT = "https://api.github.com"


class PullRequestFetchError(RuntimeError):
    """Raised when the GitHub API returns an error for a pull request."""


@dataclass
class ReviewSummary:
    approvals: int = 0
    change_requests: int = 0
    comments: int = 0

    @property
    def status(self) -> str:
        if self.change_requests:
            return "Changes requested"
        if self.approvals:
            return "Approved"
        if self.comments:
            return "Commented"
        return "Pending review"


@dataclass
class PullRequest:
    number: int
    title: str
    state: str
    draft: bool
    mergeable_state: Optional[str]
    changed_files: int
    additions: int
    deletions: int
    labels: List[str]
    html_url: str
    base_branch: str
    head_branch: str
    author: str
    updated_at: str
    body: str
    dependencies: List[int] = field(default_factory=list)
    review_summary: ReviewSummary = field(default_factory=ReviewSummary)

    @property
    def total_changes(self) -> int:
        return self.additions + self.deletions


def build_session(token: Optional[str]) -> requests.Session:
    session = requests.Session()
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "supertemplate-pr-comparison",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    session.headers.update(headers)
    return session


def fetch_pull_request(session: requests.Session, repo: str, number: int) -> PullRequest:
    response = session.get(f"{API_ROOT}/repos/{repo}/pulls/{number}")
    if response.status_code != 200:
        raise PullRequestFetchError(
            f"Failed to fetch PR #{number}: {response.status_code} {response.text}"
        )
    payload = response.json()

    labels = [label["name"] for label in payload.get("labels", [])]
    body = payload.get("body") or ""
    dependencies = parse_dependencies(body)

    pr = PullRequest(
        number=payload["number"],
        title=payload.get("title", ""),
        state=payload.get("state", "unknown"),
        draft=payload.get("draft", False),
        mergeable_state=payload.get("mergeable_state"),
        changed_files=payload.get("changed_files", 0),
        additions=payload.get("additions", 0),
        deletions=payload.get("deletions", 0),
        labels=labels,
        html_url=payload.get("html_url", ""),
        base_branch=payload.get("base", {}).get("ref", ""),
        head_branch=payload.get("head", {}).get("ref", ""),
        author=payload.get("user", {}).get("login", "unknown"),
        updated_at=payload.get("updated_at", ""),
        body=body,
        dependencies=dependencies,
    )
    pr.review_summary = fetch_review_summary(session, repo, number)
    return pr


def fetch_review_summary(session: requests.Session, repo: str, number: int) -> ReviewSummary:
    response = session.get(f"{API_ROOT}/repos/{repo}/pulls/{number}/reviews")
    if response.status_code != 200:
        return ReviewSummary()

    approvals: Dict[str, str] = {}
    change_requests: Dict[str, str] = {}
    comments = 0
    for review in response.json():
        state = review.get("state") or ""
        user = (review.get("user") or {}).get("login")
        if not user:
            continue
        normalized = state.upper()
        if normalized == "APPROVED":
            approvals[user] = review.get("submitted_at", "")
        elif normalized == "CHANGES_REQUESTED":
            change_requests[user] = review.get("submitted_at", "")
        elif normalized == "COMMENTED":
            comments += 1

    return ReviewSummary(
        approvals=len(approvals),
        change_requests=len(change_requests),
        comments=comments,
    )


_DEPENDENCY_PATTERN = re.compile(
    r"(?:depends on|blocked by|requires)\s+#(?P<number>\d+)", re.IGNORECASE
)


def parse_dependencies(body: str) -> List[int]:
    return [int(match.group("number")) for match in _DEPENDENCY_PATTERN.finditer(body)]


def compute_risk(pr: PullRequest) -> Tuple[str, List[str]]:
    score = 0
    reasons: List[str] = []

    if pr.draft:
        score += 1
        reasons.append("draft")

    mergeable = (pr.mergeable_state or "").lower()
    if mergeable in {"dirty", "blocked", "unstable"}:
        score += 2
        reasons.append(f"mergeable_state={mergeable}")
    elif mergeable in {"unknown", "behind"}:
        score += 1
        reasons.append(f"mergeable_state={mergeable}")

    if pr.review_summary.change_requests:
        score += 2
        reasons.append("changes requested")
    elif pr.review_summary.approvals == 0:
        score += 1
        reasons.append("no approvals yet")

    if pr.changed_files >= 30:
        score += 2
        reasons.append(f"{pr.changed_files} files changed")
    elif pr.changed_files >= 10:
        score += 1
        reasons.append(f"{pr.changed_files} files changed")

    if pr.total_changes >= 2000:
        score += 2
        reasons.append(f"{pr.total_changes} total changes")
    elif pr.total_changes >= 600:
        score += 1
        reasons.append(f"{pr.total_changes} total changes")

    if pr.labels:
        risk_labels = {label.lower() for label in pr.labels}
        if any(keyword in risk_labels for keyword in {"breaking", "security", "critical"}):
            score += 2
            reasons.append("high-risk label")

    if score <= 1:
        return "Low", reasons
    if score <= 3:
        return "Medium", reasons
    return "High", reasons


def suggest_action(pr: PullRequest, risk_level: str) -> str:
    if pr.state.lower() != "open":
        return "ℹ️ Closed"
    if pr.draft:
        return "📝 Draft"
    mergeable = (pr.mergeable_state or "").lower()
    if pr.review_summary.change_requests:
        return "❗ Address review changes"
    if mergeable == "clean" and risk_level == "Low":
        return "✅ Ready to merge"
    if mergeable in {"clean", "has_hooks", "unknown"}:
        return "⚠️ Needs final checks"
    return "🚧 Resolve merge blockers"


def topological_merge_order(prs: Sequence[PullRequest]) -> List[int]:
    graph: Dict[int, List[int]] = defaultdict(list)
    indegree: Dict[int, int] = {pr.number: 0 for pr in prs}
    present_numbers = {pr.number for pr in prs}

    for pr in prs:
        for dep in pr.dependencies:
            if dep in present_numbers:
                graph[dep].append(pr.number)
                indegree[pr.number] += 1

    queue: deque[int] = deque(sorted(num for num, deg in indegree.items() if deg == 0))
    order: List[int] = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for successor in sorted(graph.get(current, [])):
            indegree[successor] -= 1
            if indegree[successor] == 0:
                queue.append(successor)

    if len(order) != len(prs):
        remaining = [num for num in indegree if num not in order]
        order.extend(sorted(remaining))
    return order


def format_summary(prs: Sequence[PullRequest]) -> str:
    rows = ["| PR | Title | State | Risk | Action |", "|----|-------|-------|------|--------|"]
    for pr in sorted(prs, key=lambda p: p.number):
        risk, _ = compute_risk(pr)
        action = suggest_action(pr, risk)
        rows.append(
            f"| #{pr.number} | {pr.title} | {pr.state.title()} | {risk} | {action} |"
        )
    return "\n".join(rows)


def format_details(prs: Sequence[PullRequest]) -> str:
    sections: List[str] = []
    for pr in sorted(prs, key=lambda p: p.number):
        risk, reasons = compute_risk(pr)
        action = suggest_action(pr, risk)
        review = pr.review_summary
        details = [
            f"### PR #{pr.number}: {pr.title}",
            f"- **URL**: {pr.html_url}",
            f"- **State**: {pr.state.title()} | **Draft**: {'Yes' if pr.draft else 'No'}",
            f"- **Branches**: {pr.head_branch} → {pr.base_branch}",
            f"- **Reviews**: {review.approvals} approvals, {review.change_requests} change requests, {review.comments} comments",
            f"- **Files Changed**: {pr.changed_files} | **Total Changes**: {pr.total_changes}",
            f"- **Labels**: {', '.join(pr.labels) if pr.labels else 'None'}",
            f"- **Risk Level**: {risk}",
            f"- **Action**: {action}",
        ]
        if reasons:
            details.append(f"- **Risk Factors**: {', '.join(reasons)}")
        if pr.dependencies:
            deps = ", ".join(f"#{dep}" for dep in pr.dependencies)
            details.append(f"- **Dependencies**: {deps}")
        sections.append("\n".join(details))
    return "\n\n".join(sections)


def format_merge_order(prs: Sequence[PullRequest]) -> str:
    order = topological_merge_order(prs)
    if not order:
        return "No pull requests provided."

    lookup = {pr.number: pr for pr in prs}
    lines = ["### Recommended Merge Order"]
    for position, number in enumerate(order, start=1):
        pr = lookup[number]
        risk, _ = compute_risk(pr)
        lines.append(f"{position}. PR #{number} — {pr.title} (Risk: {risk})")
    return "\n".join(lines)


def compare_pull_requests(repo: str, numbers: Iterable[int], token: Optional[str]) -> str:
    session = build_session(token)
    pull_requests: List[PullRequest] = []

    for number in numbers:
        try:
            pull_requests.append(fetch_pull_request(session, repo, number))
        except PullRequestFetchError as exc:
            raise SystemExit(str(exc)) from exc

    report_parts = ["## Pull Request Comparison Summary", ""]
    report_parts.append(format_summary(pull_requests))
    report_parts.append("")
    report_parts.append(format_merge_order(pull_requests))
    report_parts.append("")
    report_parts.append(format_details(pull_requests))
    return "\n".join(report_parts)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare multiple GitHub pull requests and generate a review summary.",
    )
    parser.add_argument(
        "numbers",
        metavar="PR",
        type=int,
        nargs="+",
        help="Pull request numbers to compare.",
    )
    parser.add_argument(
        "--repo",
        required=True,
        help="Repository in the form 'owner/name'.",
    )
    parser.add_argument(
        "--token",
        default=os.getenv("GITHUB_TOKEN"),
        help="GitHub token with `repo` scope. Defaults to the GITHUB_TOKEN environment variable.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = parse_args(argv)
    report = compare_pull_requests(args.repo, args.numbers, args.token)
    print(report)


if __name__ == "__main__":
    main()
