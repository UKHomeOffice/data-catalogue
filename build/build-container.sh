#!/bin/bash
#get aws credentials.

AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key)

DOCKER_TAG=kb8-deployer

docker build -t ${DOCKER_TAG} --no-cache build/

docker run \
 -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
 -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
 $DOCKER_TAG
