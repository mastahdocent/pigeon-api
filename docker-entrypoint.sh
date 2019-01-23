#!/bin/bash
pip install -r requirements.txt
python makemigrations
python migrate
python manage.py runserver 0.0.0.0:8000