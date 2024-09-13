FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Psychopg2 dependencies

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application using gunicorn
CMD flask db upgrade && gunicorn --bind 0.0.0.0:8000 app:app
