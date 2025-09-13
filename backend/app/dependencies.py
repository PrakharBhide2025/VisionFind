from typing import Generator
from app.config import settings
from app.db.mongo import get_db as _get_db
from app.services.cache_service import get_cache as _get_cache

def get_settings():
    return settings

def get_db() -> Generator:
    db = _get_db()
    try:
        yield db
    finally:
        pass

def get_cache():
    return _get_cache()
