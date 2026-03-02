from sqlalchemy.orm import Session
import models, schemas
from auth_utils import get_password_hash


def get_user(db:Session , user_id:int):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()


def get_user_by_email(db:Session,user_email: str):
    return db.query(models.User).filter(
        models.User.email == user_email
    ).first()
    
def create_user(db: Session, user:schemas.UserCreate):
     db_user = models.User(
         email = user.email,
         hashed_password = get_password_hash(user.password)
     )
     db.add(db_user)
     db.commit()
     db.refresh(db_user)
     return db_user
def get_notes(db: Session, skip: int=0 , limit: int=100):
    return db.query(models.Note).offset(
        skip
    ).limit(
        limit
    ).all()

def create_user_note(db: Session, note: schemas.NoteCreate, user_id: id):
    db_notes = models.Note(**note.model_dump(), owner_id=user_id)
    db.add(db_notes)
    db.commit()
    db.refresh(db_notes)
    return db_notes
    