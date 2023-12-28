import Validators
from Models import BooksBase
from sqlalchemy.orm import Session


def create_book_item(db: Session, book: Validators.CreateBook):
    """
    To Add a Book to the database
    :param db:
    :param book:
    :return:
    """
    new_book = BooksBase()
    new_book.book_name = book.book_name
    new_book.book_description = book.book_description
    new_book.book_date = book.book_date
    new_book.book_author = book.book_author
    new_book.book_genre = book.book_genre
    db.add(new_book)
    db.commit()
    return True


def get_book_by_id(db: Session, book_id: int):
    """
    The list the book with the given id
    :param db:
    :param book_id:
    :return:
    """
    book = db.query(BooksBase).filter(BooksBase.book_id == book_id).first()
    if book:
        return book
    else:
        return f"No book found in id {book_id}"


def get_book_items(db: Session):
    """
    To retrieve all the books from databases
    :param db:
    :return:
    """
    books = db.query(BooksBase).all()
    if books:
        return books
    else:
        return "No book/books found"


def get_books_by_filter(db: Session, book_name: str, book_author: str, book_genre: str):
    """
    Filtering the books by the name, author,and genre
    :param db:
    :param book_name:
    :param book_author:
    :param book_genre:
    :return:
    """
    print(book_author)
    print(book_genre)
    print(book_name)
    return (
        db.query(BooksBase)
        .filter(
            BooksBase.book_name.ilike("%" + book_name + "%" if book_name else "%"),
            BooksBase.book_author.ilike(
                "%" + book_author + "%" if book_author else "%"
            ),
            BooksBase.book_genre.ilike("%" + book_genre + "%" if book_genre else "%"),
        )
        .all()
    )


def delete_book_by_id(db: Session, book_id: int):
    """
    To remove the book from the database by book_id
    :param db:
    :param book_id:
    :return:
    """
    book_to_be_deleted = db.query(BooksBase).filter(BooksBase.book_id == book_id).first()
    if book_to_be_deleted:
        db.query(BooksBase).filter(BooksBase.book_id == book_id).delete()
        db.commit()
        return f"Book with id {book_id} deleted successfully"
    else:
        return f"Book not found"
