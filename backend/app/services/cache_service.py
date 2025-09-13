import redis
from app.config import settings

_redis = redis.from_url(settings.REDIS_URL, decode_responses=True)

def get_cache():
    return _redis

def ping() -> bool:
    try:
        return _redis.ping()
    except Exception:
        return False
