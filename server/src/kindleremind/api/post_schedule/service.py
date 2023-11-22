from datetime import datetime

from .validator import validate_input


class CreateReminderScheduleService:
    def __init__(self, schedules_limit, storage, scheduler):
        self.storage = storage
        self.schedules_limit = schedules_limit
        self.scheduler = scheduler

    def create(self, schedule_input):
        validate_input(schedule_input)
        self._validate_limit()
        schedule = self.storage.create({
            'datetime': datetime.fromisoformat(schedule_input['datetime']),
            'weekdays': schedule_input['weekdays'],
        })
        self.scheduler.schedule_notification(schedule)

        return schedule

    def _validate_limit(self):
        if self.storage.get_schedules_count() >= self.schedules_limit:
            raise Exception('Schedules limit reached')
