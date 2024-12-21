# Python imports
import uuid
from typing import Optional

# Libraries imports
from sqlalchemy.orm import Session

# Project imports
from src.blogs.models import Blog
from src.blogs.repository import BlogRepository


class BlogService:
    def __init__(self, session: Session):
        self.repository = BlogRepository(session)

    def add(self, blog: Blog) -> Blog:
        return self.repository.add(blog)
    
    def get(self, pk: uuid.UUID) -> Optional[Blog]:
        return self.repository.get(pk)
    
    def get_all(self) -> list[Blog]:
        return self.repository.get_all()
    
    def update(self, blog: Blog) -> Blog:
        return self.repository.update(blog)
    
    def delete(self, blog: Blog) -> None:
        return self.repository.delete(blog)
