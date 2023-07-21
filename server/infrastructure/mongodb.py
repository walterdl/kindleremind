import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

print('Loading env vars')
load_dotenv(override=True)

print('Connecting to mongodb')
client = MongoClient(os.environ.get('MONGODB_URI'), server_api=ServerApi('1'))
clippings = client.kindleremind.clippings

print('Creating clipping indexes')
clippings.create_index([("key", pymongo.ASCENDING)], unique=True)

print('Done')
