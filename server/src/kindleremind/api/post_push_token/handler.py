import json

from kindleremind.lib.json import unmarshall
from .factory import get_service


def lambda_handler(event, _context=None):
    payload = unmarshall(event['body'], return_none_if_error=True, default={})
    get_service().store(payload.get('push_token'))

    return {
        'statusCode': 200,
        'body': json.dumps({'success': True}),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
