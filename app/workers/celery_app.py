from celery import Celery
from app.core.config import settings

# Celery অ্যাপ ইনস্ট্যান্স তৈরি
celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery_app.conf.update(task_track_started=True)