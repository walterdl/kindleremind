class ReminderScheduleStorage:
    def __init__(self, context, collection):
        self.context = context
        self.collection = collection

    def get_schedules_count(self):
        return self.collection.count_documents({
            'user': self.context['email']
        })

    def create(self, schedule):
        new_doc = {**schedule, 'user': self.context['email']}
        result = self.collection.insert_one(new_doc)
        del new_doc['_id']

        return {
            **new_doc,
            'id': result.inserted_id.__str__(),
        }
