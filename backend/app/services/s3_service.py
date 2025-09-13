import boto3
from app.config import settings

s3 = boto3.client(
    "s3",
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)

async def upload_fileobj(file, key: str):
    # UploadFile exposes a file-like interface via .file
    s3.upload_fileobj(file.file, settings.S3_BUCKET, key, ExtraParams={
        "ContentType": file.content_type or "application/octet-stream"
    })
    return f"s3://{settings.S3_BUCKET}/{key}"
