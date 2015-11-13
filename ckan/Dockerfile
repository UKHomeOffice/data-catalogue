FROM ckan/ckan
COPY configuration/ckan.ini /etc/ckan/default/ckan.ini
COPY init/ /etc/my_init.d/
COPY plugins /usr/lib/ckan/default/plugins
RUN apt-get -y update && apt-get install wget && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN cd /tmp && wget https://github.com/open-data/ckanext-scheming/archive/release-1.0.0.tar.gz && \
  tar -xvf release-1.0.0.tar.gz && mv ckanext-scheming-release-1.0.0/ /usr/lib/ckan/default/plugins/ckanext-scheming