from datetime import timedelta, datetime
from jose import JWTError, jwt
from passlib.context import CryptContext

from core.logger import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = 'super_secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plan_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plan_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
       Generate a JWT access token
       - data: dict containing payload (e.g. {"sub": user_id})
       - expires_delta: optional expiry override
    """

    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_access_token(token: str):
    """
        Decode and verify JWT token
        - raises JWTError if invalid/expired
    """
    try:
        pay_load = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return pay_load
    except JWTError as e:
        logger.error(f'Exception Raised : {str(e)}')
        return None