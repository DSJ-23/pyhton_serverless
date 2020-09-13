from decimalencoder import DecimalEncoder

import boto3
dynamodb = boto3.resource('dynamodb')

def delete_single(event, context):
    table = dynamodb.Table('posts')

    # delete the todo from the database
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": "Post has been deleted"
    }

    return response