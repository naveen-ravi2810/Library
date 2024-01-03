from fastapi import APIRouter, Depends
from CURD import curd_notes
from Models import session
from authorization.auth_berear import reader_auth, common_auth
from Validators.notes_validate import CreateNotes

router = APIRouter()


@router.get("/")
def get_notes(jwt_data: dict = Depends(reader_auth)):
    try:
        return {
            "status": True,
            "notes": curd_notes.get_notes_items(db=session, user_id=jwt_data["sub"]),
        }
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.post("/book")
def get_book_notes_by_id(
    book_id: int, note: CreateNotes, jwt_data: dict = Depends(common_auth)
):
    try:
        return {
            "status": True,
            "message": curd_notes.create_note(
                db=session, user_id=jwt_data["sub"], note=note, book_id=book_id
            ),
        }
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}
