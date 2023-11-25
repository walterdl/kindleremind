import json

from kindleremind.lib.json import unmarshall
from kindleremind.lib.auth_handler.cognito_auth import cognito_auth
from .factory import get_service


@cognito_auth
def lambda_handler(event):
    service = get_service(event['app_context'])
    payload = unmarshall(event['body'], return_none_if_error=True, default={})
    result = service.create(payload)

    return {
        **result,
        'datetime': result['datetime'].isoformat(),
    }
