"""
Database configuration and setup
"""
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")

# Create engine
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)


def get_session():
    """Dependency for FastAPI to get database session"""
    with Session(engine) as session:
        yield session


def init_db():
    """Initialize database by creating all tables"""
    SQLModel.metadata.create_all(engine)

