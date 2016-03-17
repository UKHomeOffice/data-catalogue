FROM quay.io/ukhomeofficedigital/ckan:v1.1.0
COPY ckan/configuration/ckan.ini $CKAN_CONFIG/ckan.ini
COPY ckan/init/ $USER_SCRIPT_DIR
COPY ckan/plugins $CKAN_PLUGINS
RUN cd /app/ckan/plugins/ckanext-datacatalogue_theme && nosetests --ckan --with-pylons=test.ini ckanext/iauthfunctions/tests
