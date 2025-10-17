"""
Initialize database with first superuser
"""
import logging

from app.config import settings
from app.database import SessionLocal
from app.crud import user as crud_user
from app.schemas.user import UserCreate
from app.database import engine
from app.models import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db() -> None:
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Create first superuser
    user = crud_user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            full_name="Admin User",
        )
        user = crud_user.create(db, obj_in=user_in)
        logger.info(f"Created superuser: {user.email}")
    else:
        logger.info(f"Superuser already exists: {user.email}")
    
    db.close()


if __name__ == "__main__":
    logger.info("Creating initial data")
    init_db()
    logger.info("Initial data created")