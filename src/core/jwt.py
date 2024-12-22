# Python imports

# Libraries imports
import jwt

# Project imports
from config.config import settings


def create_access_token(data: dict) -> str:
    return jwt.encode(data, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> dict:
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
