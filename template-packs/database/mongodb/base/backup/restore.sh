#!/bin/bash

# MongoDB Restore Script
# This script restores a MongoDB database from a backup

set -e

# Configuration
BACKUP_DIR="/backup"
DB_NAME="${DB_NAME:-appdb}"

# Check if backup file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <backup_file.tar.gz>"
    echo "Available backups:"
    docker exec mongodb ls -la "${BACKUP_DIR}/" | grep "mongodb_backup_.*\.tar\.gz" || echo "No backups found"
    exit 1
fi

BACKUP_FILE="$1"

# Check if backup file exists
if ! docker exec mongodb test -f "${BACKUP_DIR}/${BACKUP_FILE}"; then
    echo "Error: Backup file '${BACKUP_FILE}' not found in ${BACKUP_DIR}"
    echo "Available backups:"
    docker exec mongodb ls -la "${BACKUP_DIR}/" | grep "mongodb_backup_.*\.tar\.gz" || echo "No backups found"
    exit 1
fi

echo "Starting MongoDB restore from: ${BACKUP_FILE}"

# Extract backup
echo "Extracting backup..."
docker exec mongodb tar -xzf "${BACKUP_DIR}/${BACKUP_FILE}" -C "${BACKUP_DIR}"

# Get the extracted directory name
EXTRACTED_DIR=$(docker exec mongodb basename "${BACKUP_FILE}" .tar.gz)

# Drop existing database (optional - comment out if you want to keep existing data)
echo "Dropping existing database '${DB_NAME}'..."
docker exec mongodb mongosh --eval "db.getSiblingDB('${DB_NAME}').dropDatabase()" || echo "Database didn't exist or couldn't be dropped"

# Restore database
echo "Restoring database..."
docker exec mongodb mongorestore --db "${DB_NAME}" "${BACKUP_DIR}/${EXTRACTED_DIR}/${DB_NAME}"

# Clean up extracted directory
echo "Cleaning up..."
docker exec mongodb rm -rf "${BACKUP_DIR}/${EXTRACTED_DIR}"

echo "Restore completed successfully!"
echo "Database '${DB_NAME}' has been restored from ${BACKUP_FILE}"
