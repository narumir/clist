from dataclasses import dataclass


@dataclass
class SignIn:
    user_id: str
    password: str


@dataclass
class SignUp(SignIn):
    location: str


@dataclass
class Result:
    msg: str
    token: str | None = None
