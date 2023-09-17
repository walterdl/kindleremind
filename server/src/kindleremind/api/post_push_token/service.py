class StorePushTokenService:
    def __init__(self, storage):
        self._storage = storage

    def store(self, push_token):
        self._validate(push_token)
        self._storage.save_token(push_token)

    def _validate(self, push_token):
        if type(push_token) != str or len(push_token.strip()) == 0:
            raise Exception('Invalid push token')
