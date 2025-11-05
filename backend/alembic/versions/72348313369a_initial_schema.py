"""initial_schema

Revision ID: 72348313369a
Revises: 
Create Date: 2025-01-27 03:31:50.608118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSON


# revision identifiers, used by Alembic.
revision: str = '72348313369a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema - Create all tables, indexes, and RLS policies."""
    
    # Enable UUID extension if not already enabled
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    
    # Create users table (matches Supabase auth.users structure)
    op.create_table(
        'users',
        sa.Column('id', UUID(as_uuid=False), primary_key=True),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('full_name', sa.String(), nullable=True),
        sa.Column('avatar_url', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    
    # Create clients table
    op.create_table(
        'clients',
        sa.Column('id', UUID(as_uuid=False), primary_key=True),
        sa.Column('owner_id', UUID(as_uuid=False), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('company', sa.String(), nullable=True),
        sa.Column('phone', sa.String(), nullable=True),
        sa.Column('billing_notes', sa.String(), nullable=True),
        sa.Column('running_notes', sa.String(), nullable=True),
        sa.Column('tags', JSON, nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('true')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    )
    op.create_index('ix_clients_owner_id', 'clients', ['owner_id'])
    
    # Create projects table
    op.create_table(
        'projects',
        sa.Column('id', UUID(as_uuid=False), primary_key=True),
        sa.Column('client_id', UUID(as_uuid=False), nullable=False),
        sa.Column('owner_id', UUID(as_uuid=False), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('status', sa.String(), nullable=False, server_default=sa.text("'active'")),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    )
    op.create_index('ix_projects_client_id', 'projects', ['client_id'])
    op.create_index('ix_projects_owner_id', 'projects', ['owner_id'])
    
    # Create tasks table
    op.create_table(
        'tasks',
        sa.Column('id', UUID(as_uuid=False), primary_key=True),
        sa.Column('project_id', UUID(as_uuid=False), nullable=False),
        sa.Column('owner_id', UUID(as_uuid=False), nullable=False),
        sa.Column('assignee_id', UUID(as_uuid=False), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('status', sa.String(), nullable=False, server_default=sa.text("'backlog'")),
        sa.Column('due_date', sa.DateTime(timezone=True), nullable=True),
        sa.Column('is_billable', sa.Boolean(), nullable=False, server_default=sa.text('true')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['assignee_id'], ['users.id'], ),
    )
    op.create_index('ix_tasks_project_id', 'tasks', ['project_id'])
    op.create_index('ix_tasks_owner_id', 'tasks', ['owner_id'])
    
    # Create time_entries table (immutable - no updated_at)
    op.create_table(
        'time_entries',
        sa.Column('id', UUID(as_uuid=False), primary_key=True),
        sa.Column('task_id', UUID(as_uuid=False), nullable=False),
        sa.Column('owner_id', UUID(as_uuid=False), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('hours', sa.Integer(), nullable=False, server_default=sa.text('0')),
        sa.Column('minutes', sa.Integer(), nullable=False, server_default=sa.text('0')),
        sa.Column('total_minutes', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    )
    op.create_index('ix_time_entries_task_id', 'time_entries', ['task_id'])
    op.create_index('ix_time_entries_date', 'time_entries', ['date'])
    
    # Create activity_logs table (immutable - no updated_at)
    op.create_table(
        'activity_logs',
        sa.Column('id', UUID(as_uuid=False), primary_key=True),
        sa.Column('project_id', UUID(as_uuid=False), nullable=False),
        sa.Column('owner_id', UUID(as_uuid=False), nullable=False),
        sa.Column('action', sa.String(), nullable=False),
        sa.Column('entity_type', sa.String(), nullable=False),
        sa.Column('entity_id', UUID(as_uuid=False), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    )
    op.create_index('ix_activity_logs_project_id', 'activity_logs', ['project_id'])
    
    # Enable Row Level Security (RLS) on all tables
    op.execute('ALTER TABLE clients ENABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE projects ENABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE tasks ENABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE time_entries ENABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE activity_logs ENABLE ROW LEVEL SECURITY')
    
    # Create RLS Policies for multi-tenancy isolation
    # Note: These policies use auth.uid() which is provided by Supabase Auth
    
    # Clients RLS Policy
    op.execute("""
        CREATE POLICY "users_own_clients" ON clients
        FOR ALL
        USING (owner_id = auth.uid())
    """)
    
    # Projects RLS Policy
    op.execute("""
        CREATE POLICY "users_own_projects" ON projects
        FOR ALL
        USING (owner_id = auth.uid())
    """)
    
    # Tasks RLS Policy
    op.execute("""
        CREATE POLICY "users_own_tasks" ON tasks
        FOR ALL
        USING (owner_id = auth.uid())
    """)
    
    # Time Entries RLS Policy
    op.execute("""
        CREATE POLICY "users_own_time_entries" ON time_entries
        FOR ALL
        USING (owner_id = auth.uid())
    """)
    
    # Activity Logs RLS Policy
    op.execute("""
        CREATE POLICY "users_own_activity_logs" ON activity_logs
        FOR ALL
        USING (owner_id = auth.uid())
    """)


def downgrade() -> None:
    """Downgrade schema - Drop all tables, indexes, and RLS policies."""
    
    # Drop RLS Policies
    op.execute('DROP POLICY IF EXISTS "users_own_clients" ON clients')
    op.execute('DROP POLICY IF EXISTS "users_own_projects" ON projects')
    op.execute('DROP POLICY IF EXISTS "users_own_tasks" ON tasks')
    op.execute('DROP POLICY IF EXISTS "users_own_time_entries" ON time_entries')
    op.execute('DROP POLICY IF EXISTS "users_own_activity_logs" ON activity_logs')
    
    # Disable RLS
    op.execute('ALTER TABLE activity_logs DISABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE time_entries DISABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE tasks DISABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE projects DISABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE clients DISABLE ROW LEVEL SECURITY')
    
    # Drop tables in reverse order (respecting foreign key constraints)
    op.drop_table('activity_logs')
    op.drop_table('time_entries')
    op.drop_table('tasks')
    op.drop_table('projects')
    op.drop_table('clients')
    op.drop_table('users')
