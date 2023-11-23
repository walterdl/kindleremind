from kindleremind.lib.config import get_config
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(get_config('mongodb_uri'), server_api=ServerApi('1'))
clippings = client.kindleremind.clippings
pushtokens = client.kindleremind.pushtokens
api_keys = client.kindleremind.apikeys
schedules = client.kindleremind.schedules
