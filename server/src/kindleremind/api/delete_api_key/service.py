class DeleteApiKeyService:
    def __init__(self, storage):
        self.storage = storage

    def delete_api_key(self, api_key_id):
        self._validate(api_key_id)
        self.storage.delete_api_key(api_key_id)

    def _validate(self, api_key_id):
        if not api_key_id:
            raise ValueError('api_key_id is required')

        if not isinstance(api_key_id, str):
            raise TypeError('api_key_id must be a string')

        if not api_key_id.strip():
            raise ValueError('api_key_id must not be empty')
