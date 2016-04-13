FROM quay.io/ukhomeofficedigital/ckan:v1.1.0
COPY ckan/configuration/ckan.ini $CKAN_CONFIG/ckan.ini
COPY ckan/init/ $USER_SCRIPT_DIR
COPY ckan/plugins $CKAN_PLUGINS

RUN yum install -y gcc python-devel && \
    yum install -y libxml2 libxml2-devel libxslt-devel  && \
    yum clean all

RUN virtualenv $CKAN_HOME && \
    . $CKAN_HOME/bin/activate && \
    $CKAN_HOME/bin/pip install --upgrade lxml
