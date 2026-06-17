import os
import uvicorn
from fastapi import FastAPI
from app.api.endpoints import logistics

app = FastAPI(title="Resilient-Path API")

# রাউটার অন্তর্ভুক্ত করা
app.include_router(logistics.router, prefix="/api/v1/logistics", tags=["Logistics"])

@app.get("/")
def read_root():
    return {"message": "Resilient-Path AI Engine is Operational"}

if __name__ == "__main__":
    # রেন্ডার সাধারণত পোর্ট হিসেবে ১০০০০ সেট করে
    port = int(os.environ.get("PORT", 10000))
    # খেয়াল করো এখানে "main:app" ব্যবহার করা হয়েছে কারণ আমরা app ফোল্ডারের ভেতরেই আছি
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)