import pymongo


class Storage:
    def __init__(self, context, api_keys_collection):
        self.context = context
        self.api_keys_collection = api_keys_collection

    def get_api_keys(self):
        cursor = self.api_keys_collection.find(
            {'user': self.context['email']},
            sort=[('createdAt', pymongo.DESCENDING)]
        )

        return [self._format_doc(x) for x in cursor]

    def _format_doc(self, doc):
        result = {**doc, 'id': str(doc['_id'])}
        del result['_id']

        return result
