from pydantic import BaseModel, Field

class CreateBook(BaseModel):
    book_name: str = Field(min_length=3, max_length=60, description="Contains length of book name greater than 3 and lesser than 60")
    book_description: str | None = Field(default="Description not found")
    book_author : list = Field(min_length=1, max_length=8, description="Contains author name in list")
