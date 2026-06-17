from pydantic import BaseModel, Field
from typing import List, Optional

class LogisticsRequest(BaseModel):
    request_id: str
    origin: str
    destination: str
    priority: int = Field(ge=1, le=5) # ১ থেকে ৫ পর্যন্ত প্রায়োরিটি

class LogisticsResponse(BaseModel):
    request_id: str
    status: str
    optimal_path: List[str]
    estimated_time: float
    audit_id: str