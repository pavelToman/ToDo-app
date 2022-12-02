FROM python:3.11-alpine

WORKDIR /opt/todo
COPY . .

RUN pip install poetry djangorestframework django-cors-headers
RUN poetry install
