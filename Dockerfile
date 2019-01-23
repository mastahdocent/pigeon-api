FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /pigeon-api
WORKDIR /pigeon-api
ADD . /pigeon-api/

ENTRYPOINT ["bash", "docker-entrypoint.sh"]