from sqlalchemy.orm import Session
import models, schemas
from auth_utils import get_password_hash

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
    