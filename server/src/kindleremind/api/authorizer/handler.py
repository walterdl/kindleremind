from kindleremind.lib.config import get_config


def lambda_handler(event=None, context=None):
    return {
        'isAuthorized': event['headers']['authorization'] == get_config('api_key')
    }
