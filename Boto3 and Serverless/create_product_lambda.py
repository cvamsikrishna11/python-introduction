import json
import boto3

def lambda_handler(event, context):
    print(event['body'])
    print()
    print(type(json.loads(event['body'])))

    
    dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

    table = dynamodb.Table('Products')
    try:
        response = table.put_item(
            Item = json.loads(event['body'])
        )
    
        print(response)
    
        if 'HTTPStatusCode' in response['ResponseMetadata'] and response['ResponseMetadata']['HTTPStatusCode']==200: 
            return {
                'statusCode': 200,
                 'body': json.dumps({"message": "product stored successfully"})
            }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps({"Error": "Please check the input payload"})
        }



