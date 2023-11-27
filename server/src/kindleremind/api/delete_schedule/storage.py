from bson.objectid import ObjectId


class Storage():
    def __init__(self, collection):
        self.collection = collection

    def delete_schedule(self, input_):
        self.collection.delete_one({
            'user': input_['user'],
            '_id': ObjectId(input_['id']),
        })
