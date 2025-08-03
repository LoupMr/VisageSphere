# routers/face.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# from utils.database import get_db  # uncomment when using DB deps

router = APIRouter(
    prefix="/face",
    tags=["face"]
)

@router.get("/health")
async def face_health():
    return {"face_router": "healthy"}

# Example endpoint using DB dependency:
# @router.get("/entries")
# async def list_entries(db: Session = Depends(get_db)):
#     return db.query(TestEntry).all()
