#!/bin/bash

NAME="sudocode"
DJANGODIR=/var/site/airplane/site
SOCKFILE=/var/site/airplane/run/gunicorn.sock
USER=game
GROUP=game
NUM_WORKERS=3 #1 + 2 * cores
DJANGO_SETTINGS_MODULE=sudocode.settings
DJANGO_WSGI_MODULE=sudocode.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=/usr/bin/python3

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec /usr/local/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  -k gevent \
  --name $NAME \
  --workers $NUM_WORKERS \
  --threads $NUM_WORKERS \
  --max-requests 50 \
  --max-requests-jitter 5 \
  --graceful-timeout 15 \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=error \
  --log-file=/var/site/airplane/logs/gunicorn.log

