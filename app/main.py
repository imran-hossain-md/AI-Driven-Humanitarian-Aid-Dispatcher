from fastapi import FastAPI
from app.api.endpoints import logistics

app = FastAPI(title="Resilient-Path API")

# রাউটার অন্তর্ভুক্ত করা
app.include_router(logistics.router, prefix="/api/v1/logistics", tags=["Logistics"])

@app.get("/")
def read_root():
    return {"message": "Resilient-Path AI Engine is Operational"}