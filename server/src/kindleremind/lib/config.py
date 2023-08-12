import os
from dotenv import load_dotenv

load_dotenv(override=True)


class _Config():
    mongodb_uri = os.environ.get('MONGODB_URI')
    authorizer_token = os.environ.get('AUTHORIZER_TOKEN')


config = _Config()
