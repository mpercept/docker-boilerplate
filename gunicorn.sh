#/usr/bin/env bash

gunicorn --workers=1 --bind=0.0.0.0:8000 wsgi --threads=1

