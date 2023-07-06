#!/bin/bash
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    ( python3 manage.py createsuperuser --no-input)
fi
( gunicorn firstProject.wsgi --bind 0.0.0.0:8000 )
