# Data Catalogue

[![Codacy Badge](https://api.codacy.com/project/badge/grade/617b2a093c8246179ca234fcd7b765fd)](https://www.codacy.com/app/purplebooth/data-catalogue) [![Build Status](https://travis-ci.org/UKHomeOffice/data-catalogue.svg)](https://travis-ci.org/UKHomeOffice/data-catalogue) [![Docker Repository on Quay](https://quay.io/repository/ukhomeofficedigital/data-catalogue/status "Docker Repository on Quay")](https://quay.io/repository/ukhomeofficedigital/data-catalogue) [![GitHub version](https://badge.fury.io/gh/UKHomeOffice%2Fdata-catalogue.svg)](https://badge.fury.io/gh/UKHomeOffice%2Fdata-catalogue) 

A quick spike to get CKAN running in docker with our own config

## Starting
```
docker-compose up db solr
docker-compose up ckan
```

## Deploying

Kubernetes files can be found at [k8s/](k8s/)

## Loading data

Requires *Python* and *pip*

```
cd loader
pip install -r requirements.txt
python baseloader.py http://your-docker-instance your-api-key
```


