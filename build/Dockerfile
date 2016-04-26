FROM quay.io/ukhomeofficedigital/kb8or:v0.6.8

WORKDIR /var/lib/app_deploy
ADD ./ ./
RUN mv config /root/.kube/config
ENTRYPOINT ["./deploy.sh"]
