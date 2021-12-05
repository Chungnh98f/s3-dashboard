import json


def dump_bucket(bucket: dict, many=False):
    if many:
        return json.dumps({
            'buckets': [{
                'name': item.get('Name'),
                'created_at': item.get('CreationDate').strftime('%Y-%m-%d'),
            } for item in bucket]
        })

    return json.dumps({
        'name': bucket.get('Name'),
        'created_at': bucket.get('CreationDate').strftime('%Y-%m-%d'),
        'location': bucket.get('LocationConstraint')
    })



def dump_files(files: dict):
    return json.dumps({
        'files': [{
            'file_name': file.get('Key'),
            'file_size': file.get('Size'),
            'bucket_name': file.get('Bucket'),
            'file_url': f'http://localhost:4566/{file.get("Bucket")}/{file.get("Key")}'
        } for file in files]
    })
