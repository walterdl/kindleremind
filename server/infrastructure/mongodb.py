import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from lib.config import config

print('Connecting to mongodb')
client = MongoClient(config.mongodb_uri, server_api=ServerApi('1'))
clippings = client.kindleremind.clippings

print('Creating clipping indexes')
clippings.create_index([('key', pymongo.ASCENDING)], unique=True)

print('Done')
