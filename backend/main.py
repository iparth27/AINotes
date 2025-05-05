from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import SessionLocal, engine

from fastapi.middleware.cors import CORSMiddleware
import bleach
from auth import (
    get_current_user,
    get_current_active_user,
    authenticate_user,
    create_access_token,
    get_password_hash,
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from datetime import timedelta
from jose import jwt

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def sanitize_input(text: str) -> str:
    return bleach.clean(text)

@app.on_event("startup")
async def startup():
    db = SessionLocal()
    try:
        # Create test user if not exists
        if not crud.get_user_by_username(db, username="testuser"):
            crud.create_user(db, schemas.UserCreate(
                username="testuser",
                password="testpass"
            ))
        db.commit()
    finally:
        db.close()

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password) 
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.UserInDB)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/me/", response_model=schemas.UserInDB)
async def read_users_me(current_user: schemas.UserInDB = Depends(get_current_active_user)):
    return current_user

@app.get("/notes/", response_model=List[schemas.NoteInDB])
def read_notes(
    current_user: schemas.UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return crud.get_notes_by_user(db, user_id=current_user.id)

@app.post("/notes/", response_model=schemas.NoteInDB)
def create_note(
    note: schemas.NoteCreate,
    current_user: schemas.UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    sanitized_title = sanitize_input(note.title)
    sanitized_content = sanitize_input(note.content)
    sanitized_note = schemas.NoteCreate(title=sanitized_title, content=sanitized_content)
    return crud.create_note_for_user(db=db, note=sanitized_note, user_id=current_user.id)

@app.put("/notes/{note_id}", response_model=schemas.NoteInDB)
def update_note(
    note_id: int,
    note: schemas.NoteUpdate,
    current_user: schemas.UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    sanitized_title = sanitize_input(note.title)
    sanitized_content = sanitize_input(note.content)
    sanitized_note = schemas.NoteUpdate(title=sanitized_title, content=sanitized_content)
    db_note = crud.update_note_for_user(db, note_id=note_id, note=sanitized_note, user_id=current_user.id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@app.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    current_user: schemas.UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    db_note = crud.delete_note_for_user(db, note_id=note_id, user_id=current_user.id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}

