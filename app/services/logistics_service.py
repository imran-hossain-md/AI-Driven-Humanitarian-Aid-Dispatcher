from app.services.ai_engine.pathfinder import PathFinder
from app.models.audit import AuditLog
from app.core.logging import logger

class LogisticsService:
    def process_request(self, request_data):
        # ১. AI ইঞ্জিন কল করা
        pathfinder = PathFinder(grid=[])
        path = pathfinder.get_optimal_path(request_data.origin, request_data.destination)
        
        # ২. অডিট ট্রেইল তৈরি করা (আমাদের Audit-as-Code ফিচার)
        log = AuditLog(
            event_type="ROUTE_OPTIMIZATION",
            request_id=request_data.request_id,
            status="SUCCESS",
            payload={"path": path},
            decision_logic="A* Algorithm used for shortest path.",
            risk_score=0.1
        )
        
        logger.info("Decision made", audit=log.dict())
        return path