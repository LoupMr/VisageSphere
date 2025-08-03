# main.py
from fastapi import FastAPI
from utils.database import engine, Base
import utils.models  # noqa

from routers import face, search  # add this import

app = FastAPI(
    title="Face Recognition Search API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to Face Recognition Search API"}

@app.get("/status")
async def status():
    return {"status": "ok"}

# Mount routers
app.include_router(face.router)
app.include_router(search.router)
