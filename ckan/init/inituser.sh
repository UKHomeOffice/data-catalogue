#!/bin/sh

echo Creating admin user
"$CKAN_HOME"/bin/paster --plugin=ckan user add admin email=admin@example.com password=admin --config=/etc/ckan/default/ckan.ini ;
"$CKAN_HOME"/bin/paster --plugin=ckan sysadmin add admin --config=/etc/ckan/default/ckan.ini ;

# TODO move this into a `initcomments.sh` script
echo Configuring DB \for comments
"$CKAN_HOME"/bin/paster --plugin=ckanext-ytp-comments initdb --config=/etc/ckan/default/ckan.ini ;
