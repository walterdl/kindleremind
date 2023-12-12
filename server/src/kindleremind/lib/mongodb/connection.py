from bson import CodecOptions
from kindleremind.lib.config import get_config
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(get_config('mongodb_uri'), server_api=ServerApi('1'))

clippings = client.kindleremind.get_collection(
    "clippings", codec_options=CodecOptions(tz_aware=True))

pushtokens = client.kindleremind.pushtokens

api_keys = client.kindleremind.apikeys

schedules = client.kindleremind.get_collection(
    "schedules", codec_options=CodecOptions(tz_aware=True))
