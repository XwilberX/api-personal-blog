# Python imports
import uuid

# Libraries imports
from sqlalchemy.orm import Session

# Project imports
from src.auth.models import User
from src.auth.repository import AuthUserRepository
from src.core.hash import hash_password, verify_password
from src.core.jwt import create_access_token


class AuthUserService:
    def __init__(self, session: Session):
        self.repository = AuthUserRepository(session)

    def add(self, user: dict) -> User:
        user: User = User(**user)

        # verifiy existing user
        existing_user = self.repository.get_by_email(user.email)
        if existing_user:
            raise ValueError("User already exists")

        # encrypt password
        user.password = hash_password(user.password)

        return self.repository.add(user)
    
    def get(self, pk: str) -> User:
        pk = uuid.UUID(pk)
        return self.repository.get(pk)
    
    def get_all(self) -> list[User]:
        users = self.repository.get_all()
        return [user.as_dict_full for user in users]
    
    def update(self, pk: str, user: dict) -> User:
        pk = uuid.UUID(pk)
        user = User(**user)
        user = self.repository.update(pk, user)
        return user
    
    def delete(self, pk: str) -> None:
        pk = uuid.UUID(pk)
        user = self.repository.get(pk)
        return self.repository.delete(user)
    
    def login(self, data: dict) -> tuple[bool, User, str]:
        email = data.get("email", None)
        password = data.get("password", None)

        user = self.repository.get_by_email(email)
        if not user:
            return False, None, None
        
        if not verify_password(password, user.password):
            return False, None, None
        
        token = create_access_token({"id": str(user.pk)})
        return True, user, token