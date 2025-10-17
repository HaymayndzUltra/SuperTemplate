#!/bin/bash

# MongoDB Backup Script
# This script creates a backup of the MongoDB database

set -e

# Configuration
BACKUP_DIR="/backup"
DB_NAME="${DB_NAME:-appdb}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="mongodb_backup_${DB_NAME}_${TIMESTAMP}"

echo "Starting MongoDB backup..."

# Create backup directory if it doesn't exist
mkdir -p "${BACKUP_DIR}"

# Create backup
echo "Creating backup: ${BACKUP_FILE}"
docker exec mongodb mongodump \
  --db "${DB_NAME}" \
  --out "${BACKUP_DIR}/${BACKUP_FILE}"

# Compress backup
echo "Compressing backup..."
docker exec mongodb tar -czf "${BACKUP_DIR}/${BACKUP_FILE}.tar.gz" -C "${BACKUP_DIR}" "${BACKUP_FILE}"

# Remove uncompressed backup
docker exec mongodb rm -rf "${BACKUP_DIR}/${BACKUP_FILE}"

echo "Backup completed: ${BACKUP_FILE}.tar.gz"
echo "Backup size: $(docker exec mongodb du -h "${BACKUP_DIR}/${BACKUP_FILE}.tar.gz" | cut -f1)"

# Keep only last 7 days of backups
echo "Cleaning old backups..."
docker exec mongodb find "${BACKUP_DIR}" -name "mongodb_backup_*.tar.gz" -mtime +7 -delete

echo "Backup process completed successfully!"
