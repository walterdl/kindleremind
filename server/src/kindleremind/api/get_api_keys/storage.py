import pymongo


class Storage:
    def __init__(self, context, api_keys_collection):
        self.context = context
        self.api_keys_collection = api_keys_collection

    def get_api_keys(self, docs_filter=None, bypass_user_filter=False):
        cursor = self.api_keys_collection.find(
            self._query_filter(docs_filter, bypass_user_filter),
            sort=[('createdAt', pymongo.DESCENDING)]
        )

        return [self._format_doc(x) for x in cursor]

    def _query_filter(self, docs_filter, bypass_user_filter):
        result = {}

        if not bypass_user_filter:
            result['user'] = self.context['email']

        if docs_filter:
            result.update(docs_filter)

        return result

    def _format_doc(self, doc):
        result = {**doc, 'id': str(doc['_id'])}
        del result['_id']

        return result
