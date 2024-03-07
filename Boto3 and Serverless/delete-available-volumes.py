import boto3

client = boto3.client("ec2", region_name = "us-east-1")

response = client.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'available',
            ]
        }
    ],
)

for i in response["Volumes"]:
    print("Volume::::::::::::::::::::::::::", i["VolumeId"])
    response = client.delete_volume(
        VolumeId=i["VolumeId"]
    )
    print(response)
