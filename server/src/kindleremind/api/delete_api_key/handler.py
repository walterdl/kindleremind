import json

from kindleremind.lib.auth_handler.cognito_auth import cognito_auth
from .factory import get_service


@cognito_auth
def lambda_handler(event=None, context=None):
    service = get_service(event['app_context'])
    service.delete_api_key(get_api_key_param(event))


def get_api_key_param(event):
    if not event['queryStringParameters']:
        return None

    return event['queryStringParameters'].get('id', None)
