import json
from kindleremind.lib.mongodb.connection import clippings
from kindleremind.lib.json import unmarshall
from kindleremind.api.post_clippings.factory import get_service


def lambda_handler(event, context=None):
    payload = unmarshall(event['body'], return_none_if_error=True)
    get_service().write(payload)

    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Hello from Lambda!'}),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
