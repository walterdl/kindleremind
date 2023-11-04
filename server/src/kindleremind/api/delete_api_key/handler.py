import json

from kindleremind.lib.auth_handler import auth_handler
from .factory import get_service


@auth_handler
def lambda_handler(event=None, context=None):
    service = get_service(event['app_context'])
    service.delete_api_key(get_api_key_param(event))


def get_api_key_param(event):
    if not event['queryStringParameters']:
        return None

    return event['queryStringParameters'].get('id', None)
