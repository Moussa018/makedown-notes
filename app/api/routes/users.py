from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.models.user import User
router = APIRouter()

@router.get("/me", response_model=User)
def read_user_me(current_user: User = Depends(deps.get_current_user)):
    return current_user