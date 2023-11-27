class GetSchedulesService():
    def __init__(self, context, storage):
        self.context = context
        self.storage = storage

    def get_schedules(self):
        return self.storage.get_user_schedules(self.context['email'])
