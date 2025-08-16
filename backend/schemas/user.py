# Pydantic validation (for API inputs/outputs).
# This file defines how requests/responses should look.
from pydantic import BaseModel, EmailStr

# ---------------------------
# Request schema (input)
# ---------------------------

class UserCreate(BaseModel):
    username: str
    email: EmailStr # validates format of email automatically
    phone: str
    password: str # plain password (will be hashed later)

# ---------------------------
# Response schema (output)
# ---------------------------

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone: str
    bio: str
    active_now: bool

    class Config:
        orm_mode = True  # Tells Pydantic it can read data directly from SQLAlchemy models
