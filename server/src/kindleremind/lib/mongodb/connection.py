from kindleremind.lib.config import config
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(config.mongodb_uri, server_api=ServerApi('1'))
clippings = client.kindleremind.clippings
