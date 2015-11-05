FROM ckan/solr

RUN apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl vim

ENV CKAN_VERSION 2.3
RUN curl https://raw.githubusercontent.com/ckan/ckan/ckan-$CKAN_VERSION/ckan/config/solr/schema.xml > /schema.xml
RUN mv /schema.xml /opt/solr/example/solr/ckan/conf/schema.xml
