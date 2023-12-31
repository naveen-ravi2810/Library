from sqlalchemy.orm import Session
from Models.Tables import NotesBase


def get_notes_items(db: Session):
    notes = db.query(NotesBase).all()
    if notes:
        return notes
    return "No notes found"


# def create_note(db: Session):
#
