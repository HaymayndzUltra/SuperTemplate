"""
Database configuration
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings
import os

# Fallback to SQLite for tests if DATABASE_URL is unset
db_url = settings.DATABASE_URL or os.environ.get('DATABASE_URL') or 'sqlite:///./test.db'
engine = create_engine(db_url, pool_pre_ping=True, connect_args={
    'check_same_thread': False
} if db_url.startswith('sqlite') else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()