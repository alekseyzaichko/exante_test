#!/bin/sh
../wait-for-it.sh db:5432
python apps/news/fixtures/get_news.py
python manage.py migrate
python manage.py collectstatic --noinput --verbosity 0
python manage.py loaddata initial_data
gunicorn config.wsgi -w 1 -b 0.0.0.0:8000 --chdir=/app
