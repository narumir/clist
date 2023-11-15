"""entry point
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_ADDR = os.getenv("POSTGRESQL_ADDR")

engine = create_engine(DB_ADDR)
session_local = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db = None
    try:
        db = session_local()
        yield db
    finally:
        db.close()
