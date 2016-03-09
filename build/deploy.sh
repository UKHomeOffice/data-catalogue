#!/usr/bin/env bash
# Script used as deployment entrypoint

set -e
source s3.cfg

env=dev
DOCKER_TAG=kb8-deployer

#get kubeconfig from s3 bucket
s3secrets --region ${AWS_DEFAULT_REGION} s3 get --bucket ${SECRETS_BUCKET} -d /root/.kube shared/kube/config.encrypted

kb8or -e $env --log-level debug data-catalogue.yaml
