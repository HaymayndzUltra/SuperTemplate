"""
Project model with client_id and owner_id
"""
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime, text
from sqlalchemy.dialects.postgresql import UUID


class Project(SQLModel, table=True):
    """Project model with client relationship and owner_id for multi-tenancy"""
    __tablename__ = "projects"
    
    id: Optional[str] = Field(default=None, sa_column=Column(UUID(as_uuid=False), primary_key=True))
    client_id: str = Field(foreign_key="clients.id", index=True, nullable=False)
    owner_id: str = Field(foreign_key="users.id", index=True, nullable=False)  # Multi-tenancy key
    name: str = Field(nullable=False)
    description: Optional[str] = Field(default=None)
    status: str = Field(default="active")  # active, completed, archived
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=text("now()"))
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=text("now()"))
    )

