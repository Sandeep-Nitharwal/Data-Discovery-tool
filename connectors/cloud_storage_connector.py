import boto3

def connect_to_s3(bucket_name):
    s3_client = boto3.client('s3')
    return s3_client

def fetch_data_from_s3(s3_client, bucket_name, file_key):
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    return response['Body'].read()