"""
Task model with project_id, owner_id, and assignee_id
"""
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime, text
from sqlalchemy.dialects.postgresql import UUID


class Task(SQLModel, table=True):
    """Task model with project relationship, owner_id, and assignee support"""
    __tablename__ = "tasks"
    
    id: Optional[str] = Field(default=None, sa_column=Column(UUID(as_uuid=False), primary_key=True))
    project_id: str = Field(foreign_key="projects.id", index=True, nullable=False)
    owner_id: str = Field(foreign_key="users.id", index=True, nullable=False)  # Multi-tenancy key
    assignee_id: Optional[str] = Field(foreign_key="users.id", default=None)  # Can be assigned to teammate
    name: str = Field(nullable=False)
    description: Optional[str] = Field(default=None)
    status: str = Field(default="backlog")  # backlog, in_progress, done
    due_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    is_billable: bool = Field(default=True)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=text("now()"))
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=text("now()"))
    )

