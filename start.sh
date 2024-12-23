#!/bin/bash

# Ensure the script exits if any command fails
set -e

# Collect static files (make sure Django is in the correct environment)
echo "Collecting static files..."
python manage.py collectstatic --no-input || { echo "Failed to collect static files"; exit 1; }

# Apply database migrations
echo "Running migrations..."
python manage.py migrate || { echo "Migration failed"; exit 1; }

# Start Daphne server for Django
echo "Starting Uvicorn server for Django..."
uvicorn law_sys.asgi:application --host 0.0.0.0 --port 8000 --reload&

# Start Celery workers for different queues
echo "Starting Celery worker for default queue..."
celery -A law_sys worker -Q default --loglevel=info &

echo "Starting Celery worker for small queue..."
celery -A law_sys worker -Q small --loglevel=info &

echo "Starting Celery worker for medium queue..."
celery -A law_sys worker -Q medium --loglevel=info &

echo "Starting Celery worker for large queue..."
celery -A law_sys worker -Q large --loglevel=info &

# Wait for all background processes to finish
wait
