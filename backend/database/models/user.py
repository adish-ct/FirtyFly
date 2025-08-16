from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from ..database import Base
from .followers import followers_association

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

    # Back relation-ships
    profile = relationship("Profile", back_populates="user", uselist=False)

    # followers/following many-to-many
    followers = relationship(
        "user",
        secondary=followers_association,
        primaryjoin=id == followers_association.c.followed_id,
        secondaryjoin=id == followers_association.c.follower_id,
        backref="following"
    )

