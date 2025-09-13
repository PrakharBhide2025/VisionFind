from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.dependencies import get_db
from app.services.faiss_service import vector_search

router = APIRouter(prefix="/search", tags=["search"])

@router.get("")
async def search(q: Optional[str] = Query(None, description="Text query"),
                 top_k: int = 10,
                 db = Depends(get_db)):
    # Placeholder: If q is None, return latest items
    try:
        results = vector_search(query_text=q, top_k=top_k)
        return {"count": len(results), "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
