from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
import models , schemas  , crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Markwdown")

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model = schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db,user_email=user.email)
    if db_user:
        raise HTTPException(status_code=400,detail="Email déjà enregistré")
    return crud.create_user(db=db, user=user)

@app.post("/users/{user_id}/notes/", response_model= schemas.Note)
def create_note_for_user(
    user_id: int , note: schemas.NoteCreate,db: Session = Depends(get_db)
):
    return crud.create_user_note(db=db, note=note, user_id=user_id)

@app.get("/notes/", response_model= list[schemas.Note])
def read_notes(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    notes= crud.get_notes(db,skip=skip,limit=limit)
    return notes

