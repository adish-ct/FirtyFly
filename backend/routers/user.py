from fastapi import HTTPException, APIRouter, status, Depends
from sqlalchemy.orm import Session

from auth.auth import create_user
from database.database import get_db
from schemas.user import UserCreate, UserResponse
from core.logger import logger

# -----------------------
# Router
# -----------------------

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db, user)
        return db_user

    except ValueError as e:
        logger.warning(f"Value Error Raised : {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )

    except Exception as e:
        logger.error(f'Exception Raised : {str(e)}')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Some error occurred, please contact administrator."
        )
