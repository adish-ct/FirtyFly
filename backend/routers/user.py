from fastapi import HTTPException, APIRouter, status, Depends
from sqlalchemy.orm import Session

from database.models.user import User
from migrations.versions.ecfacd72486e_profile_table_created import depends_on
from schemas.user import UserCreate, UserResponse
from database.database import get_db
from auth.auth import create_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db, user)
        return db_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
