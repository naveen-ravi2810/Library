from sqlalchemy import Column, Integer, String, ForeignKey
from .db_Config import Base, engine
from datetime import datetime


class Books(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(String(60), unique=True)
    book_description = Column(String(200))
    book_add_date = datetime.utcnow()
    extend_existing = True

class Authors(Base):
    __tablename__ = "authors"
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String(80), unique=True)
    extend_existing = True


class Author_Book(Base):
    __tablename__ = "books_authors"
    coimbination_col = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))
    extend_existing = True


Base.metadata.create_all(engine)
