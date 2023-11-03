class GetApiKeysService():
    def __init__(self,  storage):
        self.storage = storage

    def get_api_keys(self):
        api_keys = self.storage.get_api_keys()

        for k in api_keys:
            k['createdAt'] = k['createdAt'].isoformat()

        return api_keys
