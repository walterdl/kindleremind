import os


class _Config():
    def __init__(self):
        self.server_url = os.environ.get('SERVER_URL')
        self.server_api_key = os.environ.get('SERVER_API_KEY')


config = _Config()
