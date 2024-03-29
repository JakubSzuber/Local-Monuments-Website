#!/bin/bash
# This script is used to: wait some time for initialization of the Postgres, print some information about Gunicorn
# container, execute init_db.py (that connects to Postgres and runs some queries to insert needed data into Postgres)
# and finally check if the working directory is correct before running the rest of Dockerfile

set -e

ERROR_NO_APP_WORKDIR=101
RIGHT_WORKDIR=/app

function description(){
  echo "Waiting for postgres..."
  sleep 7
  echo -e "Below some information about this container (wsgi gunicorn server) that is core for application work:\n"
  echo "List of objects in your $RIGHT_WORKDIR working directory:"
  ls -l .
  echo "Tree structure of $RIGHT_WORKDIR working directory:"
  tree .
  echo "List of pip packages used for this app:"
  pip list
  python main_python_files/init_db.py
}

if [ ! -d $RIGHT_WORKDIR ]; then
  echo "ERROR: No right working directory $RIGHT_WORKDIR"
  echo "Check if the Dockerfile of current container create new directory $RIGHT_WORKDIR correctly"
  exit $ERROR_NO_APP_WORKDIR
fi

description

exec "$@"
