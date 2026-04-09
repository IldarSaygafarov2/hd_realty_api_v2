FROM python:3.11-slim

WORKDIR /app

# Set environment variables to optimize Python for Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/

