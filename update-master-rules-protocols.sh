#!/bin/bash

# Master Rules Protocol Filename Update Script
# Updates all protocol filename references to match new numbering (01-27)

echo "🔄 Updating master rules protocol filename references..."

cd .cursor/rules/master-rules

# Update protocol filename references systematically
sed -i 's|00-client-discovery\.md|24-client-discovery.md|g' *
sed -i 's|01-bootstrap-architecture\.md|05-bootstrap-your-project.md|g' *
sed -i 's|02-security-design\.md|07-technical-design-architecture.md|g' *
sed -i 's|03-database-schema\.md|07-technical-design-architecture.md|g' *
sed -i 's|04-api-contracts\.md|07-technical-design-architecture.md|g' *
sed -i 's|05-generate-tasks\.md|08-generate-tasks.md|g' *
sed -i 's|06-process-tasks\.md|10-process-tasks.md|g' *
sed -i 's|07-ci-cd-setup\.md|09-environment-setup-validation.md|g' *
sed -i 's|08-testing-strategy\.md|11-integration-testing.md|g' *
sed -i 's|09-quality-audit\.md|12-quality-audit.md|g' *
sed -i 's|10-deployment\.md|15-production-deployment.md|g' *
sed -i 's|11-monitoring\.md|16-monitoring-observability.md|g' *
sed -i 's|12-docs\.md|19-documentation-knowledge-transfer.md|g' *
sed -i 's|13-retrospective\.md|22-implementation-retrospective.md|g' *

# Update specific examples
sed -i 's|00-analyze-brief\.md|03-project-brief-creation.md|g' *
sed -i 's|01-design-ui-components\.md|07-technical-design-architecture.md|g' *
sed -i 's|02-implement-frontend\.md|10-process-tasks.md|g' *
sed -i 's|03-validate-accessibility\.md|12-quality-audit.md|g' *
sed -i 's|04-deploy-static\.md|15-production-deployment.md|g' *

sed -i 's|00-data-discovery\.md|02-client-discovery-initiation.md|g' *
sed -i 's|01-data-quality-assessment\.md|12-quality-audit.md|g' *
sed -i 's|02-dashboard-design\.md|07-technical-design-architecture.md|g' *
sed -i 's|03-etl-pipeline\.md|10-process-tasks.md|g' *
sed -i 's|04-visualization-implementation\.md|10-process-tasks.md|g' *
sed -i 's|05-user-acceptance-testing\.md|13-uat-coordination.md|g' *
sed -i 's|06-monitoring\.md|16-monitoring-observability.md|g' *
sed -i 's|07-docs\.md|19-documentation-knowledge-transfer.md|g' *
sed -i 's|08-retrospective\.md|22-implementation-retrospective.md|g' *

sed -i 's|07-security-validation\.md|12-quality-audit.md|g' *
sed -i 's|08-integration-testing\.md|11-integration-testing.md|g' *
sed -i 's|09-deployment-checklist\.md|14-pre-deployment-staging.md|g' *
sed -i 's|10-monitoring-setup\.md|16-monitoring-observability.md|g' *
sed -i 's|11-retrospective\.md|22-implementation-retrospective.md|g' *

# Update specific wrong references
sed -i 's|02-generate-tasks\.md|08-generate-tasks.md|g' *
sed -i 's|01-create-prd\.md|06-create-prd.md|g' *

echo "✅ Master rules protocol filename references updated!"
echo "🔍 Verifying updates..."
grep -r "[0-9][0-9]-[a-z-]*\.md" . | head -5
