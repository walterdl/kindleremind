import pymongo


class Storage:
    def __init__(self, context, api_keys_collection):
        self.context = context
        self.api_keys_collection = api_keys_collection

    def get_api_keys(self):
        self.api_keys_collection.find(
            {'user': self.context['email']},
            projection={'_id': False},
            sort=[('createdAt', pymongo.DESCENDING)]
        )
