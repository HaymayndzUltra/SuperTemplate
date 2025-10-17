# {{PROJECT_NAME}} PostgreSQL Database

PostgreSQL database configuration for {{PROJECT_NAME}}.

## Quick Start

### Using Docker Compose

1. Start the database:

   ```bash
   docker-compose up -d
   ```

2. Access the database:

   ```bash
   # Using psql
   docker exec -it {{PROJECT_NAME}}_postgres psql -U postgres -d {{PROJECT_NAME}}

   # Using pgAdmin
   # Open http://localhost:5050
   # Email: admin@{{PROJECT_NAME}}.com
   # Password: admin
   ```

### Manual Setup

1. Install PostgreSQL 15+

2. Create database and user:

   ```sql
   CREATE DATABASE {{PROJECT_NAME}};
   CREATE USER {{PROJECT_NAME}}_user WITH ENCRYPTED PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE {{PROJECT_NAME}} TO {{PROJECT_NAME}}_user;
   ```

3. Run initialization script:

   ```bash
   psql -U postgres -d {{PROJECT_NAME}} -f init.sql
   ```

## Database Schema

### Core Tables

- **audit_log**: Tracks all database changes for compliance
- Industry-specific tables based on {{INDUSTRY}}

### Extensions Used

- **uuid-ossp**: For UUID generation
- **pgcrypto**: For encryption functions

## Backup and Restore

### Backup

```bash
# Full backup
docker exec {{PROJECT_NAME}}_postgres pg_dump -U postgres {{PROJECT_NAME}} > backup.sql

# Compressed backup
docker exec {{PROJECT_NAME}}_postgres pg_dump -U postgres -Fc {{PROJECT_NAME}} > backup.dump
```

### Restore

```bash
# From SQL file
docker exec -i {{PROJECT_NAME}}_postgres psql -U postgres {{PROJECT_NAME}} < backup.sql

# From compressed dump
docker exec -i {{PROJECT_NAME}}_postgres pg_restore -U postgres -d {{PROJECT_NAME}} < backup.dump
```

## Performance Tuning

### Recommended Settings (postgresql.conf)

```ini
# Memory
shared_buffers = 256MB
effective_cache_size = 1GB
work_mem = 4MB

# Connections
max_connections = 100

# WAL
wal_level = replica
max_wal_size = 1GB

# Query Planning
random_page_cost = 1.1  # For SSD storage
```

## Monitoring

### Useful Queries

```sql
-- Active connections
SELECT pid, usename, application_name, client_addr, state
FROM pg_stat_activity
WHERE state = 'active';

-- Database size
SELECT pg_database.datname,
       pg_size_pretty(pg_database_size(pg_database.datname)) AS size
FROM pg_database;

-- Table sizes
SELECT schemaname, tablename,
       pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Index usage
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes
ORDER BY idx_scan;
```

## Security

### Best Practices

1. Use strong passwords
2. Enable SSL/TLS connections
3. Restrict network access
4. Regular security updates
5. Enable logging for audit trail

### {{COMPLIANCE}} Compliance

Additional security measures for {{COMPLIANCE}}:

- Encryption at rest
- Audit logging enabled
- Access control implementation
- Regular backups
