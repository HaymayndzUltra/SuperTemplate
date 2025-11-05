"""
Client model with owner_id for multi-tenancy
"""
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Column, DateTime, JSON, text
from sqlalchemy.dialects.postgresql import UUID


class Client(SQLModel, table=True):
    """Client model with owner_id for multi-tenancy"""
    __tablename__ = "clients"
    
    id: Optional[str] = Field(default=None, sa_column=Column(UUID(as_uuid=False), primary_key=True))
    owner_id: str = Field(foreign_key="users.id", index=True, nullable=False)  # Multi-tenancy key
    name: str = Field(nullable=False)
    email: Optional[str] = Field(default=None)
    company: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    billing_notes: Optional[str] = Field(default=None)
    running_notes: Optional[str] = Field(default=None)
    tags: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    is_active: bool = Field(default=True)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=text("now()"))
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=text("now()"))
    )

