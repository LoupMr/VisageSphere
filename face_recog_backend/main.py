# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel
from utils.database import engine, Base
import utils.models  # noqa
from routers import face, search  # add this import
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request


class ErrorResponse(BaseModel):
    error: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Face Recognition Search API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    # Log the exception here if you set up logging (next issue)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"},
    )

# Base.metadata.create_all(bind=engine) - This will be removed

@app.get("/")
async def root():
    return {"message": "Welcome to Face Recognition Search API"}

@app.get("/status", response_model=dict[str, str], responses={500: {"model": ErrorResponse}})
async def status():
    return {"status": "ok"}

# Mount routers
app.include_router(face.router)
app.include_router(search.router)
