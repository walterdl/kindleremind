from kindleremind.lib.json import unmarshall
from kindleremind.lib.auth_handler.api_key_auth import api_key_auth
from kindleremind.api.post_clippings.factory import get_service


@api_key_auth
def lambda_handler(event, _ctx=None):
    payload = unmarshall(event['body'], return_none_if_error=True)
    write_clippings_service = get_service(event['app_context'])
    result = write_clippings_service.write(payload)

    return result
