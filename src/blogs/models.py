# Python imports
from typing import TYPE_CHECKING

# Libraries imports
from sqlalchemy import orm, ForeignKey
from sqlalchemy.dialects.sqlite import TEXT

# Project imports
from src.core.models import BaseTimestampedModel

if TYPE_CHECKING:
    from src.auth.models import User


class Blog(BaseTimestampedModel):
    __tablename__ = "blogs"
    __table_args__ = {"comment": "Stores blog information"}

    title: orm.Mapped[str] = orm.mapped_column(nullable=False)
    description: orm.Mapped[str] = orm.mapped_column(nullable=False)
    content: orm.Mapped[str] = orm.mapped_column(nullable=False, type_=TEXT)
    author_id: orm.Mapped[str] = orm.mapped_column(
        ForeignKey("users.pk"), nullable=False
    )

    author: orm.Mapped["User"] = orm.relationship("User", back_populates="blogs")

    def __repr__(self):
        return f"<Blog {self.title}> - {self.author.username}"
    
    @property
    def as_dict_full_author(self) -> dict:
        return {
            "blog": {
                c.key: getattr(self, c.key)
                for c in self.__table__.columns
                if c.key not in ("author_id")
            },
            "author": self.author.as_dict_for_blog,
        }