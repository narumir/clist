from sqlalchemy.orm import Session
from . import models, schema
import hashlib


def get_user_by_user_id(db: Session, user_id: str):
    return db.query(models.Users).filter(models.Users.user_id == user_id).first()


def create_user(db: Session, user: schema.UserCreate):
    hasher = hashlib.sha256()
    hasher.update(user.password.encode("utf-8"))
    hashed_password = hasher.hexdigest()
    db_user = models.Users(
        user_id=user.user_id, password=hashed_password, location=user.location
    )

    db.add(db_user)

    db.commit()
    db.refresh(db_user)
    return db_user
