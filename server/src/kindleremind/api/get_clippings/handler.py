import json
from kindleremind.lib.json import unmarshall
from .factory import get_service


def lambda_handler(event=None, context=None):
    clippings = get_service().get_clippings()

    return {
        'statusCode': 200,
        'body': json.dumps(clippings),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
