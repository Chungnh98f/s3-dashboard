from flask import Blueprint, request, abort
from configs import Location
from services.s3 import s3_client, s3_resource
from services.serializers import dump_bucket
from botocore.exceptions import ClientError


bucket_views: Blueprint = Blueprint('Bucket', __name__, url_prefix='/buckets')


@bucket_views.route('/', methods=['GET'])
def list_buckets():
    buckets: dict = s3_client.list_buckets().get('Buckets', [])
    return dump_bucket(buckets, many=True), 200, {
        'Content-Type': 'application/json',
    }


@bucket_views.route('/', methods=['POST'])
def create_bucket():
    bucket_name: str = request.json.get('name')
    bucket_location: str = request.json.get('location', Location.SEOUL)

    if not bucket_name:
        abort(400, 'Please provide name for the new bucket.')

    try:
        s3_client.head_bucket(Bucket=bucket_name)
        abort(400, f'Bucket {bucket_name} is already exist.')
    except ClientError:
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': bucket_location,
            },
        )
        return f'Bucket {bucket_name} is created!', 201


@bucket_views.route('/<string:bucket_name>/', methods=['GET'])
def detail_bucket(bucket_name: str):
    buckets: dict = s3_client.list_buckets().get('Buckets', [])
    bucket: dict = None
    for item in buckets:
        if item.get('Name') == bucket_name:
            bucket = item

    if not bucket:
        abort(404, f'Bucket {bucket_name} is not exist.')

    location: str = s3_client.get_bucket_location(Bucket=bucket_name) \
        .get('LocationConstraint')
    bucket['LocationConstraint'] = location
    return dump_bucket(bucket), 200, {
        'Content-Type': 'application/json',
    }


@bucket_views.route('/<string:bucket_name>/', methods=['DELETE'])
def delete_bucket(bucket_name: str):
    try:
        bucket = s3_resource.Bucket(bucket_name)
        bucket.objects.all().delete()
        bucket.delete()
    except ClientError:
        abort(404, f'Bucket {bucket_name} is not exist.')

    return f'Bucket {bucket_name} is deleted', 201
