#!/bin/bash.
#get access to push to repo.
echo "run this script in jenkins only."
version=$(grep -o '.*build' versions/ckan_container_version)
echo "building version number $version-$BUILD_NUMBER"
docker build -t quay.io/homeofficedigital/data-catalogue:$version-$BUILD_NUMBER ../

echo "Pushing version number $version-$BUILD_NUMBER"
docker push quay.io/homeofficedigital/data-catalogue:$version-$BUILD_NUMBER

echo $version-$BUILD_NUMBER > ../versions/ckan_container_version
