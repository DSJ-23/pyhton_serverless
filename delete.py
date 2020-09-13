from decimalencoder import DecimalEncoder
from handler import response_dump
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


def delete_content(event, context):
    table = dynamodb.Table('posts')
    result = table.scan()

    for instance in result['Items']:
        table.delete_item(
            Key={
                'id': instance['id']
            }
        )

    return response_dump(200, {"message": "All instances in the posts table have been deleted"})

