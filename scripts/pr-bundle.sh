#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 4 ]]; then
  echo "Usage: scripts/pr-bundle.sh <PR1> <PR2> <PR3> <PR4>"
  exit 1
fi

# Clear proxy settings for GitHub API calls to avoid 403 errors
unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy NO_PROXY no_proxy
git config --global http.https://github.com.proxy ""
git config --global https.https://github.com.proxy ""

OWNER="${GITHUB_OWNER:-HaymayndzUltra}"
REPO="${GITHUB_REPO:-SuperTemplate}"

# Auth: gh uses stored login; if you insist on PAT, export GH_SUPERTEMPLATE or GH_TOKEN
if ! gh auth status >/dev/null 2>&1; then
  if [[ -n "${GH_SUPERTEMPLATE:-}" ]]; then
    echo "$GH_SUPERTEMPLATE" | gh auth login --with-token
  elif [[ -n "${GH_TOKEN:-}" ]]; then
    echo "$GH_TOKEN" | gh auth login --with-token
  elif [[ -n "${GITHUB_TOKEN:-}" ]]; then
    echo "$GITHUB_TOKEN" | gh auth login --with-token
  else
    echo "Please run: gh auth login  (or set GH_SUPERTEMPLATE)"
    exit 1
  fi
fi

mkdir -p pr_bundle
for pr in "$@"; do
  base="pr_bundle/PR_$pr"
  mkdir -p "$base"
  # PR metadata (includes title/body/mergeable_state)
  gh api "repos/$OWNER/$REPO/pulls/$pr" > "$base/meta.json"
  # PR comments/reviews (for context, not scoring)
  gh api "repos/$OWNER/$REPO/pulls/$pr/reviews" --paginate > "$base/reviews.json"
  # Per-file summary (filenames, additions/deletions)
  gh api "repos/$OWNER/$REPO/pulls/$pr/files" --paginate > "$base/files.json"
  # Full unified diff (exact patch)
  gh pr diff "$pr" --repo "$OWNER/$REPO" > "$base/diff.patch"
  # Raw PR body (easy to read)
  jq -r '.body // ""' "$base/meta.json" > "$base/body.md"
  # PR title
  jq -r '.title' "$base/meta.json" > "$base/title.txt"
done

echo "Bundle ready in ./pr_bundle"
