#!/usr/bin/env bash

set -eu

HTTPD_RUN_DIR=/var/run/httpd

if [[ -e "${HTTPD_RUN_DIR}" ]]
then
  echo "Removing stale HTTPD run files: $HTTPD_RUN_DIR"
  rm -rf "${HTTPD_RUN_DIR}"
  mkdir /var/run/httpd
fi

