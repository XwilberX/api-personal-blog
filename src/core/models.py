# Python imports
import uuid
from datetime import datetime

# Libraries imports
from sqlalchemy import orm, func
from sqlalchemy import MetaData


naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=naming_convention)


class BaseTimestampedModel(orm.DeclarativeBase):
    """Base model for timestamped models."""

    metadata = metadata

    pk: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    created_at: orm.Mapped[datetime] = orm.mapped_column(
        default=func.now(),
        nullable=False,
    )

    updated_at: orm.Mapped[datetime] = orm.mapped_column(
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    @property
    def as_dict(self):
        return {
            c.key: getattr(self, c.key)
            for c in self.__table__.columns
            if c.key not in ("pk", "created_at", "updated_at")
        }

    @property
    def as_dict_full(self):
        return {c.key: getattr(self, c.key) for c in self.__table__.columns}

    @property
    def as_dict_full_str(self):
        return {c.key: str(getattr(self, c.key)) for c in self.__table__.columns}
