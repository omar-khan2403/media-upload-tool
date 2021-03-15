import logging
import boto3
from botocore.client import Config
from dotenv import load_dotenv
import os
from botocore.exceptions import ClientError


load_dotenv()

host = os.getenv('AWS_HOST')
port = os.getenv('AWS_PORT')
access_key = os.getenv('AWS_ACCESS_KEY')
secret_key = os.getenv('AWS_SECRET_KEY')

endpoint_url = f"http://{host}:{port}"


def upload_file(file_name, bucket, file=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client(
        's3', 
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version='s3v4')
    )
    try:
        response = s3_client.put_object(Body=file, Bucket=bucket, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client(
        's3', 
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version='s3v4')
    )
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


def get_file():

    return


def delete_file():

    return