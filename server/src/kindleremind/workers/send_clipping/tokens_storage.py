class Storage():
    def __init__(self, context, collection):
        self.context = context
        self.collection = collection

    def get_token(self):
        document = self.collection.find_one({
            'user': self.context['email']
        })

        return document['token'] if document else None
