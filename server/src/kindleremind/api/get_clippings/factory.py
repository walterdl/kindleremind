from kindleremind.lib.mongodb.connection import clippings
from .storage import Storage
from .service import GetClippingsService


def get_service(context):
    return GetClippingsService(Storage(context, clippings))
