import json
import boto3
from decimal import Decimal


# code to handle the Decimal entries to int
# class DecimalEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Decimal):
#             return str(obj)
#         return super(DecimalEncoder, self).default(obj)


def lambda_handler(event, context):
    print(event)
    print()
    print(type(event))
    print()
    print(event['queryStringParameters']['ProductId'])
    
    
    dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

    table = dynamodb.Table('Products')
    
    response = table.get_item(
        Key = {
        "ProductId":event['queryStringParameters']['ProductId']
        }
    )
    
    print(response)
    print()
    # print(response['Item'])
    
    if 'Item' in response: 
        return {
            'statusCode': 200,
             'body': json.dumps(response['Item']) # without decimal entry
            # 'body': json.dumps(response['Item'], cls=DecimalEncoder) # with decimal entry
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({})
        }

