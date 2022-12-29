#!/bin/bash
set -e

ERROR_NO_APP_WORKDIR=101
RIGHT_WORKDIR=/app

function description(){
  echo -e "Below some information about this container (wsgi gunicorn server) that is core for application work:\n"
  echo "List of objects in your $RIGHT_WORKDIR working directory:"
  ls .
  echo "Tree structure of $RIGHT_WORKDIR working directory::"
  tree .
  echo "List of pip packages used for this app:"
  pip list
}

if [ ! -d $RIGHT_WORKDIR ]; then
  echo "ERROR: No right working directory $RIGHT_WORKDIR"
  echo "xxx.."
  exit $ERROR_NO_APP_WORKDIR
fi

description

exec "$@"