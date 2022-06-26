import boto3
import time

def lambda_handler(event, context):
    ts = time.time()
    string = event['Records'][0]["body"]
    encoded_string = string.encode("utf-8")

    bucket_name = "sanpyproject1"
    s3_path = "file-"+str(ts)+".txt"
    

    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
