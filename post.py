import json
import uuid
from decimalencoder import DecimalEncoder
from handler import response_dump

import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('posts')

def create(event, context):
    
    if 'text' in event:
        data = event
        return succesful_post(data, 201)
    elif 'text' in event['body']:
        data = json.loads(event['body'])
        return succesful_post(data, 201)
    else:
        return response_dump(404, "No text provided")

    
def succesful_post(data, status):
    item = {
        'id': str(uuid.uuid1()),
        'body': data['text']
    }

    table.put_item(Item=item)

    return response_dump(status, item)

