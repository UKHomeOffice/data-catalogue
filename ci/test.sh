#!/bin/bash

#configure database.
docker run -d --name=db ckan/postgresql

#initialise solr.
docker run -d --name=solr quay.io/ukhomeofficedigital/ckan-solr:v0.1.0

#initialise ckan
docker build --no-cache -t ckan .

docker run \
  --name=ckan \
  -i \
  -p 80:80 \
  --link db:db \
  --link solr:solr \
  -e CKAN_SMTP_SERVER=mailcatcher:25 \
  ckan /userscripts/run-tests.sh

  #cleanup containers.

  docker rm -f db ckan solr
