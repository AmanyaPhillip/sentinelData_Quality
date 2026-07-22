import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.data.models import Base

# Default URL aligned with docker-compose environment variables
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://sentinel:sentinel_pass@localhost:5432/sentineldq_db"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Creates database tables if they do not exist."""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Dependency for providing database session to FastAPI routes."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
