
FROM python:3.8.5-slim-buster
RUN apt-get update \
    && apt-get -y install build-essential \
    libpq-dev libssl-dev libffi-dev \
    libxml2-dev libxslt1-dev libssl1.1 \
    postgresql-client
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8888