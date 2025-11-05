"""
ActivityLog model - immutable (no updated_at)
"""
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime, text
from sqlalchemy.dialects.postgresql import UUID


class ActivityLog(SQLModel, table=True):
    """ActivityLog model - immutable, no updated_at field"""
    __tablename__ = "activity_logs"
    
    id: Optional[str] = Field(default=None, sa_column=Column(UUID(as_uuid=False), primary_key=True))
    project_id: str = Field(foreign_key="projects.id", index=True, nullable=False)
    owner_id: str = Field(foreign_key="users.id", index=True, nullable=False)  # Multi-tenancy key
    action: str = Field(nullable=False)  # created, updated, deleted, etc.
    entity_type: str = Field(nullable=False)  # task, client, project, etc.
    entity_id: Optional[str] = Field(default=None)  # ID of the entity
    description: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=text("now()"))
    )
    # Note: No updated_at field - logs are immutable

