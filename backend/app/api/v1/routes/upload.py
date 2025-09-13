from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.services.s3_service import upload_fileobj
from app.workers.indexer import enqueue_index_job
from app.dependencies import get_db

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("")
async def upload_image(file: UploadFile = File(...), db = Depends(get_db)):
    try:
        # Upload to S3
        key = f"uploads/{file.filename}"
        await upload_fileobj(file, key)
        # Enqueue indexing
        enqueue_index_job(s3_key=key)
        return {"status": "uploaded", "s3_key": key}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
