# Pydantic validation (for API inputs/outputs).
# This file defines how requests/responses should look.
from pydantic import BaseModel, EmailStr, ConfigDict

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

    model_config = ConfigDict(from_attributes=True)
