#!/bin/sh
set -e

# ডাটাবেস বা রেডিস কানেকশন চেক করা (ঐচ্ছিক)
echo "Starting FastAPI..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}