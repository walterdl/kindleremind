class ApiKeyAuthorizer:
    def __init__(self, storage):
        self.storage = storage

    def check_api_key(self, api_key_value):
        api_keys = self.storage.get_api_keys(
            {'value': api_key_value}, bypass_user_filter=True)

        return api_keys[0] if len(api_keys) else None
