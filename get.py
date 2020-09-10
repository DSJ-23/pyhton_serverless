import os
import json

from decimalencoder import DecimalEncoder
import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table('posts')

    # fetch todo from the database
    # result = table.get_item(
    #     Key={
    #         'id': event['pathParameters']['id']
    #     }
    # )
    result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'],
                           cls=DecimalEncoder)
    }

    return response

def get_single(event, context):
    table = dynamodb.Table('posts')

    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=DecimalEncoder)
    }

    return response