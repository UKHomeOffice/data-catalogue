#!/bin/bash
#get access to push to repo.
echo "run this script in jenkins only."
source build/s3.cfg
version=$(cat build/versions/ckan_container_version)
echo "building version number $version-$BUILD_NUMBER"
docker build -t quay.io/ukhomeofficedigital/data-catalogue:$version-$BUILD_NUMBER .

#get docker config for pushing to s3
s3secrets --region ${AWS_DEFAULT_REGION} s3 get --bucket ${SECRETS_BUCKET} -d ~/.docker shared/docker/config.json.encrypted

echo "Pushing version number $version-$BUILD_NUMBER"
docker push quay.io/ukhomeofficedigital/data-catalogue:$version-$BUILD_NUMBER

#tag newest version as latest.
docker tag quay.io/ukhomeofficedigital/data-catalogue:$version-$BUILD_NUMBER quay.io/ukhomeofficedigital/data-catalogue:latest

docker push quay.io/ukhomeofficedigital/data-catalogue:latest

echo $version-$BUILD_NUMBER > versions/ckan_container_version
