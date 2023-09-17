from .service import DeletePushTokenService
from .storage import Storage
from kindleremind.lib.mongodb.connection import pushtokens


def get_service():
    return DeletePushTokenService(Storage(pushtokens))
