from datetime import datetime, timedelta
from typing import Optional
from jose import jwt

SECRET_KEY = None
ALGORITHM = None

def configure(secret_key: str, algorithm: str):
    global SECRET_KEY, ALGORITHM
    SECRET_KEY = secret_key
    ALGORITHM = algorithm

def create_access_token(subject: str, expires_minutes: int = 60) -> str:
    to_encode = {"sub": subject, "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
