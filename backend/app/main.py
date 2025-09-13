from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.core.logging import configure_logging
from app.core.monitoring import metrics_router
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.search import router as search_router
from app.api.v1.routes.upload import router as upload_router

configure_logging()

app = FastAPI(title="Image Search API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api/v1")
app.include_router(search_router, prefix="/api/v1")
app.include_router(upload_router, prefix="/api/v1")
app.include_router(metrics_router)

@app.get("/")
async def root():
    return {"status": "ok", "service": "image-search-api"}
