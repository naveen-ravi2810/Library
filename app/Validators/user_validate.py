from pydantic import BaseModel, Field


class CreateUser(BaseModel):
    user_name: str = Field(min_length=8, max_length=20)
    password: str = Field(min_length=8)


class LoginUser(BaseModel):
    user_name: str = Field(min_length=8, max_length=100)
    user_password: str
