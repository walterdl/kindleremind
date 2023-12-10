class Storage():
    def __init__(self, context, collection):
        self.context = context
        self.collection = collection

    def get_random_clipping(self):
        search_response = self.collection.aggregate([
            {"$match": {"user": self.context['email'], 'type': 'HIGHLIGHT'}},
            {"$sample": {"size": 1}}
        ])

        result = search_response.try_next()
        self._format_id(result)

        return result

    def _format_id(self, document):
        if document:
            document['id'] = str(document['_id'])
            del document['_id']
