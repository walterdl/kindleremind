from kindleremind.api.api_key_authorizer.service import ApiKeyAuthorizer
from kindleremind.api.get_api_keys.storage import Storage
from kindleremind.lib.mongodb.connection import api_keys


def get_service():
    # No context because the service is run by a Lambda authorizer.
    # And the Lambda authorizers is actually the context initializer.
    no_context = {}
    return ApiKeyAuthorizer(Storage(no_context, api_keys))
