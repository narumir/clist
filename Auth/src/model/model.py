from sqlalchemy import Column, String, UUID
import uuid
from .db import Base


class Users(Base):
    __tablename__ = "Clist_user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String)
    password = Column(String)
    location = Column(String)
