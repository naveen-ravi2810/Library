from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()
metadata = Base.metadata


class TimeBase(Base):
    __abstract__ = True
    created_at = date.today()
    updated_on = Column(Date, default=None, onupdate=date.today())


class BooksBase(TimeBase):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(String(60), unique=True, nullable=False)
    book_description = Column(String(600), nullable=False)
    book_genre = Column(String(60), nullable=False)
    book_author = Column(String(100), nullable=False)
    book_date = Column(Date, nullable=False)


class NotesBase(TimeBase):
    __tablename__ = "notes"
    notes_id = Column(Integer, primary_key=True, autoincrement=True)
    note = Column(String(1000), nullable=False)
    book_id = Column(
        Integer, ForeignKey("books.book_id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(
        Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False
    )


class UsersBase(TimeBase):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(100), unique=True, index=True)
    user_nick_name = Column(String(100), default=None)
    user_role = Column(String(20), default="reader")
    password = Column(String, nullable=False)


class RatingBase(TimeBase):
    __tablename__ = "ratings"
    rating_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False
    )
    book_id = Column(
        Integer, ForeignKey("books.book_id", ondelete="CASCADE"), nullable=False
    )
    rating = Column(Integer, nullable=False)
