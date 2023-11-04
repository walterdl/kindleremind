from .storage import ApiKeyStorage
from .service import DeleteApiKeyService
from kindleremind.lib.mongodb.connection import api_keys


def get_service(context):
    return DeleteApiKeyService(ApiKeyStorage(context, api_keys))
