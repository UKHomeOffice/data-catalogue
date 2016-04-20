#!/bin/bash
#get access to push to repo.
version=$(cat ../versions/ckan_container_version)
docker build -t quay.io/homeofficedigital/data-catalogue:$version.$BUILD_NUMBER ../

docker push quay.io/homeofficedigital/data-catalogue:$version.$BUILD_NUMBER
