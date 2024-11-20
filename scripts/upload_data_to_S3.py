import boto3
import os
import logging
import configparser
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

# getting AWS credentials
home_dir = os.getcwd() + "/"
config_dir = os.path.join(home_dir, "credentials/config.ini")
config = configparser.ConfigParser()
config.read(config_dir)

ACCESS_KEY_ID = config["AWS"]["ACCESS_KEY_ID"]
SECRET_ACCESS_KEY = config["AWS"]["SECRET_ACCESS_KEY"]

def upload_to_s3(path, bucket_name, object_name=None):
    try:
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=SECRET_ACCESS_KEY,
        )

        s3_client = session.client("s3")
        s3_client.upload_file(path, bucket_name, object_name)
        logging(f"Success: File {path} uploaded to {bucket_name} as {object_name}")
        
        return True

    except ClientError as e:
        logging(f"Error uploading file to S3: {e}")
        return False