#!/bin/bash

# Protocol Textual Mentions Update Script
# Updates "Protocol N" mentions to match new numbering

echo "🔄 Updating textual protocol mentions..."

# Update textual protocol mentions systematically
sed -i 's|Protocol 0\b|Protocol 05|g' *
sed -i 's|Protocol 00a\b|Protocol 01|g' *
sed -i 's|Protocol 00B\b|Protocol 02|g' *
sed -i 's|Protocol 01\b|Protocol 03|g' *
sed -i 's|Protocol 00\b|Protocol 04|g' *
sed -i 's|Protocol 1\b|Protocol 06|g' *
sed -i 's|Protocol 6\b|Protocol 07|g' *
sed -i 's|Protocol 2\b|Protocol 08|g' *
sed -i 's|Protocol 7\b|Protocol 09|g' *
sed -i 's|Protocol 3\b|Protocol 10|g' *
sed -i 's|Protocol 9\b|Protocol 11|g' *
sed -i 's|Protocol 4\b|Protocol 12|g' *
sed -i 's|Protocol 15\b|Protocol 13|g' *
sed -i 's|Protocol 10\b|Protocol 14|g' *
sed -i 's|Protocol 11\b|Protocol 15|g' *
sed -i 's|Protocol 12\b|Protocol 16|g' *
sed -i 's|Protocol 13\b|Protocol 17|g' *
sed -i 's|Protocol 14\b|Protocol 18|g' *
sed -i 's|Protocol 16\b|Protocol 19|g' *
sed -i 's|Protocol 17\b|Protocol 20|g' *
sed -i 's|Protocol 18\b|Protocol 21|g' *
sed -i 's|Protocol 5\b|Protocol 22|g' *
sed -i 's|Protocol 8\b|Protocol 23|g' *

echo "✅ Textual protocol mentions updated!"
echo "🔍 Verifying updates..."
grep -r "Protocol [0-9]" . | head -5
