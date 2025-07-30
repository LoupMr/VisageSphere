# main.py
from fastapi import FastAPI

app = FastAPI(
    title="Face Recognition Search API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Face Recognition Search API"}

# Later we'll include routers here:
# from routers import face, search
# app.include_router(face.router, prefix="/face", tags=["face"])
# app.include_router(search.router, prefix="/search", tags=["search"])
