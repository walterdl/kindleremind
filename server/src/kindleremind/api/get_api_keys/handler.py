import json
from kindleremind.lib.auth_handler.cognito_auth import cognito_auth
from .factory import get_service


@cognito_auth
def lambda_handler(event=None, context=None):
    service = get_service(event['app_context'])

    return service.get_api_keys()
