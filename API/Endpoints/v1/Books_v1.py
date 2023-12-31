from fastapi import APIRouter, Header
from Validators.books_validate import CreateBook
from CURD import curd_books
from Models import session
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import IntegrityError

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/")
def get_books():
    try:
        return {"status": True, "books": curd_books.get_book_items(db=session)}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.post("/", name="This is for adding book")
def add_book(book_details: CreateBook, authorization: Annotated[str | None, Header()]):
    try:
        print(authorization)
        curd_books.create_book_item(book=book_details, db=session)
        return {"status": True}
    except IntegrityError:
        return {"status": False, "message": "Book name already existed"}
    except Exception as e:
        return {"status": False, "message": f"error:{e}"}


@router.get("/filter")
def get_book_by_filter(
    book_name: str | None = None,
    book_author: str | None = None,
    book_genre: str | None = None,
):
    try:
        return curd_books.get_books_by_filter(
            db=session,
            book_name=book_name,
            book_author=book_author,
            book_genre=book_genre,
        )
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.get("/{book_id}")
def get_book(book_id: int):
    try:
        return {
            "status": True,
            "books": curd_books.get_book_by_id(book_id=book_id, db=session),
        }
    except Exception as e:
        return {"status": False, "message": f"error:{e}"}


@router.put("/{book_id}")
def update_book_by_id(book_id: int, book_details: CreateBook):
    try:
        return {
            "status": True,
            "message": curd_books.update_book_by_id(
                db=session, book_id=book_id, book_details=book_details
            ),
        }
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.delete("/{book_id}")
def delete_book(book_id: int):
    try:
        return {
            "status": True,
            "message": curd_books.delete_book_by_id(db=session, book_id=book_id),
        }
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}
