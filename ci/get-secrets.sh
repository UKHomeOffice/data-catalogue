s3secrets/bin/s3secrets \
 -R eu-west-1 \
 -p dsp-ci \
 s3 get \
 --bucket ${S3_BUCKET} \
 -d /shared \
 shared/
