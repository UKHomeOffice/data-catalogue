#!/bin/sh

echo Creating admin user
"$CKAN_HOME"/bin/paster --plugin=ckan user add admin email=admin@example.com password=admin --config=/etc/ckan/default/ckan.ini ;
"$CKAN_HOME"/bin/paster --plugin=ckan sysadmin add admin --config=/etc/ckan/default/ckan.ini ;
