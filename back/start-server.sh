#!/usr/bin/env bash

(gunicorn secret-santa.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"
