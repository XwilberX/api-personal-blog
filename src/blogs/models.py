# Python imports

# Libraries imports
from sqlalchemy import orm

# Project imports
from src.core.models import BaseTimestampedModel


class Blog(BaseTimestampedModel):
    __tablename__ = "blogs"
    __table_args__ = {"comment": "Stores blog information"}

    title: orm.Mapped[str] = orm.mapped_column(nullable=False)
    description: orm.Mapped[str] = orm.mapped_column(nullable=False)
    content: orm.Mapped[str] = orm.mapped_column(nullable=False)
