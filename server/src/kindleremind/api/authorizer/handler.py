from kindleremind.lib.config import config


def lambda_handler(event=None, context=None):
    return {
        'isAuthorized': event['headers']['authorization'] == config.authorizer_token
    }
