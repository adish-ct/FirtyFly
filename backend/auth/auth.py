from sqlalchemy.orm import Session

from core.security import hash_password
from database.models.user import User
from schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    # check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise ValueError("Email already registered.")

    # Creating instance for User model based on the input.
    db_user = User(
        username=user.username,
        email=user.email,
        phone=user.phone,
        hashed_password=hash_password(user.password)
    )

    db.add(db_user) # adding user to db
    db.commit() # commiting the changes
    db.refresh(db_user) # after commiting refreshing the db result.
    return db_user

