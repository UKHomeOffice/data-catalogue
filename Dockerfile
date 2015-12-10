FROM quay.io/ukhomeofficedigital/ckan:v1.0.2
COPY ckan/configuration/ckan.ini $CKAN_CONFIG/ckan.ini
COPY ckan/init/ $USER_SCRIPT_DIR
COPY ckan/plugins $CKAN_PLUGINS
RUN yum install -y wget && \
    yum clean all

RUN wget -O /tmp/release-1.0.0.tar.gz \
         https://github.com/open-data/ckanext-scheming/archive/release-1.0.0.tar.gz && \
    tar -C $CKAN_PLUGINS -xvf /tmp/release-1.0.0.tar.gz && \
    mv $CKAN_PLUGINS/ckanext-scheming-release-1.0.0/ $CKAN_PLUGINS/ckanext-scheming/ && \
    rm /tmp/release-1.0.0.tar.gz
