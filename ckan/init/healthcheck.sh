#!/bin/bash

STATUSCODE=$(curl -L --silent --output /dev/stderr --write-out "%{http_code}" 127.0.0.1:5000)

if test $STATUSCODE -ne 200; then
    exit 1
else 
    exit 0
fi
