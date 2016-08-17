FROM quay.io/ukhomeofficedigital/ckan:v1.2.8-rc24

COPY ckan/configuration/ckan.ini $CKAN_CONFIG/ckan.ini
COPY ckan/init/ $USER_SCRIPT_DIR
COPY ckan/plugins $CKAN_PLUGINS


#add HO overrides
#Has clamav and s3 upload code
ADD ckan/ckan/uploader.py /app/ckan/ckan/lib/uploader.py
#Has error for virus checker code
ADD ckan/ckan/package.py /app/ckan/ckan/controllers/package.py
#Has read in env vars code
ADD ckan/ckan/environment.py /app/ckan/ckan/config/environment.py
#Has download from s3 code
ADD ckan/ckan/fileapp.py /app/ckan/lib/python2.7/site-packages/paste/fileapp.py

RUN yum clean all && rpm --rebuilddb

RUN (yum install -y gcc python-devel libxml2 libxml2-devel libxslt-devel boto ||  yum install -y gcc python-devel libxml2 libxml2-devel libxslt-devel boto)

RUN pip install boto

RUN virtualenv $CKAN_HOME && \
    . $CKAN_HOME/bin/activate && \
    $CKAN_HOME/bin/pip install --upgrade lxml && \
    $CKAN_HOME/bin/pip install --upgrade boto

