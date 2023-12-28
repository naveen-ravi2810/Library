from fastapi import APIRouter
from Validators.books_validate import CreateBook
from CURD import curd_books
from Models import session

router = APIRouter()


@router.get("/")
def get_books():
    try:
        return {"status": True, "books": curd_books.get_book_items(db=session)}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.post("/")
def add_book(book_details: CreateBook):
    try:
        curd_books.create_book_item(book=book_details, db=session)
        # print(book_details)
        return {"status": True}
    except Exception as e:
        return {"status": False, "message": f"error:{e}"}


@router.get("/filter")
def get_book_by_filter(
    book_name: str | None = None,
    book_author: str | None = None,
    book_genre: str | None = None,
):
    return curd_books.get_books_by_filter(
        db=session, book_name=book_name, book_author=book_author, book_genre=book_genre
    )


@router.get("/{book_id}")
def get_book(book_id: int):
    try:
        return {
            "status": True,
            "books": curd_books.get_book_by_id(book_id=book_id, db=session),
        }
    except Exception as e:
        return {"status": False, "message": f"error:{e}"}


@router.delete("/{book_id}")
def delete_book(book_id: int):
    try:
        return {"status": True, "message": curd_books.delete_book_by_id(db=session, book_id=book_id)}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}
