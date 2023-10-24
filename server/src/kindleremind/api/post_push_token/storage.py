class Storage:
    def __init__(self, app_context, push_tokens):
        self.app_context = app_context
        self.collection = push_tokens

    def save_token(self, push_token):
        record = {
            'token': push_token,
            'user': self.app_context['email']
        }

        return self.collection.find_one_and_replace(
            # Find the record with the same token
            record,
            # And replace it with the new one
            record,
            upsert=True
        )
