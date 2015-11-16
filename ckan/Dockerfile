FROM quay.io/ukhomeofficedigital/ckan:v1.0.0
COPY configuration/ckan.ini $CKAN_CONFIG/ckan.ini
COPY init/ $USER_SCRIPT_DIR
COPY plugins $CKAN_PLUGINS
RUN yum install -y wget && \
    yum clean all

RUN cd /tmp && wget https://github.com/open-data/ckanext-scheming/archive/release-1.0.0.tar.gz && \
  tar -xvf release-1.0.0.tar.gz && mv ckanext-scheming-release-1.0.0/ $CKAN_PLUGINS/ckanext-scheming
