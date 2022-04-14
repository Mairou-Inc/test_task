FROM python:3.9.5-slim


RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
    

RUN python -m pip install --upgrade pip



ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/