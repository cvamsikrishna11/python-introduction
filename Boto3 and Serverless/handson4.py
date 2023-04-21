import boto3
s3 = boto3.resource('s3')
s3.meta.client.download_file('vamsi-tf-state-03-08-22', 'aws-logo.png', 'aws-logo.png')