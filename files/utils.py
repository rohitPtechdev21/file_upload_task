import os

import boto3


def get_s3_bucket(bucket_name):
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        bucket.load()
        return bucket
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_bucket():
    boto3.resource(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        region_name=AWS_DEFAULT_REGION,
    )

def upload_file_to_s3(_file, bucket, unique_Key):
    """Upload a file to an S3 bucket
    Parameters
    ----------
    _file: File to upload
    bucket: Name of Bucket
    unique_Key: Combinations of path and key
    """
    try:
        s3_client = boto3.client("s3")
        result = s3_client.put_object(Body=_file, Bucket=bucket, Key=unique_Key)
        response = result.get("ResponseMetadata")
        object_url = f"https://{bucket}.s3.amazonaws.com/{unique_Key}"
        return {"key": unique_Key, "object_url": object_url}
    except Exception:
        raise Exception("Error")
