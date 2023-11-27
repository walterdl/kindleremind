import pymongo


class Storage():
    def __init__(self, collection):
        self.collection = collection

    def get_user_schedules(self, user):
        schedules = self.collection.find(
            {'user': user},
            sort=[('datetime', pymongo.DESCENDING)]
        )

        return (self._format_result(schedule) for schedule in schedules)

    def _format_result(self, schedule):
        schedule['id'] = str(schedule['_id'])
        del schedule['_id']

        return schedule
