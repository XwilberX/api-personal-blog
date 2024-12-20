from config.models import BaseTimestampedModel

from sqlalchemy import orm


class User(BaseTimestampedModel):
    __tablename__ = "users"
    __table_args__ = {'comment': 'Stores user information'}

    username: orm.Mapped[str] = orm.mapped_column(nullable=False)
    email: orm.Mapped[str] = orm.mapped_column(nullable=False)
    password: orm.Mapped[str] = orm.mapped_column(nullable=False)
    is_admin: orm.Mapped[bool] = orm.mapped_column(nullable=False, default=False)

