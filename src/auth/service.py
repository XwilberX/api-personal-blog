
from sqlalchemy.orm import Session

from src.auth.models import User


def create_user(db: Session, user):
    db_user = User(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.as_dict_full
