echo "Getting shared secrets (for all environments)..."
s3secrets --region "${AWS_DEFAULT_REGION}" s3 get --bucket "${SECRETS_BUCKET}" -d ${SECRET_ROOT}/shared/ shared/
echo "Getting secrets for ${ENV}..."
s3secrets --region "${AWS_DEFAULT_REGION}" s3 get --bucket "${SECRETS_BUCKET}" -d ${SECRET_ROOT}/${ENV}/ ${ENV}/
