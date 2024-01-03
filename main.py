from fastapi import FastAPI
from API.v1.api import api
from core.settings import settings
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    description=settings.app_description,
    contact=settings.api_contact,
    summary=settings.api_summary,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api, prefix=settings.api_prefix)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
