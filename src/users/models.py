from sqlalchemy import Column, String, Integer, Boolean
from core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
