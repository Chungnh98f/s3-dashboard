import boto3
from configs import S3Config


# TODO: convert all s3_client operations to s3_resource
s3_client = boto3.client(
    's3',
    endpoint_url=S3Config.URL,
    aws_access_key_id=S3Config.ACCESS_KEY,
    aws_secret_access_key=S3Config.SECRET_KEY,
)

s3_resource = boto3.resource(
    's3',
    endpoint_url=S3Config.URL,
    aws_access_key_id=S3Config.ACCESS_KEY,
    aws_secret_access_key=S3Config.SECRET_KEY,
)
