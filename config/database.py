from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from config.config import settings

engine = create_engine(
    settings.TURSO_DATABASE_URI, connect_args={"check_same_thread": False}, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear sesión de base de datos
@contextmanager
def get_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()