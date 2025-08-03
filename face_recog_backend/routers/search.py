# routers/search.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/search",
    tags=["search"]
)

@router.get("/health")
async def search_health():
    return {"search_router": "healthy"}
