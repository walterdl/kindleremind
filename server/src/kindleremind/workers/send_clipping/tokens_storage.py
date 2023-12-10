class Storage():
    def __init__(self, context, collection):
        self.context = context
        self.collection = collection

    def get_token(self):
        return self.collection.find_one({
            'user': self.context['email']
        })
