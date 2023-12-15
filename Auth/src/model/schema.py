from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    user_id: str
    password: str


class UserCreate(UserBase):
    location: str


class User(UserBase):
    id: UUID4

    class Config:
        orm_mode = True
