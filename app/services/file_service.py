import boto3
from botocore.exceptions import  ClientError
import logging
import os

S3_BUCKET_NAME = 'nf-userdata'
S3_FOLDER_NAME = 'user_images'

def upload_file_to_s3(file ):

    s3_client = boto3.client(
        's3', 
        aws_access_key_id= os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key= os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    try:
        s3_client.upload_fileobj(file, S3_BUCKET_NAME, f"{S3_FOLDER_NAME}/{file.filename}")
        file_url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{S3_FOLDER_NAME}/{file.filename}" 
    
    except ClientError as e:
        logging.error(e)
        return False
    return file_url