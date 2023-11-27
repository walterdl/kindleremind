from kindleremind.lib.json import unmarshall
from kindleremind.lib.auth_handler.cognito_auth import cognito_auth
from .factory import get_service


@cognito_auth
def lambda_handler(event):
    service = get_service(event['app_context'])
    result = service.get_schedules()

    return format_result(result)


def format_result(result):
    return [{**x, 'datetime': x['datetime'].isoformat()} for x in result]
