from fastapi import FastAPI
from API.Endpoints.v1.Books_v1 import router as book_router

app = FastAPI()

app.include_router(book_router, prefix='/book')

