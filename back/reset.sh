#!/bin/bash

rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser --username=admin --email=admin@example.com
python manage.py runserver
