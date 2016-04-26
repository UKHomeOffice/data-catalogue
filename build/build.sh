#!/bin/bash
#get access to push to repo.
echo "run this script in jenkins only."
source build/s3.cfg
version=$(cat build/versions/ckan_container_version)
echo "building version number $version-$BUILD_NUMBER"
docker build -t quay.io/ukhomeofficedigital/data-catalogue:$version-$BUILD_NUMBER .

#wget https://github.com/UKHomeOffice/s3secrets/releases/download/v0.1.3/s3secrets_v0.1.3_linux_x86_64 -o /usr/local/bin/s3secrets && chmod +x /usr/local/bin/s3secrets
#get docker config for pushing to s3
s3secrets --region ${AWS_DEFAULT_REGION} s3 get --bucket ${SECRETS_BUCKET} -d ~/.docker shared/docker/config.json.encrypted

echo "Pushing version number $version-$BUILD_NUMBER"
docker push quay.io/ukhomeofficedigital/data-catalogue:$version-$BUILD_NUMBER

#tag newest version as latest.
docker tag quay.io/ukhomeofficedigital/data-catalogue:$version-$BUILD_NUMBER quay.io/ukhomeofficedigital/data-catalogue:latest

docker push quay.io/ukhomeofficedigital/data-catalogue:latest

echo $version-$BUILD_NUMBER > build/versions/ckan_container_version
