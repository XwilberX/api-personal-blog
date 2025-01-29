# Python imports
import uuid
from typing import Optional

# Libraries imports
from sqlalchemy.orm import Session

# Project imports
from src.blogs.models import Blog
from src.blogs.repository import BlogRepository
from src.blogs.schemas import BlogFullAuthor


class BlogService:
    def __init__(self, session: Session):
        self.repository = BlogRepository(session)

    def add(self, blog: dict) -> Blog:
        author = blog.pop("author")
        blog["author_id"] = uuid.UUID(author["pk"])
        blog = Blog(**blog)

        blog_created = self.repository.add(blog)

        return blog_created

    def get(self, pk: str) -> Optional[Blog]:
        pk = uuid.UUID(pk)
        return self.repository.get(pk)

    def get_all(self) -> list[Blog]:
        blogs = self.repository.get_all()
        return [blog.as_dict_full for blog in blogs]

    def get_all_full_author(self) -> list[BlogFullAuthor]:
        blogs = self.repository.get_all()
        return [blog.as_dict_full_author for blog in blogs]

    def update(self, pk: str, blog: dict) -> Blog:
        pk = uuid.UUID(pk)
        blog = Blog(**blog)
        blog = self.repository.update(pk, blog)
        return blog

    def delete(self, pk: str) -> None:
        pk = uuid.UUID(pk)
        blog = self.repository.get(pk)
        return self.repository.delete(blog)
