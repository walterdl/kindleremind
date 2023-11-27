from kindleremind.lib.auth_handler.cognito_auth import cognito_auth
from .factory import get_service


@cognito_auth
def lambda_handler(event):
    schedule_id = event['queryStringParameters'].get('id', None)
    service = get_service(event['app_context'])
    service.delete_schedule(schedule_id)
