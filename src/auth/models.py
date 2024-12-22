# Python imports

# Library imports
from sqlalchemy import orm

# Project imports
from src.core.models import BaseTimestampedModel


class User(BaseTimestampedModel):
    __tablename__ = "users"
    __table_args__ = {"comment": "Stores user information"}

    first_name: orm.Mapped[str] = orm.mapped_column(nullable=False)
    middle_name: orm.Mapped[str] = orm.mapped_column(nullable=True)
    last_name: orm.Mapped[str] = orm.mapped_column(nullable=False)
    username: orm.Mapped[str] = orm.mapped_column(nullable=False)
    email: orm.Mapped[str] = orm.mapped_column(nullable=False, unique=True)
    password: orm.Mapped[str] = orm.mapped_column(nullable=False)
    is_admin: orm.Mapped[bool] = orm.mapped_column(nullable=False, default=False)
    picture_profile: orm.Mapped[str] = orm.mapped_column(nullable=True)

    def __repr__(self):
        return f"<User {self.full_name}> - {self.username}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    @property
    def as_dict_full(self) -> dict:
        return {
            c.key: getattr(self, c.key)
            for c in self.__table__.columns
            if c.key not in ("password")
        }

    @property
    def as_dict_full_str(self) -> dict:
        return "-".join(
            [
                str(getattr(self, c.key))
                for c in self.__table__.columns
                if c.key not in ("password")
            ]
        )
