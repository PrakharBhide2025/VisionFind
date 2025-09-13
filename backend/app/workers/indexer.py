# Simple stub to represent async indexing; replace with Celery/RQ/SQS as needed.
from app.db.mongo import get_db
from app.services.faiss_service import vector_search

def enqueue_index_job(s3_key: str):
    # In production, enqueue to Celery/RQ/SQS. Here we just log.
    print(f"[indexer] queued indexing job for: {s3_key}")

def index_now(s3_key: str):
    # TODO: extract embeddings and insert into FAISS + Mongo
    db = get_db()
    db.assets.insert_one({"s3_key": s3_key})
    print(f"[indexer] indexed: {s3_key}")
