class PostApiKeyService:
    def __init__(self, storage):
        self.storage = storage

    def save_api_key(self, api_key_name):
        api_key = self.storage.save_api_key(api_key_name)

        return {
            **api_key,
            'createdAt': api_key['createdAt'].isoformat()
        }
