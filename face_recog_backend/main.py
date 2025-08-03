# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from utils.database import engine, Base
import utils.models  # noqa


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Face Recognition Search API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {"message": "Welcome to Face Recognition Search API"}

@app.get("/status")
async def status():
    return {"status": "ok"}

# Later we'll include routers here:
# from routers import face, search
# app.include_router(face.router, prefix="/face", tags=["face"])
# app.include_router(search.router, prefix="/search", tags=["search"])
