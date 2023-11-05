from .base import get_handler_wrapper


def cognito_auth(handler):
    return get_handler_wrapper(handler, _app_context_from_cognito_auth)


def _app_context_from_cognito_auth(event): return {
    'email': event['requestContext']['authorizer']['jwt']['claims']['email']
}
