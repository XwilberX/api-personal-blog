# Python imports
import uuid
from typing import Generic, TypeVar, Type, List, Optional

# Libraries imports
from sqlalchemy.orm import Session

# Project imports
from src.core.models import BaseTimestampedModel

ModelType = TypeVar("ModelType", bound=BaseTimestampedModel)


class SQLAlchemyRepository(Generic[ModelType]):
    """Generic repository for SQLAlchemy models"""

    def __init__(self, session: Session, model: Type[ModelType]):
        self.session = session
        self.model = model

    def add(self, entity: BaseTimestampedModel) -> BaseTimestampedModel:
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def get(self, pk: uuid.UUID) -> Optional[BaseTimestampedModel]:
        return self.session.query(self.model).get(pk)

    def get_all(self) -> List[BaseTimestampedModel]:
        return self.session.query(self.model).all()

    def update(
        self, pk: uuid.UUID, entity: BaseTimestampedModel
    ) -> BaseTimestampedModel:
        entity.pk = pk
        self.session.merge(entity)
        self.session.commit()
        return self.get(pk)

    def delete(self, entity: BaseTimestampedModel) -> None:
        self.session.delete(entity)
        self.session.commit()
        self.session.flush()
