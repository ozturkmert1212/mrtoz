# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /app

# Install system deps here if needed
# RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

COPY ai-chat-site/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ai-chat-site/ .

EXPOSE 5000

# Default entrypoint runs Waitress server
CMD ["python", "run_waitress.py"]
