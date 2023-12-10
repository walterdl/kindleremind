from datetime import datetime
from datetime import timezone


class Storage:
    def __init__(self, app_context, push_tokens):
        self.app_context = app_context
        self.collection = push_tokens

    def save_token(self, push_token):
        return self.collection.find_one_and_replace(
            # Find the record with the same token
            {'user': self.app_context['email']},
            # And replace it with the new one
            {
                'token': push_token,
                'user': self.app_context['email'],
                'createdAt': datetime.now(timezone.utc),
            },
            upsert=True
        )
