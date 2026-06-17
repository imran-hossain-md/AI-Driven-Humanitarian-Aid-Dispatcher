from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import LogisticsRequest
from app.workers.tasks import process_aid_request
from app.core.logging import logger
from app.api.dependencies import get_current_user # সিকিউরিটি ডিপেন্ডেন্সি ইমপোর্ট করলাম

router = APIRouter()

# এখন প্রতিটি রিকোয়েস্টের সাথে বৈধ টোকেন থাকতেই হবে
@router.post("/request-aid")
async def request_aid(
    request: LogisticsRequest, 
    current_user: str = Depends(get_current_user)
):
    try:
        # টাস্কটি ব্যাকগ্রাউন্ডে পাঠানোর সময় ইউজার ইনফোও রাখতে পারি (ঐচ্ছিক)
        task = process_aid_request.delay(request.model_dump())
        
        return {
            "message": "Aid request accepted and queued",
            "authenticated_by": current_user,
            "task_id": task.id,
            "status": "PENDING"
        }
    except Exception as e:
        logger.error("Task submission failed", error=str(e))
        raise HTTPException(status_code=500, detail="Failed to queue logistics request")