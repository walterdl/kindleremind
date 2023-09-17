from .service import StorePushTokenService
from .storage import Storage
from kindleremind.lib.mongodb.connection import pushtokens


def get_service():
    return StorePushTokenService(Storage(pushtokens))
