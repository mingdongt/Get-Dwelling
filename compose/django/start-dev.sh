#!/bin/sh
python manage.py migrate

# No caching.
python manage.py runserver_plus 0.0.0.0:8000 --nostatic
