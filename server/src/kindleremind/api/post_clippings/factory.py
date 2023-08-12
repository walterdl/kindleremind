import mmh3
from .service import WriteClippingsService
from .storage import Storage
from kindleremind.lib.mongodb.connection import clippings
from kindleremind.api.post_clippings.key_generator import ClippingKeyGenerator


def get_service():
    return WriteClippingsService(ClippingKeyGenerator(mmh3.hash), Storage(clippings))
