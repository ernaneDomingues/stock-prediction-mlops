# ===========================
#  Dockerfile - Stock Predictor API
# ===========================

FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY src/ ./src/
COPY models/ ./models/
COPY data/ ./data/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]


