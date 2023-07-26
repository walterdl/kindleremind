from pymongo import ReplaceOne


class Storage:
    def __init__(self, clippings_collection):
        self.collection = clippings_collection

    def save(self, clippings):
        self.collection.bulk_write([
            ReplaceOne({'hello': 'there'}),
            ReplaceOne({'hello': 'there'})
        ], ordered=False)
