FROM quay.io/ukhomeofficedigital/ckan:v1.2.8-rc12

COPY ckan/configuration/ckan.ini $CKAN_CONFIG/ckan.ini
COPY ckan/init/ $USER_SCRIPT_DIR
COPY ckan/plugins $CKAN_PLUGINS


RUN yum clean all && rpm --rebuilddb

RUN (yum install -y gcc python-devel libxml2 libxml2-devel libxslt-devel  ||  yum install -y gcc python-devel libxml2 libxml2-devel libxslt-devel )

RUN virtualenv $CKAN_HOME && \
    . $CKAN_HOME/bin/activate && \
    $CKAN_HOME/bin/pip install --upgrade lxml
