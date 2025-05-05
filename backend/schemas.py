from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True

class NoteBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=10, max_length=1000)

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class NoteInDB(NoteBase):
    id: int
    sentiment: str
    owner_id: int

    class Config:
        orm_mode = True