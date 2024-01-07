from pydantic import BaseModel
from datetime import date


class UsersDisplay(BaseModel):
    user_name: str
    user_role: str
    user_id: int
    updated_on: date
    user_nick_name: str
