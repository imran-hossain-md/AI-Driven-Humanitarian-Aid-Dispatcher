FROM python:3.10-slim

WORKDIR /app

# ফাইল কপি করা
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# সরাসরি কমান্ড রান করা, কোনো স্ক্রিপ্ট ফাইলে ডিপেন্ডেন্সি নেই
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]