import uuid
from datetime import datetime

from sqlalchemy import orm, func


class BaseTimestampedModel(orm.DeclarativeBase):
    """Base model for timestamped models."""

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
