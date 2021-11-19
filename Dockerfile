FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /test_neo4j
WORKDIR /test_neo4j

RUN apk update

RUN pip install --no-cache-dir --upgrade pip pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /test_neo4j/
EXPOSE 8000