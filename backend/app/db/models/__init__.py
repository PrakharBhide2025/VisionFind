from pydantic import BaseModel, Field
from typing import Optional, List

class ImageMeta(BaseModel):
    id: Optional[str] = None
    s3_key: str
    embeddings: Optional[List[float]] = None
    content_type: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
