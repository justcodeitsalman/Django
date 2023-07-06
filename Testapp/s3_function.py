import boto3
import os 

UPLOAD_FOLDER = "S3uploads"
BUCKET = "vmax-vedio-library"


def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

