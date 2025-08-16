from sqlalchemy import Column, Table, Integer, ForeignKey
from database.database import Base

# Followers associated table
followers_association = Table(
    "followers",
    Base.metadata,
    Column("follower_id", Integer,
           ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("followed_id", Integer,
           ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
)