FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    netcat-traditional \
    curl \
    dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/static /app/media && \
    dos2unix /app/entrypoint.sh /app/start.sh && \
    chmod +x /app/entrypoint.sh /app/start.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

