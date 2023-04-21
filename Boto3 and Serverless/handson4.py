import boto3
s3 = boto3.resource('s3')
s3.meta.client.download_file('BUCKET-NAME', 'aws-logo.png', 'aws-logo.png')