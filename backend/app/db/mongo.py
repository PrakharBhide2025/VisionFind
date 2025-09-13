from pymongo import MongoClient
from app.config import settings

_client = MongoClient(settings.MONGO_URI)
_db = _client[settings.MONGO_DB]

def get_db():
    return _db

def ping() -> bool:
    try:
        _client.admin.command('ping')
        return True
    except Exception:
        return False
