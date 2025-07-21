# Use Python 3.10 slim as base image
FROM python:3.10-slim

# Set environment variables (recommended for cleaner output & behavior)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy full project code into container
COPY . .

# Collect static files (Django will put them in STATIC_ROOT folder)
RUN python manage.py collectstatic --noinput

# Run database migrations (creates tables etc.)
RUN python manage.py migrate --noinput

# Expose port 8000 (Django/Gunicorn will run on this)
EXPOSE 8000

# Run Gunicorn as the WSGI server (entrypoint)
CMD ["gunicorn", "firstproject.wsgi:application", "--bind", "0.0.0.0:8000"]
