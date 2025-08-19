# Pydantic validation (for API inputs/outputs).
# This file defines how requests/responses should look.
from pydantic import BaseModel, EmailStr, ConfigDict

# ---------------------------
# Request schema (input) Register
# ---------------------------
class UserCreate(BaseModel):
    username: str
    email: EmailStr # validates format of email automatically
    phone: str
    password: str # plain password (will be hashed later)

# ---------------------------
# Response schema (output) Register
# ---------------------------
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone: str
    bio: str
    active_now: bool

    model_config = ConfigDict(from_attributes=True)

# ---------------------------
# Request schema (input) Login
# ---------------------------
class UserLogin(BaseModel):
    username: str
    password: str


# ---------------------------
# Response schema (output) Login
# ---------------------------
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


