import json
from kindleremind.lib.json import unmarshall
from kindleremind.lib.auth_handler import auth_handler
from kindleremind.api.post_clippings.factory import get_service


@auth_handler
def lambda_handler(event, _handler_ctx=None):
    payload = unmarshall(event['body'], return_none_if_error=True)
    write_clippings_service = get_service(event['app_context'])
    result = write_clippings_service.write(payload)

    return {
        'statusCode': 200,
        'body': json.dumps(result),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
