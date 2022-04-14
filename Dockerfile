FROM python:3.9.5-slim


RUN apt-get update && apt-get install

RUN apt-get install -y libpq-dev gcc 


RUN python -m pip install --upgrade pip

WORKDIR /code
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
COPY . /code/