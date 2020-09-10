import json

def get_response(status, body, dump=False):
    if dump == False:
        return {"statusCode": status, "body": body}
    else:
        return {"statusCode": status, "body": json.dumps(body)}

def response_dump(status, body):
    return {"statusCode": status, "body": json.dumps(body)}
    

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def post(event, callback):
    return get_response(200, json.loads(event['body']))


def test1(event, callback):
    if 'worked' in event:
        print(event)
        return get_response(200, event)
    else:
        print(event)
        data = json.loads(event['body'])
        return response_dump(200, data)
    

