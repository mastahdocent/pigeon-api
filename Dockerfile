FROM python:latest

ENV PYTHONUNBUFFERED 1

ARG mode=develop
ENV DJANGO_SETTINGS_MODULE=settings.$mode

RUN mkdir /pigeon-api
WORKDIR /pigeon-api
ADD . /pigeon-api/

RUN pip install -r requirements/$mode.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT ["bash", "docker-entrypoint.sh"]