import boto3

client = boto3.client('ec2', region_name="us-east-1")

response = client.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'available'               
            ]
        },
    ]    
)

print(response)

for i in response["Volumes"]:
    # if "Tags" not in i.keys():            
    #     print(i)
    #     print()
    #     response = client.delete_volume(
    #         VolumeId=i["VolumeId"]
    #     )
    #     print(response)
    response = client.delete_volume(
            VolumeId=i["VolumeId"]
        )
    print(response)


    
    