class DeleteScheduleService():
    def __init__(self, context, storage, validate_storage_id):
        self.context = context
        self.storage = storage
        self.validate_storage_id = validate_storage_id

    def delete_schedule(self, schedule_id):
        self._validate_input(schedule_id)
        self.storage.delete_schedule({
            "id": schedule_id,
            "user": self.context['email'],
        })

    def _validate_input(self, schedule_id):
        if not self.validate_storage_id(schedule_id):
            raise ValueError("Invalid schedule id")
