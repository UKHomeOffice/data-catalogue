FROM quay.io/ukhomeofficedigital/ckan:v1.1.0
COPY ckan/configuration/ckan.ini $CKAN_CONFIG/ckan.ini
COPY ckan/init/ $USER_SCRIPT_DIR
COPY ckan/plugins $CKAN_PLUGINS

#RUN python --version
RUN yum install -y gcc
RUN gcc --version
#RUN yum install -y python-dev libxml2 libxml2-dev libxslt libxslt-dev
RUN yum install -y libxml2-devel libxslt1-devel
RUN pip install --upgrade pip
#RUN pip install --upgrade lxml
#RUN STATIC_DEPS=true pip install lxml
RUN easy_install lxml
#RUN pip install lxml