import boto3

my_session = boto3.session.Session()


s3 = my_session.resource('s3')

buckets_list = s3.buckets.all()

for i in buckets_list:
    print(i)