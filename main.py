from fastapi import FastAPI
from API.Endpoints.v1.Books_v1 import router as book_router
from API.Endpoints.v1.Notes_v1 import router as note_router
from API.Endpoints.v1.Users_v1 import router as user_router
import uvicorn

app = FastAPI()

app.include_router(book_router, prefix="/book", tags=["CURD Books"])
app.include_router(user_router, prefix="/user", tags=["CURD Users"])
app.include_router(note_router, prefix="/note", tags=["CURD Notes"])


if __name__ == "__main__":
    uvicorn.run(app=app)
