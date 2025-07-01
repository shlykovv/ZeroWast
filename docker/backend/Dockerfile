FROM python:3.12-slim


RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY requirements.txt .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "zerowast.wsgi:application", '--bind', '0.0.0.0:8000']