import enum
from sqlalchemy import String, Integer, Column, ForeignKey, Enum, Date
from sqlalchemy.orm import relationship

from .base import TimeStampMixin
from database.database import Base


class GenderEnum(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'


class Profile(Base, TimeStampMixin):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, index=True)
    # Link to User table
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True)

    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    gender = Column(Enum(GenderEnum), nullable=False)
    date_of_birth = Column(Date, nullable=True) # YYYY-MM-DD format
    profile_pic = Column(String, nullable=True, default="Profile pic") # store URL or file path
    intrests = Column(String, nullable=True) # could store CSV or JSON string for now
    likes = Column(Integer, default=0)

    # Back relationship
    user = relationship("User", back_populates="profile")
