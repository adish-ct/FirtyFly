from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from database.database import Base
from database.models.base import TimeStampMixin

class User(Base, TimeStampMixin):
    __tablename__  = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)
    bio = Column(String, default="Hey! I'm new here 😎")
    hashed_password = Column(String, nullable=True)

    # account status
    is_verified = Column(Boolean, default=False)
    active_account = Column(Boolean, default=True)
    active_now = Column(Boolean, default=False)
    last_login = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

