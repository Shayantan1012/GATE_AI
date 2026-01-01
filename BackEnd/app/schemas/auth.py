from pydantic import BaseModel, EmailStr, Field

class RegisterSchema(BaseModel):
    name: str = Field(..., min_length=2)
    college: str
    age: int = Field(..., ge=16, le=60)
    exam: str                  # GATE
    branch: str                # CSE / EE / ME
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=10)
    password: str = Field(..., min_length=6)


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    role: str
