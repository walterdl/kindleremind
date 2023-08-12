class GetClippingsService():
    def __init__(self, storage):
        self.storage = storage

    def get_clippings(self):
        clippings = self.storage.query_clippings({
            'order_by': 'title'
        })

        for clipping in clippings:
            clipping['timestamp'] = clipping['timestamp'].isoformat()

        return clippings
