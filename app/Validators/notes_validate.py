from pydantic import BaseModel, Field


class CreateNotes(BaseModel):
    notes: str = Field(min_length=7, max_length=1000)
