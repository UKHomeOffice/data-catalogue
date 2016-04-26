#!/usr/bin/env bash
# Script used as deployment entrypoint
set -e
cd build && source s3.cfg

env=dev
DOCKER_TAG=kb8-deployer

if $1 == DIND; then
  echo "Running deployment scripts";
else
#get kubeconfig from s3 bucket
  s3secrets --region ${AWS_DEFAULT_REGION} -p dsp-ci s3 get --bucket ${SECRETS_BUCKET} -d ${PWD} shared/kube/config.encrypted
  docker build --no-cache -t ${DOCKER_TAG} .
fi
docker run --rm \
 ${DOCKER_TAG} \
 DIND data-catalogue.yaml
