#!/usr/bin/env python3
"""
Pull Request Comparison Script

Provides an offline-friendly workflow for comparing multiple GitHub pull requests
and generating actionable review guidance. The script can fetch data directly from
GitHub's REST API or ingest pre-exported JSON data for environments without
network access.
"""

from __future__ import annotations

import argparse
import importlib
import importlib.util
import json
import os
import re
import sys
from collections import deque
from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

requests_spec = importlib.util.find_spec("requests")
requests = importlib.import_module("requests") if requests_spec else None  # type: ignore[assignment]


GITHUB_API_BASE = "https://api.github.com"


@dataclass
class PullRequestSummary:
    """Normalized data about a pull request with derived insights."""

    number: int
    title: str
    state: str
    url: str
    draft: bool
    merged: bool
    author: Optional[str]
    base_branch: Optional[str]
    head_branch: Optional[str]
    additions: int
    deletions: int
    changed_files: int
    labels: List[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    body: str = ""
    review_decision: Optional[str] = None
    mergeable_state: Optional[str] = None
    dependencies: List[int] = field(default_factory=list)
    risk_level: str = "Unknown"
    risk_reasons: List[str] = field(default_factory=list)
    priority: str = "Medium"
    priority_reasons: List[str] = field(default_factory=list)
    recommended_action: str = "Review"
    approvals: int = 0
    change_requests: int = 0
    reviewers_blocking: List[str] = field(default_factory=list)
    files: List[str] = field(default_factory=list)
    tests_touched: bool = False
    conflicts: Dict[int, List[str]] = field(default_factory=dict)

    @property
    def additions_plus_deletions(self) -> int:
        return self.additions + self.deletions

    @property
    def is_open(self) -> bool:
        return self.state.lower() == "open" and not self.merged


class PullRequestComparator:
    """Compare multiple pull requests and generate review recommendations."""

    def __init__(self, repo: Optional[str] = None, token: Optional[str] = None) -> None:
        self.repo = repo
        if requests is None and repo:
            raise SystemExit(
                "The 'requests' package is required for fetching GitHub data. "
                "Install it or provide --input for offline analysis."
            )
        self.session = requests.Session() if requests else None
        if self.session:
            headers = {
                "Accept": "application/vnd.github+json",
                "User-Agent": "supertemplate-pr-comparator/1.0",
            }
            token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
            if token:
                headers["Authorization"] = f"Bearer {token}"
            self.session.headers.update(headers)

    # -------------------- Public API --------------------
    def fetch(self, numbers: Sequence[int]) -> List[PullRequestSummary]:
        if not self.repo:
            raise ValueError("Repository must be provided when fetching from GitHub.")
        summaries: List[PullRequestSummary] = []
        for number in numbers:
            payload = self._fetch_pull_request(number)
            payload["reviews"] = self._fetch_reviews(number)
            payload["files"] = self._fetch_files(number)
            summaries.append(self._normalize_payload(payload))
        self._enrich_summaries(summaries)
        return summaries

    def load_from_json(self, data: Sequence[dict]) -> List[PullRequestSummary]:
        summaries = [self._normalize_payload(item) for item in data]
        self._enrich_summaries(summaries)
        return summaries

    def render_markdown(self, summaries: Sequence[PullRequestSummary]) -> str:
        blocks: List[str] = []
        blocks.append(self._render_summary_table(summaries))
        blocks.append(self._render_review_signals(summaries))
        blocks.append(self._render_dependency_map(summaries))
        blocks.append(self._render_recommended_order(summaries))
        blocks.append(self._render_conflict_matrix(summaries))
        blocks.append(self._render_detailed_notes(summaries))
        return "\n\n".join(block for block in blocks if block)

    def render_text(self, summaries: Sequence[PullRequestSummary]) -> str:
        markdown = self.render_markdown(summaries)
        return re.sub(r"\|", "\t", markdown)

    # -------------------- Fetching helpers --------------------
    def _fetch_pull_request(self, number: int) -> dict:
        if not self.session:
            raise RuntimeError("GitHub session unavailable; cannot fetch pull requests.")
        url = f"{GITHUB_API_BASE}/repos/{self.repo}/pulls/{number}"
        response = self.session.get(url, timeout=30)
        if response.status_code == 404:
            raise SystemExit(f"Pull request #{number} not found in {self.repo}.")
        if response.status_code == 401:
            raise SystemExit("Authentication failed. Check your GitHub token.")
        if response.status_code != 200:
            raise SystemExit(
                f"GitHub API error ({response.status_code}): {response.text.strip()}"
            )
        return response.json()

    def _fetch_reviews(self, number: int) -> List[dict]:
        if not self.session:
            return []
        url = f"{GITHUB_API_BASE}/repos/{self.repo}/pulls/{number}/reviews"
        return self._paginate(url)

    def _fetch_files(self, number: int) -> List[dict]:
        if not self.session:
            return []
        url = f"{GITHUB_API_BASE}/repos/{self.repo}/pulls/{number}/files"
        return self._paginate(url)

    def _paginate(self, url: str) -> List[dict]:
        if not self.session:
            return []
        next_url: Optional[str] = url
        items: List[dict] = []
        while next_url:
            response = self.session.get(next_url, timeout=30)
            if response.status_code != 200:
                raise SystemExit(
                    f"GitHub API error ({response.status_code}): {response.text.strip()}"
                )
            payload = response.json()
            if isinstance(payload, list):
                items.extend(payload)
            next_link = response.links.get("next") if response.links else None
            next_url = next_link.get("url") if next_link else None
        return items

    # -------------------- Normalization --------------------
    def _normalize_payload(self, payload: dict) -> PullRequestSummary:
        labels = [label.get("name", "") for label in payload.get("labels", [])]
        files_payload = payload.get("files") or []
        filenames = [item.get("filename", "") for item in files_payload if item.get("filename")]
        reviews = payload.get("reviews") or []
        approvals = sum(1 for review in reviews if (review.get("state") or "").upper() == "APPROVED")
        change_requests = sum(
            1 for review in reviews if (review.get("state") or "").upper() == "CHANGES_REQUESTED"
        )
        blocking_reviewers_set = {
            (review.get("user") or {}).get("login")
            for review in reviews
            if (review.get("state") or "").upper() == "CHANGES_REQUESTED"
        }
        blocking_reviewers = sorted(reviewer for reviewer in blocking_reviewers_set if reviewer)

        summary = PullRequestSummary(
            number=int(payload.get("number")),
            title=payload.get("title", "Untitled"),
            state=payload.get("state", "unknown"),
            url=payload.get("html_url", ""),
            draft=bool(payload.get("draft", False)),
            merged=bool(payload.get("merged", False)),
            author=(payload.get("user") or {}).get("login"),
            base_branch=(payload.get("base") or {}).get("ref"),
            head_branch=(payload.get("head") or {}).get("ref"),
            additions=int(payload.get("additions") or 0),
            deletions=int(payload.get("deletions") or 0),
            changed_files=int(payload.get("changed_files") or 0),
            labels=labels,
            created_at=payload.get("created_at"),
            updated_at=payload.get("updated_at"),
            body=payload.get("body") or "",
            review_decision=payload.get("review_decision"),
            mergeable_state=payload.get("mergeable_state"),
            approvals=approvals,
            change_requests=change_requests,
            reviewers_blocking=blocking_reviewers,
            files=filenames,
            tests_touched=self._detect_tests(filenames),
        )
        summary.dependencies = self._extract_dependencies(summary.body)
        summary.risk_level, summary.risk_reasons = self._assess_risk(summary)
        summary.priority, summary.priority_reasons = self._determine_priority(summary)
        return summary

    def _enrich_summaries(self, summaries: Sequence[PullRequestSummary]) -> None:
        state_index = {summary.number: summary for summary in summaries}
        conflict_map: Dict[int, Dict[int, List[str]]] = {
            summary.number: {} for summary in summaries
        }
        file_to_prs: Dict[str, List[int]] = {}
        for summary in summaries:
            for filename in summary.files:
                file_to_prs.setdefault(filename, []).append(summary.number)
        for filename, prs in file_to_prs.items():
            if len(prs) <= 1:
                continue
            for pr in prs:
                for other in prs:
                    if pr == other:
                        continue
                    conflict_map[pr].setdefault(other, []).append(filename)
        for summary in summaries:
            summary.conflicts = {
                other: sorted(set(files))
                for other, files in conflict_map[summary.number].items()
            }
        for summary in summaries:
            summary.recommended_action = self._recommend_action(summary, state_index)

    # -------------------- Analysis helpers --------------------
    def _detect_tests(self, filenames: Sequence[str]) -> bool:
        patterns = [
            r"(^|/)tests?/",
            r"(^|/)tests?_.+",
            r"(^|/)test_.+",
            r"_test\.",
        ]
        for filename in filenames:
            lower = filename.lower()
            if any(re.search(pattern, lower) for pattern in patterns):
                return True
        return False

    def _extract_dependencies(self, text: str) -> List[int]:
        patterns = [
            r"depends on\s+#(\d+)",
            r"blocked by\s+#(\d+)",
            r"requires\s+#(\d+)",
            r"https://github\.com/[\w-]+/[\w-]+/pull/(\d+)",
        ]
        dependencies: List[int] = []
        lower_text = text.lower()
        for pattern in patterns:
            for match in re.finditer(pattern, lower_text, flags=re.IGNORECASE):
                try:
                    number = int(match.group(1))
                except ValueError:
                    continue
                if number not in dependencies:
                    dependencies.append(number)
        return dependencies

    def _assess_risk(self, summary: PullRequestSummary) -> Tuple[str, List[str]]:
        label_mapping = {
            "risk: critical": "Critical",
            "risk: high": "High",
            "risk: medium": "Medium",
            "risk: low": "Low",
            "critical": "Critical",
        }
        reasons: List[str] = []
        detected_label: Optional[str] = None
        for label in summary.labels:
            lower_label = label.lower()
            if lower_label in label_mapping:
                detected_label = label_mapping[lower_label]
                reasons.append(f"Label '{label}'")
                break
        if summary.change_requests:
            reasons.append(
                f"{summary.change_requests} change request(s) pending review resolution"
            )
            return "High", reasons
        if summary.mergeable_state and summary.mergeable_state in {"dirty", "blocked"}:
            reasons.append(f"Mergeable state is '{summary.mergeable_state}'")
            return "High", reasons
        if detected_label:
            return detected_label, reasons

        size = summary.additions_plus_deletions
        files = summary.changed_files
        if size >= 4000 or files >= 60:
            reasons.append("Large change set (>=4000 lines or >=60 files)")
            return "Critical", reasons
        if size >= 2000 or files >= 40:
            reasons.append("Significant change set (>=2000 lines or >=40 files)")
            return "High", reasons
        if size >= 800 or files >= 20:
            reasons.append("Moderate change set (>=800 lines or >=20 files)")
            return "Medium", reasons
        reasons.append("Small change set")
        return "Low", reasons

    def _determine_priority(self, summary: PullRequestSummary) -> Tuple[str, List[str]]:
        priority_mapping = {
            "p0": "Critical",
            "p1": "High",
            "p2": "Medium",
            "p3": "Low",
            "priority: critical": "Critical",
            "priority: high": "High",
            "priority: medium": "Medium",
            "priority: low": "Low",
            "urgent": "High",
        }
        reasons: List[str] = []
        for label in summary.labels:
            lower_label = label.lower()
            if lower_label in priority_mapping:
                priority = priority_mapping[lower_label]
                reasons.append(f"Label '{label}'")
                return priority, reasons
        if summary.change_requests:
            reasons.append("Outstanding change requests")
            return "High", reasons
        if summary.draft:
            reasons.append("Draft PR – treat as low priority")
            return "Low", reasons
        if summary.approvals and summary.mergeable_state == "clean":
            reasons.append(
                f"{summary.approvals} approval(s) and mergeable – ready to prioritize merge"
            )
            return "High", reasons
        if summary.risk_level in {"Critical", "High"}:
            reasons.append("High risk change")
            return "High", reasons
        reasons.append("Default priority")
        return "Medium", reasons

    def _recommend_action(
        self, summary: PullRequestSummary, index: Dict[int, PullRequestSummary]
    ) -> str:
        if summary.merged:
            return "✅ Already merged"
        if summary.state.lower() == "closed":
            return "⚠️ Closed without merge"
        if summary.draft:
            return "✏️ Draft – continue updates"

        if summary.change_requests:
            return "🛠️ Fix change requests"
        if summary.mergeable_state in {"dirty", "blocked"}:
            return "🧹 Resolve merge conflicts"
        if summary.mergeable_state == "behind":
            return "🔄 Update branch"

        unresolved = [
            dep
            for dep in summary.dependencies
            if dep in index and index[dep].is_open
        ]
        if unresolved:
            joined = ", ".join(f"#{dep}" for dep in unresolved)
            return f"⏳ Waiting on {joined}"

        if summary.approvals and summary.mergeable_state == "clean":
            return "🚢 Merge after checks"
        if summary.risk_level in {"Critical", "High"}:
            return "🔍 Schedule deep review"
        if summary.priority in {"High", "Critical"}:
            return "🚀 Prioritize review"
        return "✅ Ready for standard review"

    # -------------------- Rendering helpers --------------------
    def _render_summary_table(self, summaries: Sequence[PullRequestSummary]) -> str:
        header = "| PR | Title | State | Risk | Priority | Action |"
        separator = "|----|-------|--------|------|----------|--------|"
        rows = [header, separator]
        for summary in summaries:
            title = summary.title.replace("|", "\\|")
            action = summary.recommended_action.replace("|", "\\|")
            rows.append(
                f"| #{summary.number} | {title} | {summary.state.title()} | "
                f"{summary.risk_level} | {summary.priority} | {action} |"
            )
        return "\n".join(rows)

    def _render_review_signals(self, summaries: Sequence[PullRequestSummary]) -> str:
        header = "| PR | Approvals | Change Requests | Mergeable | Tests? |"
        separator = "|----|-----------|-----------------|-----------|--------|"
        rows = ["### Review Signals", "", header, separator]
        for summary in summaries:
            mergeable = summary.mergeable_state or "unknown"
            tests = "✅" if summary.tests_touched else "—"
            rows.append(
                f"| #{summary.number} | {summary.approvals} | {summary.change_requests} | "
                f"{mergeable} | {tests} |"
            )
        return "\n".join(rows)

    def _render_dependency_map(self, summaries: Sequence[PullRequestSummary]) -> str:
        lines = ["### Dependency Map", ""]
        for summary in summaries:
            if summary.dependencies:
                deps = ", ".join(f"#{dep}" for dep in summary.dependencies)
                lines.append(f"- PR #{summary.number} depends on {deps}")
            else:
                lines.append(f"- PR #{summary.number} has no listed dependencies")
        return "\n".join(lines)

    def _render_recommended_order(self, summaries: Sequence[PullRequestSummary]) -> str:
        order = self._compute_order(summaries)
        lines = ["### Recommended Review/Merge Order", ""]
        for position, summary in enumerate(order, start=1):
            lines.append(
                f"{position}. PR #{summary.number} – {summary.title}"
                f" (Risk: {summary.risk_level}, Priority: {summary.priority})"
            )
        return "\n".join(lines)

    def _render_conflict_matrix(self, summaries: Sequence[PullRequestSummary]) -> str:
        lines = ["### Conflict Hotspots", ""]
        conflicts_found = False
        for summary in summaries:
            if not summary.conflicts:
                continue
            conflicts_found = True
            lines.append(f"- PR #{summary.number} overlaps with:")
            for other, files in sorted(summary.conflicts.items()):
                file_list = ", ".join(files[:5])
                if len(files) > 5:
                    file_list += ", …"
                lines.append(f"  - PR #{other}: {file_list}")
        if not conflicts_found:
            lines.append("- No overlapping files detected")
        return "\n".join(lines)

    def _render_detailed_notes(self, summaries: Sequence[PullRequestSummary]) -> str:
        lines = ["### Detailed Notes", ""]
        for summary in summaries:
            lines.append(f"#### PR #{summary.number}: {summary.title}")
            lines.append("- **URL**: " + summary.url)
            lines.append(
                "- **State**: "
                f"{summary.state.title()} (Draft: {str(summary.draft).lower()}, Merged: {str(summary.merged).lower()})"
            )
            lines.append(
                "- **Branches**: "
                f"{summary.head_branch or 'unknown'} → {summary.base_branch or 'unknown'}"
            )
            lines.append(
                "- **Change Size**: "
                f"{summary.additions} additions / {summary.deletions} deletions / {summary.changed_files} files"
            )
            if summary.tests_touched:
                lines.append("- **Tests**: ✅ Tests updated")
            else:
                lines.append("- **Tests**: —")
            lines.append("- **Labels**: " + (", ".join(summary.labels) or "(none)"))
            lines.append(
                "- **Risk**: "
                f"{summary.risk_level} – {', '.join(summary.risk_reasons) or 'n/a'}"
            )
            lines.append(
                "- **Priority**: "
                f"{summary.priority} – {', '.join(summary.priority_reasons) or 'n/a'}"
            )
            lines.append("- **Recommended Action**: " + summary.recommended_action)
            if summary.dependencies:
                lines.append(
                    "- **Dependencies**: "
                    + ", ".join(f"#{dep}" for dep in summary.dependencies)
                )
            if summary.review_decision:
                lines.append("- **Review Decision**: " + summary.review_decision)
            if summary.approvals or summary.change_requests:
                lines.append(
                    "- **Reviews**: "
                    f"{summary.approvals} approvals, {summary.change_requests} change requests"
                )
            if summary.reviewers_blocking:
                joined = ", ".join(sorted(summary.reviewers_blocking))
                lines.append("- **Blocking Reviewers**: " + joined)
            if summary.mergeable_state:
                lines.append("- **Mergeable State**: " + summary.mergeable_state)
            if summary.conflicts:
                conflict_lines = []
                for other, files in sorted(summary.conflicts.items()):
                    conflict_lines.append(f"#{other} ({len(files)} files)")
                lines.append("- **Conflicts**: " + ", ".join(conflict_lines))
            if summary.body:
                snippet = self._summarize_body(summary.body)
                if snippet:
                    lines.append("- **Summary**: " + snippet)
            lines.append("")
        return "\n".join(lines).rstrip()

    def _summarize_body(self, body: str) -> str:
        cleaned = re.sub(r"`[^`]*`", "", body)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        if not cleaned:
            return ""
        return (cleaned[:180] + "…") if len(cleaned) > 200 else cleaned

    def _compute_order(
        self, summaries: Sequence[PullRequestSummary]
    ) -> List[PullRequestSummary]:
        numbers = {summary.number for summary in summaries}
        dependents: Dict[int, List[int]] = {summary.number: [] for summary in summaries}
        indegree: Dict[int, int] = {}

        for summary in summaries:
            deps = [dep for dep in summary.dependencies if dep in numbers]
            indegree[summary.number] = len(deps)
            for dep in deps:
                dependents.setdefault(dep, []).append(summary.number)

        queue: deque[int] = deque(
            sorted(
                [num for num, degree in indegree.items() if degree == 0],
                key=lambda num: self._sort_key(self._find_summary(num, summaries)),
                reverse=True,
            )
        )
        ordered: List[PullRequestSummary] = []
        indegree_copy = indegree.copy()

        while queue:
            current = queue.popleft()
            summary = self._find_summary(current, summaries)
            ordered.append(summary)
            for dependent in dependents.get(current, []):
                indegree_copy[dependent] -= 1
                if indegree_copy[dependent] == 0:
                    queue.append(dependent)
                    queue = deque(
                        sorted(
                            list(queue),
                            key=lambda num: self._sort_key(
                                self._find_summary(num, summaries)
                            ),
                            reverse=True,
                        )
                    )

        remaining = [s for s in summaries if s not in ordered]
        remaining.sort(key=self._sort_key, reverse=True)
        ordered.extend(remaining)
        return ordered

    def _sort_key(self, summary: PullRequestSummary) -> Tuple[int, int, int]:
        priority_rank = {"Critical": 3, "High": 2, "Medium": 1, "Low": 0}
        risk_rank = {"Critical": 3, "High": 2, "Medium": 1, "Low": 0}
        state_rank = 1 if summary.is_open else 0
        return (
            priority_rank.get(summary.priority, 1),
            risk_rank.get(summary.risk_level, 1),
            state_rank,
        )

    def _find_summary(
        self, number: int, summaries: Sequence[PullRequestSummary]
    ) -> PullRequestSummary:
        for summary in summaries:
            if summary.number == number:
                return summary
        raise ValueError(f"Unknown pull request #{number}")


def load_json_file(path: str) -> Sequence[dict]:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        raise SystemExit(f"Input file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare GitHub pull requests and generate review recommendations."
    )
    parser.add_argument(
        "numbers",
        metavar="PR",
        type=int,
        nargs="*",
        help="Pull request numbers to compare (requires --repo)",
    )
    parser.add_argument(
        "--repo",
        help="GitHub repository in 'owner/name' format for live API fetching.",
    )
    parser.add_argument(
        "--token",
        help="GitHub token (falls back to GITHUB_TOKEN or GH_TOKEN environment variables).",
    )
    parser.add_argument(
        "--input",
        help="Path to JSON file containing pull request data for offline analysis.",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json", "text"],
        default="markdown",
        help="Output format (default: markdown).",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_arguments(argv)
    comparator = PullRequestComparator(repo=args.repo, token=args.token)

    if args.input:
        data = load_json_file(args.input)
        summaries = comparator.load_from_json(data)
    else:
        if not args.repo or not args.numbers:
            raise SystemExit("Provide --repo and at least one pull request number, or use --input.")
        summaries = comparator.fetch(args.numbers)

    if args.format == "json":
        print(
            json.dumps(
                [asdict(summary) for summary in summaries],
                indent=2,
                ensure_ascii=False,
            )
        )
    elif args.format == "text":
        print(comparator.render_text(summaries))
    else:
        print(comparator.render_markdown(summaries))
    return 0


if __name__ == "__main__":
    sys.exit(main())
