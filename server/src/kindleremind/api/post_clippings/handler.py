import json
from kindleremind.lib.json import unmarshall
from kindleremind.api.post_clippings.factory import get_service


def lambda_handler(event, context=None):
    payload = unmarshall(event['body'], return_none_if_error=True)
    result = get_service().write(payload)

    return {
        'statusCode': 200,
        'body': json.dumps(result),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
