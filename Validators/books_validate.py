from pydantic import BaseModel, Field
from datetime import date


class CreateBook(BaseModel):
    """
    Get details like book name, description, authors name in list, published year, genre
    """

    book_name: str = Field(
        min_length=3,
        max_length=60,
        description="Contains length of book name greater than 3 and lesser than 60",
    )
    book_description: str | None = Field(
        default="Description not found", max_length=600
    )
    book_author: str = Field(
        min_length=1, max_length=60, description="Contains author name in list"
    )
    book_date: date
    book_genre: str = Field(min_length=3, max_length=50)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "book_name": "Foo",
                    "book_description": "A very nice Item",
                    "book_date": "1997-12-11",
                    "book_genre": "Action",
                    "book_author": "John Doe",
                }
            ]
        }
    }
