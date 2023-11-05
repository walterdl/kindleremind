from .factory import get_service


def lambda_handler(event=None, context=None):
    api_key_authorizer = get_service()

    api_key = api_key_authorizer.check_api_key(
        event['headers']['authorization'])

    if bool(api_key):
        return {
            'isAuthorized': True,
            'context': {
                'email': api_key['user']
            }
        }

    return {'isAuthorized': False}
