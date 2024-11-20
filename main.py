from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.auth.transport.requests import Request


from ListBucket import gcp_create_bucket, list_buckets

app = FastAPI()
class BucketRequest(BaseModel):
    bucket_name: str
    
    location: str = "US"  


@app.post("/create_bucket")
async def create_bucket(request: BucketRequest):
    """Endpoint to create a GCS bucket with a specified name and location."""
    result = gcp_create_bucket(request.bucket_name, request.location)
    return {"message": result}

@app.get("/list_buckets")
async def get_buckets():
    """Endpoint to retrieve a list of all buckets in the project."""
    return {"buckets": list_buckets()}