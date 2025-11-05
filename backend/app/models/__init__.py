"""
Import all models for Alembic autogenerate support
"""
from app.models.user import User
from app.models.client import Client
from app.models.project import Project
from app.models.task import Task
from app.models.time_entry import TimeEntry
from app.models.activity_log import ActivityLog

__all__ = [
    "User",
    "Client",
    "Project",
    "Task",
    "TimeEntry",
    "ActivityLog",
]

