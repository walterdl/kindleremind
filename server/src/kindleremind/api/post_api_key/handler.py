import json
from kindleremind.lib.auth_handler.cognito_auth import cognito_auth
from .factory import get_service


@cognito_auth
def lambda_handler(event=None, context=None):
    service = get_service(event['app_context'])

    return service.save_api_key(get_payload(event))


def get_payload(event):
    try:
        body = json.loads(event['body'])
        return body['name']
    except (TypeError, KeyError):
        return None
