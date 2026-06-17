#!/bin/sh
# স্ক্রিপ্টে কোনো ভুল থাকলে যাতে সাথে সাথে থামে
set -e

echo "Starting Uvicorn..."
# এখানে সরাসরি uvicorn কমান্ড দাও
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}