from kindleremind.lib.config import config


def lambda_handler(event=None, context=None):
    return {
        'isAuthorized': event['headers']['Authorization'] == config.authorizer_token
    }
