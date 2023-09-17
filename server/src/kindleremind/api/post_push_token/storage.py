class Storage:
    def __init__(self, push_tokens):
        self.collection = push_tokens

    def save_token(self, push_token):
        record = {
            'token': push_token
        }

        return self.collection.find_one_and_replace(
            # Find the record with the same token
            record,
            # And replace it with the new one
            record,
            upsert=True
        )
