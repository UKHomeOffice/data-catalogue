#!/usr/bin/env bash
# Script used as deployment entrypoint

set -e
#get kubeconfig from s3 bucket
s3secrets --region ${AWS_DEFAULT_REGION} -p dsp-ci s3 get --bucket ${SECRETS_BUCKET} -d ~/.kube shared/config.encrypted
DEPLOY_SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
DEPLOY_HOME=${DEPLOY_SCRIPT_DIR}/..
unset ENV
unset EXTRA_DOCKER_CMD
cd ${DEPLOY_HOME}

if [ "${1}" == "DIND" ]; then
  shift
  echo "Running DIND: with params: '$@' in dir ${PWD}..."
else
  echo "Running PRE-DIND with params:'$@' in dir ${PWD}..."
  export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id)
  export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key)

  term=
  if [ -t 0 ] ; then
    # Interactive TTY
    term=t
    echo "TTY"
  else
    echo "NO TTY"
  fi

  # Unique name...
  DOCKER_TAG=kb8-deployer
  docker build -t ${DOCKER_TAG} .
  if [ "${1}" == "MOUNT_SECRETS" -o "${1}" == "PUSH_SECRETS" ]; then
    echo "Mounting secrets."
    EXTRA_DOCKER_CMD="-v ${DEPLOY_HOME}/services/secrets:/var/lib/app_deploy/services/secrets -e 'SKIP_SECRETS=TRUE'"
    if [ "${1}" == "MOUNT_SECRETS" ]; then
        shift
    fi
  fi
  echo "Term param = ${term}"
  docker run \
    -i${term} \
    --rm=true \
    ${EXTRA_DOCKER_CMD} \
    -e AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY \
    -e AWS_DEFAULT_REGION \
    -e "KUBERNETES_SERVICE_HOST=${KUBERNETES_SERVICE_HOST}" \
    ${DOCKER_TAG} \
    DIND $@

  echo "Deploy Success!"
  exit 0
fi

if [ "${1}" == "debug" ]; then
  bash -i
  exit 0
fi
if [ "${SKIP_SECRETS}" != "TRUE" ]; then
  source ${DEPLOY_SCRIPT_DIR}/get_secrets.sh $@
fi
echo "Using kubeconfig:${KUBECONFIG}"
/var/lib/kb8or/kb8or.rb $@
