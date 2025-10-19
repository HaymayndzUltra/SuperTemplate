# run_review.sh
set -euo pipefail
REPO="${REPO:-HaymayndzUltra/SuperTemplate}"   # set mo via env kung needed
FILE="${1:-.ai-review/prs.txt}"

mapfile -t PRS < <(grep -E '^[0-9]+$' "$FILE" | xargs -n1 echo)
if [ "${#PRS[@]}" -ne 4 ]; then
  echo "❌ Need EXACTLY 4 PR numbers in $FILE (one per line). Found: ${#PRS[@]}"
  exit 1
fi

echo "🔒 Locked PRs: ${PRS[*]}"
for n in "${PRS[@]}"; do
  gh pr view "$n" --repo "$REPO" >/dev/null || { echo "❌ PR #$n not found in $REPO"; exit 1; }
done

# Create pr-review directory if it doesn't exist
mkdir -p pr-review

# (dito mo tatawagin ang review script mo; sample:)
printf "%s\n" "${PRS[@]}" \
| xargs -I{} -P4 bash -lc '
  gh pr diff {} > pr-review/pr_{}.diff
  python3 review_pr.py {}
  gh pr comment {} -F pr-review/pr_{}.review.md
'