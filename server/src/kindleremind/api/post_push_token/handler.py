import json

from kindleremind.lib.json import unmarshall
from kindleremind.lib.auth_handler.cognito_auth import cognito_auth
from .factory import get_service


@cognito_auth
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
