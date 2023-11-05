import json
from kindleremind.lib.auth_handler.api_key_auth import api_key_auth
from .factory import get_service


@api_key_auth
def lambda_handler(event=None, context=None):
    get_clippings_service = get_service(event['app_context'])
    clippings = get_clippings_service.get_clippings()

    return {
        'statusCode': 200,
        'body': json.dumps(clippings),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
