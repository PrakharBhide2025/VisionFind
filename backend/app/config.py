from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # App
    ENV: str = "development"
    DEBUG: bool = True
    CORS_ALLOW_ORIGINS: List[str] = ["*"]

    # Mongo
    MONGO_URI: str = "mongodb://mongo:27017"
    MONGO_DB: str = "imagesearch"

    # Redis
    REDIS_URL: str = "redis://redis:6379/0"

    # AWS / S3
    AWS_ACCESS_KEY_ID: str = "change-me"
    AWS_SECRET_ACCESS_KEY: str = "change-me"
    AWS_REGION: str = "us-east-1"
    S3_BUCKET: str = "your-bucket"

    # Auth
    JWT_SECRET_KEY: str = "change-me-in-prod"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"

settings = Settings()
