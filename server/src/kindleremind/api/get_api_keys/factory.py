from kindleremind.lib.mongodb.connection import api_keys
from .storage import Storage
from .service import GetApiKeysService


def get_service(context):
    return GetApiKeysService(Storage(context, api_keys))
