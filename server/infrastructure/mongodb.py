import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from kindleremind.lib.config import get_config

print('Connecting to mongodb')
client = MongoClient(get_config('mongodb_uri'), server_api=ServerApi('1'))

print('Creating clipping indexes')
clippings = client.kindleremind.clippings
clippings.create_index([('key', pymongo.ASCENDING)], unique=True)

print('Creating push tokens indexes')
pushtokens = client.kindleremind.pushtokens
pushtokens.create_index([('token', pymongo.ASCENDING)], unique=True)

print('Done')
