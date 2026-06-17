FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# এন্ট্রি পয়েন্ট স্ক্রিপ্ট রান করা
RUN chmod +x scripts/entrypoint.sh
ENTRYPOINT ["/app/scripts/entrypoint.sh"]