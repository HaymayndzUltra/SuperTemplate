#!/bin/bash

# Protocol Renumbering Reference Update Script
# Updates @apply handoff references to new filenames

echo "🔄 Updating @apply handoff references..."

# Update @apply references systematically
sed -i 's|@apply \.cursor/ai-driven-workflow/00a-client-proposal-generation\.md|@apply .cursor/ai-driven-workflow/01-client-proposal-generation.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/00B-client-discovery-initiation\.md|@apply .cursor/ai-driven-workflow/02-client-discovery-initiation.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/01-project-brief-creation\.md|@apply .cursor/ai-driven-workflow/03-project-brief-creation.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/00-project-bootstrap-and-context-engineering\.md|@apply .cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/0-bootstrap-your-project\.md|@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/1-create-prd\.md|@apply .cursor/ai-driven-workflow/06-create-prd.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/6-technical-design-architecture\.md|@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/2-generate-tasks\.md|@apply .cursor/ai-driven-workflow/08-generate-tasks.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/7-environment-setup-validation\.md|@apply .cursor/ai-driven-workflow/09-environment-setup-validation.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/3-process-tasks\.md|@apply .cursor/ai-driven-workflow/10-process-tasks.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/9-integration-testing\.md|@apply .cursor/ai-driven-workflow/11-integration-testing.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/4-quality-audit\.md|@apply .cursor/ai-driven-workflow/12-quality-audit.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/15-uat-coordination\.md|@apply .cursor/ai-driven-workflow/13-uat-coordination.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/10-pre-deployment-staging\.md|@apply .cursor/ai-driven-workflow/14-pre-deployment-staging.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/11-production-deployment\.md|@apply .cursor/ai-driven-workflow/15-production-deployment.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/12-monitoring-observability\.md|@apply .cursor/ai-driven-workflow/16-monitoring-observability.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/13-incident-response-rollback\.md|@apply .cursor/ai-driven-workflow/17-incident-response-rollback.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/14-performance-optimization\.md|@apply .cursor/ai-driven-workflow/18-performance-optimization.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/16-documentation-knowledge-transfer\.md|@apply .cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/17-project-closure\.md|@apply .cursor/ai-driven-workflow/20-project-closure.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/18-maintenance-support\.md|@apply .cursor/ai-driven-workflow/21-maintenance-support.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/5-implementation-retrospective\.md|@apply .cursor/ai-driven-workflow/22-implementation-retrospective.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/8-script-governance-protocol\.md|@apply .cursor/ai-driven-workflow/23-script-governance-protocol.md|g' *
sed -i 's|@apply \.cursor/ai-driven-workflow/00-client-discovery\.md|@apply .cursor/ai-driven-workflow/24-client-discovery.md|g' *

echo "✅ @apply handoff references updated!"
echo "🔍 Verifying updates..."
grep -r "@apply" . | head -5
