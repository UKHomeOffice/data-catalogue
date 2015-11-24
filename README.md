# Data Catalogue

[![Codacy Badge](https://api.codacy.com/project/badge/grade/0de2867370eb471880e7755569847323)](https://www.codacy.com/app/purplebooth/data-catalogue) [![Build Status](https://travis-ci.org/UKHomeOffice/data-catalogue.svg)](https://travis-ci.org/UKHomeOffice/data-catalogue) [![Docker Repository on Quay](https://quay.io/repository/ukhomeofficedigital/data-catalogue/status "Docker Repository on Quay")](https://quay.io/repository/ukhomeofficedigital/data-catalogue) [![GitHub version](https://badge.fury.io/gh/UKHomeOffice%2Fdata-catalogue.svg)](https://badge.fury.io/gh/UKHomeOffice%2Fdata-catalogue) 

A quick spike to get CKAN running in docker with our own config

## Starting
```
docker-compose up db solr
docker-compose up ckan
```

## Loading data

Requires *Python* and *pip*

```
cd loader
pip install -r requirements.txt
python loader.py http://your-docker-instance your-api-key
```


