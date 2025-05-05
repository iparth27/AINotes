from sqlalchemy.orm import Session
import models, schemas
from nlpmodel import analyze_sentiment
from auth import get_password_hash
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_notes_by_user(db: Session, user_id: int):
    return db.query(models.Note).filter(models.Note.owner_id == user_id).all()

def create_note_for_user(db: Session, note: schemas.NoteCreate, user_id: int):
    sentiment = analyze_sentiment(note.content)
    db_note = models.Note(title=note.title, content=note.content, sentiment=sentiment, owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note_for_user(db: Session, note_id: int, note: schemas.NoteUpdate, user_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == user_id).first()
    if db_note is None:
        return None
    db_note.title = note.title
    db_note.content = note.content
    db_note.sentiment = analyze_sentiment(note.content)
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note_for_user(db: Session, note_id: int, user_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == user_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note

