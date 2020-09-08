import json

from handler import response_dump
from handler import get_response


def test2(event, callback):
    if 'worked' in event:
        print(event)
        # return get_response(200, event)
        return get_response(200, event)
    else:
        print(event)
        data = json.loads(event['body'])
        # return response_dump(200, {"body":data})
        return response_dump(200, {"body":data})