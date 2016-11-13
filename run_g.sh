#!/bin/sh

GUNICORN=/usr/bin/gunicorn
ROOT=/home/box/web
PID=/var/run/gunicorn.pid

APP=main:application

if [ -f $PID ]; then rm $PID; fi

cd $ROOT
exec $GUNICORN -c $ROOT/gunicorn.conf.py --pid=$PID $APP
