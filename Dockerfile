FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN apt-get update
RUN apt-get install -y postgresql 
RUN apt-get install libpq-dev gcc
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-psycopg2 

RUN pip3 install -r requirements.txt
ADD ./ /code/