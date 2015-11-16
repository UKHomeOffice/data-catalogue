FROM ckan/solr

RUN apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    wget vim

ENV CKAN_VERSION ckan-2.4.1
RUN wget -O /opt/solr/example/solr/ckan/conf/schema.xml \
    https://raw.githubusercontent.com/ckan/ckan/$CKAN_VERSION/ckan/config/solr/schema.xml
