#!/bin/bash

# Protocol Artifact Path Update Script
# Updates .artifacts/protocol-N/ references to match new numbering

echo "🔄 Updating artifact path references..."

# Update artifact path references systematically
sed -i 's|\.artifacts/protocol-0/|.artifacts/protocol-05/|g' *
sed -i 's|\.artifacts/protocol-00a/|.artifacts/protocol-01/|g' *
sed -i 's|\.artifacts/protocol-00B/|.artifacts/protocol-02/|g' *
sed -i 's|\.artifacts/protocol-01/|.artifacts/protocol-03/|g' *
sed -i 's|\.artifacts/protocol-00/|.artifacts/protocol-04/|g' *
sed -i 's|\.artifacts/protocol-1/|.artifacts/protocol-06/|g' *
sed -i 's|\.artifacts/protocol-6/|.artifacts/protocol-07/|g' *
sed -i 's|\.artifacts/protocol-2/|.artifacts/protocol-08/|g' *
sed -i 's|\.artifacts/protocol-7/|.artifacts/protocol-09/|g' *
sed -i 's|\.artifacts/protocol-3/|.artifacts/protocol-10/|g' *
sed -i 's|\.artifacts/protocol-9/|.artifacts/protocol-11/|g' *
sed -i 's|\.artifacts/protocol-4/|.artifacts/protocol-12/|g' *
sed -i 's|\.artifacts/protocol-15/|.artifacts/protocol-13/|g' *
sed -i 's|\.artifacts/protocol-10/|.artifacts/protocol-14/|g' *
sed -i 's|\.artifacts/protocol-11/|.artifacts/protocol-15/|g' *
sed -i 's|\.artifacts/protocol-12/|.artifacts/protocol-16/|g' *
sed -i 's|\.artifacts/protocol-13/|.artifacts/protocol-17/|g' *
sed -i 's|\.artifacts/protocol-14/|.artifacts/protocol-18/|g' *
sed -i 's|\.artifacts/protocol-16/|.artifacts/protocol-19/|g' *
sed -i 's|\.artifacts/protocol-17/|.artifacts/protocol-20/|g' *
sed -i 's|\.artifacts/protocol-18/|.artifacts/protocol-21/|g' *
sed -i 's|\.artifacts/protocol-5/|.artifacts/protocol-22/|g' *
sed -i 's|\.artifacts/protocol-8/|.artifacts/protocol-23/|g' *

echo "✅ Artifact path references updated!"
echo "🔍 Verifying updates..."
grep -r "\.artifacts/protocol-" . | head -5
