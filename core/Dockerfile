FROM python:3.10

ARG WORKDIR=/wd

WORKDIR ${WORKDIR}

RUN apt update && apt upgrade -y

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY ./manage.py manage.py
COPY ./core core
COPY ./phone_book phone_book

