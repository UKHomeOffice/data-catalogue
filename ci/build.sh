#!/bin/bash
#run this script from the root of the repo.
#get access to push to repo.

version=$(grep -o '.*build' versions/ckan_container_version)
docker build -t quay.io/homeofficedigital/data-catalogue:$version-$BUILD_NUMBER ../

docker push quay.io/homeofficedigital/data-catalogue:$version-$BUILD_NUMBER

echo $version-$BUILD_NUMBER > ../versions/ckan_container_version
