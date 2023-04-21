import boto3

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

table = dynamodb.Table('Products')

# print(table.table_arn)
# print(table.table_id)
# print(table.item_count)


response = table.put_item(
    Item ={
    "ProductId": "7890",
    "ProductName": "Shoes",
    "ProductPrice": 200
    }
)

print(response)