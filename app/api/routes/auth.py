from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from fastapi.security import OAuth2PasswordRequestForm
from app.core import security
from app.crud import user as crud_user
from app.models.user import User, UserCreate, UserUpdate

router = APIRouter()

@router.post("/register", response_model=User)
def register(
    obj_in:UserCreate, db : Session = Depends(deps.get_db)
):
    user = crud_user.get_user_by_email(db=db,user_email=obj_in.email)
    if user:
        raise HTTPException(status_code=400, detail="Cet email existe déjà.")
    return crud_user.create_user(db=db,obj_in=user)
@router.post("/login", response_model=Token)
def login(
    db: Session=Depends(deps.get_db), form_data: OAuth2PasswordRequestForm=Depends()
):
    user = crud_user.authenticate(db, email=form_data.username,password = form_data.password)
    if not user :
        raise HTTPException(status_code = 400, detail ="Email ou mot de passe incorrect.")
    return {
        "access_token": security.create_access_token(user.id),
         "token_type" : "bearer"
    }