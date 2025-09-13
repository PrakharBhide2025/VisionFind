from fastapi import APIRouter
from app.db.mongo import ping as mongo_ping
from app.services.cache_service import ping as redis_ping

router = APIRouter(tags=["health"])

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/ready")
async def ready():
    return {
        "mongo": mongo_ping(),
        "redis": redis_ping(),
    }
