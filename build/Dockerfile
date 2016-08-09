FROM quay.io/ukhomeofficedigital/centos-base:latest

ENV kb8or_version 0.6.12 
ENV s3secret_version v0.1.3
WORKDIR /opt

RUN yum install -y wget unzip 
RUN yum install -y ruby \
    && gem install bundler \
    && wget https://github.com/UKHomeOffice/kb8or/archive/v${kb8or_version}.zip \
    && unzip v${kb8or_version}.zip \
    && mv kb8or-${kb8or_version} kb8or \
    && cd kb8or && bundle install 

RUN curl -O https://storage.googleapis.com/kubernetes-release/release/v1.3.4/bin/linux/amd64/kubectl && \
    chmod +x kubectl && mv kubectl /usr/bin/kubectl

RUN wget https://github.com/UKHomeOffice/s3secrets/releases/download/${s3secret_version}/s3secrets_${s3secret_version}_linux_x86_64 && \
    mv s3secrets_${s3secret_version}_linux_x86_64 /opt/s3secrets && chmod +x /opt/s3secrets

WORKDIR /var/lib/app_deploy
ADD ./ ./
ENTRYPOINT ["./deploy.sh"]
