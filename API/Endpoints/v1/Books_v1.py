from fastapi import APIRouter
from Validators.books_validate import CreateBook
router = APIRouter()


@router.get('/')
def get_books():
    try:
        return {'status':True}
    except Exception as e:
        return {'status':False}


@router.get('/{book_id}')
def get_book(book_id : int):
    try:
        return {'status':True}
    except Exception as e:
        return {'status':False}


@router.post('/')
def add_book(book_details:CreateBook):
    try:
        return {'status':True}
    except Exception as e:
        return {'status':False}


@router.delete('/{book_id}')
def delete_book(book_id:int):
    try:
        return {'status':True}
    except Exception as e:
        return {'status':False}
