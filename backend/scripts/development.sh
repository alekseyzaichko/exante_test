#!/bin/sh
../wait-for-it.sh db:5432
python manage.py migrate
python manage.py collectstatic --noinput --verbosity 0
python manage.py loaddata initial_data
python manage.py runserver 0.0.0.0:8000
