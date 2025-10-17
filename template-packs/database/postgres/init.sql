-- {{PROJECT_NAME}} Database Initialization

-- Create database if not exists (run as superuser)
-- CREATE DATABASE {{PROJECT_NAME}};

-- Connect to the database
\c {{PROJECT_NAME}};

-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Create schemas
CREATE SCHEMA IF NOT EXISTS app;

-- Set search path
SET search_path TO app, public;

-- Create base tables
CREATE TABLE IF NOT EXISTS app.audit_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    table_name VARCHAR(255) NOT NULL,
    record_id UUID NOT NULL,
    action VARCHAR(50) NOT NULL,
    user_id UUID,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    changes JSONB,
    ip_address INET,
    user_agent TEXT
);

-- Create indexes
CREATE INDEX idx_audit_log_table_name ON app.audit_log(table_name);
CREATE INDEX idx_audit_log_record_id ON app.audit_log(record_id);
CREATE INDEX idx_audit_log_timestamp ON app.audit_log(timestamp);
CREATE INDEX idx_audit_log_user_id ON app.audit_log(user_id);

-- Create audit trigger function
CREATE OR REPLACE FUNCTION app.audit_trigger_function()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO app.audit_log(table_name, record_id, action, changes)
        VALUES (TG_TABLE_NAME, NEW.id, TG_OP, to_jsonb(NEW));
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO app.audit_log(table_name, record_id, action, changes)
        VALUES (TG_TABLE_NAME, NEW.id, TG_OP, 
                jsonb_build_object('old', to_jsonb(OLD), 'new', to_jsonb(NEW)));
        RETURN NEW;
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO app.audit_log(table_name, record_id, action, changes)
        VALUES (TG_TABLE_NAME, OLD.id, TG_OP, to_jsonb(OLD));
        RETURN OLD;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Industry-specific configurations
-- {{INDUSTRY}} specific tables and configurations would go here

-- Grant permissions
GRANT USAGE ON SCHEMA app TO PUBLIC;
GRANT SELECT ON ALL TABLES IN SCHEMA app TO PUBLIC;

-- Comments
COMMENT ON SCHEMA app IS '{{PROJECT_NAME}} application schema';
COMMENT ON TABLE app.audit_log IS 'Audit trail for all database changes';

-- {{COMPLIANCE}} specific requirements
-- Add compliance-specific tables and constraints here