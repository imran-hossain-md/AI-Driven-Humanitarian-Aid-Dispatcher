import os
import uvicorn
from fastapi import FastAPI
from app.api.endpoints import logistics
from app.bootstrap import connect_all_services # কানেক্টর ইম্পোর্ট করা

app = FastAPI(title="Resilient-Path API")

# স্টার্টআপ ইভেন্ট: কানেক্টর রান করা
@app.on_event("startup")
async def startup_event():
    success = connect_all_services()
    if not success:
        print("সতর্কতা: কানেক্টর সব সার্ভিস লোড করতে ব্যর্থ হয়েছে!")

# রাউটার অন্তর্ভুক্ত করা
app.include_router(logistics.router, prefix="/api/v1/logistics", tags=["Logistics"])

@app.get("/")
def read_root():
    return {"message": "Resilient-Path AI Engine is Operational"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    # রেন্ডারের পাথ অনুযায়ী সঠিক কমান্ড
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)