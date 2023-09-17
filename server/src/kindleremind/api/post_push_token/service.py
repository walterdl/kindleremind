from .validate_token import validate_push_token


class StorePushTokenService:
    def __init__(self, storage):
        self._storage = storage

    def store(self, push_token):
        validate_push_token(push_token)
        self._storage.save_token(push_token)
