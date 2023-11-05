from .base import get_handler_wrapper


def api_key_auth(handler):
    return get_handler_wrapper(handler, _app_context_from_api_key_auth)


def _app_context_from_api_key_auth(event): return {
    'email': event['requestContext']['authorizer']['lambda']['email']
}
