FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# এপিআই পোর্ট
EXPOSE 8000

# রান কমান্ড (এটি প্রসেস টাইপ অনুযায়ী চেঞ্জ হবে)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]