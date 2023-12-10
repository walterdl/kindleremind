import firebase_admin
from firebase_admin import messaging
import json

from kindleremind.lib.config import get_config
from kindleremind.lib.mongodb.connection import pushtokens, clippings
from .clipping_storage import Storage as ClippingStorage
from .tokens_storage import Storage as TokensStorage
from .sender import ClippingSender
from .service import ClippingSenderService


firebase_private_key = get_config('firebase_service_account_private_key')
firebase_credentials = firebase_admin.credentials.Certificate(
    json.loads(firebase_private_key)
)
firebase_admin.initialize_app(firebase_credentials)


def get_service(context):
    return ClippingSenderService(
        ClippingStorage(context, clippings),
        TokensStorage(context, pushtokens),
        ClippingSender(messaging)
    )
