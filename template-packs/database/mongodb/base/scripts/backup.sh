#!/bin/bash

# MongoDB Backup Script
# Usage: ./backup.sh [database_name]

set -e

# Load environment variables
if [ -f ../.env ]; then
    export $(cat ../.env | grep -v '^#' | xargs)
fi

# Configuration
DB_NAME=${1:-$MONGO_DATABASE}
BACKUP_DIR="./backup"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="${DB_NAME}_backup_${TIMESTAMP}"
CONTAINER_NAME="${PROJECT_NAME}_mongodb"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "🔵 Starting MongoDB backup..."

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Check if container is running
if ! docker ps | grep -q "$CONTAINER_NAME"; then
    echo -e "${RED}❌ MongoDB container '$CONTAINER_NAME' is not running${NC}"
    exit 1
fi

# Perform backup
echo "📦 Backing up database: $DB_NAME"

if docker exec "$CONTAINER_NAME" mongodump \
    --username="$MONGO_USERNAME" \
    --password="$MONGO_PASSWORD" \
    --authenticationDatabase=admin \
    --db="$DB_NAME" \
    --archive="/backup/${BACKUP_NAME}.gz" \
    --gzip; then
    
    echo -e "${GREEN}✅ Backup completed successfully${NC}"
    echo "📍 Backup location: $BACKUP_DIR/${BACKUP_NAME}.gz"
    
    # List backup files
    echo -e "\n📋 Available backups:"
    ls -lh "$BACKUP_DIR"/*.gz 2>/dev/null || echo "No backups found"
    
    # Optional: Remove old backups (keep last 7 days)
    if [ "$REMOVE_OLD_BACKUPS" = "true" ]; then
        echo -e "\n🗑️  Removing backups older than 7 days..."
        find "$BACKUP_DIR" -name "*.gz" -mtime +7 -delete
    fi
else
    echo -e "${RED}❌ Backup failed${NC}"
    exit 1
fi

# Optional: Upload to cloud storage
if [ -n "$BACKUP_S3_BUCKET" ]; then
    echo -e "\n☁️  Uploading to S3..."
    aws s3 cp "$BACKUP_DIR/${BACKUP_NAME}.gz" "s3://$BACKUP_S3_BUCKET/mongodb-backups/${BACKUP_NAME}.gz"
    echo -e "${GREEN}✅ Uploaded to S3${NC}"
fi

echo -e "\n🎉 MongoDB backup process completed!"