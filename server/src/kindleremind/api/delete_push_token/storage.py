class Storage():
    def __init__(self, push_tokens):
        self._collection = push_tokens

    def delete_push_token(self, push_token):
        self._collection.delete_one({'token': push_token})
