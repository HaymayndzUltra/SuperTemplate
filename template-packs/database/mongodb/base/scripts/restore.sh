#!/bin/bash

# MongoDB Restore Script
# Usage: ./restore.sh <backup_file> [database_name]

set -e

# Load environment variables
if [ -f ../.env ]; then
    export $(cat ../.env | grep -v '^#' | xargs)
fi

# Check if backup file is provided
if [ -z "$1" ]; then
    echo "❌ Error: Please provide a backup file"
    echo "Usage: ./restore.sh <backup_file> [database_name]"
    echo ""
    echo "Available backups:"
    ls -lh ./backup/*.gz 2>/dev/null || echo "No backups found"
    exit 1
fi

# Configuration
BACKUP_FILE="$1"
DB_NAME=${2:-$MONGO_DATABASE}
CONTAINER_NAME="${PROJECT_NAME}_mongodb"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🔵 Starting MongoDB restore..."

# Check if backup file exists
if [ ! -f "$BACKUP_FILE" ]; then
    echo -e "${RED}❌ Backup file not found: $BACKUP_FILE${NC}"
    exit 1
fi

# Check if container is running
if ! docker ps | grep -q "$CONTAINER_NAME"; then
    echo -e "${RED}❌ MongoDB container '$CONTAINER_NAME' is not running${NC}"
    exit 1
fi

# Warning
echo -e "${YELLOW}⚠️  WARNING: This will restore database '$DB_NAME' from backup${NC}"
echo -e "${YELLOW}   All existing data in '$DB_NAME' will be overwritten!${NC}"
echo ""
read -p "Are you sure you want to continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "❌ Restore cancelled"
    exit 0
fi

# Copy backup file to container
echo "📤 Copying backup file to container..."
docker cp "$BACKUP_FILE" "$CONTAINER_NAME:/tmp/restore.gz"

# Perform restore
echo "📥 Restoring database: $DB_NAME"

if docker exec "$CONTAINER_NAME" mongorestore \
    --username="$MONGO_USERNAME" \
    --password="$MONGO_PASSWORD" \
    --authenticationDatabase=admin \
    --nsInclude="${DB_NAME}.*" \
    --drop \
    --archive="/tmp/restore.gz" \
    --gzip; then
    
    echo -e "${GREEN}✅ Restore completed successfully${NC}"
    
    # Clean up
    docker exec "$CONTAINER_NAME" rm /tmp/restore.gz
    
    # Verify restore
    echo -e "\n📊 Verifying restore..."
    docker exec "$CONTAINER_NAME" mongosh \
        --username="$MONGO_USERNAME" \
        --password="$MONGO_PASSWORD" \
        --authenticationDatabase=admin \
        --eval "use $DB_NAME; db.getCollectionNames().forEach(function(c) { print(c + ': ' + db[c].countDocuments() + ' documents'); })"
else
    echo -e "${RED}❌ Restore failed${NC}"
    docker exec "$CONTAINER_NAME" rm -f /tmp/restore.gz
    exit 1
fi

echo -e "\n🎉 MongoDB restore completed successfully!"