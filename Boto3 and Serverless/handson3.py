import boto3

iam_client = boto3.client("iam")

response = iam_client.list_roles()

# print(response)

for i in response["Roles"]:
    print(i["Arn"])