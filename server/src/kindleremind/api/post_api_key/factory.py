from .service import PostApiKeyService
from .storage import ApiKeyStorage
from kindleremind.lib.mongodb.connection import api_keys


def get_service(context):
    return PostApiKeyService(ApiKeyStorage(context, api_keys))
