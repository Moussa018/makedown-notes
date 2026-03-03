from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.note import Note 

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    email: str
    username: str   
    password: str

class User(UserBase):
    id: int
    is_active: bool
    notes: list[Note] = []
    class Config:
        from_attributes = True