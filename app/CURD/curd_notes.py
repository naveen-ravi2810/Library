from sqlalchemy.orm import Session
from Models.Tables import NotesBase
from Validators.notes_validate import CreateNotes


def get_notes_items(db: Session, user_id: int):
    notes = db.query(NotesBase).filter(NotesBase.user_id == user_id).all()
    if notes:
        return notes
    return "No notes found"


def create_note(db: Session, user_id: int, note: CreateNotes, book_id: int):
    try:
        new_note = NotesBase()
        new_note.user_id = user_id
        new_note.book_id = book_id
        new_note.note = note.notes
        db.add(new_note)
        db.commit()
        return f"Note added to book ID {book_id}."
    except Exception as e:
        raise Exception(f"Note not added, Error{e}")
