import json
from kindleremind.lib.auth_handler import auth_handler
from .factory import get_service


@auth_handler
def lambda_handler(event=None, context=None):
    service = get_service(event['app_context'])

    return service.get_api_keys()
