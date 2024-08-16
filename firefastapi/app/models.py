from pydantic import BaseModel, EmailStr

class AuthData(BaseModel):
    email: EmailStr
    password: str

class TokenData(BaseModel):
    token: str

class UserResponse(BaseModel):
    user_id: str
    message: str
