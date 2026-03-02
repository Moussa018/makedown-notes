from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#How the data will be sent to the API and how it will be stored in the database
class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    created_at: datetime
    owner_id: int
    
    class Config:
        from_attributes = True
        
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