from sqlalchemy.orm import Session
from database.models.user import User
from schemas.user import UserCreate, UserResponse

def create_user(db: Session, user: UserCreate):
    pass