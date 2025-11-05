"""
User model - matches Supabase auth.users structure
Note: In Supabase, auth.users table already exists. This model is for reference/extension.
"""
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID


class User(SQLModel, table=True):
    """User model matching Supabase auth.users structure"""
    __tablename__ = "users"
    
    id: Optional[str] = Field(
        default=None,
        sa_column=Column(UUID(as_uuid=False), primary_key=True)
    )
    email: str = Field(unique=True, index=True, nullable=False)
    full_name: Optional[str] = Field(default=None)
    avatar_url: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=text("now()"))
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=text("now()"))
    )

