from .service import StorePushTokenService
from .storage import Storage
from kindleremind.lib.mongodb.connection import pushtokens


def get_service(app_context):
    return StorePushTokenService(Storage(app_context, pushtokens))
