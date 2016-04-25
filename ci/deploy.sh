#!/usr/bin/env bash
# Script used as deployment entrypoint
set -e
source ci/s3.cfg
#get kubeconfig from s3 bucket
s3secrets --region ${AWS_DEFAULT_REGION} s3 get --bucket ${SECRETS_BUCKET} -d ~/.kube shared/kube/config.encrypted

docker run --rm \
 -v /home/giles/.kube:/root/.kube/ \
 -v ${PWD}:/var/lib/deploy \
 quay.io/ukhomeofficedigital/kb8or:v0.6.12 -e $env \
 --log-level debug data-catalogue.yml
