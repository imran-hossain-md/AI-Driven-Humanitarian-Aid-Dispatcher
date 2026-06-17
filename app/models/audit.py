from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, Dict

class AuditLog(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    event_type: str
    request_id: str
    status: str
    payload: Dict[str, Any]
    decision_logic: str # এআই কেন এই সিদ্ধান্ত নিল তার সংক্ষিপ্ত বিবরণ
    risk_score: float