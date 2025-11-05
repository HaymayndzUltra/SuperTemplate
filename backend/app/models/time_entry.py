"""
TimeEntry model - immutable (no updated_at)
"""
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime, Date, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Date as SQLDate


class TimeEntry(SQLModel, table=True):
    """TimeEntry model - immutable, no updated_at field"""
    __tablename__ = "time_entries"
    
    id: Optional[str] = Field(default=None, sa_column=Column(UUID(as_uuid=False), primary_key=True))
    task_id: str = Field(foreign_key="tasks.id", index=True, nullable=False)
    owner_id: str = Field(foreign_key="users.id", index=True, nullable=False)  # Multi-tenancy key
    date: Optional[str] = Field(sa_column=Column(SQLDate, nullable=False, index=True))  # Store as date string
    hours: int = Field(default=0)  # Hours component
    minutes: int = Field(default=0)  # Minutes component
    total_minutes: int = Field(nullable=False)  # Automatically calculated: hours * 60 + minutes
    description: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=text("now()"))
    )
    # Note: No updated_at field - entries are immutable

