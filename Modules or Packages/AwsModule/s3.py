import boto3

def list_all_buckets():
    print("Listing s3 buckets...")
    s3_resource = boto3.resource("s3")

    for bucket in s3_resource.buckets.all():
        print(bucket.name)

