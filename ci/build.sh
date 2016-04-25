#!/bin/bash
#get access to push to repo.
echo "run this script in jenkins only."
source ci/s3.cfg
version=$(grep versions/ckan_container_version)
echo "building version number $version-$BUILD_NUMBER"
docker build -t quay.io/ukhomeofficedigital/data-catalogue:$version-$BUILD_NUMBER .

#get docker config for pushing to s3
s3secrets --region ${AWS_DEFAULT_REGION} -p dsp-ci s3 get --bucket ${SECRETS_BUCKET} -d ~/.docker shared/docker/config.json.encrypted

echo "Pushing version number $version-$BUILD_NUMBER"
docker push quay.io/ukhomeofficedigital/data-catalogue:$version-build-$BUILD_NUMBER

echo $version-$BUILD_NUMBER > versions/ckan_container_version
