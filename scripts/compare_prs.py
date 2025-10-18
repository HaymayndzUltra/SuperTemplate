"""Command-line utility for comparing multiple GitHub pull requests.

This script fetches metadata and file lists for up to four pull requests and
produces a textual report that highlights risk, priority, file conflicts, and a
recommended merge order.  It is intentionally lightweight so it can run in
restricted environments (no external dependencies beyond the standard
library).

Typical usage:

```
python scripts/compare_prs.py 1 3 4 8 --repo HaymayndzUltra/SuperTemplate
```

Authentication is optional.  If a GitHub token is provided (via the
`--token` argument or the `GITHUB_TOKEN` environment variable) the script will
use it to avoid low unauthenticated rate limits.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import os
import re
import subprocess
import sys
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from typing import Dict, List, Optional, Sequence, Tuple


GITHUB_API_ROOT = "https://api.github.com"
DEFAULT_USER_AGENT = "SuperTemplate-PR-Comparator"


class GitHubAPIError(RuntimeError):
    """Raised when the GitHub API returns an unexpected response."""


def _build_headers(token: Optional[str]) -> Dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": DEFAULT_USER_AGENT,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _read_json(url: str, headers: Dict[str, str]) -> Tuple[dict, Dict[str, str]]:
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request) as response:
            content_type = response.headers.get("Content-Type", "application/json")
            if "json" not in content_type:
                raise GitHubAPIError(f"Unexpected content type: {content_type}")
            charset = response.headers.get_content_charset("utf-8")
            payload = response.read().decode(charset)
            return json.loads(payload), dict(response.headers.items())
    except urllib.error.HTTPError as exc:  # pragma: no cover - network errors are runtime issues
        message = exc.read().decode() if exc.fp else exc.reason
        raise GitHubAPIError(f"GitHub API error {exc.code}: {message}") from exc
    except urllib.error.URLError as exc:  # pragma: no cover
        raise GitHubAPIError(f"Network error: {exc.reason}") from exc


def _paginated_get(path: str, headers: Dict[str, str], params: Optional[Dict[str, str]] = None) -> List[dict]:
    results: List[dict] = []
    page = 1
    params = params or {}
    while True:
        params_with_page = {**params, "page": str(page), "per_page": "100"}
        url = f"{GITHUB_API_ROOT}{path}?{urllib.parse.urlencode(params_with_page)}"
        data, _ = _read_json(url, headers)
        if not isinstance(data, list):
            raise GitHubAPIError(f"Expected list response for {path}, got {type(data).__name__}")
        if not data:
            break
        results.extend(data)
        if len(data) < 100:
            break
        page += 1
        time.sleep(0.1)  # be gentle with the API
    return results


def _get_repo_from_git() -> Optional[str]:
    try:
        remote_url = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

    if remote_url.endswith(".git"):
        remote_url = remote_url[:-4]

    if remote_url.startswith("git@"):
        # git@github.com:owner/repo
        _, path = remote_url.split(":", 1)
    elif remote_url.startswith("https://") or remote_url.startswith("http://"):
        path = urllib.parse.urlparse(remote_url).path.lstrip("/")
    else:
        return None

    if path.count("/") >= 1:
        owner, repo = path.split("/", 1)
        return f"{owner}/{repo}"
    return None


@dataclasses.dataclass
class PullRequestAnalysis:
    number: int
    title: str
    state: str
    draft: bool
    created_at: str
    updated_at: str
    additions: int
    deletions: int
    changed_files: int
    labels: Sequence[str]
    reviewers: Sequence[str]
    review_decision: Optional[str]
    body: str
    files: Sequence[str]
    dependencies: Sequence[int]
    tests_changed: bool

    def lines_changed(self) -> int:
        return self.additions + self.deletions

    def priority_level(self) -> str:
        for label in self.labels:
            lower = label.lower()
            if any(keyword in lower for keyword in ("p0", "critical", "urgent", "priority:critical")):
                return "critical"
            if any(keyword in lower for keyword in ("p1", "high", "priority:high")):
                return "high"
        for label in self.labels:
            if any(keyword in label.lower() for keyword in ("medium", "p2", "priority:medium")):
                return "medium"
        for label in self.labels:
            if any(keyword in label.lower() for keyword in ("low", "p3", "priority:low")):
                return "low"
        return "medium"

    def risk_level(self) -> str:
        for label in self.labels:
            lower = label.lower()
            if "risk:high" in lower or "high risk" in lower:
                return "high"
            if "risk:medium" in lower or "medium risk" in lower:
                return "medium"
            if "risk:low" in lower or "low risk" in lower:
                return "low"
        lines = self.lines_changed()
        if lines > 600 or self.changed_files > 30:
            return "high"
        if lines > 250 or self.changed_files > 15:
            return "medium"
        if self.tests_changed:
            return "low"
        return "medium"

    def readiness(self) -> str:
        if self.state != "open":
            return "closed"
        if self.draft:
            return "draft"
        if self.review_decision:
            return self.review_decision.lower()
        return "ready"


DEPENDENCY_PATTERN = re.compile(r"(?:depends on|blocked by)\s+#(\d+)", re.IGNORECASE)


def extract_dependencies(text: str) -> Sequence[int]:
    return [int(match) for match in DEPENDENCY_PATTERN.findall(text or "")]


def detect_tests(files: Sequence[str]) -> bool:
    return any(re.search(r"(test|spec)\.", path, re.IGNORECASE) for path in files)


def fetch_pull_request(repo: str, number: int, token: Optional[str]) -> PullRequestAnalysis:
    headers = _build_headers(token)
    path = f"/repos/{repo}/pulls/{number}"
    data, _ = _read_json(f"{GITHUB_API_ROOT}{path}", headers)

    if "message" in data and "Not Found" in data["message"]:
        raise GitHubAPIError(f"Pull request #{number} not found in {repo}")

    files = _paginated_get(path + "/files", headers)
    file_paths = [item.get("filename", "") for item in files]

    labels = [label.get("name", "") for label in data.get("labels", [])]
    reviewers = [user.get("login", "") for user in data.get("requested_reviewers", [])]
    dependencies = extract_dependencies(data.get("body", ""))
    tests_changed = detect_tests(file_paths)

    return PullRequestAnalysis(
        number=number,
        title=data.get("title", ""),
        state=data.get("state", "unknown"),
        draft=bool(data.get("draft")),
        created_at=data.get("created_at", ""),
        updated_at=data.get("updated_at", ""),
        additions=int(data.get("additions", 0)),
        deletions=int(data.get("deletions", 0)),
        changed_files=int(data.get("changed_files", 0)),
        labels=labels,
        reviewers=reviewers,
        review_decision=data.get("review_decision"),
        body=data.get("body", ""),
        files=file_paths,
        dependencies=dependencies,
        tests_changed=tests_changed,
    )


def score_pr(pr: PullRequestAnalysis, conflict_count: int) -> float:
    priority_weights = {
        "critical": 4.0,
        "high": 3.0,
        "medium": 2.0,
        "low": 1.0,
    }
    risk_weights = {
        "low": 1.5,
        "medium": 1.0,
        "high": -0.5,
    }
    readiness_weights = {
        "ready": 1.0,
        "approved": 1.5,
        "changes_requested": -1.0,
        "review_required": 0.2,
        "draft": -1.5,
        "closed": -2.0,
    }

    score = priority_weights.get(pr.priority_level(), 1.0)
    score += risk_weights.get(pr.risk_level(), 0.5)
    score += readiness_weights.get(pr.readiness(), 0.0)

    # Encourage PRs that modify tests or have smaller surface area
    if pr.tests_changed:
        score += 0.5
    if pr.lines_changed() < 150 and pr.changed_files <= 5:
        score += 0.5

    # Penalize PRs that conflict heavily with others
    score -= min(conflict_count, 3) * 0.5

    return score


def summarise_labels(labels: Sequence[str]) -> str:
    return ", ".join(labels) if labels else "(none)"


def pluralize(word: str, count: int) -> str:
    return f"{count} {word}{'' if count == 1 else 's'}"


def build_conflict_matrix(prs: Sequence[PullRequestAnalysis]) -> Dict[str, List[int]]:
    matrix: Dict[str, List[int]] = defaultdict(list)
    for pr in prs:
        for path in pr.files:
            matrix[path].append(pr.number)
    return matrix


def classify_conflict(pr_numbers: Sequence[int]) -> str:
    if len(pr_numbers) >= 3:
        return "critical"
    if len(pr_numbers) == 2:
        return "high"
    return "low"


def format_conflict_table(conflicts: Dict[str, List[int]]) -> str:
    if not conflicts:
        return "No overlapping files detected between the analysed pull requests."

    headers = ["File Path", "PRs", "Risk"]
    rows = []
    for path, numbers in sorted(conflicts.items()):
        if len(numbers) < 2:
            continue
        rows.append((path, ", ".join(f"#{num}" for num in numbers), classify_conflict(numbers)))

    if not rows:
        return "No overlapping files detected between the analysed pull requests."

    output_lines = [" | ".join(headers), " | ".join(["-" * len(h) for h in headers])]
    for path, prs, risk in rows:
        output_lines.append(f"{path} | {prs} | {risk.upper()}")
    return "\n".join(output_lines)


def format_summary_table(prs: Sequence[PullRequestAnalysis]) -> str:
    headers = ["PR", "Title", "Lines", "Files", "Risk", "Priority", "Readiness"]
    col_widths = [len(header) for header in headers]
    rows = []
    for pr in prs:
        row = [
            f"#{pr.number}",
            pr.title,
            str(pr.lines_changed()),
            str(pr.changed_files),
            pr.risk_level(),
            pr.priority_level(),
            pr.readiness(),
        ]
        rows.append(row)
        col_widths = [max(cw, len(cell)) for cw, cell in zip(col_widths, row)]

    def format_row(row_values: Sequence[str]) -> str:
        return " | ".join(value.ljust(width) for value, width in zip(row_values, col_widths))

    lines = [format_row(headers), format_row(["-" * len(h) for h in headers])]
    for row in rows:
        lines.append(format_row(row))
    return "\n".join(lines)


def describe_pr(pr: PullRequestAnalysis, conflict_matrix: Dict[str, List[int]]) -> str:
    conflicts = [path for path in pr.files if len(conflict_matrix.get(path, [])) > 1]
    conflict_summary = (
        "No conflicting files detected."
        if not conflicts
        else f"Conflicts in: {', '.join(conflicts[:10])}{' …' if len(conflicts) > 10 else ''}"
    )
    dependencies = ", ".join(f"#{num}" for num in pr.dependencies) if pr.dependencies else "None"
    reviewers = ", ".join(pr.reviewers) if pr.reviewers else "None"

    details = textwrap.dedent(
        f"""
        ### PR #{pr.number}: {pr.title}
        * Lines changed: {pr.lines_changed()} ({pr.additions} additions / {pr.deletions} deletions)
        * Files changed: {pr.changed_files}
        * Labels: {summarise_labels(pr.labels)}
        * Priority: {pr.priority_level().upper()} | Risk: {pr.risk_level().upper()} | Readiness: {pr.readiness()}
        * Requested reviewers: {reviewers}
        * Dependencies: {dependencies}
        * Tests touched: {'yes' if pr.tests_changed else 'no'}
        * Conflict summary: {conflict_summary}
        """
    ).strip()
    return details


def pick_recommendation(prs: Sequence[PullRequestAnalysis], conflict_matrix: Dict[str, List[int]]) -> Tuple[PullRequestAnalysis, Dict[int, float]]:
    conflict_counts = {pr.number: 0 for pr in prs}
    for path, numbers in conflict_matrix.items():
        if len(numbers) < 2:
            continue
        for number in numbers:
            conflict_counts[number] += 1

    scores = {pr.number: score_pr(pr, conflict_counts[pr.number]) for pr in prs}
    recommended = max(prs, key=lambda pr: scores[pr.number])
    return recommended, scores


def format_recommendation(pr: PullRequestAnalysis, scores: Dict[int, float]) -> str:
    reasons = [
        f"Priority: {pr.priority_level().upper()}",
        f"Risk level: {pr.risk_level().upper()}",
        f"Readiness: {pr.readiness()}",
        f"Tests touched: {'yes' if pr.tests_changed else 'no'}",
        f"Score: {scores[pr.number]:.2f}",
    ]
    bullet_points = "\n".join(f"- {reason}" for reason in reasons)
    return textwrap.dedent(
        f"""
        ## 🏆 Recommended Pull Request to Merge First

        **PR #{pr.number}: {pr.title}**

        {bullet_points}
        """
    ).strip()


def format_merge_order(prs: Sequence[PullRequestAnalysis], scores: Dict[int, float]) -> str:
    sorted_prs = sorted(prs, key=lambda pr: scores[pr.number], reverse=True)
    lines = ["## Suggested Merge Order"]
    for index, pr in enumerate(sorted_prs, start=1):
        lines.append(
            f"{index}. PR #{pr.number} – {pr.title} (priority: {pr.priority_level()}, risk: {pr.risk_level()}, score: {scores[pr.number]:.2f})"
        )
    return "\n".join(lines)


def build_report(prs: Sequence[PullRequestAnalysis]) -> str:
    conflict_matrix = build_conflict_matrix(prs)
    recommended, scores = pick_recommendation(prs, conflict_matrix)

    parts = [
        format_recommendation(recommended, scores),
        "",
        "## Summary Overview",
        format_summary_table(prs),
        "",
        format_merge_order(prs, scores),
        "",
        "## File Conflict Matrix",
        format_conflict_table(conflict_matrix),
    ]

    for pr in prs:
        parts.extend(["", describe_pr(pr, conflict_matrix)])

    return "\n".join(parts).strip()


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare multiple GitHub pull requests.")
    parser.add_argument(
        "numbers",
        metavar="PR",
        nargs="+",
        help="Pull request numbers to compare",
    )
    parser.add_argument(
        "--repo",
        help="GitHub repository in the form owner/name. If omitted the script attempts to infer it from the current git remote.",
    )
    parser.add_argument(
        "--token",
        help="GitHub access token. If omitted, the GITHUB_TOKEN environment variable is used when available.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    if len(args.numbers) < 2:
        print("Please provide at least two pull request numbers to compare.", file=sys.stderr)
        return 2

    repo = args.repo or _get_repo_from_git()
    if not repo:
        print("Unable to determine repository. Please pass --repo owner/name.", file=sys.stderr)
        return 2

    token = args.token or os.environ.get("GITHUB_TOKEN")

    try:
        pr_numbers = [int(num) for num in args.numbers]
    except ValueError:
        print("All pull request identifiers must be integers.", file=sys.stderr)
        return 2

    analyses: List[PullRequestAnalysis] = []
    for number in pr_numbers:
        try:
            analyses.append(fetch_pull_request(repo, number, token))
        except GitHubAPIError as error:
            print(f"Failed to fetch PR #{number}: {error}", file=sys.stderr)
            return 1

    report = build_report(analyses)
    print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
