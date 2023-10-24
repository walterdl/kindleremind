import json

from kindleremind.lib.json import unmarshall
from kindleremind.lib.auth_handler import auth_handler
from .factory import get_service


@auth_handler
def lambda_handler(event, _context=None):
    service = get_service(event['app_context'])
    payload = unmarshall(event['body'], return_none_if_error=True, default={})
    service.store(payload.get('pushToken'))

    return {
        'statusCode': 200,
        'body': json.dumps({'success': True}),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
