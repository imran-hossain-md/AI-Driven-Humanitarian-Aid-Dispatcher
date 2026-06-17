from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.postgres import Base
import datetime

class AuditLogDB(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String, unique=True, index=True)
    event_type = Column(String)
    status = Column(String)
    risk_score = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)