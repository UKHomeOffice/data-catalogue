#!/bin/bash
. /app/ckan/bin/activate
pip install -r /app/ckan/dev-requirements.txt
#nosetests --ckan --with-pylons=test-core.ini ckan
