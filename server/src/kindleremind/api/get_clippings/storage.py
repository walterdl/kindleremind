import pymongo


class Storage():
    def __init__(self, clippings_collection):
        self.collection = clippings_collection

    def query_clippings(self, options={}):
        cursor = self.collection.find(
            {}, projection={'_id': False}, sort=self.format_sorting(options))

        return list(cursor)

    def format_sorting(self, options):
        if 'sort' not in options:
            return []

        result = []
        for key in options['sort']:
            order = options['sort'][key]
            pymongo_order = pymongo.ASCENDING if order == 'asc' else pymongo.DESCENDING
            result.append((key, pymongo_order))

        return result
