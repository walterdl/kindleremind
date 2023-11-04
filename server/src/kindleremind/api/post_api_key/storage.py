import secrets
from datetime import datetime


class ApiKeyStorage:
    def __init__(
        self, context, api_keys_collection, token_generator=secrets.token_hex
    ):
        self.context = context
        self.collection = api_keys_collection
        self.token_generator = token_generator

    def save_api_key(self, api_key_name):
        record = {
            'name': api_key_name,
            'value': self.token_generator(),
            'user': self.context['email'],
            'createdAt': self._now()
        }

        self.collection.insert_one(record)
        self._format_created_id(record)

        return record

    def _now(self):
        return datetime.now()

    def _format_created_id(self, record):
        record['id'] = str(record['_id'])
        del record['_id']
