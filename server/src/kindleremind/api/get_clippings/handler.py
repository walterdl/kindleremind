import json
from kindleremind.lib.json import unmarshall
from kindleremind.lib.auth_handler import auth_handler
from .factory import get_service


@auth_handler
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
