#!/bin/bash
#get access to push to repo.
echo "run this script in jenkins only."
source ci/s3.cfg
version=$(grep -o '.*build' versions/ckan_container_version)
echo "building version number $version-$BUILD_NUMBER"
docker build -t quay.io/homeofficedigital/data-catalogue:$version-$BUILD_NUMBER .

#get docker config for pushing to s3
s3secrets --region ${AWS_DEFAULT_REGION} s3 get --bucket ${SECRETS_BUCKET} -d ~/.docker shared/config.json.encrypted

echo "Pushing version number $version-$BUILD_NUMBER"
docker push quay.io/homeofficedigital/data-catalogue:$version-$BUILD_NUMBER

echo $version-$BUILD_NUMBER > ../versions/ckan_container_version
