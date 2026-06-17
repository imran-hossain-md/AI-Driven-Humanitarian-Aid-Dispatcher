from app.db.postgres import SessionLocal
from app.models.domain import AuditLogDB

class AuditService:
    @staticmethod
    def save_log(log_data):
        db = SessionLocal()
        db_log = AuditLogDB(**log_data)
        db.add(db_log)
        db.commit()
        db.refresh(db_log)
        db.close()