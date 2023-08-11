import mmh3
from .service import WriteClippingsService
from .storage import Storage
from kindleremind.lib.mongodb.connection import clippings


def get_service():
    return WriteClippingsService(mmh3.hash, Storage(clippings))
