# Python imports

# Libraries imports
from sqlalchemy.orm import Session

# Project imports
from src.core.repository import SQLAlchemyRepository
from src.blogs.models import Blog


class BlogRepository(SQLAlchemyRepository[Blog]):
    def __init__(self, session: Session):
        super().__init__(session, Blog)

    def get_by_title(self, title: str) -> Blog:
        return self.session.query(Blog).filter(Blog.title == title).first()