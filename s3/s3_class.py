import boto3
import gzip
from io import BytesIO

class S3Class():
    def __init__(self, s3_client, bucket_name: str, key: str):
        self.s3_client      = s3_client
        self.bucket_name    = bucket_name
        self.key            = key
        
        # Check if the file is with .gz extension
        self.isGzFile       = False
        if self.key.endswith('.gz'):
            self.isGzFile = True

    def get_bucket_name(self) -> str:
        return self.bucket_name
        
    def get_key(self) -> str:
        return self.key
        
    def get_file_content(self):
        object_data = self.s3_client.get_object(
            Bucket=self.bucket_name,
            Key=self.key
        )
        
        if self.isGzFile:
            bytes_stream    = BytesIO(object_data['Body'].read())
            object_data     = gzip.GzipFile(mode='rb', fileobj=bytes_stream).read()
        else:
            object_data     = object_data['Body'].read()
        
        return object_data
        