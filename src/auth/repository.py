# Python imports

# Libraries imports
from sqlalchemy.orm import Session

# Project imports
from src.core.repository import SQLAlchemyRepository
from src.auth.models import User


class AuthUserRepository(SQLAlchemyRepository[User]):
    def __init__(self, session: Session):
        super().__init__(session, User)

    def get_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()
