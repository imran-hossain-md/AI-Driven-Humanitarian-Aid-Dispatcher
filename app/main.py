import os
from fastapi import FastAPI
from app.api.endpoints import logistics

app = FastAPI(title="Resilient-Path API")

# রাউটার অন্তর্ভুক্ত করা
app.include_router(logistics.router, prefix="/api/v1/logistics", tags=["Logistics"])

@app.get("/")
def read_root():
    return {"message": "Resilient-Path AI Engine is Operational"}

# এটি যোগ করা খুব জরুরি যাতে সার্ভার ক্র্যাশ না করে
if __name__ == "__main__":
    import uvicorn
    # রেন্ডার থেকে পাওয়া পোর্ট অথবা ডিফল্ট ১০০০০
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)