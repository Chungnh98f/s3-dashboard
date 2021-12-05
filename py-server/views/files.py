from flask import request, Blueprint, abort
from services.s3 import s3_client, s3_resource
from services.serializers import dump_files
from botocore.exceptions import ClientError


file_views: Blueprint = Blueprint(
    'File',
    __name__,
    url_prefix='/buckets/<string:bucket_name>/files',
)


@file_views.route('/', methods=['GET'])
def list_files(bucket_name: str):
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except ClientError:
        abort(404, f'Bucket {bucket_name} is not exist.')

    files: list = s3_client.list_objects(Bucket=bucket_name).get('Contents', [])

    for file in files:
        file['Bucket'] = bucket_name

    return dump_files(files), 200, {
        'Content-Type': 'application/json',
    }


@file_views.route('/', methods=['POST'])
def upload_file(bucket_name: str):
    if not request.files:
        abort(400, 'No file uploaded.')

    file = request.files['file']
    s3_client.upload_fileobj(
        Fileobj=file,
        Bucket=bucket_name,
        Key=file.filename,
        ExtraArgs={
            'ACL': 'public-read',
            'ContentType': file.content_type,
        }
    )

    return f"""File {file.filename} is uploaded!
    Check it out: http://localhost:4566/{bucket_name}/{file.filename}
    """, 201


@file_views.route('/<string:file_name>/', methods=['DELETE'])
def delete_file(bucket_name: str, file_name: str):
    bucket = s3_resource.Bucket(bucket_name)

    if not bucket.creation_date:
        abort(404, f'Bucket {bucket_name} is not exist.')


    for file in bucket.objects.all():
        if file.key == file_name:
            file.delete()
            return f'File {file.key} is deleted!', 201

    return f'File {file_name} does not exist.'
