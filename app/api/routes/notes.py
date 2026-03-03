from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.note import Note, NoteCreate, NoteUpdate
from app.crud import note as crud_note
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=Note)
def create_note(
    note_in: NoteCreate, 
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    # La note est automatiquement liée à l'utilisateur connecté
    return crud_note.create_with_owner(db=db, obj_in=note_in, owner_id=current_user.id)

@router.get("/", response_model=list[Note])
def read_notes(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    # On ne renvoie QUE les notes de l'utilisateur actuel
    return crud_note.get_multi_by_owner(db=db, owner_id=current_user.id)