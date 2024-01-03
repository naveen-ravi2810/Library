from fastapi import APIRouter
from API.v1.endpoints import Books, Notes, Users


api = APIRouter()
api.include_router(Books.router, prefix="/book", tags=["CURD Books"])
api.include_router(Users.router, prefix="/user", tags=["CURD Users"])
api.include_router(Notes.router, prefix="/note", tags=["CURD Notes"])
