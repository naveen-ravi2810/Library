from fastapi import APIRouter

router = APIRouter()
from CURD import curd_notes
from Models import session


@router.get("/")
def get_notes():
    try:
        return {"status": True, "notes": curd_notes.get_notes_items(db=session)}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}
