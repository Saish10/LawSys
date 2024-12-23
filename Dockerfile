# Use the official Python 3.13 image as a base
FROM python:3.13-slim

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Set the default command to run the app
CMD ["./start.sh"]
