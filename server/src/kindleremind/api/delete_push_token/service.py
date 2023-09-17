from kindleremind.api.post_push_token.validate_token import validate_push_token


class DeletePushTokenService:
    def __init__(self, storage):
        self._storage = storage

    def delete_push_token(self, push_token):
        validate_push_token(push_token)
        self._storage.delete_push_token(push_token)
