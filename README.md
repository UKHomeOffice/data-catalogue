# CKAN Spike

A quick spike to get CKAN running in docker with our own config and then load some test data

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


