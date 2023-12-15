"""entry point
"""
import os
import hashlib
import jwt
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .model import crud, models, schema
from .model.db import session_local, engine
from .model.authclass import Result

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALOG = os.getenv("JWT_ALOG")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = None
    try:
        db = session_local()
        yield db
    finally:
        db.close()


@app.post("/signin")
def sign_in(user: schema.UserBase, db: Session = Depends(get_db)):
    """handler for signin
    if user_id and password(hashed) is match then return jwt and 200

    if not match then return 403

    Args:
        sign (SignIn): _description_
    """
    # hash it
    user_row = crud.get_user_by_user_id(db, user.user_id)
    if user_row is None:
        return Result("user not exist")
    hasher = hashlib.sha256()
    hasher.update(user.password)
    hashed_password = hasher.hexdigest()
    if hashed_password != user_row.password:
        return Result("password not matched")

    print(user_row.id)

    token: str = issue_jwt(user_id=user_row.id, location=user_row.location)
    return Result("ok", token=token)


@app.post("/signup")
def sign_up(user: schema.UserCreate, db: Session = Depends(get_db)):
    """handler sign up

    check user_id exists

    Args:
        sign (SignIn): _description_
    """
    user_row = crud.get_user_by_user_id(db, user.user_id)
    if user_row is not None:
        return Result("user exist")

    crud.create_user(db, user)

    return Result("ok")


def issue_jwt(user_id: str, location: str) -> str:
    """
    issue token

    Args:
        user_id (str): user uuid
        location (str): user location (KR or ENG)

    Returns:
        str: issued jwt
    """

    return jwt.encode(
        {
            "location": location,
            "https://hasura.io/jwt/claims": {
                "x-hasura-default-role": "user",
                "x-hasura-allowed-roles": ["user", "admin"],
                "x-hasura-user-id": user_id,
            },
        },
        key=JWT_SECRET,
        algorithm=JWT_ALOG,
    )
