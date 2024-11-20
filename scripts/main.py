from get_data import *
from upload_data_to_S3 import *


url = "http://restcountries.com/v3.1/all"
file_name = "data/raw_dataset.parquet"
bucket = "cde-peace-bucket"

def main():
    get_data()

    upload_to_s3(path=file_name, bucket_name=bucket, object_name="raw_dataset.parquet")


if __name__ == "__main__":
    main()