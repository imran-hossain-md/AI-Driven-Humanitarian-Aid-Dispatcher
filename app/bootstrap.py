# app/bootstrap.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_all_services():
    logger.info("--- কানেক্টর সচল হচ্ছে: সব সার্ভিস চেক করা হচ্ছে ---")
    try:
        # এখানে তোমার বিদ্যমান DB/Redis মডিউলগুলো কল করো
        # উদাহরণস্বরূপ:
        # from app.db import postgres, redis_client
        # postgres.verify_connection()
        # redis_client.verify_connection()
        
        logger.info("সব সার্ভিস সফলভাবে সংযুক্ত হয়েছে।")
        return True
    except Exception as e:
        logger.error(f"সার্ভিস কানেকশনে সমস্যা: {e}")
        return False