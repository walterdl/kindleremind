from pymongo import ReplaceOne


class Storage:
    def __init__(self, clippings_collection):
        self.collection = clippings_collection

    def save(self, clippings):
        result = self.collection.bulk_write(
            # ordered=False to speed up the replacement processes
            [self.replace_clipping(x) for x in clippings], ordered=False)

        return {
            'inserted': result.upserted_count,
            'updated': result.modified_count,
        }

    def replace_clipping(self, clipping):
        return ReplaceOne(self._clipping_filter(clipping), clipping, upsert=True)

    def _clipping_filter(self, clipping):
        return {'key': clipping['key']}
