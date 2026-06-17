from app.workers.celery_app import celery_app
from app.services.logistics_service import LogisticsService

@celery_app.task(name="process_aid_request_task")
def process_aid_request(request_data_dict):
    # এখানে লজিস্টিক সার্ভিস কল করা হবে
    service = LogisticsService()
    # Pydantic মডেলটি পুনরায় তৈরি করে নেওয়া
    from app.models.schemas import LogisticsRequest
    request_data = LogisticsRequest(**request_data_dict)
    
    return service.process_request(request_data)