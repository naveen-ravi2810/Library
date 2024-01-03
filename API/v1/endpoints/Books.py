from fastapi import APIRouter, Depends
from Validators.books_validate import CreateBook
from CURD import curd_books
from Models import session
from sqlalchemy.exc import IntegrityError
from authorization.auth_berear import common_auth, admin_auth

router = APIRouter()


@router.get("/")
def get_books(jwt_data=Depends(common_auth)):
    try:
        return {"status": True, "books": curd_books.get_book_items(db=session)}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.post("/", name="This is for adding book", description="By admins only")
def add_book(book_details: CreateBook, jwt_data=Depends(admin_auth)):
    try:
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
    jwt_data=Depends(common_auth),
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
def get_book(book_id: int, jwt_data=Depends(common_auth)):
    try:
        return {
            "status": True,
            "books": curd_books.get_book_by_id(book_id=book_id, db=session),
        }
    except Exception as e:
        return {"status": False, "message": f"error:{e}"}


@router.put("/{book_id}")
def update_book_by_id(
    book_id: int, book_details: CreateBook, jwt_data=Depends(admin_auth)
):
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
def delete_book(book_id: int, jwt_data=Depends(admin_auth)):
    try:
        return {
            "status": True,
            "message": curd_books.delete_book_by_id(db=session, book_id=book_id),
        }
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}
