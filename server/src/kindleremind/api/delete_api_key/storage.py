from bson.objectid import ObjectId


class ApiKeyStorage:
    def __init__(self, context, api_keys_collection):
        self.context = context
        self.collection = api_keys_collection

    def delete_api_key(self, api_key_id):
        self.collection.delete_one({
            '_id': ObjectId(api_key_id),
            'user': self.context['email']
        })
