"""entry point
"""
import os
import jwt
from fastapi import FastAPI

from .model.authclass import SignUp, SignIn, Result

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALOG = os.getenv("JWT_ALOG")


app = FastAPI()


@app.post("/signin")
def sign_in(sign: SignIn):
    """handler for signin
    if user_id and password(hashed) is match then return jwt and 200

    if not match then return 403

    Args:
        sign (SignIn): _description_
    """
    # hash it
    user_id: str = ""
    location: str = ""
    token: str = issue_jwt(user_id=user_id, location=location)
    return Result("ok", token=token)


@app.post("/signup")
def sign_up(sign: SignUp):
    """handler sign up

    check user_id exists

    Args:
        sign (SignIn): _description_
    """
    pass
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
