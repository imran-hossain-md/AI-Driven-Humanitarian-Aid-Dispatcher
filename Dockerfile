# পাইথনের হালকা ভার্সন ব্যবহার করা
FROM python:3.10-slim

# ওয়ার্কিং ডিরেক্টরি
WORKDIR /app

# রিকোয়ারমেন্ট কপি ও ইন্সটল
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# সব ফাইল কপি করা
COPY . .

# পোর্ট এক্সপোজ করা
EXPOSE 10000

# অ্যাপ রান করার কমান্ড
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]